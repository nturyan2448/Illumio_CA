import csv
from math import floor

class Firewall:
    def __init__(self, filename):
        self.rules = []
        with open(filename) as csv_file:
            rules = csv.reader(csv_file, delimiter=',')
            for rule in rules:
                rule[2] = list(map(int, rule[2].split('-')))
                rule[3] = [list(map(int, ip.split('.'))) for ip in rule[3].split('-')]
                self.rules.append(rule)
        self.rules.sort()

    def binary_search(self, packet, rule):
        for i in range(0,2):
            if packet[i] != rule[i]:
                if packet[i] < rule[i]:
                    return -1
                return 1
        for i in range(2,4):
            if packet[i] < rule[i][0]:
                return -1
            if packet[i] > rule[i][-1]:
                return 1
        # if packet[0] != rule[0]: (direction)
        #     if packet[0] < rule[0]:
        #         return -1
        #     else:
        #         return 1
        # if packet[1] != rule[1]: (protocol)
        #     if packet[1] < rule[1]:
        #         return -1
        #     else:
        #         return 1
        # if packet[2] < rule[2][0]: (port, could be a range)
        #     return -1
        # if packet[2] > rule[2][-1]:
        #     return 1
        # if packet[3] < rule[3][0]: (IP, could be a range)
        #     return -1
        # if packet[3] > rule[3][-1]:
        #     return 1
        return 0

    def accept_packet(self, direction, protocol, port, IP):
        left = 0
        right = len(self.rules)-1
        while left <= right:
            mid = floor(left + (right - left)/2)
            search_result = self.binary_search((direction, protocol, port, list(map(int,IP.split('.')))), self.rules[mid])
            # print(mid, self.rules[mid], search_result)
            if search_result == 0:
                return True
            if search_result == -1:
                right = mid-1
            else:
                left = mid+1
        return False
