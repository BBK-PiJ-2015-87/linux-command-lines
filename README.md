#One liners

#Disk usage
du -sh *
df -h
du -x /var/log/ | sort -n | tail -40



telnet

#User access
Access control list
Mount with ACL
mount -t ext3 -o acl device-name partition
setfacl -m rules files
setfacl -m d:o:rx /share
getfacl home/john/picture.png

#Privileges
su - setuid command

dd users to the special administrative group called wheel:
usermod -a -G wheel username


The sudo command offers another approach to giving users administrative access.
The sudo command allows for a high degree of flexibility. For instance, only users listed in the /etc/sudoers configuration file are allowed to use the sudo command and the command is executed in the user's shell, not a root shell.

Each successful authentication using the sudo command is logged to the file /var/log/messages and the command issued along with the issuer's user name is logged to the file /var/log/secure.


Administrators wanting to edit the sudo configuration file, /etc/sudoers, should use the visudo command.


To give someone full administrative privileges, type visudo and add a line similar to the following in the user privilege specification section:

juan ALL=(ALL) ALL


#YUM

set global yum options by editing the [main] section of the /etc/yum.conf configuration file;
set options for individual repositories by editing the [repository] sections in /etc/yum.conf and .repo files in the /etc/yum.repos.d/ directory;
use yum variables in /etc/yum.conf and files in the /etc/yum.repos.d/ directory so that dynamic version and architecture values are handled correctly;
add, enable, and disable yum repositories on the command line; and
set up your own custom yum repository.
#Network tools
telnet localcost 25
dig example.com +trace
traceroute
curl