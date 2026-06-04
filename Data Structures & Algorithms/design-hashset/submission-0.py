class MyHashSet:

    FIXED_SIZE_OF_ARRAY = 1009;

    def __init__(self):
        self.hashset = [0] * self.FIXED_SIZE_OF_ARRAY

    def _hashing(self,key: int):
          return key % self.FIXED_SIZE_OF_ARRAY
        

    def add(self, key: int) -> None:
        index = self._hashing(key)
        if self.hashset[index] != 0:
            # Not empty
            for elements in self.hashset[index]:
                # Iterating each bucket
                if elements == key:
                    return
            # If not found the element in the bucket
            self.hashset[index].append(key)
        else:
            # The bucket is empty
            self.hashset[index]  = [key]           

    def remove(self, key: int) -> None:
         index = self._hashing(key)
         if self.hashset[index] != 0:
            # Not empty
            for elements in self.hashset[index]:
                # Iterating each bucket
                if elements == key:
                    # Removing the key once found
                    self.hashset[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hashing(key)
        if self.hashset[index] != 0:
            # Not empty
            for element in self.hashset[index]:
                # Iterating each bucket
                if element == key:
                    # Removing the key once found
                    return True
        return False    

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)