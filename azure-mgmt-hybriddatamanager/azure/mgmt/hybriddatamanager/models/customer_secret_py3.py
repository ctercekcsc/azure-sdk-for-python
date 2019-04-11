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


class CustomerSecret(Model):
    """The pair of customer secret.

    All required parameters must be populated in order to send to Azure.

    :param key_identifier: Required. The identifier to the data service input
     object which this secret corresponds to.
    :type key_identifier: str
    :param key_value: Required. It contains the encrypted customer secret.
    :type key_value: str
    :param algorithm: Required. The encryption algorithm used to encrypt data.
     Possible values include: 'None', 'RSA1_5', 'RSA_OAEP', 'PlainText'
    :type algorithm: str or
     ~azure.mgmt.hybriddatamanager.models.SupportedAlgorithm
    """

    _validation = {
        'key_identifier': {'required': True},
        'key_value': {'required': True},
        'algorithm': {'required': True},
    }

    _attribute_map = {
        'key_identifier': {'key': 'keyIdentifier', 'type': 'str'},
        'key_value': {'key': 'keyValue', 'type': 'str'},
        'algorithm': {'key': 'algorithm', 'type': 'SupportedAlgorithm'},
    }

    def __init__(self, *, key_identifier: str, key_value: str, algorithm, **kwargs) -> None:
        super(CustomerSecret, self).__init__(**kwargs)
        self.key_identifier = key_identifier
        self.key_value = key_value
        self.algorithm = algorithm