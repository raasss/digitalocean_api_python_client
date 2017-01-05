from .api import Api
from .account_resource import AccountResource
from .image_resource import ImageResource
from .action_resources import ActionResource
from .volume_resources import VolumeResource
from .volume_action_resources import VolumeActionResource
from .domain_resource import DomainResource
from .domain_record_resource import DomainRecordResource
from .droplet_resource import DropletResource
from .droplet_action_resource import DropletActionResource
from .snapshot_resource import SnapshotResource
from .ssh_key_resource import SshKeyResource

import os
import yaml

class Client(object):
    def __init__(self, token=None):

        homedir = os.path.expanduser('~')
        config_file = '{}/.digitalocean_api_python_client/config.yml'.format(homedir)

        if token is not None:
            Api().init(token)
        else:
            if os.path.isfile(config_file):
                with open(config_file, 'r') as f:
                    config = yaml.load(f)
                Api().init(config['access_token'])
            else:
                raise ValueError('token value is unknown!')

        self.account = AccountResource()
        self.images = ImageResource()
        self.actions = ActionResource()
        self.volumes = VolumeResource()
        self.volume_actions = VolumeActionResource()
        self.domains = DomainResource()
        self.domain_records = DomainRecordResource()
        self.droplets = DropletResource()
        self.snapshots = SnapshotResource()
        self.droplet_actions = DropletActionResource()
        self.ssh_keys = SshKeyResource()
