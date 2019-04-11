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


class JobStages(Model):
    """Job stages.

    All required parameters must be populated in order to send to Azure.

    :param stage_name: Name of the job stage.
    :type stage_name: str
    :param stage_status: Required. Status of the job stage. Possible values
     include: 'None', 'InProgress', 'Succeeded', 'WaitingForAction', 'Failed',
     'Cancelled', 'Cancelling'
    :type stage_status: str or ~azure.mgmt.hybriddatamanager.models.JobStatus
    :param job_stage_details: Job Stage Details
    :type job_stage_details: object
    :param error_details: Error details for the stage. This is optional
    :type error_details:
     list[~azure.mgmt.hybriddatamanager.models.ErrorDetails]
    """

    _validation = {
        'stage_status': {'required': True},
    }

    _attribute_map = {
        'stage_name': {'key': 'stageName', 'type': 'str'},
        'stage_status': {'key': 'stageStatus', 'type': 'JobStatus'},
        'job_stage_details': {'key': 'jobStageDetails', 'type': 'object'},
        'error_details': {'key': 'errorDetails', 'type': '[ErrorDetails]'},
    }

    def __init__(self, *, stage_status, stage_name: str=None, job_stage_details=None, error_details=None, **kwargs) -> None:
        super(JobStages, self).__init__(**kwargs)
        self.stage_name = stage_name
        self.stage_status = stage_status
        self.job_stage_details = job_stage_details
        self.error_details = error_details