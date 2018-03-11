import updater
import test
location = input("Please enter the bin location: ")
nickname = input("Please enter the bin nickname: ")


while not updater.init_bin(location = location, nickname = nickname):
	print('Nickname already in use')
	location = input("Please enter the bin location: ")
	nickname = input("Please enter the bin nickname: ")

test.run()