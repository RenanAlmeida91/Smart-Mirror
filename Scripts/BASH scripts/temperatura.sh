#!/bin/sh
wget -q -O /home/abdsantos/Scripts/temperatura.xml - "http://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo&mode=xml&APPID=4c3ddb738f9fbefdbb28963642aafc1a"
temp_1=$(xmlstarlet sel -t -v "current/temperature/@value" /home/abdsantos/Scripts/temperatura.xml)
umidade=$(xmlstarlet sel -t -v "current/humidity/@value" /home/abdsantos/Scripts/temperatura.xml)
temp_c=$(echo "$temp_1 - 272.15" | bc)
echo ${temp_c}C / ${umidade}% 
