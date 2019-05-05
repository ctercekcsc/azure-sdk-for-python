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


class Display(Model):
    """Contains the localized display information for this particular operation /
    action. These value will be used by several clients for (1) custom role
    definitions for RBAC; (2) complex query filters for the event service; and
    (3) audit history / records for management operations.

    :param provider: The provider. The localized friendly form of the resource
     provider name – it is expected to also include the publisher/company
     responsible. It should use Title Casing and begin with "Microsoft" for 1st
     party services. e.g. "Microsoft Monitoring Insights" or "Microsoft
     Compute."
    :type provider: str
    :param resource: The resource. The localized friendly form of the resource
     related to this action/operation – it should match the public
     documentation for the resource provider. It should use Title Casing. This
     value should be unique for a particular URL type (e.g. nested types should
     *not* reuse their parent’s display.resource field). e.g. "Virtual
     Machines" or "Scheduler Job Collections", or "Virtual Machine VM Sizes" or
     "Scheduler Jobs"
    :type resource: str
    :param operation: The operation. The localized friendly name for the
     operation, as it should be shown to the user. It should be concise (to fit
     in drop downs) but clear (i.e. self-documenting). It should use Title
     Casing. Prescriptive guidance: Read Create or Update Delete 'ActionName'
    :type operation: str
    :param description: The description. The localized friendly description
     for the operation, as it should be shown to the user. It should be
     thorough, yet concise – it will be used in tool tips and detailed views.
     Prescriptive guidance for namespaces: Read any 'display.provider' resource
     Create or Update any 'display.provider' resource Delete any
     'display.provider' resource Perform any other action on any
     'display.provider' resource Prescriptive guidance for namespaces: Read any
     'display.resource' Create or Update any 'display.resource' Delete any
     'display.resource' 'ActionName' any 'display.resources'
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, resource: str=None, operation: str=None, description: str=None, **kwargs) -> None:
        super(Display, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description
