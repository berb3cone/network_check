from data_structures.entry import Entry
import re


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipv4_network
        self.entries = [
            Entry(val["address"], val["available"], val["last_used"])
            for val in raw_entry_list
        ]

    def __repr__(self):
        return repr([self.ipv4_network, self.entries])

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        ipv4 = self.ipv4_network.split("/")[0]
        mask = int(self.ipv4_network.split("/")[1])
        bin_ipv4 = ""
        rem_list = []
        for i in ipv4.split("."):
            bin_ipv4 += format(int(i), "#010b")[2:]
        for entry in self.entries:
            if re.search("^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", entry.address):
                e_bin_ipv4 = ""
                for i in entry.address.split("."):
                    if int(i) < 256:
                        e_bin_ipv4 += format(int(i), "#010b")[2:]
                    else:
                        rem_list.append(entry)
                        break
                if bin_ipv4[:mask] != e_bin_ipv4[:mask]:
                    rem_list.append(entry)
            else:
                rem_list.append(entry)
        for entry in rem_list:
            self.entries.remove(entry)

        # by uncommenting the line below, the remaining entries will be sorted ascending by address
        # self.sort_records()

        return self

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)

    def get_net_col(self):
        return self.ipv4_network, list(entry.get_entries() for entry in self.entries)
