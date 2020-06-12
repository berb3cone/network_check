import re


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipv4_network
        self.raw_entry_list = raw_entry_list

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        ipv4 = self.ipv4_network.split("/")[0]
        mask = int(self.ipv4_network.split("/")[1])
        bin_ipv4 = ""
        for i in ipv4.split("."):
            bin_ipv4 += format(int(i), "#010b")[2:]
        for j in list(self.raw_entry_list):
            c = 1
            if re.search("^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", j["address"]):
                e_bin_ipv4 = ""
                for i in j["address"].split("."):
                    if int(i) < 256:
                        e_bin_ipv4 += format(int(i), "#010b")[2:]
                    else:
                        c = 0
                        break
                if bin_ipv4[:mask] != e_bin_ipv4[:mask]:
                    c = 0
            else:
                c = 0
            if not c:
                self.raw_entry_list.remove(j)

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
