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
module: google.gcp.gcp_compute_interconnect_attachment_info
description:
- Gather info for GCP InterconnectAttachment
- This module was called C(google.gcp.gcp_compute_interconnect_attachment_facts) before Ansible
  2.9. The usage has not changed.
short_description: Gather info for GCP InterconnectAttachment
version_added: 2.8
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  filters:
    description:
    - A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/sdk/gcloud/reference/topic/filters).
    - Each additional filter in the list will act be added as an AND condition (filter1
      and filter2) .
    type: list
  region:
    description:
    - Region where the regional interconnect attachment resides.
    required: true
    type: str
extends_documentation_fragment: google.gcp.gcp
'''

EXAMPLES = '''
- name: get info on an interconnect attachment
  gcp_compute_interconnect_attachment_info:
    region: us-central1
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    adminEnabled:
      description:
      - Whether the VLAN attachment is enabled or disabled. When using PARTNER type
        this will Pre-Activate the interconnect attachment .
      returned: success
      type: bool
    cloudRouterIpAddress:
      description:
      - IPv4 address + prefix length to be configured on Cloud Router Interface for
        this interconnect attachment.
      returned: success
      type: str
    customerRouterIpAddress:
      description:
      - IPv4 address + prefix length to be configured on the customer router subinterface
        for this interconnect attachment.
      returned: success
      type: str
    interconnect:
      description:
      - URL of the underlying Interconnect object that this attachment's traffic will
        traverse through. Required if type is DEDICATED, must not be set if type is
        PARTNER.
      returned: success
      type: str
    description:
      description:
      - An optional description of this resource.
      returned: success
      type: str
    bandwidth:
      description:
      - Provisioned bandwidth capacity for the interconnect attachment.
      - For attachments of type DEDICATED, the user can set the bandwidth.
      - For attachments of type PARTNER, the Google Partner that is operating the
        interconnect must set the bandwidth.
      - Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED,
        Defaults to BPS_10G .
      returned: success
      type: str
    edgeAvailabilityDomain:
      description:
      - Desired availability domain for the attachment. Only available for type PARTNER,
        at creation time. For improved reliability, customers should configure a pair
        of attachments with one per availability domain. The selected availability
        domain will be provided to the Partner via the pairing key so that the provisioned
        circuit will lie in the specified domain. If not specified, the value will
        default to AVAILABILITY_DOMAIN_ANY.
      returned: success
      type: str
    pairingKey:
      description:
      - '[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier
        of an PARTNER attachment used to initiate provisioning with a selected partner.
        Of the form "XXXXX/region/domain" .'
      returned: success
      type: str
    partnerAsn:
      description:
      - "[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN
        for the router that should be supplied by a layer 3 Partner if they configured
        BGP on behalf of the customer."
      returned: success
      type: str
    privateInterconnectInfo:
      description:
      - Information specific to an InterconnectAttachment. This property is populated
        if the interconnect that this is attached to is of type DEDICATED.
      returned: success
      type: complex
      contains:
        tag8021q:
          description:
          - 802.1q encapsulation tag to be used for traffic between Google and the
            customer, going to and from this network and region.
          returned: success
          type: int
    type:
      description:
      - The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
      returned: success
      type: str
    state:
      description:
      - "[Output Only] The current state of this attachment's functionality."
      returned: success
      type: str
    googleReferenceId:
      description:
      - Google reference ID, to be used when raising support tickets with Google or
        otherwise to debug backend connectivity issues.
      returned: success
      type: str
    router:
      description:
      - URL of the cloud router to be used for dynamic routing. This router must be
        in the same region as this InterconnectAttachment. The InterconnectAttachment
        will automatically connect the Interconnect to the network & region within
        which the Cloud Router is configured.
      returned: success
      type: dict
    creationTimestamp:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    id:
      description:
      - The unique identifier for the resource. This identifier is defined by the
        server.
      returned: success
      type: str
    name:
      description:
      - Name of the resource. Provided by the client when the resource is created.
        The name must be 1-63 characters long, and comply with RFC1035. Specifically,
        the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
        which means the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last character,
        which cannot be a dash.
      returned: success
      type: str
    candidateSubnets:
      description:
      - Up to 16 candidate prefixes that can be used to restrict the allocation of
        cloudRouterIpAddress and customerRouterIpAddress for this attachment.
      - All prefixes must be within link-local address space (169.254.0.0/16) and
        must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused
        /29 from the supplied candidate prefix(es). The request will fail if all possible
        /29s are in use on Google's edge. If not supplied, Google will randomly select
        an unused /29 from all of link-local space.
      returned: success
      type: list
    vlanTag8021q:
      description:
      - The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using
        PARTNER type this will be managed upstream.
      returned: success
      type: int
    region:
      description:
      - Region where the regional interconnect attachment resides.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################
from ansible_collections.google.gcp.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str'), region=dict(required=True, type='str')))

    if module._name == 'gcp_compute_interconnect_attachment_facts':
        module.deprecate(
            "The 'gcp_compute_interconnect_attachment_facts' module has been renamed to 'gcp_compute_interconnect_attachment_info'", version='2.13'
        )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    return_value = {'resources': fetch_list(module, collection(module), query_options(module.params['filters']))}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/interconnectAttachments".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    return auth.list(link, return_if_object, array_name='items', params={'filter': query})


def query_options(filters):
    if not filters:
        return ''

    if len(filters) == 1:
        return filters[0]
    else:
        queries = []
        for f in filters:
            # For multiple queries, all queries should have ()
            if f[0] != '(' and f[-1] != ')':
                queries.append("(%s)" % ''.join(f))
            else:
                queries.append(f)

        return ' '.join(queries)


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
