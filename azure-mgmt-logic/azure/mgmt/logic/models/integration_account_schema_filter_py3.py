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


class IntegrationAccountSchemaFilter(Model):
    """The integration account schema filter for odata query.

    All required parameters must be populated in order to send to Azure.

    :param schema_type: Required. The schema type of integration account
     schema. Possible values include: 'NotSpecified', 'Xml'
    :type schema_type: str or ~azure.mgmt.logic.models.SchemaType
    """

    _validation = {
        'schema_type': {'required': True},
    }

    _attribute_map = {
        'schema_type': {'key': 'schemaType', 'type': 'str'},
    }

    def __init__(self, *, schema_type, **kwargs) -> None:
        super(IntegrationAccountSchemaFilter, self).__init__(**kwargs)
        self.schema_type = schema_type
