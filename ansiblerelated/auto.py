
import os 


li, ipa, line = [], [], ""
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
        f.write(line)
        f.write('\n')


""" asking the user to create a group name for ansbile inventory file """
grp = raw_input("Please enter a group name:")
grp = "[" + grp + "]"

""" writing the group name to the inventory file """
os.system('echo ' + grp + ' > inventory')


with open(filename2, 'a') as f:
    for line in ipa:
        f.write(line)
        f.write('\n')


