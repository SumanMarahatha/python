class dog:
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind
    
d = dog("john","white")
e = dog("jonny","")

print(d.kind)  #output of d.kind

print(d.name)  #output of d.name

print(e.kind)  #output of e.kind

print(e.name)  #output of e.name
