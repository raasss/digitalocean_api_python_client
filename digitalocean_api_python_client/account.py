class Account(object):
    """Account class as per https://developers.digitalocean.com/documentation/v2/#account"""

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
