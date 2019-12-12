#!/bin/bash
TYPE=$1
ID=$2
VAL=$3
row=`cat $TYPE.json | jq -r --arg ID "$ID" --arg VAL "$VAL" '.[] | select (.[$ID]|tostring == $VAL)'`
id=`echo $row | jq '._id'`

echo "id: "$id

echo $row | jq -r 'keys_unsorted[] as $k |[ $k, .[$k]|tostring] | @tsv'