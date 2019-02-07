#!/bin/bash
wget -q -O /home/abdsantos/Scripts/feedsulamerica.html "http://apps.band.com.br/sulamerica/ocorrencias/leitura"
wget -q -O /home/abdsantos/Scripts/currency.xml "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22USDBRL%22%2C%22EURBRL%22%2C%22JPYBRL%22)&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
Dolar="$(xmlstarlet sel -t -v "query/results/rate/Rate" /home/abdsantos/Scripts/currency.xml | cut -d$'\n' -f1)"
Euro="$(xmlstarlet sel -t -v "query/results/rate/Rate" /home/abdsantos/Scripts/currency.xml | cut -d$'\n' -f2)"
Iene="$(xmlstarlet sel -t -v "query/results/rate/Rate" /home/abdsantos/Scripts/currency.xml | cut -d$'\n' -f3)"
echo -e "Dolar:$Dolar  -  Euro:$Euro - Iene:$Iene"
