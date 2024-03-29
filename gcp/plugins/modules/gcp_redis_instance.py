#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: google.gcp.gcp_redis_instance
description:
- A Google Cloud Redis instance.
short_description: Creates a GCP Instance
version_added: 2.8
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  alternative_location_id:
    description:
    - Only applicable to STANDARD_HA tier which protects the instance against zonal
      failures by provisioning it across two zones.
    - If provided, it must be a different zone from the one provided in [locationId].
    required: false
    type: str
  authorized_network:
    description:
    - The full name of the Google Compute Engine network to which the instance is
      connected. If left unspecified, the default network will be used.
    required: false
    type: str
  display_name:
    description:
    - An arbitrary and optional user-provided name for the instance.
    required: false
    type: str
  labels:
    description:
    - Resource labels to represent user provided metadata.
    required: false
    type: dict
  redis_configs:
    description:
    - Redis configuration parameters, according to U(http://redis.io/topics/config).
    - 'Please check Memorystore documentation for the list of supported parameters:
      U(https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs)
      .'
    required: false
    type: dict
  location_id:
    description:
    - The zone where the instance will be provisioned. If not provided, the service
      will choose a zone for the instance. For STANDARD_HA tier, instances will be
      created across two zones for protection against zonal failures. If [alternativeLocationId]
      is also provided, it must be different from [locationId].
    required: false
    type: str
  name:
    description:
    - The ID of the instance or a fully qualified identifier for the instance. .
    required: true
    type: str
  memory_size_gb:
    description:
    - Redis memory size in GiB.
    required: true
    type: int
  redis_version:
    description:
    - 'The version of Redis software. If not provided, latest supported version will
      be used. Currently, the supported values are: - REDIS_4_0 for Redis 4.0 compatibility
      - REDIS_3_2 for Redis 3.2 compatibility .'
    required: false
    type: str
  reserved_ip_range:
    description:
    - The CIDR range of internal addresses that are reserved for this instance. If
      not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29
      or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing subnets
      in an authorized network.
    required: false
    type: str
  tier:
    description:
    - 'The service tier of the instance. Must be one of these values: - BASIC: standalone
      instance - STANDARD_HA: highly available primary/replica instances .'
    - 'Some valid choices include: "BASIC", "STANDARD_HA"'
    required: false
    default: BASIC
    type: str
  region:
    description:
    - The name of the Redis region of the instance.
    required: true
    type: str
extends_documentation_fragment: google.gcp.gcp
notes:
- 'API Reference: U(https://cloud.google.com/memorystore/docs/redis/reference/rest/)'
- 'Official Documentation: U(https://cloud.google.com/memorystore/docs/redis/)'
'''

EXAMPLES = '''
- name: create a network
  gcp_compute_network:
    name: network-instance
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a instance
  gcp_redis_instance:
    name: instance37
    tier: STANDARD_HA
    memory_size_gb: 1
    region: us-central1
    location_id: us-central1-a
    redis_version: REDIS_3_2
    display_name: Ansible Test Instance
    reserved_ip_range: 192.168.0.0/29
    labels:
      my_key: my_val
      other_key: other_val
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
alternativeLocationId:
  description:
  - Only applicable to STANDARD_HA tier which protects the instance against zonal
    failures by provisioning it across two zones.
  - If provided, it must be a different zone from the one provided in [locationId].
  returned: success
  type: str
authorizedNetwork:
  description:
  - The full name of the Google Compute Engine network to which the instance is connected.
    If left unspecified, the default network will be used.
  returned: success
  type: str
createTime:
  description:
  - The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
  returned: success
  type: str
currentLocationId:
  description:
  - The current zone where the Redis endpoint is placed.
  - For Basic Tier instances, this will always be the same as the [locationId] provided
    by the user at creation time. For Standard Tier instances, this can be either
    [locationId] or [alternativeLocationId] and can change after a failover event.
  returned: success
  type: str
displayName:
  description:
  - An arbitrary and optional user-provided name for the instance.
  returned: success
  type: str
host:
  description:
  - Hostname or IP address of the exposed Redis endpoint used by clients to connect
    to the service.
  returned: success
  type: str
labels:
  description:
  - Resource labels to represent user provided metadata.
  returned: success
  type: dict
redisConfigs:
  description:
  - Redis configuration parameters, according to U(http://redis.io/topics/config).
  - 'Please check Memorystore documentation for the list of supported parameters:
    U(https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs)
    .'
  returned: success
  type: dict
locationId:
  description:
  - The zone where the instance will be provisioned. If not provided, the service
    will choose a zone for the instance. For STANDARD_HA tier, instances will be created
    across two zones for protection against zonal failures. If [alternativeLocationId]
    is also provided, it must be different from [locationId].
  returned: success
  type: str
name:
  description:
  - The ID of the instance or a fully qualified identifier for the instance. .
  returned: success
  type: str
memorySizeGb:
  description:
  - Redis memory size in GiB.
  returned: success
  type: int
port:
  description:
  - The port number of the exposed Redis endpoint.
  returned: success
  type: int
redisVersion:
  description:
  - 'The version of Redis software. If not provided, latest supported version will
    be used. Currently, the supported values are: - REDIS_4_0 for Redis 4.0 compatibility
    - REDIS_3_2 for Redis 3.2 compatibility .'
  returned: success
  type: str
reservedIpRange:
  description:
  - The CIDR range of internal addresses that are reserved for this instance. If not
    provided, the service will choose an unused /29 block, for example, 10.0.0.0/29
    or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing subnets
    in an authorized network.
  returned: success
  type: str
tier:
  description:
  - 'The service tier of the instance. Must be one of these values: - BASIC: standalone
    instance - STANDARD_HA: highly available primary/replica instances .'
  returned: success
  type: str
region:
  description:
  - The name of the Redis region of the instance.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.gcp.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            alternative_location_id=dict(type='str'),
            authorized_network=dict(type='str'),
            display_name=dict(type='str'),
            labels=dict(type='dict'),
            redis_configs=dict(type='dict'),
            location_id=dict(type='str'),
            name=dict(required=True, type='str'),
            memory_size_gb=dict(required=True, type='int'),
            redis_version=dict(type='str'),
            reserved_ip_range=dict(type='str'),
            tier=dict(default='BASIC', type='str'),
            region=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), fetch)
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, create_link(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'redis')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, fetch):
    auth = GcpSession(module, 'redis')
    params = {'updateMask': updateMask(resource_to_request(module), response_to_hash(module, fetch))}
    request = resource_to_request(module)
    del request['name']
    return wait_for_operation(module, auth.patch(link, request, params=params))


def updateMask(request, response):
    update_mask = []
    if request.get('displayName') != response.get('displayName'):
        update_mask.append('displayName')
    if request.get('labels') != response.get('labels'):
        update_mask.append('labels')
    if request.get('redisConfigs') != response.get('redisConfigs'):
        update_mask.append('redisConfigs')
    if request.get('memorySizeGb') != response.get('memorySizeGb'):
        update_mask.append('memorySizeGb')
    return ','.join(update_mask)


def delete(module, link):
    auth = GcpSession(module, 'redis')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'alternativeLocationId': module.params.get('alternative_location_id'),
        u'authorizedNetwork': module.params.get('authorized_network'),
        u'displayName': module.params.get('display_name'),
        u'labels': module.params.get('labels'),
        u'redisConfigs': module.params.get('redis_configs'),
        u'locationId': module.params.get('location_id'),
        u'name': module.params.get('name'),
        u'memorySizeGb': module.params.get('memory_size_gb'),
        u'redisVersion': module.params.get('redis_version'),
        u'reservedIpRange': module.params.get('reserved_ip_range'),
        u'tier': module.params.get('tier'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'redis')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://redis.googleapis.com/v1/projects/{project}/locations/{region}/instances/{name}".format(**module.params)


def collection(module):
    return "https://redis.googleapis.com/v1/projects/{project}/locations/{region}/instances".format(**module.params)


def create_link(module):
    return "https://redis.googleapis.com/v1/projects/{project}/locations/{region}/instances?instanceId={name}".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'alternativeLocationId': module.params.get('alternative_location_id'),
        u'authorizedNetwork': module.params.get('authorized_network'),
        u'createTime': response.get(u'createTime'),
        u'currentLocationId': module.params.get('current_location_id'),
        u'displayName': response.get(u'displayName'),
        u'host': response.get(u'host'),
        u'labels': response.get(u'labels'),
        u'redisConfigs': response.get(u'redisConfigs'),
        u'locationId': module.params.get('location_id'),
        u'name': module.params.get('name'),
        u'memorySizeGb': response.get(u'memorySizeGb'),
        u'port': response.get(u'port'),
        u'redisVersion': module.params.get('redis_version'),
        u'reservedIpRange': module.params.get('reserved_ip_range'),
        u'tier': module.params.get('tier'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://redis.googleapis.com/v1/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response)
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['done'])
    wait_done = wait_for_completion(status, op_result, module)
    raise_if_errors(wait_done, ['error'], module)
    return navigate_hash(wait_done, ['response'])


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while not status:
        raise_if_errors(op_result, ['error'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, False)
        status = navigate_hash(op_result, ['done'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


if __name__ == '__main__':
    main()
