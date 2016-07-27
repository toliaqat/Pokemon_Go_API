import base64
import time
import re
import random
from datetime import datetime
import threading
import argparse
import os
import platform
import sys

import config
import login
from getpass import getpass
import public_proto_pb2
import logic
import dirty
import api

def get_acces_token(usr, pws):
	access_token = None
	ltype = None
	if '@' in usr:
		print '[!] Using google as login..'
		google_data = None
		if platform.system() == 'Windows':
			google_data = login.login_google(usr,pws)
			if google_data is not None:
				access_token = google_data['id_token']
		else:
			access_token = login.login_google_v2(usr,pws)
		if access_token is not None:
			ltype = 'google'
	else:
		print '[!] I am a poketrainer..'
		access_token = login.login_pokemon(usr,pws)
		ltype = 'ptc'
	return access_token, ltype

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--username", help = "Login", default = None)
	parser.add_argument("-p", "--password", help = "Password", default = None)
	parser.add_argument("-l", "--location", help = "Location", required = True)
	args = parser.parse_args()
	if not args.username:
		args.username = getpass("Username: ")
	if not args.password:
		args.password = getpass("Password: ")
	access_token, ltype = get_acces_token(args.username, args.password)
	if access_token is not None:
		dirty.start_private_show(access_token, ltype, args.location)
	else:
		print '[-] access_token bad'

if __name__ == '__main__':
	main()
