import digitalocean_api_python_client
import time

client = digitalocean_api_python_client.Client()

###############################################################################
###############################################################################

account = client.account.info()

print('Cleaning account {} ...'.format(account.email))

###############################################################################
###############################################################################

domains = client.domains.all()

for domain in domains:
    print('Searching for domain records in {}'.format(domain.name))

    drecords = client.domain_records.all(domain_name=domain.name)

    for drecord in drecords:
        print('Deleting domain record (id={}, name={}) ...'.format(drecord.id, drecord.name))
        client.domain_records.delete(for_domain=domain.name, record_id=drecord.id)

    print('Deleting domain (name = {}) ...'.format(domain.name))
    client.domains.delete(domain.name)

###############################################################################
###############################################################################

volumes = client.volumes.all()

for volume in volumes:
    for droplet_id in volume.droplet_ids:
        print(
        'Detaching volume (id={}, name={}) from droplet (id={}) in region (slug={}) ...'.format(volume.id, volume.name,
                                                                                                droplet_id,
                                                                                                volume.region['slug']))
        action = client.volume_actions.detach(volume_id=volume.id, droplet_id=droplet_id, region=volume.region['slug'])
        while action.status != 'completed':
            print("Action status is not completed ({}). Sleeping for 5s ...".format(action.status))
            time.sleep(5)
            action = client.volume_actions.find(volume_id=volume.id, action_id=action.id)

    print('Deleting volume (id={}, name={}) ...'.format(volume.id, volume.name))
    client.volumes.delete(volume.id)

###############################################################################
###############################################################################

snapshots = client.snapshots.all()

for snapshot in snapshots:
    print('Deleting snapshot (id={}, name={}) ...'.format(snapshot.id, snapshot.name))
    client.snapshots.delete(snapshot.id)

###############################################################################
###############################################################################

images = client.images.all(private=True)

for image in images:
    print(image)

    if image.type == 'backup':
        print('Skipping backup image (id={}, name={}) ...'.format(image.id, image.name))
    else:
        print('Deleting image (id={}, name={}) ...'.format(image.id, image.name))
        client.images.delete(image.id)

###############################################################################
###############################################################################

droplets = client.droplets.all()

for droplet in droplets:
    print('Deleting droplet (id={}, name={}) ...'.format(droplet.id, droplet.name))
    client.droplets.delete(droplet.id)

###############################################################################
###############################################################################
