#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {[count]} items.")

    def remove(self, item):
        print(f"Removed {[item]} from the list.")
        super().remove(item)  # This will raise ValueError if item not in list

    def pop(self, index=-1):
        item = self[index]  # Check what will be popped first
        print(f"Popped {[item]} from the list.")
        return super().pop(index)
