from data_structures.cluster import Cluster
import re


class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.clusters = [
            Cluster(key, value["networks"], value["security_level"])
            for key, value in cluster_dict.items()
        ]

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        pref = self.name[0:3].upper()
        rem_list = []
        for cluster in self.clusters:
            res = re.search("^(%s)-(\d{1,3}$)" % pref, cluster.name)
            if not res:
                rem_list.append(cluster)
        for cluster in rem_list:
            self.clusters.remove(cluster)

        # by uncommenting the lines below, the entries with wrong address will be removed
        # for cluster in self.clusters:
        #     cluster.rem_rec()

    def get_datacenter(self):
        return self.name, list(cluster.get_cluster() for cluster in self.clusters)
