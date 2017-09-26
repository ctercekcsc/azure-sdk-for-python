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

from .control_activity import ControlActivity


class ForEachActivity(ControlActivity):
    """This activity is used for iterating over a collection and execute given
    activities.

    :param name: Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list of :class:`ActivityDependency
     <azure.mgmt.datafactory.models.ActivityDependency>`
    :param type: Polymorphic Discriminator
    :type type: str
    :param is_sequential: Should the loop be executed in sequence or in
     parallel (max 20)
    :type is_sequential: bool
    :param items: Collection to iterate.
    :type items: :class:`Expression
     <azure.mgmt.datafactory.models.Expression>`
    :param activities: List of activities to execute .
    :type activities: list of :class:`Activity
     <azure.mgmt.datafactory.models.Activity>`
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'items': {'required': True},
        'activities': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'type': {'key': 'type', 'type': 'str'},
        'is_sequential': {'key': 'typeProperties.isSequential', 'type': 'bool'},
        'items': {'key': 'typeProperties.items', 'type': 'Expression'},
        'activities': {'key': 'typeProperties.activities', 'type': '[Activity]'},
    }

    def __init__(self, name, items, activities, description=None, depends_on=None, is_sequential=None):
        super(ForEachActivity, self).__init__(name=name, description=description, depends_on=depends_on)
        self.is_sequential = is_sequential
        self.items = items
        self.activities = activities
        self.type = 'ForEach'