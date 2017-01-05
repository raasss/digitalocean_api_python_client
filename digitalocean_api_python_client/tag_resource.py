from .api import Api


class TagResource(Api):
    api_uri_path = '/v2/tags'

    def new(self, name):
        api_uri_query = ""
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"name": name}
        response_header_status_ok = 201
        response_body_json_key = "tag"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def find(self, name):
        api_uri_query = "{}".format(name)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = ""
        response_header_status_ok = 201
        response_body_json_key = "tag"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def all(self, name):
        api_uri_query = ""
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = ""
        response_header_status_ok = 200
        response_body_json_key = "tags"

        o = self.get_api_response_objects(request_method,
                                          api_uri,
                                          response_header_status_ok,
                                          self.generate_http_request_headers(),
                                          request_body,
                                          response_body_json_key)

        return o

    def update(self, name, new_name):
        api_uri_query = "/{}".format(name)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "PUT"
        request_body = {"name": new_name}
        response_header_status_ok = 200
        response_body_json_key = "tag"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def tag_resources(self, name, resources):
        api_uri_query = "/{}/resources".format(name)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"resources": resources}
        response_header_status_ok = 204
        response_body_json_key = ""

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def untag_resources(self, name, resources):
        api_uri_query = "/{}/resources".format(name)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "DELETE"
        request_body = {"resources": resources}
        response_header_status_ok = 204
        response_body_json_key = ""

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def delete(self, name):
        api_uri_query = "/{}".format(name)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "DELETE"
        request_body = ""
        response_header_status_ok = 204
        response_body_json_key = ""

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o
