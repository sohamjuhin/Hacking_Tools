
import   nmap
ns = nmap.PortScanner()
print (ns.nmap_version())
ns.scan('127.0.0.1','1-10','-v')
print (ns.scaninfo())
print (ns.cvs())

