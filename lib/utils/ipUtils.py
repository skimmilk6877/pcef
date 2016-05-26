#-*- coding:UTF-8 -*-
#!/usr/bin/python



#iplist=get_ip('172.17.203.11-172.17.203.38')


def get_ip(ip):
    ip_segment =  ".".join(ip.split('-')[0].split('.')[:-1])
    ip_start= int(ip.split('-')[0].split('.')[-1])
    ip_end= int(ip.split('-')[1].split('.')[-1])
    range_end=ip_end+1

    return [ ip_segment +'.'+ str(x) for x in range(ip_start, range_end)]


len