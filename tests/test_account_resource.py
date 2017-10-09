import mock
import unittest

# import sys
# sys.path.append('..')

from digitalocean_api_python_client.account_resource import AccountResource


def fake_request(*args, **kwargs):
    response = {'url': 'https://api.digitalocean.com/v2/account',
                'status': 200,
                'body': {'account': {'status': 'active',
                                     'uuid': 'aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd',
                                     'floating_ip_limit': 3,
                                     'email_verified': True,
                                     'droplet_limit': 25,
                                     'status_message': '',
                                     'email': 'user@test.com'}},
                'headers': {'X-Request-Id': '1110143d-2640-4c0f-9110-8cd7b788954d',
                            'Ratelimit-Remaining': '4999',
                            'X-Gateway': 'Edge Gateway',
                            'X-Content-Type-Options': 'nosniff',
                            'Content-Encoding': 'gzip',
                            'Transfer-Encoding': 'chunked',
                            'Set-Cookie': '__cfduid=df384abc639d2e058d1205c7a099409fa1483644509; expires=Fri, 05-Jan-18 19:28:29 GMT; path=/; domain=.digitalocean.com; HttpOnly',
                            'Ratelimit-Limit': '5000', 'Ratelimit-Reset': '1483648110', 'Server': 'cloudflare-nginx',
                            'Connection': 'keep-alive', 'Etag': 'W/"c17f0f7a15e9b0e896de9fddc4af8f23"',
                            'Cache-Control': 'max-age=0, private, must-revalidate', 'Date': 'Thu, 05 Jan 2017 19:28:30 GMT',
                            'X-Frame-Options': 'SAMEORIGIN', 'X-Runtime': '0.070152',
                            'Content-Type': 'application/json; charset=utf-8', 'CF-RAY': '31c9556b28383ff6-SOF',
                            'X-Xss-Protection': '1; mode=block'}}

    return response


class AccountResourceTestCase(unittest.TestCase):

    def test_info(self):
        accounts = AccountResource()
        accounts.request = fake_request
        account = accounts.info()

        self.assertEqual(account.status, 'active')
        self.assertEqual(account.uuid, 'aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd')
        self.assertEqual(account.floating_ip_limit, 3)
        self.assertEqual(account.email_verified, True)
        self.assertEqual(account.droplet_limit, 25)
        self.assertEqual(account.status_message, '')
        self.assertEqual(account.email, 'user@test.com')

    @mock.patch.object(AccountResource, 'get_object')
    def test_info_call(self, mock_get_object):
        accounts = AccountResource()
        account = accounts.info()

        mock_get_object.assert_called_with(
            method='GET',
            url="https://api.digitalocean.com/v2/account",
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer '},
            body=None,
            response_ok=200,
            response_body_json_key='account')
