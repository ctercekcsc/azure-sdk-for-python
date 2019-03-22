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


class Model(Model):
    """Model.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The identifier of this entity
    :type id: str
    :param base_model: The base model used for adaptation
    :type base_model: ~azure.cognitiveservices.speechservices.models.Model
    :param datasets: Datasets used for adaptation
    :type datasets:
     list[~azure.cognitiveservices.speechservices.models.Dataset]
    :param model_kind: Required. The kind of this model (e.g. acoustic,
     language ...). Possible values include: 'AcousticAndLanguage', 'None',
     'Acoustic', 'Language', 'CustomVoice', 'LanguageGeneration', 'Sentiment',
     'LanguageIdentification'
    :type model_kind: str or
     ~azure.cognitiveservices.speechservices.models.enum
    :param name: Required. The name of the object
    :type name: str
    :param description: The description of the object
    :type description: str
    :param properties: The custom properties of this entity
    :type properties: dict[str, str]
    :param locale: The locale of the contained data
    :type locale: str
    :param created_date_time: Required. The time-stamp when the object was
     created
    :type created_date_time: datetime
    :param last_action_date_time: Required. The time-stamp when the current
     status was entered
    :type last_action_date_time: datetime
    :param status: Required. The status of the object. Possible values
     include: 'Succeeded', 'Failed', 'NotStarted', 'Running'
    :type status: str or ~azure.cognitiveservices.speechservices.models.enum
    """

    _validation = {
        'id': {'required': True},
        'model_kind': {'required': True},
        'name': {'required': True},
        'created_date_time': {'required': True},
        'last_action_date_time': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'base_model': {'key': 'baseModel', 'type': 'Model'},
        'datasets': {'key': 'datasets', 'type': '[Dataset]'},
        'model_kind': {'key': 'modelKind', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'locale': {'key': 'locale', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_action_date_time': {'key': 'lastActionDateTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, *, id: str, model_kind, name: str, created_date_time, last_action_date_time, status, base_model=None, datasets=None, description: str=None, properties=None, locale: str=None, **kwargs) -> None:
        super(Model, self).__init__(**kwargs)
        self.id = id
        self.base_model = base_model
        self.datasets = datasets
        self.model_kind = model_kind
        self.name = name
        self.description = description
        self.properties = properties
        self.locale = locale
        self.created_date_time = created_date_time
        self.last_action_date_time = last_action_date_time
        self.status = status