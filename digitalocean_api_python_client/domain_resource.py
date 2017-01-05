from .api import Api
import logging

class DomainResource(Api):
    def __init__(self):
        self.path = '/v2/domains'

    def all(self, page=None, per_page=None):
        logging.info('List all Domains. (page={}, per_page={})'.format(page, per_page))

        query = '?page={}&per_page={}'.format(page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='domains',
                                  page=page,
                                  per_page=per_page)

    def create(self, domain_def):
        query = ''
        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=domain_def,
                               response_ok=201,
                               response_body_json_key='domain')

    def find(self, name):
        api_uri_query = "/{}".format(name)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = None
        response_header_status_ok = 200
        response_body_json_key = "domain"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def delete(self, name):
        query = "/{}".format(name)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)
