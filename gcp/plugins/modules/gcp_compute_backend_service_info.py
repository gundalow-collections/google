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
module: google.gcp.gcp_compute_backend_service_info
description:
- Gather info for GCP BackendService
- This module was called C(google.gcp.gcp_compute_backend_service_facts) before Ansible 2.9.
  The usage has not changed.
short_description: Gather info for GCP BackendService
version_added: 2.7
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
extends_documentation_fragment: google.gcp.gcp
'''

EXAMPLES = '''
- name: get info on a backend service
  gcp_compute_backend_service_info:
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
    affinityCookieTtlSec:
      description:
      - Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If
        set to 0, the cookie is non-persistent and lasts only until the end of the
        browser session (or equivalent). The maximum allowed value for TTL is one
        day.
      - When the load balancing scheme is INTERNAL, this field is not used.
      returned: success
      type: int
    backends:
      description:
      - The set of backends that serve this BackendService.
      returned: success
      type: complex
      contains:
        balancingMode:
          description:
          - Specifies the balancing mode for this backend.
          - For global HTTP(S) or TCP/SSL load balancing, the default is UTILIZATION.
            Valid values are UTILIZATION, RATE (for HTTP(S)) and CONNECTION (for TCP/SSL).
          returned: success
          type: str
        capacityScaler:
          description:
          - A multiplier applied to the group's maximum servicing capacity (based
            on UTILIZATION, RATE or CONNECTION).
          - Default value is 1, which means the group will serve up to 100% of its
            configured capacity (depending on balancingMode). A setting of 0 means
            the group is completely drained, offering 0% of its available Capacity.
            Valid range is [0.0,1.0].
          returned: success
          type: str
        description:
          description:
          - An optional description of this resource.
          - Provide this property when you create the resource.
          returned: success
          type: str
        group:
          description:
          - The fully-qualified URL of an Instance Group or Network Endpoint Group
            resource. In case of instance group this defines the list of instances
            that serve traffic. Member virtual machine instances from each instance
            group must live in the same zone as the instance group itself. No two
            backends in a backend service are allowed to use same Instance Group resource.
          - For Network Endpoint Groups this defines list of endpoints. All endpoints
            of Network Endpoint Group must be hosted on instances located in the same
            zone as the Network Endpoint Group.
          - Backend service can not contain mix of Instance Group and Network Endpoint
            Group backends.
          - Note that you must specify an Instance Group or Network Endpoint Group
            resource using the fully-qualified URL, rather than a partial URL.
          returned: success
          type: str
        maxConnections:
          description:
          - The max number of simultaneous connections for the group. Can be used
            with either CONNECTION or UTILIZATION balancing modes.
          - For CONNECTION mode, either maxConnections or one of maxConnectionsPerInstance
            or maxConnectionsPerEndpoint, as appropriate for group type, must be set.
          returned: success
          type: int
        maxConnectionsPerInstance:
          description:
          - The max number of simultaneous connections that a single backend instance
            can handle. This is used to calculate the capacity of the group. Can be
            used in either CONNECTION or UTILIZATION balancing modes.
          - For CONNECTION mode, either maxConnections or maxConnectionsPerInstance
            must be set.
          returned: success
          type: int
        maxConnectionsPerEndpoint:
          description:
          - The max number of simultaneous connections that a single backend network
            endpoint can handle. This is used to calculate the capacity of the group.
            Can be used in either CONNECTION or UTILIZATION balancing modes.
          - For CONNECTION mode, either maxConnections or maxConnectionsPerEndpoint
            must be set.
          returned: success
          type: int
        maxRate:
          description:
          - The max requests per second (RPS) of the group.
          - Can be used with either RATE or UTILIZATION balancing modes, but required
            if RATE mode. For RATE mode, either maxRate or one of maxRatePerInstance
            or maxRatePerEndpoint, as appropriate for group type, must be set.
          returned: success
          type: int
        maxRatePerInstance:
          description:
          - The max requests per second (RPS) that a single backend instance can handle.
            This is used to calculate the capacity of the group. Can be used in either
            balancing mode. For RATE mode, either maxRate or maxRatePerInstance must
            be set.
          returned: success
          type: str
        maxRatePerEndpoint:
          description:
          - The max requests per second (RPS) that a single backend network endpoint
            can handle. This is used to calculate the capacity of the group. Can be
            used in either balancing mode. For RATE mode, either maxRate or maxRatePerEndpoint
            must be set.
          returned: success
          type: str
        maxUtilization:
          description:
          - Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization
            target for the group. The default is 0.8. Valid range is [0.0, 1.0].
          returned: success
          type: str
    cdnPolicy:
      description:
      - Cloud CDN configuration for this BackendService.
      returned: success
      type: complex
      contains:
        cacheKeyPolicy:
          description:
          - The CacheKeyPolicy for this CdnPolicy.
          returned: success
          type: complex
          contains:
            includeHost:
              description:
              - If true requests to different hosts will be cached separately.
              returned: success
              type: bool
            includeProtocol:
              description:
              - If true, http and https requests will be cached separately.
              returned: success
              type: bool
            includeQueryString:
              description:
              - If true, include query string parameters in the cache key according
                to query_string_whitelist and query_string_blacklist. If neither is
                set, the entire query string will be included.
              - If false, the query string will be excluded from the cache key entirely.
              returned: success
              type: bool
            queryStringBlacklist:
              description:
              - Names of query string parameters to exclude in cache keys.
              - All other parameters will be included. Either specify query_string_whitelist
                or query_string_blacklist, not both.
              - "'&' and '=' will be percent encoded and not treated as delimiters."
              returned: success
              type: list
            queryStringWhitelist:
              description:
              - Names of query string parameters to include in cache keys.
              - All other parameters will be excluded. Either specify query_string_whitelist
                or query_string_blacklist, not both.
              - "'&' and '=' will be percent encoded and not treated as delimiters."
              returned: success
              type: list
        signedUrlCacheMaxAgeSec:
          description:
          - Maximum number of seconds the response to a signed URL request will be
            considered fresh, defaults to 1hr (3600s). After this time period, the
            response will be revalidated before being served.
          - 'When serving responses to signed URL requests, Cloud CDN will internally
            behave as though all responses from this backend had a "Cache-Control:
            public, max-age=[TTL]" header, regardless of any existing Cache-Control
            header. The actual headers served in responses will not be altered.'
          returned: success
          type: int
    connectionDraining:
      description:
      - Settings for connection draining .
      returned: success
      type: complex
      contains:
        drainingTimeoutSec:
          description:
          - Time for which instance will be drained (not accept new connections, but
            still work to finish started).
          returned: success
          type: int
    creationTimestamp:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    fingerprint:
      description:
      - Fingerprint of this resource. A hash of the contents stored in this object.
        This field is used in optimistic locking.
      returned: success
      type: str
    description:
      description:
      - An optional description of this resource.
      returned: success
      type: str
    enableCDN:
      description:
      - If true, enable Cloud CDN for this BackendService.
      returned: success
      type: bool
    healthChecks:
      description:
      - The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health
        checking this BackendService. Currently at most one health check can be specified,
        and a health check is required.
      - For internal load balancing, a URL to a HealthCheck resource must be specified
        instead.
      returned: success
      type: list
    id:
      description:
      - The unique identifier for the resource.
      returned: success
      type: int
    iap:
      description:
      - Settings for enabling Cloud Identity Aware Proxy.
      returned: success
      type: complex
      contains:
        enabled:
          description:
          - Enables IAP.
          returned: success
          type: bool
        oauth2ClientId:
          description:
          - OAuth2 Client ID for IAP .
          returned: success
          type: str
        oauth2ClientSecret:
          description:
          - OAuth2 Client Secret for IAP .
          returned: success
          type: str
        oauth2ClientSecretSha256:
          description:
          - OAuth2 Client Secret SHA-256 for IAP .
          returned: success
          type: str
    loadBalancingScheme:
      description:
      - Indicates whether the backend service will be used with internal or external
        load balancing. A backend service created for one type of load balancing cannot
        be used with the other. Must be `EXTERNAL` or `INTERNAL_SELF_MANAGED` for
        a global backend service. Defaults to `EXTERNAL`.
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
    portName:
      description:
      - Name of backend port. The same name should appear in the instance groups referenced
        by this service. Required when the load balancing scheme is EXTERNAL.
      returned: success
      type: str
    protocol:
      description:
      - The protocol this BackendService uses to communicate with backends.
      - 'Possible values are HTTP, HTTPS, HTTP2, TCP, and SSL. The default is HTTP.
        **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may
        result in errors if used with the GA API.'
      returned: success
      type: str
    securityPolicy:
      description:
      - The security policy associated with this backend service.
      returned: success
      type: str
    sessionAffinity:
      description:
      - Type of session affinity to use. The default is NONE.
      - When the load balancing scheme is EXTERNAL, can be NONE, CLIENT_IP, or GENERATED_COOKIE.
      - When the protocol is UDP, this field is not used.
      returned: success
      type: str
    timeoutSec:
      description:
      - How many seconds to wait for the backend before considering it a failed request.
        Default is 30 seconds. Valid range is [1, 86400].
      returned: success
      type: int
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
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str')))

    if module._name == 'gcp_compute_backend_service_facts':
        module.deprecate("The 'gcp_compute_backend_service_facts' module has been renamed to 'gcp_compute_backend_service_info'", version='2.13')

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    return_value = {'resources': fetch_list(module, collection(module), query_options(module.params['filters']))}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/backendServices".format(**module.params)


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
