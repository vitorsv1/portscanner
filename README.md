# 🚪 Portscanner
A Simple Python Portscanner for TCP ports in a specific target.

## Dependencies
There are some libraries for depencies used with Python 3.x

```bash
pip3 install nmap argparse
```
## Usage
For usage run:

```bash
python3 portscanner.py $HOST $ARG $PORT
```
- $HOST
  - IP or domain like "192.168.0.1"
- $ARG
  - For specific port you can use "-p" or "--portrange"  
- $PORT
  - Use an specific number "8080" or range "50-500"
