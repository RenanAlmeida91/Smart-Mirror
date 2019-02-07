#!/bin/sh
#wget -q -O - checkip.dyndns.org|sed -e 's/.*Current IP Address: //' -e 's/<.*$//'
meuip="$(wget -q -O - whatismijnip.nl|sed -e 's/.*Your IP address is //')"
whois="$(whois $meuip | grep person|sed -e 's/.*person://' -e 's/^[ \t]*//' -e 's/[ \t]*$//'|grep -v "Band")"
if [ "$whois" = "Security Office" ]; then
	whois="uol/diveo";
fi
echo -e "$meuip - $whois"
