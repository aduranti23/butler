import os

def fetchServices(status):
    command = "systemctl --type=service #argument | awk '{print $1 "  ";"  "$2"  ";"  "$3"  ";"  "$4" ";" "$5}'"
    command = command.replace("#argument", printStatus(status))
    serviceList = os.system(command)
    return serviceList
    

def printStatus(status):
    if status == "running":
        return "--state=running"
    if status == "all":
        return ""