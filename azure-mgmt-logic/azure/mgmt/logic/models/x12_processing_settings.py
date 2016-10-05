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


class X12ProcessingSettings(Model):
    """X12ProcessingSettings.

    :param mask_security_info: The value indicating whether to mask security
     information.
    :type mask_security_info: bool
    :param convert_implied_decimal: The value indicating whether to convert
     numerical type to implied decimal.
    :type convert_implied_decimal: bool
    :param preserve_interchange: The value indicating whether to preserve
     interchange.
    :type preserve_interchange: bool
    :param suspend_interchange_on_error: The value indicating whether to
     suspend interchange on error.
    :type suspend_interchange_on_error: bool
    :param create_empty_xml_tags_for_trailing_separators: The value
     indicating whether to create empty xml tags for trailing separators.
    :type create_empty_xml_tags_for_trailing_separators: bool
    :param use_dot_as_decimal_separator: The value indicating whether to use
     dot as decimal separator.
    :type use_dot_as_decimal_separator: bool
    """ 

    _attribute_map = {
        'mask_security_info': {'key': 'maskSecurityInfo', 'type': 'bool'},
        'convert_implied_decimal': {'key': 'convertImpliedDecimal', 'type': 'bool'},
        'preserve_interchange': {'key': 'preserveInterchange', 'type': 'bool'},
        'suspend_interchange_on_error': {'key': 'suspendInterchangeOnError', 'type': 'bool'},
        'create_empty_xml_tags_for_trailing_separators': {'key': 'createEmptyXmlTagsForTrailingSeparators', 'type': 'bool'},
        'use_dot_as_decimal_separator': {'key': 'useDotAsDecimalSeparator', 'type': 'bool'},
    }

    def __init__(self, mask_security_info=None, convert_implied_decimal=None, preserve_interchange=None, suspend_interchange_on_error=None, create_empty_xml_tags_for_trailing_separators=None, use_dot_as_decimal_separator=None):
        self.mask_security_info = mask_security_info
        self.convert_implied_decimal = convert_implied_decimal
        self.preserve_interchange = preserve_interchange
        self.suspend_interchange_on_error = suspend_interchange_on_error
        self.create_empty_xml_tags_for_trailing_separators = create_empty_xml_tags_for_trailing_separators
        self.use_dot_as_decimal_separator = use_dot_as_decimal_separator