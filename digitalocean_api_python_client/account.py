class Account(object):
    """Account object as per https://developers.digitalocean.com/documentation/v2/#account

    :param droplet_limit: The total number of droplets the user may have.
    :param floating_ip_limit: The total number of floating IPs the user may have.
    :param email: The email the user has registered for Digital Ocean with.
    :param uuid: The universal identifier for this user (alphanumeric).
    :param email_verified: If true, the user has verified their account via email. False otherwise.
    :param status: This value is one of "active", "warning" or "locked".
    :param status_message: A human-readable message giving more details about the status of the account.

    :type droplet_limit: number
    :type floating_ip_limit: number
    :type email: string
    :type uuid: string alphanumeric
    :type email_verified: boolean
    :type status: string
    :type status_message: string
    """

    def __init__(self,
                 droplet_limit,
                 floating_ip_limit,
                 email,
                 uuid,
                 email_verified,
                 status,
                 status_message):
        self.droplet_limit = droplet_limit
        self.floating_ip_limit = floating_ip_limit
        self.email = email
        self.uuid = uuid
        self.email_verified = email_verified
        self.status = status
        self.status_message = status_message

    def __repr__(self):
        s = 'uuid             : {}\n'.format(self.uuid)
        s += 'email            : {}\n'.format(self.email)
        s += 'email_verified   : {}\n'.format(self.email_verified)
        s += 'droplet_limit    : {}\n'.format(self.droplet_limit)
        s += 'floating_ip_limit: {}\n'.format(self.floating_ip_limit)
        s += 'status           : {}\n'.format(self.status)
        s += 'status_message   : {}'.format(self.status_message or None)

        return s
