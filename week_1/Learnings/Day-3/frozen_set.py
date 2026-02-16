fs = frozenset([1,2,3])
print(fs)
print(type(fs))
#fs.append(4)
 
d = {
    frozenset([1,2]) : "group A",
    frozenset([3,4]) : "group B"
}
print(d)
