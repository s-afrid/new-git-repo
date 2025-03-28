from traceback import print_tb


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    #Get hash value of a key
    def get_hash(self,key):
        hash = 0
        for c in key:
            hash += ord(c)
        return hash % self.MAX

    #Print hash table
    def get_table(self):
        for i in self.arr:
            if i == []:
                pass
            else:
                print(i)

    #Get value by key
    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    #Insert element by key
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    #Delete by key
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]

t = HashTable()

t['march 6'] = 179
t['march 7'] = 200
t['march 17'] = 490
t.get_table()
