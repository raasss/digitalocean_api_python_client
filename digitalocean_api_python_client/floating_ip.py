class FloatingIp(object):
    """Floating IP object as per https://developers.digitalocean.com/documentation/v2/#floating-ips

    :param ip: The public IP address of the Floating IP. It also serves as its identifier.
    :param region: The region that the Floating IP is reserved to. When you query a Floating IP, the
                   entire region object will be returned.
    :param droplet: The Droplet that the Floating IP has been assigned to. When you query a Floating
                    IP, if it is assigned to a Droplet, the entire Droplet object will be returned.
                    If it is not assigned, the value will be null.

    :type ip: string
    :type region: object
    :type droplet: object
    """
    def __init__(self,
                 ip,
                 region,
                 droplet):
        self.ip = ip
        self.region = region
        self.droplet = droplet
