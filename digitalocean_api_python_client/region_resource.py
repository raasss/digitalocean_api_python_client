from .api import Api


class RegionResource(Api):
    api_uri_path = '/v2/regions'

    def all(self, image_id):
        api_uri_query = ""
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = None
        response_header_status_ok = 200
        response_body_json_key = "regions"

        o = self.get_api_response_objects(request_method,
                                          api_uri,
                                          response_header_status_ok,
                                          self.generate_http_request_headers(),
                                          request_body,
                                          response_body_json_key)

        return o
