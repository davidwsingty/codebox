# Python Script to install and configure ansible
# Python Version: 2.7
# Author: David Ingty <wsingty@gmail.com>
# Updated Date: 22/10/2019 02:45 IST


import os
import socket 


filename1 = "/etc/hosts"
filename2 = "inventory"
li, ipa, line = [], [], ""
myli = []


def find_line(word, filename):
    with open(filename, 'r') as f:
        for line in f:
            if word in line:
                return line



def checkfile(keyword, filename):
    with open(filename) as f:
        for eachline in f:
            if keyword in str(eachline):
                return "YES"



an = raw_input('Do you want to install ansible? Type y or n:')
if an == 'y':
    os.system('apt install ansible -y')


os.system('cp /etc/hosts /etc/hosts.`date +%s`')



print("This will append entries in the /etc/hosts file")

while line != "q":
    line = raw_input("Enter HOSTNAME or 'q' to Quit:\n")
    print("=" * 30 + "\n\n")
    addr1 = socket.gethostbyname_ex(line)
    data = "".join(addr1[-1]) +" "+ "".join(addr1[0])
    if data not in li:
        if line != "q":
            li.append(data)
    ip_addr = data.split()
    if ip_addr[0] not in ipa:
        if line != "q":
            ipa.append(ip_addr[0])



""" deleting q from the lists"""
try:
    ipa.pop(ipa.index('q'))
    li.pop(li.index('q'))
except:
    pass



""" adding a newline to the /etc/hosts file """
try:
    with open(filename1, 'a') as f:
        x = checkfile("Ansible nodes", filename1)
        if x == None:
            f.write('\n')
            f.write('Ansible nodes')
            f.write('\n')
            f.write('=' * 30)
            f.write('\n')
except:
    pass



""" adding the ip-add hostname entries to /etc/hosts file """
with open(filename1, 'a') as f:
    for line in li:  # li list holds IP-addr hostname mapping
        x = checkfile(str(line), filename1)
        if x == None:
            f.write(line)
            f.write('\n')


""" asking the user to create a group name for ansbile inventory file """
grp = raw_input("Please enter a group name:")
grp = "[" + grp + "]"



x = checkfile(grp, filename2)
if x == None:
    os.system('echo ' + grp + ' >> inventory') # append group name to inventory file



with open(filename2, 'a') as f:
    for line in ipa:
        x = find_line(line, filename2)
        if x == None:
            f.write(line)
            f.write('\n')



""" Generating and copying the ssh keys """
ans = raw_input("Do you want to generate new ssh key? Type y or n:")
if ans == "y":
    os.system('ssh-keygen')

ans2 = raw_input("Do you want to copy the ssh key to the hosts? Type y or n:")
if ans == "y":
    for item in ipa:
        print(ipa)
        os.system('ssh-copy-id root@' + item)
