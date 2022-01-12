#!/usr/bin/python3
import argparse
import vagrant

parser = argparse.ArgumentParser()
parser.add_argument("action", choices=["init", "start", "stop", "destroy"], help="Action that script should do. It can be 'init', 'start', 'stop' or 'destroy'")
arg = parser.parse_args()

v = vagrant.Vagrant()

if arg.action == "init":
    if not v.box_list():
        v.box_add("centos/7", "https://app.vagrantup.com/centos/boxes/7", provider="virtualbox")
    else:
        print(v.box_list())
    #v.init(box_name="centos/7")
    v.up()
    pathtokey = v.keyfile()
    username = v.user()
    hostname = v.hostname()
    sshport = v.port()
    f = open("ansible/invent.txt","w")
    f.write("selftesthost ansible_host="+hostname+" ansible_user="+username+" ansible_ssh_private_key_file="+pathtokey+" ansible_port="+sshport)
    f.close()
    
    print ("VM has been created")
elif arg.action == "start":
    v.up()
    print ("VM has been started")
elif arg.action == "stop":
    v.halt()
    print ("VM has been stopped")
else:
    v.halt()
    v.destroy()
    #v.box_remove("centos/7","virtualbox")
    print ("VM has been destroyed")