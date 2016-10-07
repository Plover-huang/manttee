import argparse
ip="45.32.51.20"
programName="azolla"
parser = argparse.ArgumentParser()
parser.add_argument("-p","--port",help="specify the port number", type=int)
parser.add_argument("-P","--password",help="specify the password")
parser.add_argument("-L","--label",help="specify label", default="{}_{}".format(programName,ip))
parser.add_argument("-m","--method", help="specify method", default="aes-256-cfb")
parser.add_argument("-v","--verbose", help="view configuration",action="store_true" )
args = parser.parse_args()
if args.port!=None and args.password!=None:
    pass
if args.verbose:
        print(args.port,args.password,args.label,args.method)
