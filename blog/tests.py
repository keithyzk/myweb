from django.test import TestCase

# Create your tests here.
def insertDBlist():
    ip = '192.168.1.1'
    mysqltype = 1
    username = 'yzk'
    password = 'addcn123'
    port = 3306
    master_ip = '192.168.1.2'
    master_port = 3307
    mysql_list.objects.create(ip=ip,mysqltype=mysqltype,username=username,password=password,port=port,master_ip=master_ip,master_port=master_port)

insertDBlist()