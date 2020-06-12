from data_structures.network_collection import NetworkCollection


class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        self.name = name
        self.security_level = security_level
        self.networks = [
            NetworkCollection(key, value)
            for key, value in network_dict.items()
        ]

    def get_cluster(self):
        return self.name, self.security_level, list(net_col.get_net_col() for net_col in self.networks)

    def rem_rec(self):
        for net in self.networks:
            net.remove_invalid_records()
