class Domain(object):
    def __init__(self,
                 name,
                 ttl,
                 zone_file):
        self.name = name
        self.ttl = ttl
        self.zone_file = zone_file
