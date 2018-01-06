class Kernel(object):
    """Kernel object as per
    https://developers.digitalocean.com/documentation/v2/#list-all-available-kernels-for-a-droplet

    :param id: A unique number used to identify and reference a specific kernel.
    :param name: The display name of the kernel. This is shown in the web UI and is generally a
                 descriptive title for the kernel in question.
    :param version: A standard kernel version string representing the version, patch, and release
                    information.

    :type id: number
    :type name: string
    :type version: string
    """

    def __init__(self,
                 id,
                 name,
                 version):
        self.id = id
        self.name = name
        self.version = version
