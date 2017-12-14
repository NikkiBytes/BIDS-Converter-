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
    milk = create_key('func/sub-' + subject + '_task-milkshake_B')
    #milkA = create_key('func/sub-' + subject + '_pace_moco_milkshake_A')
    noGo = create_key('func/sub-' + subject + '_task-Go_NoGo')
    #noGo2 = create_key('func/sub-' + subject + '_pace_moco_Go_NoGo2')



    info = {t1: [], fmap_phase: [], fmap_magnitude: [], milk: [], noGo: [] }

    for s in seqinfo:
        print(s)
        if (s.dim1 == 256) and ('t1' in s.protocol_name):
            info[t1].append(s.series_id)  ## append if multiple series meet criteria
        if (s.dim4 == 475 and s.is_motion_corrected == False ) and ('milkshake' in s.protocol_name):
            info[milk].append(s.series_id)  ## append if multiple series meet criteria
        if (s.dim4 == 195 and s.is_motion_corrected == False) and ('Go' in s.protocol_name):
            info[noGo].append(s.series_id)  ## append if multiple series meet criteria
        if (s.dim3 == 27) and ('field' in s.protocol_name):
            info[fmap_magnitude].append(s.series_id)  ## append if multiple series meet criteria
        if (s.dim3 == 54) and ('field' in s.protocol_name):
            info[fmap_phase].append(s.series_id)  ## append if multiple series meet criteria



    return info
