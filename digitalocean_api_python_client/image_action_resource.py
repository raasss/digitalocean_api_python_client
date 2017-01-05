from .api import Api


class ImageActionResource(Api):
    api_uri_path = '/v2/images'

    def all(self, image_id):
        api_uri_query = "/{}/actions".format(image_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = None
        response_header_status_ok = 200
        response_body_json_key = "actions"

        o = self.get_api_response_objects(request_method,
                                          api_uri,
                                          response_header_status_ok,
                                          self.generate_http_request_headers(),
                                          request_body,
                                          response_body_json_key)

        return o

    def transfer(self, image_id, region):
        api_uri_query = "/{}/actions".format(droplet_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "transfer",
                        "region": region}
        response_header_status_ok = 201
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def convert(self, image_id):
        api_uri_query = "/{}/actions".format(droplet_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "convert"}
        response_header_status_ok = 201
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def find(self, image_id, action_id):
        api_uri_query = "/{}/actions/{}".format(image_id, action_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
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
