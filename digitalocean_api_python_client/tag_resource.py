from .api import Api


class TagResource(Api):
    def __init__(self):
        self.path = '/v2/tags'

    def create(self, name):
        query = ""

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"name": name},
                               response_ok=201,
                               response_body_json_key='tag')

    def find(self, name):
        query = "{}".format(name)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=201,
                               response_body_json_key='tag')

    def all(self, name):
        query = '?page={}&per_page={}'.format(page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='tags',
                                  page=page,
                                  per_page=per_page)

    def update(self, name, new_name):
        query = "/{}".format(name)

        return self.get_object(method='PUT',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"name": new_name},
                               response_ok=200,
                               response_body_json_key='tag')

    def tag_resources(self, name, resources):
        query = "/{}/resources".format(name)

        return self.request(method='POST',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body={"resources": resources},
                            response_ok=204)

    def untag_resources(self, name, resources):
        query = "/{}/resources".format(name)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body={"resources": resources},
                            response_ok=204)

    def delete(self, name):
        query = "/{}".format(name)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)
