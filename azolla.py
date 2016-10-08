import argparse

class encryptChoice(list):
	def __init__(self, arg):
		super(encryptChoice, self).__init__()
		self.arg = arg
	def __contain__(self,other):
		return super(encryptChoice,self).__contains__(other.lower())

choices=encryptChoice(["AES-128-CFB", "AES-192-CFB", "AES-256-CFB", "BF-CFB", "Camellia-128-CFB", "Camellia-192-CFB", "Camellia-256-CFB", "CAST5-CFB", "ChaCha20", "DES-CFB", "IDEA-CFB", "RC2-CFB", "RC4-MD5", "Salsa20", "SEED-CFB", "Serpent-CFB"]);
ip="45.32.51.20"
programName="azolla"

parser = argparse.ArgumentParser()
parser.add_argument("-p","--port",help="specify the port number", type=int)
parser.add_argument("-P","--password",help="specify the password")
parser.add_argument("-L","--label",help="specify label", default="{}_{}".format(programName,ip))
parser.add_argument("-m","--method", help="specify method", default="AES-256-CFB",choice=choices)
parser.add_argument("-v","--verbose", help="view configuration",action="store_true" )
args = parser.parse_args()
if args.port!=None and args.password!=None:
    vport=args.port
    vpasswd=args.password
    vlabel=ip+"_"+vport
    vmethod=args.method
if args.verbose:
        print(args.port,args.password,args.label,args.method)
