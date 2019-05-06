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


class CheckNameResult(Model):
    """The result returned from a check name availability request.

    :param name_available: Specifies a Boolean value that indicates if the
     name is available.
    :type name_available: bool
    :param name: The name that was checked.
    :type name: str
    :param message: Message indicating an unavailable name due to a conflict,
     or a description of the naming rules that are violated.
    :type message: str
    :param reason: Message providing the reason why the given name is invalid.
     Possible values include: 'Invalid', 'AlreadyExists'
    :type reason: str or ~azure.mgmt.kusto.models.Reason
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckNameResult, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.name = kwargs.get('name', None)
        self.message = kwargs.get('message', None)
        self.reason = kwargs.get('reason', None)
