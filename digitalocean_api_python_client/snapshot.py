class Snapshot(object):
    """Snapshot object as per https://developers.digitalocean.com/documentation/v2/#snapshots

    :param id: The unique identifier for the snapshot.
    :param name: A human-readable name for the snapshot.
    :param created_at: A time value given in ISO8601 combined date and time format that represents when the snapshot was created.
    :param regions: An array of the regions that the image is available in. The regions are represented by their identifying slug values.
    :param resource_id: A unique identifier for the resource that the action is associated with.
    :param resource_type: The type of resource that the action is associated with.
    :param min_disk_size: The minimum size in GB required for a volume or Droplet to use this snapshot.
    :param size_gigabytes: The billable size of the snapshot in gigabytes.

    :type id: string
    :type name: string
    :type created_at: string
    :type regions: array
    :type resource_id: string
    :type resource_type: string
    :type min_disk_size: number
    :type size_gigabytes: number
    """

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
