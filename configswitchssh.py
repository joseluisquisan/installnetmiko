#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime

f = open ('myswitches.txt')

start_time = datetime.now()
for line in f:
    hostname = line.strip()

    iosv_l2 = {
        'device_type': 'cisco_ios',
        'ip': hostname,
        'username': 'metroadmin',
        'password': 'M3Tr0SO!8#',
        "global_delay_factor": .2,
    }

    commands = [
        'enable',
        'access-list 30 permit 10.251.0.0 0.0.0.255',
        'do wr',
    ]

#    start_time = datetime.now()
    net_connect = ConnectHandler(**iosv_l2)
    print ("#" * 35)
    print ("Configurando Switch: " + str(hostname))
    print ("#" * 35)
    net_connect.enable()
    output = net_connect.send_config_set(commands, delay_factor=.2)
    net_connect.disconnect()
    print output
end_time = datetime.now()
total_time = end_time - start_time
print ("Tiempo total del Script " + str(total_time))
