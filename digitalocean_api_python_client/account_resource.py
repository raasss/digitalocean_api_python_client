from .api import Api
import logging


class AccountResource(Api):
    """Account Resource as per https://developers.digitalocean.com/documentation/v2/#account"""

    def __init__(self):
        self.path = '/v2/account'

    def info(self):
        """Get User Information as per """

        logging.info('Get User Information')

        query = ''

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='account')
