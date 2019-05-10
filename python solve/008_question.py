def append(item , lst):
    lst.append(item)
    return lst

a = append(1, [])
print(a)

b = append(2, a)
print(b)

c = append(3, [])
print(c)

#output value of a is appended along with 2 in list b