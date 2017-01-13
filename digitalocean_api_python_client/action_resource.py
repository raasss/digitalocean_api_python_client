from .api import Api
import logging
import time


class ActionResource(Api):
    """Action object as per https://developers.digitalocean.com/documentation/v2/#actions

    :param id: A unique numeric ID that can be used to identify and reference an action.
    :param status: The current status of the action. This can be "in-progress", "completed", or "errored".
    :param type: This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action.
    :param started_at: A time value given in ISO8601 combined date and time format that represents when the action was initiated.
    :param completed_at: A time value given in ISO8601 combined date and time format that represents when the action was completed.
    :param resource_id: A unique identifier for the resource that the action is associated with.
    :param resource_type: The type of resource that the action is associated with.
    :param region: (deprecated) A slug representing the region where the action occurred.
    :param region_slug: A slug representing the region where the action occurred.
    """

    def __init__(self):
        self.path = '/v2/actions'

    def all(self, page=None, per_page=None):
        """Action object as per https://developers.digitalocean.com/documentation/v2/#actions

        :param id: A unique numeric ID that can be used to identify and reference an action.
        :param status: The current status of the action. This can be "in-progress", "completed", or "errored".
        :param type: This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action.
        :param started_at: A time value given in ISO8601 combined date and time format that represents when the action was initiated.
        :param completed_at: A time value given in ISO8601 combined date and time format that represents when the action was completed.
        :param resource_id: A unique identifier for the resource that the action is associated with.
        :param resource_type: The type of resource that the action is associated with.
        :param region: (deprecated) A slug representing the region where the action occurred.
        :param region_slug: A slug representing the region where the action occurred.
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
        """Action object as per https://developers.digitalocean.com/documentation/v2/#actions

        :param id: A unique numeric ID that can be used to identify and reference an action.
        :param status: The current status of the action. This can be "in-progress", "completed", or "errored".
        :param type: This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action.
        :param started_at: A time value given in ISO8601 combined date and time format that represents when the action was initiated.
        :param completed_at: A time value given in ISO8601 combined date and time format that represents when the action was completed.
        :param resource_id: A unique identifier for the resource that the action is associated with.
        :param resource_type: The type of resource that the action is associated with.
        :param region: (deprecated) A slug representing the region where the action occurred.
        :param region_slug: A slug representing the region where the action occurred.
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
        """Action object as per https://developers.digitalocean.com/documentation/v2/#actions

        :param id: A unique numeric ID that can be used to identify and reference an action.
        :param status: The current status of the action. This can be "in-progress", "completed", or "errored".
        :param type: This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action.
        :param started_at: A time value given in ISO8601 combined date and time format that represents when the action was initiated.
        :param completed_at: A time value given in ISO8601 combined date and time format that represents when the action was completed.
        :param resource_id: A unique identifier for the resource that the action is associated with.
        :param resource_type: The type of resource that the action is associated with.
        :param region: (deprecated) A slug representing the region where the action occurred.
        :param region_slug: A slug representing the region where the action occurred.
        """

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
