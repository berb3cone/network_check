from resources.paths import RESOURCES_PATH
from data_structures.network_collection import NetworkCollection
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

if __name__ == "__main__":
    for file in ["network1", "network2"]:
        net_col = [
            NetworkCollection(key, value)
            for key, value in read_collection(file+".json").items()
        ]
        print("##### Validating \'remove_invalid_records\' method {} containing {} network collection(s) "
              "#####\n".format(file, len(net_col)))
        output = read_expected_results(file+".txt")
        if output:
            # print(output)
            if len(net_col) == len(output):

                for i in range(len(net_col)):
                    print("Validating network collection {}...".format(i+1))
                    print("Initial list:  {}".format(net_col[i]))
                    print("Expected list: {}".format(output[i]))
                    print("Updated list:  {}".format(net_col[i].remove_invalid_records()))
                    if output[i] == str(net_col[i]):
                        print("Validation successful! The updated list matches the expected output!\n")
                print("\n")
            else:
                print("ERROR! Wrong length for expected output file!\n")
                continue
        else:
            print("ERROR! Expected output file doesn't exist! Please add file {}.txt in {}\n".format(file,
                                                                                                     RESOURCES_PATH))
            continue
