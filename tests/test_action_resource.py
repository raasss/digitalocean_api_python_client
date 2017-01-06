import mock
import unittest

from digitalocean_api_python_client.action_resource import ActionResource

class ActionResourceTestCase(unittest.TestCase):

    @mock.patch.object(ActionResource, 'get_paginator')
    def test_all_method_with_no_parameters(self, mock_get_paginator):
        actions = ActionResource()
        actions.all()

        mock_get_paginator.assert_called_with(
            method='GET',
            url="https://api.digitalocean.com/v2/actions?page=1&per_page=200",
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer '},
            body=None,
            response_ok=200,
            response_body_json_key='actions',
            page=None,
            per_page=None)

    @mock.patch.object(ActionResource, 'get_paginator')
    def test_all_method_with_page_and_per_page_parameters(self, mock_get_paginator):
        page = 2
        per_page = 100

        actions = ActionResource()
        actions.all(page=page, per_page=per_page)

        mock_get_paginator.assert_called_with(
            method='GET',
            url="https://api.digitalocean.com/v2/actions?page=2&per_page=100",
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer '},
            body=None,
            response_ok=200,
            response_body_json_key='actions',
            page=page,
            per_page=per_page)

    @mock.patch.object(ActionResource, 'get_object')
    def test_find_method(self, mock_get_object):
        action_id = 157679524

        actions = ActionResource()
        actions.find(action_id)

        mock_get_object.assert_called_with(method='GET',
                            url="https://api.digitalocean.com/v2/actions/{}".format(action_id),
                            headers={'Content-Type': 'application/json',
                                     'Authorization': 'Bearer '},
                            body=None,
                            response_ok=200,
                            response_body_json_key='action')