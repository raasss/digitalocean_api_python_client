class Volume(object):
    """Volume object as per https://developers.digitalocean.com/documentation/v2/#block-storage

    :param id: The unique identifier for the Block Storage volume.
    :param region: The region that the Block Storage volume is located in. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region object will be returned.
    :param droplet_ids: An array containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet.
    :param name: A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
    :param description: An optional free-form text field to describe a Block Storage volume.
    :param size_gigabytes: The size of the Block Storage volume in GiB (1024^3).
    :param created_at: The size of the Block Storage volume in GiB (1024^3).

    :type id: string
    :type region: object
    :type droplet_ids: array
    :type name: string
    :type description: string
    :type size_gigabytes: number
    :type created_at: string
    """

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
