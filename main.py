from libs.vconsole2_lib import VConsole2Lib
import time
import requests
import sys
import json

__author__ = 'itsJarrett'

# CHANGE THIS VARIABLE TO THE SERVER IP WITH PORT AS STRING.
server_ip = raw_input("What is the server ip with port?")
joined = False


def server_json():
    if server_online():
        req = requests.get('https://servers-live.fivem.net/api/servers/single/' + server_ip)
        return req.json()


def server_online():
    req = requests.get('https://servers-live.fivem.net/api/servers/single/' + server_ip)
    if req.status_code == 200:
        return True
    return False


def server_joinable():
    if server_online() and server_json()["Data"]["clients"] < 32:
        return True
    else:
        return False


def my_on_disconnected(vconsole):
    """
    :param vconsole: VConsole2Lib
    """
    vconsole.log("Disconnected, trying reconnect...")
    while not vconsole.connect():
        pass
    vconsole.log("Connected...")


def my_on_prnt_received(vconsole, channel_name, msg):
    """
    :param vconsole: VConsole2Lib
    :param channel_name: str
    :param msg: str
    """
    vconsole.log(channel_name + " " + msg)
    pass


def main():
    vconsole = VConsole2Lib()
    vconsole.on_disconnected = my_on_disconnected
    vconsole.on_prnt_received = my_on_prnt_received

    print "Trying connect..."
    while not vconsole.connect('localhost', 29100):
        pass

    print "Connected..."
    print "Waiting 15 seconds..."
    time.sleep(15)

    while not joined:
        if server_joinable():
            print "Sending connect..."
            vconsole.send_cmd('connect ' + server_ip)
            time.sleep(10)
            sys.exit()
        else:
            if not server_online():
                print "Server Offline..."
            else:
                print "Full... Player Count: " + str(server_json()["Data"]["clients"])


if __name__ == "__main__":
    main()
