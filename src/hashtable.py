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
            # wrap the key,value in the "linked Pair" and assign it to that key
        # otherwise - there might be some collision occuring because the index already exsists
            # if the current key matches the key passed in
                # replace the current value
            # otherwise deal with the next slot
                # store next value in variable
                # while next slot exsists
                    # if the next slot's key matches the passed in key
                        # replace the value of the slot
                    # elif there is no next in the chain
                        # wrap the key,value in the "linked pair" and assign it to that key
                    # otherwise
                        # rest the next variable
        # increate the size using the resize method below
        # dont forget to return
    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # TODO:
        # hash the key and use as index
        # if the key exsists
            # check if the keys match
                # set the value to None
            # otherwise handle the collision
                # store next value in variable
                # while next slot exsists
                    # if the next slot's key matches the passed in key
                        # replace with None
                    # otherwise
                        # rest the next variable
        # otherwise
            # print the key is not found
        # dont forget to return
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #TODO:
        # hash the key and use as index
        # if the key exsists
            # check if the keys match
                # return the value
            # otherwise handle the collision
                # store next value in variable
                # while next slot exsists
                    # if the next slot's key matches the passed in key
                        # return the value
                    # otherwise:
                        # rest the next variable
        # otherwise
            # return None
        # dont forget to return


        pass


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Do this first because everything needs to use it
        Fill this in.
        '''
        #TODO:
        # muliply capacity by 2 and set it to the new value
        # Allocate storage with the new size
        # Loop through the list
            # rehash all the key/value pairs
            # add each to the newly created array.
        # reset storage to the new list

        pass



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
