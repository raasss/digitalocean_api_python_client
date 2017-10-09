from .api import Api


class FloatingIpResource(Api):
    def __init__(self):
        self.path = '/v2/floating_ips'

    def all(self):
        query = ""

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='floating_ips')

    def create(self, droplet_id=None, region=None):
        query = ""

        if droplet_id is not None and region is None:
            body = {"droplet_id": droplet_id}
        elif region is not None and droplet_id is None:
            body = {"region": region}
        else:
            raise ValueError

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=body,
                               response_ok=202,
                               response_body_json_key='floating_ip')

    def find(self, floating_ip_address):
        query = "/{}".format(floating_ip_address)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='floating_ip')

    def delete(self, floating_ip_address):
        query = "/{}".format(floating_ip_address)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)
