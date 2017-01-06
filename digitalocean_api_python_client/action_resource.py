from .api import Api
import logging
import time


class ActionResource(Api):
    def __init__(self):
        self.path = '/v2/actions'

    def all(self, page=None, per_page=None):
        logging.info('List all Actions. (page={}, per_page={})'.format(page, per_page))

        query = '?page={}&per_page={}'.format(page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='actions',
                                  page=page,
                                  per_page=per_page)

    def find(self, id):
        logging.info('Retrieve an existing Action. (id={})'.format(id))

        query = '/{}'.format(id)

        return self.get_object(method='GET',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=200,
                            response_body_json_key='action')

    def wait_for_actions_completion(self, object_with_actions, number_of_retries=24):
        logging.info('Waiting for all actions to be completed. (actions={})'.format(vars(object_with_actions)))

        try:
            actions = object_with_actions.response['body']['links']['actions']
        except:
            raise ValueError('Can not find argument actions!')

        i=0

        while True:
            all_actions_completed = True

            for action in actions:
                id = action['id']

                a = self.find(id)
                logging.debug('Action {} status: {}'.format(a.id, a.status))

                if a.status != 'completed':
                    all_actions_completed = False
                    continue

            if all_actions_completed == True:
                return True

            i += 1
            if i == number_of_retries:
                raise RuntimeError('Number of retries reached! ({})'.format(number_of_retries))

            time.sleep(5)
