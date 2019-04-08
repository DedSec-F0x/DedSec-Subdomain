import os
import urllib
import sys
import requests
# ________________________________________________
#|                                                |
#|   DEDSEC HACKING GROUP ---->> CREATED BY F0OX  |
#|________________________________________________|

if len(sys.argv) < 2:
	print(">>>>===========DEDSEC============<<<<")
	print(" Use 'python searchsubdns.py <host>'")
	print(">>>>===========DEDSEC============<<<<")
	sys.exit(0)

dns1 = sys.argv[1]
file = open("wordlist.txt","r").readlines()
for linha in file:
	linha1 = linha.strip()
	dns2 = str(dns1)
	sub = "https://" + linha1 + dns2
	r = requests.get(sub)
	if r.status_code == 200:
		print ("HOST ECONTRADO =======>>> " + r.url)
	else:
		print(" ")








#for palavra in $(cat sub);do host $palavra.grupobussinescorp.com;done
