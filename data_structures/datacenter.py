import re


class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.cluster_dict = cluster_dict

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        pref = self.name[0:3].upper()
        for cluster in list(self.cluster_dict):
            res = re.search("^(%s)-(\d{1,3}$)" % pref, cluster)
            if not res:
                del self.cluster_dict[cluster]
            #     print("Wrong: {}".format(cluster))
            # else:
            #     print("Correct: {}".format(cluster))
