from .api import Api
import logging

class SnapshotResource(Api):
    def __init__(self):
        self.path = '/v2/snapshots'

    def all(self, resource_type=None, page=None, per_page=None):
        logging.info('List all snapshots. (resource_type={}, page={}, per_page={})'.format(resource_type, page, per_page))

        if resource_type is None:
            query = '?page={}&per_page={}'.format(page or 1, per_page or self.per_page)
        else:
            query = '?resource_type={}&page={}&per_page={}'.format(
                resource_type, page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='snapshots',
                                  page=page,
                                  per_page=per_page)

    def delete(self, resource_id):
        query = "/{}".format(resource_id)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)
