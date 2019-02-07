#!/bin/bash
#REDE WIRELESS

#Down na interface eth0
#echo -e "Matando eth0:"
#sudo ifconfig eth0 down
#echo -e "DHCP release:"
#sudo dhclient -r eth0


#Down na interface
echo -e "Matando wlan0:"
if sudo ifconfig wlan0 down; then
echo "wlan0 down"
else
echo "Falha"
exit 1
fi

#Up na interface
echo "Subindo wlan0:"
if sudo ifconfig wlan0 up; then
echo "wlan0 up"
else
echo "Falha"
exit 1
fi

##Matar processos existentes
echo "Matando processos WPA:"
sudo killall wpa_supplicant
sudo dhclient -r wlan0
sudo killall wpa_supplicant
echo "Processos WPA e dhcp down"

#Mostrar redes disponiveis:
echo "Redes disponiveis:"
sudo iwlist wlan0 scan | grep -w 'ESSID\|Quality\|key'

#Mostrar redes ja criadas:
sudo ls -la /etc/wpa_supplicant/ | grep .conf

#WPA ou WEP
echo -e "WPA ou WEP?[a/e]\c"
read Tipo

#Ler rede a se conectar
echo -e "Rede: \c" 
read Wireless

#Conecta em WEP
if [ "$Tipo" = "e" ]; then
echo -e "SSID: \c"
read SSID
echo -e "Senha: \c"
read Senha
echo "Conectando a rede WEP:"
	if [ -z "$Senha" ]; then
	sudo iwconfig wlan0 essid ${SSID} key off ap any mode managed
	exit 0
	else
	sudo iwconfig wlan0 essid ${SSID} key ${senha} mode managed
	exit 0
	fi
else
echo "WPA:"
fi

#Verificar se rede ja existe
echo "Verificando se rede ja existe"
if [ ! -f "/etc/wpa_supplicant/${Wireless}.conf" ]; then
        echo "Arquivo nao existe!"
        echo "/etc/wpa_supplicant/${Wireless}.conf"
	echo -e "Digite ESSID: \c"
        read SSID
        echo -e "Digite a senha: \c"
        read senha
        wpa_passphrase "${SSID}" "${senha}" > /etc/wpa_supplicant/${Wireless}.conf
	#echo -e "# WPA-PSK/TKIP\nupdate_config=1\nctrl_interface=/var/run/wpa_supplicant\n\nnetwork={\n\tssid="$SSID"\n\tpsk="$senha"\n}" >> /etc/wpa_supplicant/${Wireless}.conf
else
echo "Arquivo ja existe!"
fi

#Conectar
echo "Conectando à rede:"
sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/${Wireless}.conf
sleep 10
if iwconfig wlan0 | grep "ESSID" | grep "off"; then
echo "Falha ao conectar"
exit 1
else
iwconfig wlan0 | grep "ESSID"
echo "Conectado"
fi

#IP
echo "Startando DHCP"
sudo dhclient wlan0
ifconfig wlan0 | grep "inet addr"

#Teste conectividade
if ping -c 1 -W 1 8.8.8.8 | grep ttl > /dev/null; then
echo "Conectado!"
else
echo "Sem Conexao"
fi
