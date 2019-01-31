#!/usr/bin/env python3
import re
import socket
import optparse

def get_paras():

    usage = "usage: scan.py --host <ip> --port <port>"
    parser = optparse.OptionParser(usage)
    parser.add_option("--host",dest="ip_address",type="string")
    parser.add_option("--port",dest="port1")
    (options,args) = parser.parse_args()
    addr_temp=options.ip_address
    port_temp = options.port1

    if addr_temp == None or port_temp == None:
        print("ParameterError")
        exit(0)



    match = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',addr_temp)
    if match:
        addr = addr_temp
    else:

        print("ParameterError")

    if '-' in port_temp:
         ports = port_temp.split('-')
    else:
        ports = [port_temp,port_temp]
    port_list =[int(ports[0]),int(ports[1])]
    return addr,port_list




def scan():
    host,ports = get_paras()
    for port in range(ports[0],ports[1]+1):
        s = socket.socket()
        s.settimeout(0.1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(port,'open')
        else:
            print(port,'closed')



if __name__ == '__main__':
    scan()



