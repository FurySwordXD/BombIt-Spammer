from spammer import Spammer

delay = input('Enter the delay: ')
mobile = input('Enter the mobile number: ')
count = input('Enter the number of blasts: ')
Spammer(mobile, count, delay).redbus_blast()