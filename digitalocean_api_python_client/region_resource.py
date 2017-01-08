from .api import Api


class RegionResource(Api):
    def __init__(self):
        self.path = '/v2/regions'

    def all(self):
        query = '?page={}&per_page={}'.format(page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='regions',
                                  page=page,
                                  per_page=per_page)
