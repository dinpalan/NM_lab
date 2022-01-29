#! /usr/bin/env python3
#SHEBANG
from netmiko import ConnectHandler
import logging
from loguru import logger
from time import sleep
#import modules with methods in this space

def network():
    N=4;
    while N<7:
        ipl = f'198.51.100.{N}'
        details = {
            'device_type':'cisco_ios',
            'ip': ipl,
            'username': 'netman',
            'password': 'netman',
            'secret': 'netman',
            }
        print("successfully SSH into the router using Netmiko \n Login details are shown below:")
        print(details)
        config_commands = ['int fa1/0','ip add dhcp','no sh'];
        vty = ConnectHandler(**details)
        vty.enable()
        output1=vty.send_config_set(config_commands, delay_factor=5)
        print("Configuring the interfaces:")
        print(output1)
        print("Printing Interface configurations after change");
        ping = 'sh ip int bri | i 1/0'
        sleep(8)
        output = vty.send_command(ping)
        print(output);
        vty.disconnect()
        N=N+1;
def main():
#write your main function here 
    try:
        network()
    except KeyboardInterrupt:

        print("Exiting because of program interpreted by user"); print("Thanks for using my application");

if __name__=='__main__':
       main()
