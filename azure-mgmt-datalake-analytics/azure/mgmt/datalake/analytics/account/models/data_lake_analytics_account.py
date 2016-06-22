# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataLakeAnalyticsAccount(Model):
    """A Data Lake Analytics account object, containing all information
    associated with the named Data Lake Analytics account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param location: the account regional location.
    :type location: str
    :param name: the account name.
    :type name: str
    :ivar type: the namespace and type of the account.
    :vartype type: str
    :ivar id: the account subscription ID.
    :vartype id: str
    :param tags: the value of custom properties.
    :type tags: dict
    :param properties: the properties defined by Data Lake Analytics all
     properties are specific to each resource provider.
    :type properties: :class:`DataLakeAnalyticsAccountProperties
     <azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountProperties>`
    """ 

    _validation = {
        'type': {'readonly': True},
        'id': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'DataLakeAnalyticsAccountProperties'},
    }

    def __init__(self, location=None, name=None, tags=None, properties=None):
        self.location = location
        self.name = name
        self.type = None
        self.id = None
        self.tags = tags
        self.properties = properties