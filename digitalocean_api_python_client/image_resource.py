from .api import Api


class ImageResource(Api):
    def __init__(self):
        self.path = '/v2/images'

    def all(self, type=None, private=None, page=None, per_page=None):
        query = '?page={}&per_page={}'.format(page or 1, per_page or self.per_page)

        if type is not None and private is not None:
            raise ValueError('Only one of parameters type/private can be specified!')

        if type is not None:
            if type == 'application':
                query += '&type={}'.format(type)
            elif type == 'distribution':
                query += '&type={}'.format(type)
            else:
                raise ValueError('Unknown value for parameter type: {}'.format(type))

        if private is not None:
            if private is True:
                query += '&private=true'
            else:
                raise ValueError('Unknown value for parameter private: {}'.format(private))

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='images',
                                  page=page,
                                  per_page=per_page)

    def actions(self, image_id):
        query = "/{}/actions".format(image_id)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='actions',
                                  page=page,
                                  per_page=per_page)

    def find(self, image_id_or_name):
        query = '/{}'.format(image_id_or_name)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='image')

    def update(self, image_id, name):
        query = '/{}'.format(image_id)

        return self.get_object(method='PUT',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body={"name": name},
                               response_ok=200,
                               response_body_json_key='image')

    def delete(self, image_id):
        query = "/{}".format(image_id)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)
