from data_structures.datacenter import Datacenter
from data_structures.cluster import Cluster
from data_structures.network_collection import NetworkCollection
from urllib import request
import json
from time import sleep


URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    att = 0
    while att < max_retries:
        try:
            with request.urlopen(url) as content_http:
                content = content_http.read().decode()
            return json.loads(content)
        except:
            att += 1
        sleep(delay_between_retries)
    return False


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)
    # print(data)
    # print(type(data))
    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    # verify remove_invalid_clusters() method
    for d in datacenters:
        d.remove_invalid_clusters()

    # generating clusters list
    clusters = [
        Cluster(key, value["networks"], value["security_level"])
        for d in datacenters for key, value in d.cluster_dict.items()
    ]

    # generating net_col list
    net_col = [
        NetworkCollection(key, value)
        for c in clusters for key, value in c.network_dict.items()
    ]

    # call remove_invalid_records() method
    for netw in net_col:
        netw.remove_invalid_records()

    # pass  # the rest of your logic here


if __name__ == '__main__':
    main()
