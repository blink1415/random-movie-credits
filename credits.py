import random, time

f = open("firstnames.txt", "r")
firstnames = f.readlines()
f.close()

firstnames = [name.replace(' \xa0\n', '') for name in firstnames]

f = open("surnames.txt", "r")
surnames = f.readlines()
f.close()

surnames = [name.replace('\n', '') for name in surnames]

f = open("roles.txt", "r")
source = f.readlines()
f.close()

prefixes = []
roles = []
parts = []

source = [entry.replace('\n', '') for entry in source]

lists = [prefixes, roles, parts]
list_index = 0

for entry in source:
    if entry == "---":
        list_index += 1
        continue
    elif entry[0] == "#":
        continue
    else:
        lists[list_index].append(entry)

def random_name():
    name = []
    name.append(random.choice(firstnames))
    if random.randint(0,10) > 7:
        second_name = random.choice(firstnames)
        while second_name == name[0]:
            second_name = random.choice(firstnames)
        if random.randint(0, 10) > 7:
            second_name = second_name[0] + "."
        elif random.randint(0, 10) > 8:
            name[0] += "-" + second_name
        else:
            name.append(second_name)

    name.append(random.choice(surnames))
    return name

def random_role():
    role = random.choice(roles)
    if role[0] == "*" and random.randint(0,10) > 7:
        role = random.choice(prefixes) + " " + role
    return role.replace("*", "")


print("{:<30} {:<30}".format("Role", "Name"))

# while True:
#    name = random_name()
#    role = random_role()
# 
#    output = ""
# 
#    for n in name:
#        output += n + " "
#    print("{:<30} {:<30}".format(role, output))
#    time.sleep(0.5)

print(chr(27) + "[2J")

for role in roles:
    plural = random.randint(0,3) == 0
    plural_s = ""
    if plural:
        plural_s = "s"
    if role[0] == "*":
        name = random_name()
        output = ""
        for n in name:
            output += n + " "

        

        print("{:<30} {:<30}".format(role.replace("*", "") + plural_s, output))
        if plural:
            count = random.randint(1,4)
            for i in range(0,count):
                name = random_name()
                output = ""
                for n in name:
                    output += n + " "

                print("{:<30} {:<30}".format("", output))

        time.sleep(0.5)
        
        num_prefixes = random.randint(0,2)
        prefix_choices = prefixes.copy()
        for i in range(0, num_prefixes):
            name = random_name()
            
            prefix = random.choice(prefix_choices)
            prefixed_role = prefix + " " + role

            output = ""
            for n in name:
                output += n + " "

            print("{:<30} {:<30}".format(prefixed_role.replace("*", ""), output))
            time.sleep(0.5)
    else:

        name = random_name()
        output = ""
        for n in name:
            output += n + " "

        print("{:<30} {:<30}".format(role.replace("*", ""), output))
        time.sleep(0.5)
    print()
