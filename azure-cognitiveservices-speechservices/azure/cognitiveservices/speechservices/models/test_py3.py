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


class Test(Model):
    """Test.

    All required parameters must be populated in order to send to Azure.

    :param dataset: Information about the dataset used in the test
    :type dataset: ~azure.cognitiveservices.speechservices.models.Dataset
    :param id: Required. The identifier of this entity
    :type id: str
    :param word_error_rate: Required. The word error rate of the tested model
    :type word_error_rate: float
    :param results_url: The URL that can be used to download the test results.
     Each line in the file represents a tab separated list of filename,
     reference transcription and decoder output.
     The URL will only be valid, if the test completed successfully
    :type results_url: str
    :param created_date_time: Required. The time-stamp when the object was
     created
    :type created_date_time: datetime
    :param last_action_date_time: Required. The time-stamp when the current
     status was entered
    :type last_action_date_time: datetime
    :param status: Required. The status of the object. Possible values
     include: 'Succeeded', 'Failed', 'NotStarted', 'Running'
    :type status: str or ~azure.cognitiveservices.speechservices.models.enum
    :param models_property: Required. Information about the models used for
     this accuracy test
    :type models_property:
     list[~azure.cognitiveservices.speechservices.models.Model]
    :param name: Required. The name of the object
    :type name: str
    :param description: The description of the object
    :type description: str
    :param properties: The custom properties of this entity
    :type properties: dict[str, str]
    """

    _validation = {
        'id': {'required': True},
        'word_error_rate': {'required': True},
        'created_date_time': {'required': True},
        'last_action_date_time': {'required': True},
        'status': {'required': True},
        'models_property': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'dataset': {'key': 'dataset', 'type': 'Dataset'},
        'id': {'key': 'id', 'type': 'str'},
        'word_error_rate': {'key': 'wordErrorRate', 'type': 'float'},
        'results_url': {'key': 'resultsUrl', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_action_date_time': {'key': 'lastActionDateTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'models_property': {'key': 'models', 'type': '[Model]'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(self, *, id: str, word_error_rate: float, created_date_time, last_action_date_time, status, models_property, name: str, dataset=None, results_url: str=None, description: str=None, properties=None, **kwargs) -> None:
        super(Test, self).__init__(**kwargs)
        self.dataset = dataset
        self.id = id
        self.word_error_rate = word_error_rate
        self.results_url = results_url
        self.created_date_time = created_date_time
        self.last_action_date_time = last_action_date_time
        self.status = status
        self.models_property = models_property
        self.name = name
        self.description = description
        self.properties = properties