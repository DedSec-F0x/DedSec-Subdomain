import sys
import dns.resolver
# ________________________________________________
#|                                                |
#|   DEDSEC HACKING GROUP ---->> CREATED BY F0OX  |
#|________________________________________________|

if len(sys.argv) < 2:
	print(">>>>===========DEDSEC============<<<<")
	print(" Use 'python searchsubdns.py <host>'")
	print(">>>>===========DEDSEC============<<<<")
	sys.exit(0)
dominio = sys.argv[1]
arquivo = open("wordlist.txt")
linhas = arquivo.read().splitlines()

for linha in linhas:
	subdominio = linha + dominio
	try:
		receive = dns.resolver.query(subdominio, 'a')
		for resultado in receive:
			print ("HOST ECONTRADO =======>>> " + subdominio)
	except:
		pass








#for palavra in $(cat sub);do host $palavra.grupobussinescorp.com;done
