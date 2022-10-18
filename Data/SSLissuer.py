

from lxml import etree
import sys

nmapFile = sys.argv[1]

xml = etree.parse(open(nmapFile))

for host in xml.xpath("//host"):
	for addr in host.xpath("address/@addr"):
		print("------------------------------")
		print("Host: " + addr)
	for port in host.xpath("ports/port"):
		for issuer in port.xpath('script[@id="ssl-cert"]/table[@key="issuer"]/elem[@key="commonName"]'):
			print("Issuer: " + issuer.text)