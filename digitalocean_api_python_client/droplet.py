class Droplet(object):
    """Droplet object as per https://developers.digitalocean.com/documentation/v2/#droplets

    :param id: A unique identifier for each Droplet instance. This is automatically generated upon
               Droplet creation.
    :param name: The human-readable name set for the Droplet instance.
    :param memory: Memory of the Droplet in megabytes.
    :param vcpus: The number of virtual CPUs.
    :param disk: The size of the Droplet's disk in gigabytes.
    :param locked: A boolean value indicating whether the Droplet has been locked, preventing
                   actions by users.
    :param created_at: A time value given in ISO8601 combined date and time format that represents
                       when the Droplet was created.
    :param status: A status string indicating the state of the Droplet instance. This may be "new",
                   "active", "off", or "archive".
    :param backup_ids: An array of backup IDs of any backups that have been taken of the Droplet
                       instance. Droplet backups are enabled at the time of the instance creation.
    :param snapshot_ids: An array of snapshot IDs of any snapshots created from the Droplet
                         instance.
    :param features: An array of features enabled on this Droplet.
    :param region: The region that the Droplet instance is deployed in. When setting a region, the
                   value should be the slug identifier for the region. When you query a Droplet, the
                   entire region object will be returned.
    :param image: The base image used to create the Droplet instance. When setting an image, the
                  value is set to the image id or slug. When querying the Droplet, the entire image
                  object will be returned.
    :param size: The current size object describing the Droplet. When setting a size, the value is
                 set to the size slug. When querying the Droplet, the entire size object will be
                 returned. Note that the disk volume of a droplet may not match the size's disk due
                 to Droplet resize actions. The disk attribute on the Droplet should always be
                 referenced.
    :param size_slug: The unique slug identifier for the size of this Droplet.
    :param networks: The details of the network that are configured for the Droplet instance. This
                     is an object that contains keys for IPv4 and IPv6. The value of each of these
                     is an array that contains objects describing an individual IP resource
                     allocated to the Droplet. These will define attributes like the IP address,
                     netmask, and gateway of the specific network depending on the type of network
                     it is.
    :param kernel: The current kernel. This will initially be set to the kernel of the base image
                   when the Droplet is created.
    :param next_backup_window: The details of the Droplet's backups feature, if backups are
                               configured for the Droplet. This object contains keys for the start
                               and end times of the window during which the backup will start.
    :param tags: An array of Tags the Droplet has been tagged with.
    :param volume_ids: A flat array including the unique identifier for each Block Storage volume
                       attached to the Droplet.

    :type id: number
    :type name: string
    :type memory: number
    :type vcpus: number
    :type disk: number
    :type locked: boolean
    :type created_at: string
    :type status: string
    :type backup_ids: array
    :type snapshot_ids: array
    :type features: array
    :type region: object
    :type image: object
    :type size: object
    :type size_slug: string
    :type networks: object
    :type kernel: nullable object
    :type next_backup_window: nullable object
    :type tags: array
    :type volume_ids: array
    """
    def __init__(self,
                 id,
                 name,
                 memory,
                 vcpus,
                 disk,
                 locked,
                 created_at,
                 status,
                 backup_ids,
                 snapshot_ids,
                 features,
                 region,
                 image,
                 size,
                 size_slug,
                 networks,
                 kernel,
                 next_backup_window,
                 tags,
                 volume_ids):
        """

        :param id:
        :param name:
        :param memory:
        :param vcpus:
        :param disk:
        :param locked:
        :param created_at:
        :param status:
        :param backup_ids:
        :param snapshot_ids:
        :param features:
        :param region:
        :param image:
        :param size:
        :param size_slug:
        :param networks:
        :param kernel:
        :param next_backup_window:
        :param tags:
        :param volume_ids:
        """
        self.id = id
        self.name = name
        self.memory = memory
        self.vcpus = vcpus
        self.disk = disk
        self.locked = locked
        self.created_at = created_at
        self.status = status
        self.backup_ids = backup_ids
        self.snapshot_ids = snapshot_ids
        self.features = features
        self.region = region
        self.image = image
        self.size = size
        self.size_slug = size_slug
        self.networks = networks
        self.kernel = kernel
        self.next_backup_window = next_backup_window
        self.tags = tags
        self.volume_ids = volume_ids

        self.response = None

    def public_ipv4(self):
        for ip in self.networks['v4']:
            if ip['type'] == 'public':
                return ip['ip_address']
