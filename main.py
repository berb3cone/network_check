from data_structures.datacenter import Datacenter
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

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    # by editing datacenter.py (uncommenting lines 34-35) invalid network records will be removed
    # by editing network_collections.py (uncommenting line 51) remaining entries will be sorted by address
    for d in datacenters:
        # print(d.get_datacenter())
        d.remove_invalid_clusters()
        # print(d.get_datacenter())


if __name__ == '__main__':
    main()
