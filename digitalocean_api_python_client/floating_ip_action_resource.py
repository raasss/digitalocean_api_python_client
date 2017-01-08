from .api import Api


class FloatingIpActionResource(Api):
    api_uri_path = '/v2/floating_ips'

    def assign(self, floating_ip_address, droplet_id):
        query = "/{}/actions".format(floating_ip_address)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "assign",
                                     "droplet_id": droplet_id},
                               response_ok=201,
                               response_body_json_key='action')

    def unassign(self, floating_ip_address):
        query = "/{}/actions".format(floating_ip_address)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "unassign"},
                               response_ok=201,
                               response_body_json_key='action')

    def all(self, floating_ip_address):
        query = "/{}/actions".format(floating_ip_address)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='actions')

    def find(self, floating_ip_address, action_id):
        query = "/{}/actions/{}".format(floating_ip_address, action_id)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='action')
