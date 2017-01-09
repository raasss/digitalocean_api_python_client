import logging
from .api import Api


class VolumeResource(Api):
    def __init__(self):
        self.path = '/v2/volumes'

    def all(self, region=None, page=None, per_page=None):
        logging.info('List all Volumes. (region={}, page={}, per_page={})'.format(region, page, per_page))

        query = '?page={}&per_page={}'.format(page or 1, per_page or self.per_page)

        if region is not None:
            query += "&region={}".format(region)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='volumes',
                                  page=page,
                                  per_page=per_page)

    def create(self, volume_def):
        logging.info('Create a new volume. (volume_dev={})'.format(volume_def))

        query = ''

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=volume_def,
                               response_ok=201,
                               response_body_json_key='volume')

    def find(self, id):
        logging.info('Retrieve an existing Block Storage volume. (id={})'.format(id))

        query = "/{}".format(id)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='volume')

    def find_by_name(self, name, region, page=None, per_page=None):
        query = '?name={}&region={}&page={}&per_page={}'.format(name, region, page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='volumes',
                                  page=page,
                                  per_page=per_page)

    def snapshots(self, volume_id, page=None, per_page=None):
        query = '/{}/snapshots?page={}&per_page={}'.format(volume_id, page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='snapshots',
                                  page=page,
                                  per_page=per_page)

    def create_snapshot(self, volume_id, snapshot_name):
        query = "/{}".format(volume_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"name": snapshot_name},
                               response_ok=201,
                               response_body_json_key='snapshot')

    def delete(self, volume_id):
        query = "/{}".format(volume_id)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)

    def delete_by_name(self, volume_name, region_slug):
        query = "?name={}&region={}".format(volume_name, region_slug)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)

