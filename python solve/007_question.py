def append(item , lst):
    lst = []
    lst.append(item)
    return lst

a = append(1, [])
print(a)

b = append(2, a)
print(b)

c = append(3, [])
print(c)

#output = 1 2 3  are kept in different list at different time
