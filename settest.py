#!/usr/bin/python


import sets

def main():
    set1 = sets.MySet()
    set1.add(1)
    set1.add(2)
    print(set1.list)
    set2 = sets.MySet()
    set2.add(2)
    set2.add(3)
    set3 = set1 & set2
    print(set3.size())
    set1.remove(1)
    print(set1.list)
    set4 = set2 | set1
    print(set4.list)
    set2.add(1)
    print(set2.list)
    print(set1.list)
    set5 = set2 - set1
    print(set5.list)    

if __name__ == '__main__': main()







