from fabric.api import *
from fabric.contrib import *


def deploy():
	put("userparameter_mongodb.conf","/etc/zabbix/zabbix_agentd.d/", use_sudo=True)
	put("zabbix_mongo_status.py","/usr/share/zabbix-agent/", use_sudo=True)
	sudo("chmod 755 /usr/share/zabbix-agent/zabbix_mongo_status.py")
	sudo("service zabbix-agent restart")
