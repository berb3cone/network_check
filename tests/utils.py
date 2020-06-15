"""
#================================================#
# This file contains methods used by test_runner #
# Possible functionss:                            #
#        remove_invalid_records                  #
#        sort_records                            #
#================================================#
"""

from data_structures.network_collection import NetworkCollection
from resources.paths import RESOURCES_PATH
from os import path
import json


def read_collection(file):
    with open(path.join(RESOURCES_PATH, file), 'r') as network:
        data = network.read()
    return json.loads(data)


def read_expected_results(file):
    try:
        with open(path.join(RESOURCES_PATH, file), 'r') as output:
            data = output.read().splitlines()
        return data
    except FileNotFoundError:
        return False


def verify_method(file, func):
    net_col = [
        NetworkCollection(key, value)
        for key, value in read_collection(file + ".json").items()
    ]
    output = read_expected_results(file + ".txt")
    if output:
        if len(net_col) == len(output):
            for i in range(len(net_col)):
                getattr(net_col[i], func)()
                if output[i] != str(net_col[i]):
                    return False, "Network collection no. {} in {} has a different output than " \
                                  "xpected!".format(i+1, file)
        else:
            return False, "In {}.txt we have {} collection(s), while in {}.json we have {} " \
                          "collection(s)!".format(file, len(output), file, len(net_col))
    else:
        return False, "Missing {}.txt file from resources!".format(file)
    return True, "ok"
