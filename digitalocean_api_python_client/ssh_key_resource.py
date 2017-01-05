from .api import Api
import logging


class SshKeyResource(Api):
    def __init__(self):
        self.path = '/v2/account/keys'

    def all(self, page=None, per_page=None):
        logging.info('List all Keys. (page={}, per_page={})'.format(page, per_page))

        query = '?page={}&per_page={}'.format(page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='ssh_keys',
                                  page=page,
                                  per_page=per_page)

    def create(self, ssh_key_def):
        api_uri_query = ""
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = ssh_key_def
        response_header_status_ok = 201
        response_body_json_key = "ssh_key"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def find(self, id):
        api_uri_query = "/{}".format(id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)
        request_method = "GET"
        request_body = None
        response_header_status_ok = 200
        response_body_json_key = "ssh_key"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def update(self, id, name):
        api_uri_query = "/{}".format(id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "PUT"
        request_body = {"name": name}
        response_header_status_ok = 200
        response_body_json_key = "ssh_key"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def delete(self, ssh_key_id):
        api_uri_query = "/{}".format(volume_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "DELETE"
        request_body = ""
        response_header_status_ok = 204
        response_body_json_key = ""

        r = requests.request(method=request_method,
                             url=api_uri,
                             headers=self.generate_http_request_headers())

        if r.status_code != response_header_status_ok:
            raise ValueError("HTTP request failed")

        return r.status_code
