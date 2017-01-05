class DomainRecord(object):
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
