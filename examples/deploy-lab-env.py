import digitalocean_api_python_client
import time

# import logging

# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

client = digitalocean_api_python_client.Client()

###############################################################################
### testing client.ssh_keys.all()
###############################################################################

print
print('### Getting all SSH Keys ###')
print

print('>>> Fetching all SSH Keys associated with DigitalOcean account...\n')
ssh_keys = client.ssh_keys.all()

my_ssh_keys = []
for ssh_key in ssh_keys:
    print('{}\n'.format(ssh_key))
    my_ssh_keys.append(ssh_key.fingerprint)

print('>>> While printing fetched ssh keys we already generated array of key fingerprints to be used in droplet '
      'creation.\n')
print('my_ssh_keys = {}\n'.format(my_ssh_keys))

temp_ssh_key_fingerprint = 'f0:13:aa:90:5c:2f:7f:6d:dd:5b:55:0b:40:07:18:de'
temp_ssh_key_def = {'name': 'Temp SSH Public Key',
                    'public_key': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCjQFINvxMD/3ZZZUGOZrtQ2ltNWHC1GYWGToVmUYKcnTZL62T+fg1I0zFA0aI66ZmE2Wxv5k/M02gdunAeqsknYH8VLSTqcqNoYjFxJ7uvfEIbFq/pGjH/dugoOlS4duUmc0OAgbHykLU5X5Qi/FM5wHyZpuvGavCDxHh8aLtAMSL2t28cVVKggyEppW94d+uuudphKtT5PDLV6Q0WkDa312QoghkklbUD6kKh8oAkFgpVXTvX3yQ3fpAI/hCHhJ2tihuMpgjjoIdHgqSAo9IfTc7YSXrTUx81/zeBlASUrZMRiY8UFwDbBmAGG4H3nDRqNELlZNPYEiCeHUCXtMhF temp_public_key'}

print('>>> Checking if Temp SSH key with known fingerprint already exists\n')
try:
    temp_ssh_key = client.ssh_keys.find(temp_ssh_key_fingerprint)
except ValueError:
    temp_ssh_key = None

if temp_ssh_key is not None:
    print('>>> Found Temp SSH key\n')
    print(temp_ssh_key)

    print('>>> Deleting Temp SSH key with fingerprint {}\n'.format(temp_ssh_key_fingerprint))
    client.ssh_keys.delete(temp_ssh_key_fingerprint)
else:
    print('>>> Temp SSH key with fingerprint {} does not exist.\n'.format(temp_ssh_key_fingerprint))

###############################################################################
### testing client.ssh_keys.create()
###############################################################################

print('>>> Adding Temp SSH key to DigitalOcean account...\n')
temp_ssh_key = client.ssh_keys.create(temp_ssh_key_def)
print(temp_ssh_key)

###############################################################################
### testing client.ssh_keys.update()
###############################################################################

print('>>> Updating Temp SSH key to "Temp SSH Public Key - updated\n')
temp_ssh_key_updated = client.ssh_keys.update(temp_ssh_key.id, 'Temp SSH Public Key - updated')
if temp_ssh_key_updated.name == 'Temp SSH Public Key - updated':
    print(temp_ssh_key_updated)
else:
    raise RuntimeError('Temp SSH Public Key name updating failed!')

###############################################################################
### testing client.ssh_keys.find()
###############################################################################

print('>>> Finding Temp SSH Public Key by already known fingerprint\n')
temp_ssh_key_updated2 = client.ssh_keys.find(temp_ssh_key_fingerprint)
if temp_ssh_key_updated2.fingerprint == temp_ssh_key_fingerprint:
    print('>>> Found Temp SSH Public Key by fingerprint {}\n'.format(temp_ssh_key_fingerprint))
    print(temp_ssh_key_updated2)

print('>>> Finding Temp SSH Public Key by already known ID\n')
temp_ssh_key_updated2 = client.ssh_keys.find(temp_ssh_key_updated.id)
if temp_ssh_key_updated2.fingerprint == temp_ssh_key_fingerprint:
    print('>>> Found Temp SSH Public Key by ID {}\n'.format(temp_ssh_key_updated.id))
    print(temp_ssh_key_updated2)

###############################################################################
###############################################################################
###############################################################################

print
print('### Creating droplet(s) ###')
print

droplet1_def = {'name': 'droplet1',
                'region': 'fra1',
                'size': '512mb',
                'image': 'ubuntu-16-04-x64',
                'ssh_keys': my_ssh_keys,
                'backups': False,
                'ipv6': True,
                'user_data': None,
                'private_networking': True,
                'volumes': None}

droplets = client.droplets.all()

i = 0
for droplet in droplets:
    print('>>> Found droplet: {}'.format(vars(droplet)))
    if droplet.name == droplet1_def['name'] && droplet.region == droplet1_def['region']:
        print('>>> Droplet already created!')
        droplet1 = droplet
        i += 1
    if i > 1:
        raise ValueError('Found multiple droplets but expecting only one!')

if i == 0:
    print('>>> Creating droplet ...')
    droplet1 = client.droplets.create(droplet1_def)

if droplet1.locked == True:
    while True:
        droplet1 = client.droplets.find(droplet1.id)
        if droplet1.locked == False:
            break
        print("Droplet {} still locked. Sleeping for 5s ...".format(droplet1.id))
        time.sleep(5)

print
print('droplet1 = {}'.format(vars(droplet1)))

print
print('### Enable backups for just created droplet ###')
print

droplet1 = client.droplets.find(droplet1.id)
if 'backups' not in droplet1.features:
    print('>>> Enabling backups for {}...'.format(droplet1.name))
    action = client.droplet_actions.enable_backups(droplet1.id)
else:
    print('>>> Backups already enabled for {}.'.format(droplet1.name))

print
print('droplet1.features = {}'.format(droplet1.features))

###############################################################################
###############################################################################
###############################################################################

print
print('### Creating/attaching volume(s) ###')
print

volume1_def = {"size_gigabytes": 10,
               "name": "volume-droplet1-1",
               "description": "Block store for api testing",
               "region": droplet1.region['slug']}

volumes = client.volumes.all()

volume1 = None
for volume in volumes:
    print('>>> Found volume: {}'.format(vars(volume)))
    if volume.name == volume1_def['name']:
        print('>>> Volume already created!')
        volume1 = volume
        break

if volume1 is None:
    print('>>> Creating volume ...')
    volume1 = client.volumes.create(volume1_def)

print
print('volume1 = {}'.format(vars(volume1)))

if droplet1.id not in volume1.droplet_ids:
    print('>>> Attaching volume to droplet ...')
    client.volume_actions.attach(volume_id=volume1.id,
                                 droplet_id=droplet1.id,
                                 region=volume1.region['slug'])
else:
    print('>>> Volume already attached to droplet!')

print
print('volume1 = {}'.format(vars(volume1)))

###############################################################################
###############################################################################
###############################################################################

print
print('### Creating domain(s) ###')
print

domain1_def = {'name': 'tokatiti.com',
               'ip_address': droplet1.public_ipv4()}

domains = client.domains.all()

domain1 = None
for domain in domains:
    print('>>> Found domain: {}'.format(vars(domain)))
    if domain.name == domain1_def['name']:
        print('>>> Domain already created!')
        domain1 = domain
        break

if domain1 is None:
    print('>>> Creating domain ...')
    domain1 = client.domains.create(domain1_def)

print
print('domain1: {}'.format(vars(domain1)))

print
print('### Find just created domain ###')
print

domain = client.domains.find(domain1_def['name'])

print
print('domain: {}'.format(vars(domain)))

###############################################################################
###############################################################################
###############################################################################

print
print('### Creating domain record(s) ###')
print

drecord1_def = {'type': 'A',
                'name': droplet1.name,
                'data': droplet1.public_ipv4()}

drecords = client.domain_records.all(domain1.name)

drecord1 = None
for drecord in drecords:
    print('>>> Found domain record: {}'.format(vars(drecord)))
    if drecord.name == drecord1_def['name']:
        print('>>> Domain record already created!')
        drecord1 = drecord
        break

if drecord1 is None:
    print('>>> Creating domain record ...')
    drecord1 = client.domain_records.create(drecord1_def, domain1.name)

print
print('drecord1 = {}'.format(vars(drecord1)))

print
print('### Find previously created domain record ###')
print

drecord2 = client.domain_records.find(domain_name=domain1.name, record_id=drecord1.id)

print
print('drecord2 = {}'.format(vars(drecord2)))

print
print('### Delete/Create/Update test record ###')
print

drecord3_def = {'type': 'A',
                'name': 'droplet-test-alias',
                'data': droplet1.public_ipv4()}

drecord4_def = {'name': 'droplet-updated-alias'}

drecords = client.domain_records.all(domain1.name)

drecord3 = None
drecord4 = None
for drecord in drecords:
    if drecord.name == drecord3_def['name']:
        drecord3 = drecord
    if drecord.name == drecord4_def['name']:
        drecord4 = drecord
    if drecord3 is not None and drecord4 is not None:
        break

if drecord3 is not None:
    client.domain_records.delete(for_domain=domain1.name, record_id=drecord3.id)

if drecord4 is not None:
    client.domain_records.delete(for_domain=domain1.name, record_id=drecord4.id)

drecord3 = client.domain_records.create(record=drecord3_def, for_domain=domain1.name)

print
print('drecord3 = {}'.format(vars(drecord3)))

drecord4 = client.domain_records.update(record=drecord4_def, for_domain=domain1.name, record_id=drecord3.id)

print
print('drecord4 = {}'.format(vars(drecord4)))
