#!/bin/bash
head --lines=50 /home/abdsantos/Scripts/feedsulamerica.html | grep "<td>" | sed '1,3d' | sed '2,5d' | awk '{gsub("<td>", "");print}' | awk '{gsub("  ", "");print}' | awk '{gsub("</td>", "");print}' | recode html..ISO-8859-1 | sed -e "s/.\{30\}/&\n/g"
