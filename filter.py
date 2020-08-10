f = open("surnames.txt", "r")
lines = f.readlines()
f.close()
names = ""
for line in lines:
    line = line.split(' ')
    names += line[1] + "\n"
print(names)

f = open("sn.txt", "w")
f.write(names)
f.close()
