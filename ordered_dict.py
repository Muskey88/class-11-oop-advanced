class OrderedDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        result = []
        for key, value in zip(self._keys, self._values):
            result.append((key, value))
        return result
    
    def __setitem__(self, key, value):
        if key not in self._keys:    
            self._keys.append(key)
            self._values.append(value)
        if key in self._keys:
            for ind, values in enumerate(self._keys):
                if key == values:
                    self._values[ind] = value
                    
                
    def __getitem__(self, a_key):
        for key, value in zip(self._keys, self._values):
            if a_key == key:
                return value 
        raise KeyError(repr(a_key))
        
    def __contains__(self, a_key):
        for key in self._keys:
            if a_key == key:
                return True
        return False
        
    def __len__(self):
        return len(self._keys)
    
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for key, value in zip(self._keys, self._values):
            if key not in other or other[key] != value:
                return False
        return True
    
    def __ne__(self, other):
        for key1, key2 in zip(self._keys, other._keys):
            if key1 != key2:
                return True
        return False
            
    def __str__(self):
        s = '{'
        for key, value in zip(self._keys, self._values):
            s += '{}: {}, '.format(repr(key), repr(value))
        s = s.rstrip(', ')
        s += '}'
        return s
    
    __repr__ = __str__
        
    def __add__(self, other):
        new = OrderedDict()
        
        for key, value in self.items():
            new[key] = value 
            
        for key, value in other.items():
            if key in new:
                for index, keys in enumerate(self._keys):
                    if key == keys:
                        new._values[index] = value
            if key not in new:
                new[key] = value
        return new
    
    
        
    
    @classmethod
    def from_keys(cls, string):
        new = OrderedDict()
        for elem in string:
            new[elem] = None
        return new