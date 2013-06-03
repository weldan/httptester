#!/usr/bin/env python
"""
HTTP Connection Tester
Weldan Jamili, <mweldan@gmail.com>
Usage: python httptester.py -h # for usage instructions 
"""

import argparse
import requests
import requesocks
import sys

"""
Overwrite error message handling, show help
"""
class MyParser(argparse.ArgumentParser):
	def error(self, message):
		sys.stderr.write("Error: %s\n" % message)
		sys.stderr.write("============================\n")
		self.print_help()
		sys.exit(2)		

"""
target host objects
"""
class target:
	pass
	
"""
parameters checking
"""	
def checkparam(request):
	if target.raw is not None:
		print "============================"
		print "Print Response Content:"
		print "============================"
		print request.text
		print "============================"
	if target.status is not None:
		print "============================"
		print "Print Response Status Code:"
		print "============================"
		print request.status_code
		print "============================"
	if target.raw is None and target.status is None:
		if request.ok is True:
			print "HTTP connection OK"
		else:
			print "HTTP connection KO"

"""
run test
"""
def runtest():
	if target.tor is None and target.proxy is None and target.socks is None:
		try:
			request = requests.get(target.host)
			checkparam(request)
		except requests.ConnectionError as error_message:
			print "============================"
			print "HTTP connection failed with status message:"
			print error_message
			print "============================"

	elif target.tor is not None and target.proxy is None and target.socks is None:
		try:		
			session = requesocks.session()
			session.proxies = {
				"socks5": "socks5://127.0.0.1:9050"
			}
			request = session.get(target.host, auth=('user','pass'))
			checkparam(request)
		except requesocks.exceptions.ConnectionError as error_message:
			print "============================"
			print "HTTP connection failed with status message:"
			print error_message
			print "============================"

	elif target.proxy is not None and target.tor is None and target.socks is None:
		proxy = {
			"http": "http://"+target.proxy,
			"https": "https://"+target.proxy
		}
		try:
			request = requests.get(target.host, proxies=proxy)
			checkparam(request)
		except requests.ConnectionError as error_message:
			print "============================"
			print "HTTP connection failed with status message:"
			print error_message
			print "============================"		 	

	elif target.socks is not None and target.proxy is None and target.tor is None:
		try:		
			session = requesocks.session()
			session.proxies = {
				"socks4": "socks4://"+target.socks,
				"socks5": "socks5://"+target.socks
			}
			request = session.get(target.host, auth=('user','pass'))
			checkparam(request)
		except requesocks.exceptions.ConnectionError as error_message:
			print "============================"
			print "HTTP connection failed with status message:"
			print error_message
			print "============================"
	
"""
run script
"""
def main():
	parser = MyParser(
		prog="httptester.py",
		description="A script to test http connection directly, \
		or via http proxy or via tor network [ \
		Weldan Jamili <mweldan@gmail.com> ]"
	)
	parser.add_argument(
		'--host', 
		help='Target protocol, hostname and path', 
		required=True, 
		metavar='http://mweldan.com/search'
	)
	parser.add_argument(
		'--tor', 
		help='Connect via tor network',  
		metavar='1'
	)
	parser.add_argument(
		'--proxy', 
		help='Connect via http proxy',  
		metavar='IP:PORT'
	)
	parser.add_argument(
		'--socks', 
		help='Connect via socks proxy',  
		metavar='IP:PORT'
	)	
	parser.add_argument(
		'--raw', 
		help='Print raw response content',  
		metavar='1'
	)
	parser.add_argument(
		'--status', 
		help='Print response status code',  
		metavar='1'
	)							
	
	arguments = parser.parse_args(namespace=target)
	
	if target.host is not None and target.host.find("//") != -1:
		runtest()
	else:
		parser.print_help()
		
if __name__ == "__main__":
	main()
