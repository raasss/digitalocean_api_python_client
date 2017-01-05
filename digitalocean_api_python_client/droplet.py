class Droplet(object):
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
