#!/bin/sh

NOW=`date '+%H'`
#echo NOW
if [ $NOW -ge 21 -o $NOW -lt 8 ]; then #現在時刻が21時~翌8時の間なら
    systemctl stop plc_log
    echo 'test'
    exit 0 #正常終了
else
    systemctl start plc_log
    echo $NOW
fi
exit 0 #正常終了