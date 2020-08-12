import random, time

def random_name():
    # Makes a random name from one or two first names and a surname.
    name = []
    
    # Randomly selects name #1
    name.append(random.choice(firstnames))
    
    # Sometimes selects a first name #2
    if random.randint(0,10) > 7:
        second_name = random.choice(firstnames)

        # Makes sure that name #1 and name #2 are different
        while second_name == name[0]:
            second_name = random.choice(firstnames)

        # Sometimes shortens first name #2 to the initial
        # For example "Eric" would be shortened to "E."
        if random.randint(0, 10) >= 6:
            second_name = second_name[0] + "."
            name.append(second_name)

        # Sometimes hyphenates name #1 and name #2 together
        elif random.randint(0, 10) > 7:
            name[0] += "-" + second_name

        else:
            name.append(second_name)

    name.append(random.choice(surnames))
    return name

# This function is not in use, as the script currently iterates 
# through the list of roles. Might be used in the future tho, so
# I've left this in.
def random_role():
    role = random.choice(roles)
    if role[0] == "*" and random.randint(0,10) > 7:
        role = random.choice(prefixes) + " " + role
    return role.replace("*", "")

# Gets list of first names from file
f = open("firstnames.txt", "r")
firstnames = f.readlines()
f.close()

firstnames = [name.replace(' \xa0\n', '') for name in firstnames]

# Gets list of surnames from file
f = open("surnames.txt", "r")
surnames = f.readlines()
f.close()

surnames = [name.replace('\n', '') for name in surnames]

# Gets list of roles, prefixes and parts from file
f = open("roles.txt", "r")
source = f.readlines()
f.close()

# Lists used to store the values from roles.txt
prefixes = []
roles = []
parts = []

source = [entry.replace('\n', '') for entry in source]

lists = [prefixes, roles, parts]
list_index = 0

# Sorts the values from roles.txt into their respective list
for entry in source:
    if entry == "---":
        list_index += 1
        continue
    elif entry[0] == "#":
        continue
    else:
        lists[list_index].append(entry)

# Clears console before printing credits
print(chr(27) + "[2J")


# Used to center the text in the console. This is temporary, and I will
# make a better system for centering text later.
# If the text isn't centered on your system, edit these values and see
# if it improves.
space = ""
for x in range(0, 35):
    space += " "

# Iterates through roles and randomly assigns names and prefixes to each role
for role in roles:

    # If the role starts with "!" it is a header. 
    # We print the header centered and with an extra space before it.
    if role[0] == "!":
        time.sleep(0.5)
        print()
        time.sleep(0.5)
        print(role.replace("!", "").center(len(space)*2 + 80))
        time.sleep(0.5)
        continue

    # Randomly decides to make a role occupied by multiple people
    plural = random.randint(0,3) == 0
    plural_s = ""
    if plural:
        plural_s = "s"

    # "*" at the beginning of a role indicates that it can take a prefix.
    if role[0] == "*":
        # Gets a random name
        name = random_name()
        output = ""
        for n in name:
            output += n + " "

        
        # If the role ends in "." we remove it to make space for the plural s.
        # This is neccessary for roles that end in "Tech." for instance.
        if role[len(role) - 1] == ".":
            role = [0,len(role)-2]

        print(space + "{:<40} {:<40}".format((role.replace("*", "") + plural_s).rjust(40), output))

        # If we decided to make this role plural we need to generate more names.
        if plural:
            # Makes a random number of extra people to fill a plural role 
            count = random.randint(1,4)
            for i in range(0,count):
                name = random_name()
                output = ""
                for n in name:
                    output += n + " "
                
                time.sleep(0.5)

                # These are printed without the role on the left, as this was
                # already printed on the line before
                print(space + "{:<40} {:<40}".format("", output))

        time.sleep(0.5)
        
        num_prefixes = random.randint(0,2)
        prefix_choices = prefixes.copy()
        for i in range(0, num_prefixes):
            name = random_name()
            
            prefix = random.choice(prefix_choices)
            if prefix == "Assistant" and random.randint(0,10) == 10:
                prefix += " to the"
            prefixed_role = prefix + " " + role

            output = ""
            for n in name:
                output += n + " "


            plural = random.randint(0,3) == 0
            plural_s = ""
            if plural:
                plural_s = "s"


            print(space + "{:<40} {:<40}".format((prefixed_role.replace("*", "") + plural_s).rjust(40), output))
            time.sleep(0.5)

            if plural:
                count = random.randint(1,4)
                for i in range(0,count):
                    name = random_name()
                    output = ""
                    for n in name:
                        output += n + " "
                    
                    time.sleep(0.5)
                    print(space + "{:<40} {:<40}".format("", output))
    else:

        name = random_name()
        output = ""
        for n in name:
            output += n + " "

        print(space + "{:<40} {:<40}".format((role.replace("*", "")).rjust(40), output))
        time.sleep(0.5)
    print()
for x in range(0,5):
    time.sleep(0.5)
    print()

print(space + "{:<40} {:<40}".format("The".rjust(40), "End"))

for x in range(0,15):
    time.sleep(0.5)
    print()
