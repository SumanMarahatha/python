def student(name,roll,age,address):
  print(name,roll,age,address)

student("pratima",name="partima",20,20,20)
#output= SyntaxError

student("pratima",20,age=25,"kathmandu")
#output= SyntaxError

student("pratima")
#output= Missing Arguments
