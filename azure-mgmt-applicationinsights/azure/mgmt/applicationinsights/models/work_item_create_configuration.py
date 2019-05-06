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

from msrest.serialization import Model


class WorkItemCreateConfiguration(Model):
    """Work item configuration creation payload.

    :param connector_id: Unique connector id
    :type connector_id: str
    :param connector_data_configuration: Serialized JSON object for detailed
     properties
    :type connector_data_configuration: str
    :param validate_only: True or false string indicating validate only
    :type validate_only: str
    :param work_item_properties: Custom work item properties
    :type work_item_properties: dict[str, str]
    """

    _attribute_map = {
        'connector_id': {'key': 'ConnectorId', 'type': 'str'},
        'connector_data_configuration': {'key': 'ConnectorDataConfiguration', 'type': 'str'},
        'validate_only': {'key': 'ValidateOnly', 'type': 'str'},
        'work_item_properties': {'key': 'WorkItemProperties', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(WorkItemCreateConfiguration, self).__init__(**kwargs)
        self.connector_id = kwargs.get('connector_id', None)
        self.connector_data_configuration = kwargs.get('connector_data_configuration', None)
        self.validate_only = kwargs.get('validate_only', None)
        self.work_item_properties = kwargs.get('work_item_properties', None)
