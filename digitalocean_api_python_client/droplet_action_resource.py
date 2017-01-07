from .api import Api


class DropletActionResource(Api):
    path = '/v2/droplets'

    def all(self, droplet_id, page=None, per_page=None):
        query = '/{}/actions?page={}&per_page={}'.format(droplet_id, page or 1, per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='actions',
                                  page=page,
                                  per_page=per_page)

    def enable_backups(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "enable_backups"},
                               response_ok=201,
                               response_body_json_key='action')

    def enable_backups_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "enable_backups"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def disable_backups(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "disable_backups"},
                               response_ok=201,
                               response_body_json_key='action')

    def disable_backups_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "disable_backups"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def reboot(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "reboot"},
                               response_ok=201,
                               response_body_json_key='action')

    def power_cycle(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "power_cycle"},
                               response_ok=201,
                               response_body_json_key='action')

    def power_cycle_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "power_cycle"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def shutdown(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "shutdown"},
                               response_ok=201,
                               response_body_json_key='action')

    def shutdown_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "shutdown"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def power_off(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "power_off"},
                               response_ok=201,
                               response_body_json_key='action')

    def power_off_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "power_off"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def power_on(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "power_on"},
                               response_ok=201,
                               response_body_json_key='action')

    def power_on_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "power_on"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def restore(self, droplet_id, image_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "restore",
                                     "image": image_id},
                               response_ok=201,
                               response_body_json_key='action')

    def password_reset(self, droplet_id):
        api_uri_query = "/{}/actions".format(droplet_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "password_reset"}
        response_header_status_ok = 201
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def resize(self, droplet_id, size):
        api_uri_query = "/{}/actions".format(droplet_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "resize",
                        "disk": True,
                        "size": size}
        response_header_status_ok = 201
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def rebuild(self, droplet_id, image):
        api_uri_query = "/{}/actions".format(droplet_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "rebuild",
                        "image": image}
        response_header_status_ok = 201
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def rename(self, droplet_id, name):
        api_uri_query = "/{}/actions".format(droplet_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "rename",
                        "name": name}
        response_header_status_ok = 201
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def change_kernel(self, droplet_id, kernel):
        api_uri_query = "/{}/actions".format(droplet_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "change_kernel",
                        "kernel": kernel}
        response_header_status_ok = 201
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def enable_ipv6(self, droplet_id=None, tag=None):
        if droplet_id is not None and tag is None:
            api_uri_query = "/{}/actions".format(droplet_id)
            response_body_json_key = "action"
        elif tag is not None and droplet_id is None:
            api_uri_query = "/actions?tag_name={}".format(tag)
            response_body_json_key = "actions"
        else:
            raise ValueError()

        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "enable_ipv6"}
        response_header_status_ok = 201

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def enable_private_networking(self, droplet_id=None, tag=None):
        if droplet_id is not None and tag is None:
            api_uri_query = "/{}/actions".format(droplet_id)
            response_body_json_key = "action"
        elif tag is not None and droplet_id is None:
            api_uri_query = "/actions?tag_name={}".format(tag)
            response_body_json_key = "actions"
        else:
            raise ValueError()

        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "enable_private_networking"}
        response_header_status_ok = 201

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def snapshot(self, droplet_id=None, tag=None, name=None):
        if name is None:
            raise ValueError

        if droplet_id is not None and tag is None:
            api_uri_query = "/{}/actions".format(droplet_id)
            response_body_json_key = "action"
        elif tag is not None and droplet_id is None:
            api_uri_query = "/actions?tag_name={}".format(tag)
            response_body_json_key = "actions"
        else:
            raise ValueError()

        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "POST"
        request_body = {"type": "snapshot",
                        "name": name}
        response_header_status_ok = 201

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o

    def find(self, droplet_id, action_id):
        api_uri_query = "/{}/actions/{}".format(droplet_id, action_id)
        api_uri = "{base}{path}{query}".format(base=self.api_uri_base, path=self.api_uri_path, query=api_uri_query)

        request_method = "GET"
        request_body = None
        response_header_status_ok = 200
        response_body_json_key = "action"

        o = self.get_api_response_object(request_method,
                                         api_uri,
                                         response_header_status_ok,
                                         self.generate_http_request_headers(),
                                         request_body,
                                         response_body_json_key)

        return o
