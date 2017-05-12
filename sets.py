import math

class MySet:
    """A class of a logical set"""
    def __init__(self):
        self.list = []

    def contains(self, elem):
        for i in self.list:
            if i == elem:
                return True
        return False

    def add(self, elem):
        if not self.contains(elem):
            self.list.append(elem)

    def remove(self, elem):
        if self.contains(elem):
            self.list.remove(elem)

    def size(self):
        return len(self.list)

    def __and__(self, o):
        intersection = MySet()
        for i in self.list:
            if o.contains(i):
                intersection.add(i)
        return intersection

    def __or__(self, o):
        union = MySet()
        union.list = self.list
        for i in o.list:
            if not self.contains(i):
                union.add(i)
        return union

    def __sub__(self, o):
        difference = MySet()
        difference.list = self.list
        intersection = self & o
        for i in intersection.list:
            difference.list.remove(i)
        return difference
        
