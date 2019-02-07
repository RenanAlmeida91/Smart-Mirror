#!/bin/bash
if curl -s --head  --request GET http://avexnet.jp | grep "200 OK" > /dev/null
then
   echo "UP"
else
   echo "DOWN"
fi
