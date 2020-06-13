class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used

    def __lt__(self, other):
        num_add1 = [int(add) for add in self.address.split(".")]
        num_add2 = [int(add) for add in other.address.split(".")]
        return num_add1 < num_add2

    def __repr__(self):
        return repr(self.address)

    def get_entries(self):
        return self.address, self.available, self.last_used
