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
module: google.gcp.gcp_compute_url_map
description:
- UrlMaps are used to route requests to a backend service based on rules that you
  define for the host and path of an incoming URL.
short_description: Creates a GCP UrlMap
version_added: 2.6
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
  default_service:
    description:
    - A reference to BackendService resource if none of the hostRules match.
    - 'This field represents a link to a BackendService resource in GCP. It can be
      specified in two ways. First, you can place a dictionary with key ''selfLink''
      and value of your resource''s selfLink Alternatively, you can add `register:
      name-of-resource` to a google.gcp.gcp_compute_backend_service task and then set this default_service
      field to "{{ name-of-resource }}"'
    required: true
    type: dict
  description:
    description:
    - An optional description of this resource. Provide this property when you create
      the resource.
    required: false
    type: str
  host_rules:
    description:
    - The list of HostRules to use against the URL.
    required: false
    type: list
    suboptions:
      description:
        description:
        - An optional description of this HostRule. Provide this property when you
          create the resource.
        required: false
        type: str
      hosts:
        description:
        - The list of host patterns to match. They must be valid hostnames, except
          * will match any string of ([a-z0-9-.]*). In that case, * must be the first
          character and must be followed in the pattern by either - or .
        required: true
        type: list
      path_matcher:
        description:
        - The name of the PathMatcher to use to match the path portion of the URL
          if the hostRule matches the URL's host portion.
        required: true
        type: str
  name:
    description:
    - Name of the resource. Provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
    type: str
  path_matchers:
    description:
    - The list of named PathMatchers to use against the URL.
    required: false
    type: list
    suboptions:
      default_service:
        description:
        - A reference to a BackendService resource. This will be used if none of the
          pathRules defined by this PathMatcher is matched by the URL's path portion.
        - 'This field represents a link to a BackendService resource in GCP. It can
          be specified in two ways. First, you can place a dictionary with key ''selfLink''
          and value of your resource''s selfLink Alternatively, you can add `register:
          name-of-resource` to a google.gcp.gcp_compute_backend_service task and then set this
          default_service field to "{{ name-of-resource }}"'
        required: true
        type: dict
      description:
        description:
        - An optional description of this resource.
        required: false
        type: str
      name:
        description:
        - The name to which this PathMatcher is referred by the HostRule.
        required: true
        type: str
      path_rules:
        description:
        - The list of path rules.
        required: false
        type: list
        suboptions:
          paths:
            description:
            - 'The list of path patterns to match. Each must start with / and the
              only place a * is allowed is at the end following a /. The string fed
              to the path matcher does not include any text after the first ? or #,
              and those chars are not allowed here.'
            required: true
            type: list
          service:
            description:
            - A reference to the BackendService resource if this rule is matched.
            - 'This field represents a link to a BackendService resource in GCP. It
              can be specified in two ways. First, you can place a dictionary with
              key ''selfLink'' and value of your resource''s selfLink Alternatively,
              you can add `register: name-of-resource` to a google.gcp.gcp_compute_backend_service
              task and then set this service field to "{{ name-of-resource }}"'
            required: true
            type: dict
  tests:
    description:
    - The list of expected URL mappings. Requests to update this UrlMap will succeed
      only if all of the test cases pass.
    required: false
    type: list
    suboptions:
      description:
        description:
        - Description of this test case.
        required: false
        type: str
      host:
        description:
        - Host portion of the URL.
        required: true
        type: str
      path:
        description:
        - Path portion of the URL.
        required: true
        type: str
      service:
        description:
        - A reference to expected BackendService resource the given URL should be
          mapped to.
        - 'This field represents a link to a BackendService resource in GCP. It can
          be specified in two ways. First, you can place a dictionary with key ''selfLink''
          and value of your resource''s selfLink Alternatively, you can add `register:
          name-of-resource` to a google.gcp.gcp_compute_backend_service task and then set this
          service field to "{{ name-of-resource }}"'
        required: true
        type: dict
extends_documentation_fragment: google.gcp.gcp
'''

EXAMPLES = '''
- name: create a instance group
  gcp_compute_instance_group:
    name: instancegroup-urlmap
    zone: us-central1-a
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instancegroup

- name: create a HTTP health check
  gcp_compute_http_health_check:
    name: httphealthcheck-urlmap
    healthy_threshold: 10
    port: 8080
    timeout_sec: 2
    unhealthy_threshold: 5
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: healthcheck

- name: create a backend service
  gcp_compute_backend_service:
    name: backendservice-urlmap
    backends:
    - group: "{{ instancegroup.selfLink }}"
    health_checks:
    - "{{ healthcheck.selfLink }}"
    enable_cdn: 'true'
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: backendservice

- name: create a URL map
  gcp_compute_url_map:
    name: test_object
    default_service: "{{ backendservice }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
defaultService:
  description:
  - A reference to BackendService resource if none of the hostRules match.
  returned: success
  type: dict
description:
  description:
  - An optional description of this resource. Provide this property when you create
    the resource.
  returned: success
  type: str
hostRules:
  description:
  - The list of HostRules to use against the URL.
  returned: success
  type: complex
  contains:
    description:
      description:
      - An optional description of this HostRule. Provide this property when you create
        the resource.
      returned: success
      type: str
    hosts:
      description:
      - The list of host patterns to match. They must be valid hostnames, except *
        will match any string of ([a-z0-9-.]*). In that case, * must be the first
        character and must be followed in the pattern by either - or .
      returned: success
      type: list
    pathMatcher:
      description:
      - The name of the PathMatcher to use to match the path portion of the URL if
        the hostRule matches the URL's host portion.
      returned: success
      type: str
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
fingerprint:
  description:
  - Fingerprint of this resource. This field is used internally during updates of
    this resource.
  returned: success
  type: str
name:
  description:
  - Name of the resource. Provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
pathMatchers:
  description:
  - The list of named PathMatchers to use against the URL.
  returned: success
  type: complex
  contains:
    defaultService:
      description:
      - A reference to a BackendService resource. This will be used if none of the
        pathRules defined by this PathMatcher is matched by the URL's path portion.
      returned: success
      type: dict
    description:
      description:
      - An optional description of this resource.
      returned: success
      type: str
    name:
      description:
      - The name to which this PathMatcher is referred by the HostRule.
      returned: success
      type: str
    pathRules:
      description:
      - The list of path rules.
      returned: success
      type: complex
      contains:
        paths:
          description:
          - 'The list of path patterns to match. Each must start with / and the only
            place a * is allowed is at the end following a /. The string fed to the
            path matcher does not include any text after the first ? or #, and those
            chars are not allowed here.'
          returned: success
          type: list
        service:
          description:
          - A reference to the BackendService resource if this rule is matched.
          returned: success
          type: dict
tests:
  description:
  - The list of expected URL mappings. Requests to update this UrlMap will succeed
    only if all of the test cases pass.
  returned: success
  type: complex
  contains:
    description:
      description:
      - Description of this test case.
      returned: success
      type: str
    host:
      description:
      - Host portion of the URL.
      returned: success
      type: str
    path:
      description:
      - Path portion of the URL.
      returned: success
      type: str
    service:
      description:
      - A reference to expected BackendService resource the given URL should be mapped
        to.
      returned: success
      type: dict
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.gcp.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
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
            default_service=dict(required=True, type='dict'),
            description=dict(type='str'),
            host_rules=dict(
                type='list',
                elements='dict',
                options=dict(
                    description=dict(type='str'), hosts=dict(required=True, type='list', elements='str'), path_matcher=dict(required=True, type='str')
                ),
            ),
            name=dict(required=True, type='str'),
            path_matchers=dict(
                type='list',
                elements='dict',
                options=dict(
                    default_service=dict(required=True, type='dict'),
                    description=dict(type='str'),
                    name=dict(required=True, type='str'),
                    path_rules=dict(
                        type='list',
                        elements='dict',
                        options=dict(paths=dict(required=True, type='list', elements='str'), service=dict(required=True, type='dict')),
                    ),
                ),
            ),
            tests=dict(
                type='list',
                elements='dict',
                options=dict(
                    description=dict(type='str'),
                    host=dict(required=True, type='str'),
                    path=dict(required=True, type='str'),
                    service=dict(required=True, type='dict'),
                ),
            ),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#urlMap'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.put(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#urlMap',
        u'defaultService': replace_resource_dict(module.params.get(u'default_service', {}), 'selfLink'),
        u'description': module.params.get('description'),
        u'hostRules': UrlMapHostrulesArray(module.params.get('host_rules', []), module).to_request(),
        u'name': module.params.get('name'),
        u'pathMatchers': UrlMapPathmatchersArray(module.params.get('path_matchers', []), module).to_request(),
        u'tests': UrlMapTestsArray(module.params.get('tests', []), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/urlMaps/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/urlMaps".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
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
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'defaultService': response.get(u'defaultService'),
        u'description': response.get(u'description'),
        u'hostRules': UrlMapHostrulesArray(response.get(u'hostRules', []), module).from_response(),
        u'id': response.get(u'id'),
        u'fingerprint': response.get(u'fingerprint'),
        u'name': module.params.get('name'),
        u'pathMatchers': UrlMapPathmatchersArray(response.get(u'pathMatchers', []), module).from_response(),
        u'tests': UrlMapTestsArray(response.get(u'tests', []), module).from_response(),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/global/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#urlMap')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class UrlMapHostrulesArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'description': item.get('description'), u'hosts': item.get('hosts'), u'pathMatcher': item.get('path_matcher')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'description': item.get(u'description'), u'hosts': item.get(u'hosts'), u'pathMatcher': item.get(u'pathMatcher')})


class UrlMapPathmatchersArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict(
            {
                u'defaultService': replace_resource_dict(item.get(u'default_service', {}), 'selfLink'),
                u'description': item.get('description'),
                u'name': item.get('name'),
                u'pathRules': UrlMapPathrulesArray(item.get('path_rules', []), self.module).to_request(),
            }
        )

    def _response_from_item(self, item):
        return remove_nones_from_dict(
            {
                u'defaultService': item.get(u'defaultService'),
                u'description': item.get(u'description'),
                u'name': item.get(u'name'),
                u'pathRules': UrlMapPathrulesArray(item.get(u'pathRules', []), self.module).from_response(),
            }
        )


class UrlMapPathrulesArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'paths': item.get('paths'), u'service': replace_resource_dict(item.get(u'service', {}), 'selfLink')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'paths': item.get(u'paths'), u'service': item.get(u'service')})


class UrlMapTestsArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict(
            {
                u'description': item.get('description'),
                u'host': item.get('host'),
                u'path': item.get('path'),
                u'service': replace_resource_dict(item.get(u'service', {}), 'selfLink'),
            }
        )

    def _response_from_item(self, item):
        return remove_nones_from_dict(
            {u'description': item.get(u'description'), u'host': item.get(u'host'), u'path': item.get(u'path'), u'service': item.get(u'service')}
        )


if __name__ == '__main__':
    main()
