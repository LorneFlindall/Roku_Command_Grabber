import telnetlib

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


stuff = get_command_from_logs("10.100.88.90")

print(stuff)

