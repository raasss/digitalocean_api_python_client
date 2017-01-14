class Tag(object):
    """Tag object as per https://developers.digitalocean.com/documentation/v2/#tags

    :param name: Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.
    :param resources: An embedded object containing key value pairs of resource type and resource statistics.

    :type name: string
    :type resources: object
    """

    def __init__(self,
                 name,
                 resources):
        self.name = name
        self.resources = resources
