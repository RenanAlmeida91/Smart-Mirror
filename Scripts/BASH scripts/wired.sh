#!/bin/bash
#sudo ip link set eno1 up
#sudo ip addr add 11.1.102.170/24 dev eno1
#sudo ip route add default via 11.1.102.20
sudo echo -e "nameserver 10.1.3.53\nnameserver 10.1.3.54\nnameserver 10.1.3.52\nnameserver 8.8.8.8\nsearch bandeirantes.com.br" >> /etc/resolv.conf
