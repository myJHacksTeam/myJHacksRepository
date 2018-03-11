import updater
import test
import argparse
location = input("Please enter the bin location: ")
nickname = input("Please enter the bin nickname: ")


while not updater.init_bin(location = location, nickname = nickname):
	print('Nickname already in use')
	location = input("Please enter the bin location: ")
	nickname = input("Please enter the bin nickname: ")

parser = argparse.ArgumentParser(description='init script for ReUniversity')
parser.add_argument('-d','--debug',help='Flag to turn on manual captcha solving mode',default=False,action='store_true')
args = parser.parse_args()

test.run(args.debug)