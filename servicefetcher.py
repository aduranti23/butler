import os
import service

def fetchServices(status):
    command = "systemctl --type=service #argument | awk '{print $1 " "," "$2" "," "$3" "," "$4" "," "$5" ";}'"
    command = command.replace("#argument", printStatus(status))
    serviceList = os.popen(command).read()
    return serviceList


def printStatus(status):
    if status == "running":
        return "--state=running"
    if status == "all":
        return ""

def getServiceList(status):
    serviceList = []
    rawList = fetchServices(status)
    for line in rawList.splitlines():
        lineSplit = line.split(" ")
        if not line.startswith("UNIT"):
            serviceList.append(service.service(str(lineSplit[0]), str(lineSplit[4]), str(lineSplit[2])))
    return serviceList