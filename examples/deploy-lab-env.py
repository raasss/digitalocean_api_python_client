import digitalocean_api_python_client
import time

# import logging

# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

client = digitalocean_api_python_client.Client()

###############################################################################
###############################################################################
###############################################################################

print
print('### Getting all SSH Keys ###')
print

ssh_keys = client.ssh_keys.all()

my_ssh_keys = []
for ssh_key in ssh_keys:
    print('>>> Found ssh_key: {}'.format(vars(ssh_key)))
    my_ssh_keys.append(ssh_key.fingerprint)

print
print('my_ssh_keys = {}'.format(my_ssh_keys))

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
    if droplet.name == droplet1_def['name']:
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

quit()

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
