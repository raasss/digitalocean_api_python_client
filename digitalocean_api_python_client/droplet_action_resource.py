from .api import Api


class DropletActionResource(Api):
    path = '/v2/droplets'

    # def all(self, droplet_id, page=None, per_page=None):
    #     query = '/{}/actions?page={}&per_page={}'.format(droplet_id, page or 1, per_page)
    #
    #     return self.get_paginator(method='GET',
    #                               url=self.add_query_to_url(query),
    #                               headers=self.headers,
    #                               body=None,
    #                               response_ok=200,
    #                               response_body_json_key='actions',
    #                               page=page,
    #                               per_page=per_page)

    def enable_backups(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "enable_backups"},
                               response_ok=201,
                               response_body_json_key='action')

    def disable_backups(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "disable_backups"},
                               response_ok=201,
                               response_body_json_key='action')

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

    def shutdown(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "shutdown"},
                               response_ok=201,
                               response_body_json_key='action')

    def power_off(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "power_off"},
                               response_ok=201,
                               response_body_json_key='action')

    def power_on(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "power_on"},
                               response_ok=201,
                               response_body_json_key='action')

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
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "password_reset"},
                               response_ok=201,
                               response_body_json_key='action')

    def resize(self, droplet_id, size):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "resize",
                                     "disk": True,
                                     "size": size},
                               response_ok=201,
                               response_body_json_key='action')

    def rebuild(self, droplet_id, image):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "rebuild",
                                     "image": image},
                               response_ok=201,
                               response_body_json_key='action')

    def rename(self, droplet_id, name):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "rename",
                                     "name": name},
                               response_ok=201,
                               response_body_json_key='action')

    def change_kernel(self, droplet_id, kernel):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "change_kernel",
                                     "kernel": kernel},
                               response_ok=201,
                               response_body_json_key='action')

    def enable_ipv6(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "enable_ipv6"},
                               response_ok=201,
                               response_body_json_key='action')

    def enable_private_networking(self, droplet_id):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "enable_private_networking"},
                               response_ok=201,
                               response_body_json_key='action')

    def snapshot(self, droplet_id, name):
        query = "/{}/actions".format(droplet_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "snapshot",
                                     "name": name},
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

    def power_on_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "power_on"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def power_off_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "power_off"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def shutdown_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "shutdown"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def enable_private_networking_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "enable_private_networking"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def enable_ipv6_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "enable_ipv6"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def enable_backups_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "enable_backups"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def disable_backups_for_tag(self, tag):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "disable_backups"},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def snapshot_for_tag(self, tag, name):
        query = "/actions?tag_name={}".format(tag)

        return self.get_collection(method='POST',
                                   url=self.add_query_to_url(query),
                                   headers=self.headers,
                                   body={"type": "snapshot",
                                         "name": name},
                                   response_ok=201,
                                   response_body_json_key='actions')

    def find(self, droplet_id, action_id):
        query = "/{}/actions/{}".format(droplet_id, action_id)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='action')
