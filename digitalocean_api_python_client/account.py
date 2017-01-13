class Account(object):
    """Account object as per https://developers.digitalocean.com/documentation/v2/#account"""

    def __init__(self,
                 droplet_limit,
                 floating_ip_limit,
                 email,
                 uuid,
                 email_verified,
                 status,
                 status_message):

        self.droplet_limit = droplet_limit
        """(int) The total number of droplets the user may have."""

        self.floating_ip_limit = floating_ip_limit
        """(int) The total number of floating IPs the user may have."""

        self.email = email
        """(str) The email the user has registered for Digital Ocean with."""

        self.uuid = uuid
        """(str) The universal identifier for this user (alphanumeric)."""

        self.email_verified = email_verified
        """(bool) If true, the user has verified their account via email. False otherwise."""

        self.status = status
        """(str) This value is one of "active", "warning" or "locked"."""

        self.status_message = status_message
        """(str) A human-readable message giving more details about the status of the account."""

    def __repr__(self):
        s = 'uuid             : {}\n'.format(self.uuid)
        s += 'email            : {}\n'.format(self.email)
        s += 'email_verified   : {}\n'.format(self.email_verified)
        s += 'droplet_limit    : {}\n'.format(self.droplet_limit)
        s += 'floating_ip_limit: {}\n'.format(self.floating_ip_limit)
        s += 'status           : {}\n'.format(self.status)
        s += 'status_message   : {}'.format(self.status_message or None)

        return s
