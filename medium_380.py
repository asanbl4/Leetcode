import random


class RandomizedSet:
    def __init__(self):
        self.list = []
        self.hashmap = dict()

    def insert(self, val: int) -> bool:
        if val not in self.hashmap.keys() or not self.hashmap.get(val):
            self.hashmap[val] = True
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.hashmap.keys() or not self.hashmap.get(val):
            return False
        self.list.remove(val)
        self.hashmap[val] = False
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)

#
#
# if __name__ == '__main__':
#     randomizedSet = RandomizedSet()
#     randomizedSet.insert(1)
#     randomizedSet.remove(2)
#     randomizedSet.insert(2);
#     randomizedSet.getRandom()
#     randomizedSet.remove(1)
#     randomizedSet.insert(2)
#     randomizedSet.getRandom()