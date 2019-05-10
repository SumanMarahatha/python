# Write in to a file
w_file = open("bee.txt", "w")

w_file.write("hello bee\n")

w_file.close()

# Read contents from a file
r_file = open("bee.txt", "r")

content = r_file.read()
print(content.upper())  # Print contents of the file in uppercase

r_file.close()

