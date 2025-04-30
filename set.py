unique_set = set()

# unique_set.add("manager")
#
# unique_set.discard("manager")
#
# unique_set.remove('manager') #throw error when param dont exists

set1 = {3,4,2,5,6,8}
set2 = {0,9,1,5,6,8}
set3 = set1 - set2

set4 = set1.symmetric_difference(set2)
set5 = set2.union(set3)
set6 = set3 ^ set4 #shortcut for symmetric difference

# subset
set7 = set4.issubset(set5)

set8 = set5 <= set6

set9 = set5.issuperset(set6)

set10 = set6.isdisjoint(set7) #have nothing in common

print(set3)
print(set4)
print(set1.difference(set2))
print(set1.intersection(set2))
