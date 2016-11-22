#One liners

#Disk usage
du -sh *
df -h
du -x /var/log/ | sort -n | tail -40


#Network tools
telnet localcost 25
dig example.com +trace
traceroute
curl