import random
f = open("firstnames.txt", "r")
firstnames = f.readlines()
f.close()

firstnames = [name.replace(' \xa0\n', '') for name in firstnames]

f = open("surnames.txt", "r")
surnames = f.readlines()
f.close()

surnames = [name.replace('\n', '') for name in surnames]

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

while True:
    name = random_name()

    output = ""

    for n in name:
        output += n + " "
    print(output)
    input()
