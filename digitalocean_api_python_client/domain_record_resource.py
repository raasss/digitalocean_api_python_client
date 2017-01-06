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
        query = "/{}/records/{}".format(domain_name, record_id)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='domain_record')

    def update(self, record, for_domain, record_id):
        query = "/{}/records/{}".format(for_domain, record_id)

        return self.get_object(method='PUT',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=record,
                               response_ok=200,
                               response_body_json_key='domain_record')

    def delete(self, for_domain, record_id):
        query = "/{}/records/{}".format(for_domain, record_id)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)
