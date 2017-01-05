class Snapshot(object):
    def __init__(self,
                 id,
                 name,
                 created_at,
                 regions,
                 resource_id,
                 resource_type,
                 min_disk_size,
                 size_gigabytes):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.regions = regions
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.min_disk_size = min_disk_size
        self.size_gigabytes = size_gigabytes
