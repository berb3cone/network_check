"""
#=============================================================#
# Purpose: from this filw will be executed the existing tests #
# To be used from main(), else the paths wont't work          #
#=============================================================#
"""


from tests.utils import *
from datetime import datetime
from resources.paths import LOG_PATH
from os import path


def test_runner():
    now = datetime.now()
    dt = now.strftime("%d_%m_%Y_%H_%M_%S")+".txt"
    # print(LOG_PATH)
    f = open(path.join(LOG_PATH, dt), "a")

    # TEST 1
    # Check the functionality of remove_invalid_records method in NetworkCollection
    f.write(run_test(["network1", "network2"], "remove_invalid_records"))

    # TEST 2
    # Check the functionality of sort_records method in NetworkCollection
    # This test simply sorts the values in the json files, so it does'n validate those values first
    # Some wrong IP addresses were left on purpose on the JSON files used by this test
    f.write(run_test(["network3", "network4"], "sort_records"))

    f.close()

    print("The logs of the 2 tests were saved in logs\\{}".format(dt))

# To be used from main(), else the paths wont't work
# if __name__ == "__main__":
#     test_runner()
