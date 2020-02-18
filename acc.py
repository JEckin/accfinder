#!/usr/bin/python
import smtplib
import threading
from optparse import *
import time
from proxylist import ProxyList
from mechanize import Browser
from os import *
import sys
import logging
import io

brows = Browser()

brows.set_handle_robots(False)
brows._factory.is_html = True
brows.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)')]
print("Email:")
email=raw_input()
print("Password:")
password=raw_input()
#print(email)
#print(password)

def Netflix():
	print("Trying Netflix:")
	url = "https://www.netflix.com/sa/login"
	try:
		brows.open(url, timeout=10)
		brows.select_form(nr=0)
        	brows.form['userLoginId'] = email
        	brows.form['password'] = password
        	brows.method = "POST"
        	submit = brows.submit()
		if 'https://www.netflix.com/browse' in  submit.geturl():
			print("{}[True][+] Password Found [{}][+]".format(password))
		else :
			print("%s[!] False Login Password%s\n")
	except:
		print('[!] <<<There are speeches in Communication>>> \n')
Netflix()
