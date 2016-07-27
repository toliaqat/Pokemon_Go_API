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
	login_session = login.get_login_session(args.username, args.password)
	dirty.start_private_show(login_session, args.location)

if __name__ == '__main__':
	main()
