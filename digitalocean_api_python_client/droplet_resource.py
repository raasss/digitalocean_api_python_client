from .api import Api


class DropletResource(Api):
    def __init__(self):
        self.path = '/v2/droplets'

    def create(self, droplet_def):
        query = ''
        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=droplet_def,
                               response_ok=202,
                               response_body_json_key='droplet')

    def create_multiple(self, droplets_def):
        query = ''
        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body=droplets_def,
                                   response_ok=202,
                                   response_body_json_key='droplets')

    def find(self, droplet_id):
        query = '/{}'.format(droplet_id)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='droplet')

    def wait_until_unlocked(self, droplet_id, retries=24, sleep=5):
        i = 0
        while i < 24:
            droplet = self.find(droplet_id)
        droplet = self.find(droplet_id)
        return droplet.locked

    def all(self, tag=None, page=None, per_page=None):
        query = '?page={}&per_page={}'.format(page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='droplets',
                                  page=page,
                                  per_page=per_page)

    def delete(self, droplet_id):
        query = "/{}".format(droplet_id)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)

    def delete_for_tag(self, tag):
        query = "?tag_name={}".format(tag)e

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)

    def kernels(self, droplet_id):
        query = "/{}/kernels".format(droplet_id)

        return self.get_collection(method='GET',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body=None,
                                   response_ok=200,
                                   response_body_json_key='kernels')
