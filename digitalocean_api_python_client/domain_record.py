class DomainRecord(object):
    """Domain Record object as per https://developers.digitalocean.com/documentation/v2/#domain-records

    :param id: A unique identifier for each domain record.
    :param type: The type of the DNS record (ex: A, CNAME, TXT, ...).
    :param name: The name to use for the DNS record.
    :param data: The value to use for the DNS record.
    :param priority: The priority for SRV and MX records.
    :param port:  The port for SRV records.
    :param weight: The weight for SRV records.

    :type id: number
    :type type: string
    :type name: string
    :type data: string
    :type priority: nullable number
    :type port: nullable number
    :type weight: nullable number
    """
    def __init__(self,
                 id,
                 type,
                 name,
                 data,
                 priority,
                 port,
                 weight):
        self.id = id
        self.type = type
        self.name = name
        self.data = data
        self.priority = priority
        self.port = port
        self.weight = weight
