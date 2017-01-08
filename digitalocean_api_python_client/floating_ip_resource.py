from .api import Api


class FloatingIpResource(Api):
    api_uri_path = '/v2/floating_ips'

    def all(self):
        api_uri_query = ""
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = None
        response_header_status_ok = 200
        response_body_json_key = "floating_ips"

        o = self.get_api_response_objects(request_method,
                                          api_uri,
                                          response_header_status_ok,
                                          self.generate_http_request_headers(),
                                          request_body,
                                          response_body_json_key)

        return o

    def create(self, droplet_id=None, region=None):
        api_uri_query = ""
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        if droplet_id is not None and region is None:
            request_body = {"droplet_id": droplet_id}
        elif region is not None and droplet_id is None:
            request_body = {"region": region}
        else:
            raise ValueError
        response_header_status_ok = 202
        response_body_json_key = "floating_ip"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def find(self, floating_ip_address):
        api_uri_query = "/{}".format(floating_ip_address)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = ""
        response_header_status_ok = 200
        response_body_json_key = "floating_ip"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def delete(self, floating_ip_address):
        api_uri_query = "/{}".format(floating_ip_address)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "DELETE"
        request_body = ""
        response_header_status_ok = 204
        response_body_json_key = ""

        r = requests.request(method=request_method,
                             url=api_uri,
                             headers=self.generate_http_request_headers())

        if r.status_code != response_header_status_ok:
            raise ValueError("HTTP request failed")

        return r.status_code
