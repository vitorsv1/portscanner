#!/usr/bin/env python
import argparse
import nmap

def parse(port_range):
    ports = "-p" + port_range
    return f'{ports}'

def print_results(nmp):
    for host in nmp.all_hosts():
        lport = nmp[host]['tcp'].keys()
        for port in lport:
            host_name = f'{host} ({nmp[host].hostname()})'
            port = f'{port}/TCP'
            state = nmp[host]['TCP'][port]['state']
            name = nmp[host]['TCP'][port]['name']
            print('Host Name - Port - State - Port Name')
            print(f'{host_name} - {port} - {state} - {name}')


def main():
    parser = argparse.ArgumentParser(
        description='Port Scanner'
    )
    parser.add_argument('host', type=str, help="IP ou Dominio a ser scaneado. Ex. 192.168.0.1 ")
    parser.add_argument('-p', '--portrange', type=str, help="Range das portas a ser scaneadas. Ex. 0-1000", default='0-500')
    arg = parser.parse_args()

    nmp = nmap.PortScanner()
    args = parse(arg.port_range)
    nmp.scan(hosts=arg.host, arguments=args)

    print_results(nmp)

if __name__ == "__main__":
    main()
