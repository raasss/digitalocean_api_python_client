class Image(object):
    """Image object as per https://developers.digitalocean.com/documentation/v2/#images

    :param id: A unique number that can be used to identify and reference a specific image.
    :param name: The display name that has been given to an image. This is what is shown in the control panel and is generally a descriptive title for the image in question.
    :param type: The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".
    :param distribution: This attribute describes the base distribution used for this image.
    :param slug: A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.
    :param public: This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account.
    :param regions: This attribute is an array of the regions that the image is available in. The regions are represented by their identifying slug values.
    :param min_disk_size: The minimum 'disk' required for a size to use this image.
    :param size_gigabytes: The size of the image in gigabytes.
    :param created_at: A time value given in ISO8601 combined date and time format that represents when the Image was created.

    :type id: number
    :type name: string
    :type type: string
    :type distribution: string
    :type slug: nullable string
    :type public: boolean
    :type regions: array
    :type min_disk_size: number
    :type size_gigabytes: number
    :type created_at: string
    """

    def __init__(self,
                 id,
                 name,
                 type,
                 distribution,
                 slug,
                 public,
                 regions,
                 min_disk_size,
                 size_gigabytes,
                 created_at):
        self.id = id
        self.name = name
        self.type = type
        self.distribution = distribution
        self.slug = slug
        self.public = public
        self.regions = regions
        self.min_disk_size = min_disk_size
        self.size_gigabytes = size_gigabytes
        self.created_at = created_at
