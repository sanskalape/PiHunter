import nmap

scanner = nmap.PortScanner()
scanner.scan('192.168.1.0/24','22-80')

print(scanner.all_hosts())
