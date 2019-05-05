# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource_py3 import ProxyOnlyResource


class DiagnosticSettingsResource(ProxyOnlyResource):
    """The diagnostic setting resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar location: Azure resource location
    :vartype location: str
    :ivar kind: Azure resource kind
    :vartype kind: str
    :ivar tags: Azure resource tags
    :vartype tags: str
    :ivar identity: Azure resource identity
    :vartype identity: str
    :param storage_account_id: The resource ID of the storage account to which
     you would like to send Diagnostic Logs.
    :type storage_account_id: str
    :param service_bus_rule_id: The service bus rule Id of the diagnostic
     setting. This is here to maintain backwards compatibility.
    :type service_bus_rule_id: str
    :param workspace_id: The workspace ID (resource ID of a Log Analytics
     workspace) for a Log Analytics workspace to which you would like to send
     Diagnostic Logs. Example:
     /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
    :type workspace_id: str
    :param event_hub_authorization_rule_id: The resource Id for the event hub
     authorization rule.
    :type event_hub_authorization_rule_id: str
    :param event_hub_name: The name of the event hub. If none is specified,
     the default event hub will be selected.
    :type event_hub_name: str
    :param metrics: The list of metric settings.
    :type metrics: list[~microsoft.aadiam.models.MetricSettings]
    :param logs: The list of logs settings.
    :type logs: list[~microsoft.aadiam.models.LogSettings]
    :param log_analytics_destination_type: The type of log analyitics
     destination.
    :type log_analytics_destination_type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'kind': {'readonly': True},
        'tags': {'readonly': True},
        'identity': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'str'},
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'service_bus_rule_id': {'key': 'properties.serviceBusRuleId', 'type': 'str'},
        'workspace_id': {'key': 'properties.workspaceId', 'type': 'str'},
        'event_hub_authorization_rule_id': {'key': 'properties.eventHubAuthorizationRuleId', 'type': 'str'},
        'event_hub_name': {'key': 'properties.eventHubName', 'type': 'str'},
        'metrics': {'key': 'properties.metrics', 'type': '[MetricSettings]'},
        'logs': {'key': 'properties.logs', 'type': '[LogSettings]'},
        'log_analytics_destination_type': {'key': 'properties.logAnalyticsDestinationType', 'type': 'str'},
    }

    def __init__(self, *, storage_account_id: str=None, service_bus_rule_id: str=None, workspace_id: str=None, event_hub_authorization_rule_id: str=None, event_hub_name: str=None, metrics=None, logs=None, log_analytics_destination_type: str=None, **kwargs) -> None:
        super(DiagnosticSettingsResource, self).__init__(**kwargs)
        self.storage_account_id = storage_account_id
        self.service_bus_rule_id = service_bus_rule_id
        self.workspace_id = workspace_id
        self.event_hub_authorization_rule_id = event_hub_authorization_rule_id
        self.event_hub_name = event_hub_name
        self.metrics = metrics
        self.logs = logs
        self.log_analytics_destination_type = log_analytics_destination_type
