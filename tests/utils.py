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


def run_test(files, func):
    result = ""
    for file in files:
        net_col = [
            NetworkCollection(key, value)
            for key, value in read_collection(file+".json").items()
        ]
        result += "##### Validating \'{}\' method using {} config containing {} network collection(s) #####\n".format\
            (func, file, len(net_col))
        output = read_expected_results(file+".txt")
        if output:
            if len(net_col) == len(output):

                for i in range(len(net_col)):
                    result += "Validating network collection {}...\n".format(i+1)
                    result += "Initial list:  {}\n".format(net_col[i])
                    result += "Expected list: {}\n".format(output[i])
                    # net_col[i].sort_records()
                    getattr(net_col[i], func)()
                    result += "Updated list:  {}\n".format(net_col[i])
                    if output[i] == str(net_col[i]):
                        result += "Validation successful! The updated list matches the expected output!\n"
                result += "\n"
            else:
                result += "ERROR! Wrong length for expected output file!\n"
                continue
        else:
            result += "ERROR! Expected output file doesn't exist! Please add file {}.txt in {}\n".format(file,
                                                                                                         RESOURCES_PATH)
            continue
    result += "\n"
    print(result)
    return result
