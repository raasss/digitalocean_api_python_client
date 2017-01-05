from .api import Api
import logging


class AccountResource(Api):
    def __init__(self):
        self.path = '/v2/account'

    def info(self):
        logging.info('Get User Information')

        query = ''

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='account')
