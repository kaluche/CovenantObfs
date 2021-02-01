#!/usr/bin/python3
import random, string
from pathlib import Path

# Description: just a PoC for doing some tests about detection of Grunt by EDR.

if __name__ == '__main__':

	outputDir = Path('output')
	outputDir.mkdir(exist_ok=True)
	STAGERCODE_FILE_SRC  = "templates/StagerCode.cs.tpl"
	print("[+] Using template Stager : \33[34m{}\33[0m".format(STAGERCODE_FILE_SRC))
	STAGERCODE_FILE_OUT  = outputDir / "StagerCode.cs"

	EXECUTOR_FILE_SRC = "templates/ExecutorCode.cs.tpl"
	print("[+] Using template Executor : \33[34m{}\33[0m".format(EXECUTOR_FILE_SRC))
	EXECUTOR_FILE_OUT = outputDir / "ExecutorCode.cs"

	STAGERCODE_PS_FILE_SRC  = "templates/StagerCodePS.cs.tpl"
	print("[+] Using template StagerPS : \33[34m{}\33[0m\n".format(STAGERCODE_PS_FILE_SRC))
	STAGERCODE_PS_FILE_OUT  = outputDir / "StagerCodePS.cs"
	
	with open(STAGERCODE_FILE_SRC,'r') as f:
		stagercode = f.read()
	with open(STAGERCODE_PS_FILE_SRC,'r') as f:
		stagercodePS = f.read()
	with open(EXECUTOR_FILE_SRC,'r') as f:
		executorcode = f.read()

	# all of this is going to be replace by random strings
	bad = [
	"Grunt",
	"grunt",
	"Stager",
	"Execute",
	"Covenant",
	"Stage0Body",
	"Stage0Response",
	"Stage1Body",
	"Stage1Response",
	"Stage2Body",
	"Stage2Response",
	"ValidateCert",
	"UseCertPinning",
	"SetupAESKey",
	"Executor",
	"GUID"
	""
	]
	for x in bad:
		rand = ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase, random.randint(10,20)))
		stagercode = stagercode.replace(x,rand)
		stagercodePS = stagercodePS.replace(x,rand)
		executorcode = executorcode.replace(x,rand)
		print("\33[33m{}\33[0m ==> \33[32m{}\33[0m".format(x,rand))

	with open(STAGERCODE_FILE_OUT,'w') as f:
		f.write(stagercode)
		print("\n[+] Output Stager : \33[95m{}\33[0m".format(STAGERCODE_FILE_OUT))
	with open(EXECUTOR_FILE_OUT,'w') as f:
		f.write(executorcode)
		print("[+] Output Executor : \33[95m{}\33[0m".format(EXECUTOR_FILE_OUT))
	with open(STAGERCODE_PS_FILE_OUT,'w') as f:
		f.write(stagercodePS)
		print("[+] Output Stager PS : \33[95m{}\33[0m".format(STAGERCODE_PS_FILE_OUT))