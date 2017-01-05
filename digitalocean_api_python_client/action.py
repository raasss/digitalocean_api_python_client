class Action(object):
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
        self.status = status
        self.type = type
        self.started_at = started_at
        self.completed_at = completed_at
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.region = region
        self.region_slug = region_slug

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
