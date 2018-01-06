class SshKey(object):
    """SSH Key object as per https://developers.digitalocean.com/documentation/v2/#ssh-keys

    :param id: This is a unique identification number for the key. This can be used to reference a
               specific SSH key when you wish to embed a key into a Droplet.
    :param fingerprint: This attribute contains the fingerprint value that is generated from the
                        public key. This is a unique identifier that will differentiate it from other keys using a
                        format that SSH recognizes.
    :param public_key: This attribute contains the entire public key string that was uploaded. This
    is what is embedded into the root user's authorized_keys file if you choose to include this SSH
    key during Droplet creation.
    :param name: This is the human-readable display name for the given SSH key. This is used to
    easily identify the SSH keys when they are displayed.

    :type id: number
    :type fingerprint: string
    :type public_key: string
    :type name: string
    """

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
