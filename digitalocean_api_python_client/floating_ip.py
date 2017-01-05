class FloatingIp(object):
    def __init__(self,
                 ip,
                 region,
                 droplet):
        self.ip = ip
        self.region = region
        self.droplet = droplet
