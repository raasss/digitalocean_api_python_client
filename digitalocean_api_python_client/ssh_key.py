class SshKey(object):
    def __init__(self,
                 id,
                 fingerprint,
                 public_key,
                 name):
        self.id = id
        self.fingerprint = fingerprint
        self.public_key = public_key
        self.name = name

    def __repr__(self):
        return str(vars(self))

    def __repr__(self):
        s = 'id          : {}\n'.format(self.id)
        s += 'fingerprint : {}\n'.format(self.fingerprint)
        s += 'public_key  : {}\n'.format(self.public_key)
        s += 'name        : {}'.format(self.name)

        return s
