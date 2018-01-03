import telnetlib
import xml.etree.ElementTree as ET


def get_client_Logs(ip):
    '''open telnet session and retrieve the current loaded texture info, return string '''
    print("Setup Telnet Session")
    tn = telnetlib.Telnet(ip,'8085')
    tn.read_until(b"Running ",timeout=30)
    print("Getting Logs")
    stuff = tn.read_until(b"stop", timeout=90)
    print(stuff)
    tn.close()
    return stuff

def get_command_from_logs(ip):
    '''open telnet session and retrieve the current loaded texture info, return string '''
    print("Setup Telnet Session")
    stop = True
    commands = []
    tn = telnetlib.Telnet(ip,'8085')
    print("Restart the app to start grabbing commands")
    tn.read_until(b"Running ",timeout=30)
    while stop:
        tn.read_until(b"Sending ",timeout=30)
        command = tn.read_until(b" over", timeout=90)
        if b"data" in command:
            continue
        else:
            cmd_strip = command.strip(b" over")
            commands.append(cmd_strip)
            print(cmd_strip)

        if b"stop" in command:
            stop = False
    tn.close()
    return commands

def check_for_xml(xmlString):
    '''Check for valid sgnode xml'''
    tree = ET.ElementTree(ET.fromstring(xmlString))
    root = tree.getroot()
    # Look at each child for the app name and then return the app id for it
    for child in root:
        #print child.tag
        if child.tag == 'CloudYouiLib':
            results = child.tag
            print ('Found: ' + results)
            return True




#stuff = get_client_Logs("10.100.89.60")

stuff = get_command_from_logs("10.100.88.90")

print(stuff)

