#!/usr/bin/env bash

######################################################################################################################################
"""
# @Author: Nichollette Acosta
# @Title: Bids Polish
# @Description:  This script will grab the participants and make a participants.tsv
                  file for our BIDS folder, as well as polish our BIDS conversion
"""

######################################################################################################################################


(echo -e "participant_id \t age \t sex") | column -t >> participants.txt

# get subject / folder names
folders=(sub*)

# start loop
for f in ${folders[@]}; do
    cd $f

    #get participants
    subject=$(awk 'NR == 2 {print  $1}' participants.tsv)
    info=$(awk 'NR == 2 {print  " \t" $2 " \t" $3}' participants.tsv)
    info="${f}${info}"
    participant=$info
    #participants=(${participants[@]} $info)
    #echo ${particpants[@]}


    cd ..

    echo "$subject  $f" >> subject_conversion.txt

    echo  "$participant" >> participants.txt

    cd $f

    lsfor
    task="${f}task"

    rm task* README CHANGES data* part* $task*

    ls
    cd ..
done

column -t participants.txt >> participants.tsv
rm participants.txt
