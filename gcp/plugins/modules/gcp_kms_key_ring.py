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
module: google.gcp.gcp_kms_key_ring
description:
- A `KeyRing` is a toplevel logical grouping of `CryptoKeys`.
short_description: Creates a GCP KeyRing
version_added: 2.9
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
  name:
    description:
    - The resource name for the KeyRing.
    required: true
    type: str
  location:
    description:
    - The location for the KeyRing.
    - A full list of valid locations can be found by running `gcloud kms locations
      list`.
    required: true
    type: str
extends_documentation_fragment: google.gcp.gcp
notes:
- 'API Reference: U(https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings)'
- 'Creating a key ring: U(https://cloud.google.com/kms/docs/creating-keys#create_a_key_ring)'
'''

EXAMPLES = '''
- name: create a key ring
  gcp_kms_key_ring:
    name: test_object
    location: us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - The resource name for the KeyRing.
  returned: success
  type: str
creationTime:
  description:
  - The time that this resource was created on the server.
  - This is in RFC3339 text format.
  returned: success
  type: str
location:
  description:
  - The location for the KeyRing.
  - A full list of valid locations can be found by running `gcloud kms locations list`.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.gcp.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            location=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloudkms']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module))
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
    auth = GcpSession(module, 'kms')
    return return_if_object(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    delete(module, self_link(module))
    create(module, create_link(module))


def delete(module, link):
    module.fail_json(msg="KeyRings cannot be deleted")


def resource_to_request(module):
    request = {u'name': module.params.get('name')}
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'kms')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://cloudkms.googleapis.com/v1/projects/{project}/locations/{location}/keyRings/{name}".format(**module.params)


def collection(module):
    return "https://cloudkms.googleapis.com/v1/projects/{project}/locations/{location}/keyRings".format(**module.params)


def create_link(module):
    return "https://cloudkms.googleapis.com/v1/projects/{project}/locations/{location}/keyRings?keyRingId={name}".format(**module.params)


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

    result = decode_response(result, module)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)
    request = decode_response(request, module)

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
    return {u'name': response.get(u'name'), u'creationTime': response.get(u'creationTime')}


def decode_response(response, module):
    if 'name' in response:
        response['name'] = response['name'].split('/')[-1]
    return response


if __name__ == '__main__':
    main()
