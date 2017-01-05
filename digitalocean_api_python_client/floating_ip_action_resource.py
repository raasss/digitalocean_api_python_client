from .api import Api


class FloatingIpActionResource(Api):
    api_uri_path = '/v2/floating_ips'

    def assign(self, floating_ip_address, droplet_id):
        api_uri_query = "/{}/actions".format(floating_ip_address)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "assign",
                        "droplet_id": droplet_id}
        response_header_status_ok = 201
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def unassign(self, floating_ip_address):
        api_uri_query = "/{}/actions".format(floating_ip_address)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "unassign"}
        response_header_status_ok = 201
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def all(self, floating_ip_address):
        api_uri_query = "/{}/actions".format(floating_ip_address)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = ""
        response_header_status_ok = 200
        response_body_json_key = "actions"

        o = self.get_api_response_objects(request_method,
                                          api_uri,
                                          response_header_status_ok,
                                          self.generate_http_request_headers(),
                                          request_body,
                                          response_body_json_key)

        return o

    def find(self, floating_ip_address, action_id):
        api_uri_query = "/{}/actions/{}".format(floating_ip_address, action_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = ""
        response_header_status_ok = 200
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o
