#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        return self  # An iterator must return itself for iter()

    def __next__(self):
        try:
            item = next(self.iterator)  # Get next item from underlying iterator
            self.counter += 1           # Increment counter
            return item
        except StopIteration:
            raise  # Propagate StopIteration when no items are left

    def get_count(self):
        return self.counter
