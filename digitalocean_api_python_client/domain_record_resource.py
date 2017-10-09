from .api import Api


class DomainRecordResource(Api):
    """Domain Records resources

    Domain record resources are used to set or retrieve information about the
    individual DNS records configured for a domain. This allows you to build
    and manage DNS zone files by adding and modifying individual records for a
    domain.

    .. todo:: The DigitalOcean DNS management interface allows you to
        configure the following DNS records: ???

    There is also an additional field called id that is auto-assigned for each
    record and used as a unique identifier for requests. Each record contains
    all of these attribute types. For record types that do not utilize all
    fields, a value of null will be set for that record.

    .. seealso:: https://developers.digitalocean.com/documentation/v2/#domain-records
    """

    def __init__(self):
        self.path = '/v2/domains'

    def all(self, domain_name, page=None, per_page=None):
        """List all Domain Records

        Get a listing of all records configured for a domain.

        The response will be a JSON object with a key called domain_records.
        The value of this will be an array of domain record objects, each of
        which contains the standard domain record attributes.

        For attributes that are not used by a specific record type, a value of
        null will be returned. For instance, all records other than SRV will
        have null for the weight and port attributes.

        .. seealso::  https://developers.digitalocean.com/documentation/v2/#list-all-domain-records

        """
        query = '/{}/records?page={}&per_page={}'.format(domain_name, page or 1, per_page or self.per_page)

        return self.get_paginator(method='GET',
                                  url=self.add_query_to_url(query),
                                  headers=self.headers,
                                  body=None,
                                  response_ok=200,
                                  response_body_json_key='domain_records',
                                  page=page,
                                  per_page=per_page)

    def create(self, record, for_domain):
        """Create a new Domain Record

        To create a new record to a domain, request must include all of the
        required fields for the domain record type being added. The required
        attributes per domain record type:

        +------------+-------------------+-------------------------------------------------------------------------------------------------------------------+------------------------------------+
        | Name       | Type              | Description                                                                                                       | Required                           |
        +============+===================+===================================================================================================================+====================================+
        | type       | string            | The record type (A, MX, CNAME, etc).                                                                              | All Records                        |
        +------------+-------------------+-------------------------------------------------------------------------------------------------------------------+------------------------------------+
        | name       | string            | The host name, alias, or service being defined by the record.                                                     | A, AAAA, CNAME, TXT, SRV           |
        +------------+-------------------+-------------------------------------------------------------------------------------------------------------------+------------------------------------+
        | data       | string            | Variable data depending on record type. See the [Domain Records]() section for more detail on each record type.   | A, AAAA, CNAME, MX, TXT, SRV, NS   |
        +------------+-------------------+-------------------------------------------------------------------------------------------------------------------+------------------------------------+
        | priority   | nullable number   | The priority of the host (for SRV and MX records. null otherwise).                                                | MX, SRV                            |
        +------------+-------------------+-------------------------------------------------------------------------------------------------------------------+------------------------------------+
        | port       | nullable number   | The port that the service is accessible on (for SRV records only. null otherwise).                                | SRV                                |
        +------------+-------------------+-------------------------------------------------------------------------------------------------------------------+------------------------------------+
        | weight     | nullable number   | The weight of records with the same priority (for SRV records only. null otherwise).                              | SRV                                |
        +------------+-------------------+-------------------------------------------------------------------------------------------------------------------+------------------------------------+

        :param record: Domain record definition.
        :param for_domain: Domain name where domain record should be created.

        :type record: dict
        :type for_domain: str

        :return: DomainRecord

        Example of A record parameter::

            record1 = {'type': 'A',
                       'name': 'www1',
                       'data': '127.127.127.127'}

        Example of MX record parameter::

            record2 = {'type': 'MX',
                       'name': 'smtp',
                       'data': '127.127.127.127',
                       'priority': 20}

        Example of SRV record parameter::

            record3 = {'type': 'SRV',
                       'name': '_http._tcp',
                       'data': 'www.example.com',
                       'priority': 10,
                       'port': 80,
                       'weight': 50}

        .. seealso:: https://developers.digitalocean.com/documentation/v2/#create-a-new-domain-record
        """
        query = "/{}/records".format(for_domain)

        return self.get_object(method='POST',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=record,
                               response_ok=201,
                               response_body_json_key='domain_record')

    def find(self, domain_name, record_id):
        query = "/{}/records/{}".format(domain_name, record_id)

        return self.get_object(method='GET',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=None,
                               response_ok=200,
                               response_body_json_key='domain_record')

    def update(self, record, for_domain, record_id):
        query = "/{}/records/{}".format(for_domain, record_id)

        return self.get_object(method='PUT',
                               url=self.add_query_to_url(query),
                               headers=self.headers,
                               body=record,
                               response_ok=200,
                               response_body_json_key='domain_record')

    def delete(self, for_domain, record_id):
        query = "/{}/records/{}".format(for_domain, record_id)

        return self.request(method='DELETE',
                            url=self.add_query_to_url(query),
                            headers=self.headers,
                            body=None,
                            response_ok=204)
