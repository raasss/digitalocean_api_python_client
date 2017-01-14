class Size(object):
    """Size object as per https://developers.digitalocean.com/documentation/v2/#sizes

    :param slug: A human-readable string that is used to uniquely identify each size.
    :param available: This is a boolean value that represents whether new Droplets can be created with this size.
    :param transfer: The amount of transfer bandwidth that is available for Droplets created in this size. This only counts traffic on the public interface. The value is given in terabytes.
    :param price_monthly: This attribute describes the monthly cost of this Droplet size if the Droplet is kept for an entire month. The value is measured in US dollars.
    :param price_hourly: This describes the price of the Droplet size as measured hourly. The value is measured in US dollars.
    :param memory: The amount of RAM allocated to Droplets created of this size. The value is represented in megabytes.
    :param vcpus: The number of virtual CPUs allocated to Droplets of this size.
    :param disk: The amount of disk space set aside for Droplets of this size. The value is represented in gigabytes.
    :param regions: An array containing the region slugs where this size is available for Droplet creates.

    :type slug: string
    :type available: boolean
    :type transfer: number
    :type price_monthly: number
    :type price_hourly: number
    :type memory: number
    :type vcpus: number
    :type disk: number
    :type regions: array
    """

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
