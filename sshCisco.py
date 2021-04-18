import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetmikoTimeoutException

USERNAME = input("Please enter you SSH username: ")
PASS = getpass("Please enter you SSH password: ")

device = {
    'ip': '192.168.1.10',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    f = open('backup.conf', 'x')
    f.write(output)
    f.close()
except (AuthenticationException):
    print("An authentication error occurred while connecting to: " + device['ip'])
except (SSHException):
    print("An error occurred while connecting to the device " + device['ip'] + " via ssh. Is SSH enabled?")
except (NetmikoTimeoutException):
    print("The device" + device['ip'] + " timed out when attempting to connect")
