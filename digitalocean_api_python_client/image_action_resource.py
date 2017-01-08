from .api import Api


class ImageActionResource(Api):
    def __init__(self):
        self.path = '/v2/images'

    def transfer(self, image_id, region):
        query = "/{}/actions".format(image_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "transfer",
                                     "region": region},
                               response_ok=201,
                               response_body_json_key='action')

    def convert(self, image_id):
        query = "/{}/actions".format(image_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"type": "convert"},
                               response_ok=201,
                               response_body_json_key='action')

    def find(self, image_id, action_id):
        query = "/{}/actions/{}".format(image_id, action_id)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='action')
