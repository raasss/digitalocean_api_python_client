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
        query = ""

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=ssh_key_def,
                               response_ok=201,
                               response_body_json_key='ssh_key')

    def find(self, id):
        query = "/{}".format(id)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='ssh_key')

    def update(self, id, name):
        query = "/{}".format(id)

        return self.get_object(method='PUT',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"name": name},
                               response_ok=200,
                               response_body_json_key='ssh_key')

    def delete(self, ssh_key_id):
        query = "/{}".format(ssh_key_id)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)
