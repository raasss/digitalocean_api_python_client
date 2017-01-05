class Size(object):
    def __init__(self,
                 slug,
                 available,
                 transfer,
                 price_monthly,
                 price_hourly,
                 memory,
                 vcpus,
                 disk,
                 regions):
        self.slug = slug
        self.available = available
        self.transfer = transfer
        self.price_monthly = price_monthly
        self.price_hourly = price_hourly
        self.memory = memory
        self.vcpus = vcpus
        self.disk = disk
        self.regions = regions
