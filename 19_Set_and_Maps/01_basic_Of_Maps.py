def main():
    d = {}
    
    d[10] = "number"          # int
    d[3.14] = "float"        # float
    d[True] = "boolean"     # bool
    d[(1, 2)] = "tuple"     # tuple (immutable)
    d["A"] = "string"       # string

    print(d)
    for key, value in d.items():
        print(key, value)
       

if __name__ == "__main__":
    main()

# Dictonary key must be hashable that means it must be immutable (they must not change)
# So key cannot be a list, set or dict

# d.items() returns an iterator of (key, value) pairs, eg: [ (key1, value1), (key2, value2), ... ] 
