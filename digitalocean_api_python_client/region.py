class Region(object):
    """Region object as per https://developers.digitalocean.com/documentation/v2/#regions

    :param slug: A human-readable string that is used as a unique identifier for each region.
    :param name: The display name of the region. This will be a full name that is used in the
                 control panel and other interfaces.
    :param sizes: This attribute is set to an array which contains the identifying slugs for the
                  sizes available in this region.
    :param available: This is a boolean value that represents whether new Droplets can be created in
                      this region.
    :param features: This attribute is set to an array which contains features available in this
                     region.

    :type slug: string
    :type name: string
    :type sizes: array
    :type available: boolean
    :type features: array
    """

    def __init__(self,
                 slug,
                 name,
                 sizes,
                 available,
                 features):
        self.slug = slug
        self.name = name
        self.sizes = sizes
        self.available = available
        self.features = features
