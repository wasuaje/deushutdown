
# -*- coding: utf-8 -*-
#!/usr/bin/env python
import getpass
import sys
import telnetlib
import commands

unix_cmd="shutdown now"
linux_cmd="shutdown -h now"
data=[{"server":"sapapp",
		"ip":"10.2.60.3",
		"cmd":unix_cmd,
		"tipo":"unix"
		},
		{"server":"sapap2",
		"ip":"10.2.60.4",
		"cmd":unix_cmd,
		"tipo":"unix"
		},
		{"server":"universal3",
		"ip":"10.6.0.43",
		"cmd":linux_cmd,
		"tipo":"linux"
		},
	]

def run_cmd(comando):
	out = commands.getoutput(comando)
	print out
	return out  # This is the stdout from the shell command

def run_unix(host,user,password,cmd):
	HOST = host	

	tn = telnetlib.Telnet(HOST)

	tn.read_until("login: ")
	tn.write(user + "\n")
	if password:
	    tn.read_until("Password: ")
	    tn.write(password + "\n")
	
	tn.write("ls\n")
	tn.write("exit\n")

	print tn.read_all()


#Solicito passwor inicialmente para los servidores unix
#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()

for i in data:
	print "Apagando servidor %s - %s - %s " % (i["server"],i["ip"],i["cmd"])
	if i["tipo"]=="unix":
		print "unix"
	else:
		print "linux"

print "vmware"
run_cmd("ssh root@10.6.0.43 ls -la")