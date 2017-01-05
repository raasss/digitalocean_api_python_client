class Image(object):
    def __init__(self,
                 id,
                 name,
                 type,
                 distribution,
                 slug,
                 public,
                 regions,
                 min_disk_size,
                 size_gigabytes,
                 created_at):
        self.id = id
        self.name = name
        self.type = type
        self.distribution = distribution
        self.slug = slug
        self.public = public
        self.regions = regions
        self.min_disk_size = min_disk_size
        self.size_gigabytes = size_gigabytes
        self.created_at = created_at
