# Sample test 
from firewall import Firewall        
            
fw = Firewall('rule1.csv')
print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")) # return True
print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1")) # return True
print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11")) # return True
print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2")) # return False
print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92")) # return False