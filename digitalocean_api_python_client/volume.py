class Volume(object):
    def __init__(self,
                 id,
                 region,
                 droplet_ids,
                 name,
                 description,
                 size_gigabytes,
                 created_at):
        self.id = id
        self.region = region
        self.droplet_ids = droplet_ids
        self.name = name
        self.description = description
        self.size_gigabytes = size_gigabytes
        self.created_at = created_at

    def __repr__(self):
        s = 'id             : {}\n'.format(self.id)
        s += 'region        : {}\n'.format(self.region)
        s += 'droplet_ids   : {}\n'.format(self.droplet_ids)
        s += 'name          : {}\n'.format(self.name)
        s += 'description   : {}\n'.format(self.description)
        s += 'size_gigabytes: {}\n'.format(self.size_gigabytes)
        s += 'created_at    : {}'.format(self.created_at)

        return s
