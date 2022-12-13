import os
import nmap
nm = nmap.PortScanner()
def attempt(ip):
    nm.scan(ip)
    host = nm.all_hosts()
    ports = nm[host]['tcp'].keys()
    if ("21" in ports):
        os.system("./ftp.sh")
    if ("80" in ports):
        os.system("./http.sh")
    if ("445" in ports):
        os.system("./smb.sh")