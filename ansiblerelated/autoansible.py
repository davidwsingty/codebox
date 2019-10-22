# Python Script to install and configure ansible
# Python Version: 2.7
# Author: David Ingty <wsingty@gmail.com>
# Updated Date: 22/10/2019 02:45 IST


import os 


li, ipa, line = [], [], ""
myli = []

def find_line(word):
    with open('inventory', 'r') as f:
        for line in f:
            if word in line:
                return line



an = raw_input('Do you want to install ansible? Type y or n:')
if an == 'y':
    os.system('apt install ansible -y')


os.system('cp /etc/hosts /etc/hosts.`date +%F`')
filename1 = "/etc/hosts"
filename2 = "inventory"


print("This will append entries in the /etc/hosts file")

while line != "q":
    line = raw_input("Enter <IP-ADDR> <HOSTNAME> or 'q' to Quit:")
    if line not in li:
        li.append(line)
    ip_addr = line.split()
    if ip_addr[0] not in ipa:
        ipa.append(ip_addr[0])


""" deleting q from the lists"""
ipa.pop(ipa.index('q'))
li.pop(li.index('q'))

""" adding a newline to the /etc/hosts file """
with open(filename1, 'a') as f:
    f.write('\n')

""" adding the ip-add hostname entries to /etc/hosts file """
with open(filename1, 'a') as f:
    for line in li:
        x = find_line(line)
        if not x:
            f.write(line)
            f.write('\n')



uniqlines = set(open('/etc/hosts').readlines())
with open('/etc/hosts', 'w') as f:
    f. writelines(set(uniqlines))



""" asking the user to create a group name for ansbile inventory file """
grp = raw_input("Please enter a group name:")
grp = "[" + grp + "]"


"""
with open('inventory', 'r') as f:
    for eachline in f:
        if "[" + grp + "]" in eachline:
            myli = []
            if eachline not in myli:             
                myli.append(eachline)


for line in myli:
    if "[" + grp + "]" in line:
        os.system('echo ' + grp + ' >> inventory')
"""

os.system('echo ' + grp + ' > inventory')

with open(filename2, 'a') as f:
    for line in ipa:
        x = find_line(line)
        if x != str(line):
            f.write(line)
            f.write('\n')


"""
uniqlines = set(open(filename2).readlines())
with open(filename2, 'w') as f:
    f. writelines(set(uniqlines))
"""


""" Generating and copying the ssh keys """
ans = raw_input("Do you want to generate new ssh key? Type y or n:")
if ans == "y":
    os.system('ssh-keygen')

ans2 = raw_input("Do you want to copy the ssh key to the hosts? Type y or n:")
if ans == "y":
    for item in ipa:
        os.system('ssh-copy-id root@' + item)
