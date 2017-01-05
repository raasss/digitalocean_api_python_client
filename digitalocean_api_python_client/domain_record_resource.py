from .api import Api


class DomainRecordResource(Api):
    def __init__(self):
        self.path = '/v2/domains'

    def all(self, domain_name, page=None, per_page=None):
        query = '/{}/records?page={}&per_page={}'.format(domain_name, page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='domain_records',
                                  page=page,
                                  per_page=per_page)

    def create(self, record, for_domain):
        query = "/{}/records".format(for_domain)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=record,
                               response_ok=201,
                               response_body_json_key='domain_record')

    def find(self, domain_name, record_id):
        api_uri_query = "/{}/records/{}".format(domain_name, record_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = None
        response_header_status_ok = 200
        response_body_json_key = "domain_record"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def update(self, record, for_domain, record_id):
        api_uri_query = "/{}/records/{}".format(for_domain, record_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "PUT"
        request_body = record
        response_header_status_ok = 200
        response_body_json_key = "domain_record"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def delete(self, for_domain, record_id):
        query = "/{}/records/{}".format(for_domain, record_id)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)
