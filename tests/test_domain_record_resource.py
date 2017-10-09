import mock
import unittest

from digitalocean_api_python_client.domain_record_resource import DomainRecordResource

class DomainRecordResourceTestCase(unittest.TestCase):

    @mock.patch.object(DomainRecordResource, 'get_paginator')
    def test_all_method_with_page_and_per_page_not_set(self, mock_get_paginator):
        domain_name = "test.com"

        o = DomainRecordResource()
        o.all(domain_name)

        mock_get_paginator.assert_called_with(
            method='GET',
            url="https://api.digitalocean.com/v2/domains/{}/records?page=1&per_page=200".format(domain_name),
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer '},
            body=None,
            response_ok=200,
            response_body_json_key='domain_records',
            page=None,
            per_page=None)

    @mock.patch.object(DomainRecordResource, 'get_paginator')
    def test_all_method_with_page_and_per_page_set(self, mock_get_paginator):
        domain_name = "test.com"
        page=1
        per_page=150

        o = DomainRecordResource()
        o.all(domain_name=domain_name, page=page, per_page=per_page)

        mock_get_paginator.assert_called_with(
            method='GET',
            url="https://api.digitalocean.com/v2/domains/{}/records?page={}&per_page={}".format(domain_name, page, per_page),
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer '},
            body=None,
            response_ok=200,
            response_body_json_key='domain_records',
            page=page,
            per_page=per_page)
