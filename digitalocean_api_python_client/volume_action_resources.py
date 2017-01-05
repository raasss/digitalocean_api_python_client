from .api import Api
import logging
import time


class VolumeActionResource(Api):
    def __init__(self):
        self.path = '/v2/volumes'

    def attach(self, volume_id, droplet_id, region):
        query = "/{}/actions".format(volume_id)

        request_body = {'type': 'attach',
                        'droplet_id': droplet_id,
                        'region': region}

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=request_body,
                               response_ok=202,
                               response_body_json_key='action')


    def detach(self, volume_id, droplet_id, region):
        query = "/{}/actions".format(volume_id)

        request_body = {'type': 'detach',
                        'droplet_id': droplet_id,
                        'region': region}

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=request_body,
                               response_ok=202,
                               response_body_json_key='action')

    def resize(self, volume_id, size_gigabytes, region):
        api_uri_query = "/{}/actions".format(volume_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {'type': 'resize',
                        'size_gigabytes': size_gigabytes,
                        'region': region}
        response_header_status_ok = 202
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def all(self, volume_id, page=None, per_page=None):
        logging.info('List all actions for a volume. (volume_id={}, page={}, per_page={})'.format(volume_id, page, per_page))

        query = '/{}/actions?page={}&per_page={}'.format(volume_id, page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='actions',
                                  page=page,
                                  per_page=per_page)

    def find(self, volume_id, action_id):
        logging.info('Retrieve an existing Volume Action. (volume_id={}, action_id={})'.format(volume_id, action_id))

        query = "/{}/actions/{}".format(volume_id, action_id)

        return self.get_object(method='GET',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=200,
                            response_body_json_key='action')
