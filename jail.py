from libs.vconsole2_lib import VConsole2Lib
__author__ = 'itsJarrett'


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


if __name__ == "__main__":
    main()
