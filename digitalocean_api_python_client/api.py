import requests
from .droplet import Droplet
from .account import Account
from .action import Action
from .volume import Volume
from .snapshot import Snapshot
from .domain import Domain
from .ssh_key import SshKey
from .domain_record import DomainRecord
from .image import Image
from .floating_ip import FloatingIp
from .region import Region
from .size import Size

class Api(object):
    token = ''
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer '}
    protocol = 'https'
    host = 'api.digitalocean.com'
    per_page = 200

    def init(self, token):
        self.__class__.token = token
        self.__class__.headers['Authorization'] += token

    def add_query_to_url(self, query):
        url = '{protocol}://{host}{path}{query}'.format(protocol=self.protocol,
                                                        host=self.host,
                                                        path=self.path,
                                                        query=query)
        return url

    def create_object_from_params(self, json, key):
        converter = {'account': Account,
                     'actions': Action,
                     'action': Action,
                     'volumes': Volume,
                     'volume': Volume,
                     'droplets': Droplet,
                     'droplet': Droplet,
                     'snapshots': Snapshot,
                     'snapshot': Snapshot,
                     'domains': Domain,
                     'domain': Domain,
                     'ssh_key': SshKey,
                     'ssh_keys': SshKey,
                     'domain_record': DomainRecord,
                     'domain_records': DomainRecord,
                     'backups': Image,
                     'floating_ips': FloatingIp,
                     'floating_ip': FloatingIp,
                     'regions': Region,
                     'sizes': Size}

        return converter[key](**json)

    @staticmethod
    def request(method, url, headers, body, response_ok):
        r = requests.request(method=method,
                             url=url,
                             headers=headers,
                             json=body)

        try:
            json_body = r.json()
        except ValueError:
            json_body = None

        response = {'url': r.url,
                    'status': r.status_code,
                    'headers': r.headers,
                    'body': json_body}

        if r.status_code != response_ok:
            raise ValueError('Got wrong HTTP status code! (response = {}'.format(response))

        return response

    def get_object(self,
                   method,
                   url,
                   headers,
                   body,
                   response_ok,
                   response_body_json_key):
        r = self.request(method, url, headers, body, response_ok)

        json_object = r['body'][response_body_json_key]
        object = self.create_object_from_params(json_object, response_body_json_key)

        object.response = r

        return object

    def get_collection(self,
                       method,
                       url,
                       headers,
                       body,
                       response_ok,
                       response_body_json_key):
        r = self.request(method, url, headers, body, response_ok)

        body = r['body']
        c = Collection()

        for object in body[response_body_json_key]:
            o = self.create_object_from_params(object)
            c.items.append(o)

        c.response = r

        return c

    def get_paginator(self,
                      method,
                      url,
                      headers,
                      body,
                      response_ok,
                      response_body_json_key,
                      page=None,
                      per_page=None):
        r = self.request(method, url, headers, body, response_ok)

        body = r['body']
        p = Paginator()

        for object in body[response_body_json_key]:
            o = self.create_object_from_params(object, response_body_json_key)
            p.items.append(o)

        p.page = page
        p.per_page = per_page

        try:
            p.first_page = body['links']['pages']['first']
        except KeyError:
            p.first_page = None

        try:
            p.prev_page = body['links']['pages']['prev']
        except KeyError:
            p.prev_page = None

        try:
            p.next_page = body['links']['pages']['next']
        except KeyError:
            p.next_page = None

        try:
            p.last_page = body['links']['pages']['last']
        except KeyError:
            p.last_page = None

        try:
            p.total_items = body['meta']['total']
        except KeyError:
            p.total_items = None

        p.method = method
        p.url = url
        p.headers = headers
        p.body = body
        p.response_ok = response_ok
        p.response_body_json_key = response_body_json_key

        p.invoker = self.get_paginator

        return p


class Paginator(object):
    def __init__(self):
        self.items = []

        self.current_page = None
        self.first_page = None
        self.prev_page = None
        self.next_page = None
        self.last_page = None

        self.total_items = None

        self.method = None
        self.url = None
        self.headers = None
        self.body = None
        self.response_ok = None
        self.response_body_json_key = None
        self.page = None
        self.per_page = None

        self.invoker = None

    def __iter__(self):
        for item in self.items:
            yield item

        if self.page is not None:
            return

        while True:
            if self.next_page is None:
                break

            page = self.invoker(method=self.method,
                                url=self.next_page,
                                headers=self.headers,
                                body=self.body,
                                response_ok=self.response_ok,
                                response_body_json_key=self.response_body_json_key)
            self.next_page = page.next_page

            for item in page.items:
                yield item


class Collection(object):
    def __init__(self):
        self.items = []

    def __iter__(self):
        for item in self.items:
            yield item
