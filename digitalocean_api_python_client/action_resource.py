from .api import Api
import logging
import time


class ActionResource(Api):
    """Actions as per https://developers.digitalocean.com/documentation/v2/#actions

    Actions are records of events that have occurred on the resources in your account. These can be things like rebooting a Droplet, or transferring an image to a new region.

    An action object is created every time one of these actions is initiated. The action object contains information about the current status of the action, start and complete timestamps, and the associated resource type and ID.

    Every action that creates an action object is available through this endpoint. Completed actions are not removed from this list and are always available for querying.
    """

    def __init__(self):
        self.path = '/v2/actions'

    def all(self, page=None, per_page=None):
        """List all Actions as per https://developers.digitalocean.com/documentation/v2/#list-all-actions

        To list all of the actions that have been executed on the current account, send a GET request to /v2/actions.

        This will be the entire list of actions taken on your account, so it will be quite large. As with any large collection returned by the API, the results will be paginated with only 25 on each page by default.

        The results will be returned as a JSON object with an actions key. This will be set to an array filled with action objects containing the standard action attributes:
        """

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
        """Retrieve an existing Action as per https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-action

        To retrieve a specific action object, send a GET request to /v2/actions/$ACTION_ID.

        The result will be a JSON object with an action key. This will be set to an action object containing the standard action attributes.
        """

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

        i = 0

        while True:
            all_actions_completed = True

            for action in actions:
                id = action['id']

                a = self.find(id)
                logging.debug('Action {} status: {}'.format(a.id, a.status))

                if a.status != 'completed':
                    all_actions_completed = False
                    continue

            if all_actions_completed is True:
                return True

            i += 1
            if i == number_of_retries:
                raise RuntimeError('Number of retries reached! ({})'.format(number_of_retries))

            time.sleep(5)
