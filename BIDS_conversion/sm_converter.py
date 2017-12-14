#!/usr/bin/env bash

######################################################################################################################################
"""
# @Author: Nichollette Acosta
# @Title: Heuristic Conversion File
# @Description:  This script is unique for your subject. The parameters below need to
                be made for yoour specific data. This is used when we run the bidsconversion file. 
"""
######################################################################################################################################



import os
subject = os.environ["value"]

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    # create directories

    # anat/
    t1 = create_key('anat/sub-' + subject+ '_T1w')


    # fmap/
    fmap_phase = create_key('fmap/sub-' + subject + '_phasediff')
    fmap_magnitude = create_key('fmap/sub-' + subject + '_magnitude')


    # func/
    rest = create_key('func/sub-' + subject + '_task-rest_bold')
    train = create_key('func/sub-' + subject + '_task-train_bold')
    predict = create_key('func/sub-' + subject + '_task-predictionerror_bold')




    info = {t1: [],  fmap_phase: [], fmap_magnitude: [], rest: [], train: [], predict: [] }

    for s in seqinfo:
        print(s)
        if (s.dim3 == 192) and ('t1' in s.protocol_name):
            info[t1].append(s.series_id)  ## append if multiple series meet criteria
        if (s.dim3 == 72) and ('field_mapping' in s.protocol_name):
            info[fmap_magnitude].append(s.series_id)  ## append if multiple series meet criteria
        if (s.dim3 == 36) and ('field_mapping' in s.protocol_name):
            info[fmap_phase].append(s.series_id)  # append if multiple series meet criteria
        if (s.dim4 == 348) and ('bold' in s.protocol_name):
            info[train].append(s.series_id)  # append if multiple series meet criteria
        if (s.dim4 == 147) and ('resting' in s.protocol_name):
            info[rest].append(s.series_id)  # append if multiple series meet criteria
        if (s.dim4 == 193) and ('bold' in s.protocol_name):
            info[predict].append(s.series_id)  # append if multiple series meet criteria
        ##if (s.dim4 == 170) and ('bold' in s.protocol_name):
            #info[pictures].append(s.series_id)  # append if multiple series meet criteria

    return info
