# https://codelearn.io/training/detail/3884
import ipaddress

def isIPv4Address(inputString):
    try:
        ipaddress.ip_network(inputString)
        return True
    except:
        return False
