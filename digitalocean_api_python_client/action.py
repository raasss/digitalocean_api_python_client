class Action(object):
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

    def __init__(self,
                 id,
                 status,
                 type,
                 started_at,
                 completed_at,
                 resource_id,
                 resource_type,
                 region,
                 region_slug):
        self.id = id
        # """(int) A unique numeric ID that can be used to identify and reference an action."""

        self.status = status
        # """(str) The current status of the action. This can be "in-progress", "completed", or "errored"."""

        self.type = type
        # """(str) This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action."""

        self.started_at = started_at
        # """(str) A time value given in ISO8601 combined date and time format that represents when the action was initiated."""

        self.completed_at = completed_at
        # """(str) A time value given in ISO8601 combined date and time format that represents when the action was completed."""

        self.resource_id = resource_id
        # """A unique identifier for the resource that the action is associated with."""

        self.resource_type = resource_type
        # """(str) The type of resource that the action is associated with."""

        self.region = region
        # """(str(deprecated) A slug representing the region where the action occurred."""

        self.region_slug = region_slug
        # """A slug representing the region where the action occurred."""

    def __repr__(self):
        s = 'id           : {}\n'.format(self.id)
        s += 'status       : {}\n'.format(self.status)
        s += 'type         : {}\n'.format(self.type)
        s += 'started_at   : {}\n'.format(self.started_at)
        s += 'completed_at : {}\n'.format(self.completed_at)
        s += 'resource_id  : {}\n'.format(self.resource_id)
        s += 'resource_type: {}\n'.format(self.resource_type)
        s += 'region       : {}\n'.format(self.region)
        s += 'region_slug  : {}'.format(self.region_slug)

        return s
