import os
import nmap
nm = nmap.PortScanner()
def attempt(ip):
    nm.scan(ip)
    host = nm.all_hosts()
    ports = nm[host]['tcp'].keys()
    if ("21" in ports):
        os.system("ftp " + ip)
        os.system("anonymous")
    if ("80" in ports):
        #a lot of things
        s = "" #placeholder
    if ("445" in ports):
        os.system("smbclient -L ")