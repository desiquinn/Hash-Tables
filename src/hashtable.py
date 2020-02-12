# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity # Allocating memory


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        reference: https://runestone.academy/runestone/books/published/pythonds/SortSearch/Hashing.html

        Fill this in.
        '''
        # TODO: 
        # Hash the key and it will return an index
        index = self._hash_mod(key)

        # if the index doesn't exsist
        if self.storage[index] == None:
            # wrap the key,value in the "linked Pair" and assign it to that key
            self.storage[index] = LinkedPair(key, value)
        # otherwise - there might be some collision occuring because the index already exsists
        else:
            # if the current key matches the key passed in
            if self.storage[index].key == key:
                # replace the current value
                self.storage[index].value = value
            # otherwise deal with the next slot
            else:
                # store next value in variable
                next_item = self.storage[index].next
                # while next slot exsists
                while next_item is not None:
                    # if the next slot's key matches the passed in key
                    if next_item.key == key:
                        # replace the value of the slot
                        next_item.value = value
                    # elif there is no next in the chain
                    elif next_item == None:
                        # wrap the key,value in the "linked pair" and assign it to that key
                        next_item = LinkedPair(key,value)                  
                    # otherwise
                    else:
                        # rest the next variable
                        next_item = next_item.next
        # increate the size using the resize method below
        # self.resize()
        # dont forget to return
        return
    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # TODO:
        # hash the key and use as index
        index = self._hash_mod(key)
        # if the key exsists
        if self.storage[index] is not None:
            # check if the keys match
            if self.storage[index].key == key:
                # set the value to None
                self.storage[index] = None
            # otherwise handle the collision
            else:
                # store next value in variable
                next_item = self.storage[index].next
                # while next slot exsists
                while next_item is not None:
                    # if the next slot's key matches the passed in key
                    if next_item.key == key:
                        # replace with None
                        next_item = None
                    # otherwise
                    else:
                        # rest the next variable
                        next_item = next_item.next
        # otherwise
        else:
            # print the key is not found
            print(f"This key {key} is not found")
        # dont forget to return
        return


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #TODO:
        # hash the key and use as index
        index = self._hash_mod(key)
        # if the key exsists
        if self.storage[index] is not None:
            # check if the keys match
            if self.storage[index].key == key:
                # return the value
                return self.storage[index].value
            # otherwise handle the collision
            else:
                # store next value in variable
                next_item = self.storage[index].next
                # while next slot exsists
                while next_item:
                    # if the next slot's key matches the passed in key
                    if next_item.key == key:
                        # return the value
                        return next_item.value
                    # otherwise:
                    else:
                        # rest the next variable
                        next_item = next_item.next
        # otherwise
        else:
            # return None
            return None
        # dont forget to return
        return


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Do this first because everything needs to use it
        Fill this in.
        '''
        #TODO:
        old_storage = self.storage
        # muliply capacity by 2 and set it to the new value
        self.capacity *= 2
        # Allocate storage with the new size
        new_storage = [None] * self.capacity
        # reset storage to the new list
        self.storage = new_storage
        # Loop through the list
        for item in old_storage:
            # rehash all the key/value pairs using self.insert
            # add each to the newly created array.
            self.insert(item[0],item[1])




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
