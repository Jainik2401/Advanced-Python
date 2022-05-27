#Write a Python program to create an union and intersection of sets.
set1 = set([1,2,3])
set2 = set([2,3,4])
union = set1.union(set2)
intersect = set1.intersection(set2)

print(f"union of {set1} and {set2} is {union}")
print(f"Intersection between {set1} and {set2} is {intersect}")
