# https://codelearn.io/training/detail/44246
import ipaddress

calculateNetworkAddress = lambda x: str(ipaddress.ip_network(x, strict=False).network_address)

