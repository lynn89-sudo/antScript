import random
import sys

def dev(message):
    print("$DEVLOG:", message)

def fail(message, index):
    error = "!-ERROR-! :"
    print("")
    print("================================")
    print(error, message)
    print("-- LINE", index, "--")
    print("================================")

def queen(ants):
    return ants[0][1]

def double(chunk):
    if ("fused" in chunk):
        #dev("true")
        return 2
    else:
        #dev("false")
        return 1


def runScript(filename, varsheet):
    operators = ["etvar", "sansvar", "var", "est", "et", "sans"]
    with open(varsheet, "r") as file:
        raw = []
        vars = []
        list = file.readlines()
        for el in list:
            raw.append(el.strip())
        print("")
        print("Imported Variable Names:", raw)
        for ra in raw:
            vars.append([ra, 0])
    
    interdit = []
    for i in operators:
        interdit.append(i)
    for i in raw:
        interdit.append(i.strip())

    with open(filename, "r") as file:
        lines = file.readlines()
    
    index = 1

    food = 6
    ants = [["queen", True, 1]]
    fused = []


    if (lines[len(lines)-1] != "*enfin"):
        fail("You did not end this antScript with 'enfin'", len(lines))
    else:
        for line in lines:
            if (index == 1):
                if (line != "*create le monde\n"):
                    fail("You have not created the world, use 'create le monde'", index)
                    break
            else:
                if (len(line) >= 2 and line[0:2] == "//"):
                    pass
                elif (line == "*create le monde\n"):
                    fail("You have already created the world, you cannot make multiple worlds", index)
                    break
                elif (line == "queen list\n"):
                    food -= 1
                    if (queen(ants)):
                        print("")
                        for ant in ants:
                            if (ant[1]):
                                alive = "alive"
                            else:
                                alive = "dead"
                            print("[", ant[0], "|", alive)
                    else:
                        fail("The queen is dead, you cannot run this task", index)
                        break
                elif (line == "queen food\n"):
                    food -= 1
                    if (queen(ants)):
                        print("")
                        print("Food Reserves:", food)
                    else:
                        fail("The queen is dead, you cannot run this task", index)
                        break
                elif ("*kill" in line):
                    chunk = line[6:]
                    chunk = chunk.strip()
                    found = False
                    for ant in ants:
                        if (ant[0] == chunk and ant[1] == True):
                            ant[1] = False
                            print("")
                            print("You have squashed", chunk)
                            found = True
                            break
                    if (found == False):
                        fail("Could not find given name, ant does not exist or is already dead", index)
                        break
                elif ("queen birth" in line):
                    food -= 1
                    if (queen(ants)):
                        chunk = line[12:]
                        chunk = chunk.strip()
                        if (chunk == ""):
                            fail("Name was not given, cannot create new ant", index)
                            break
                        elif (chunk in interdit):
                            fail("Operators cannot be included in a given name, cannot create new ant", index)
                            break
                        else:
                            valid = True
                            for ant in ants:
                                if (ant[0] == chunk):
                                    valid = False
                                    break
                            if (valid):
                                ants.append([chunk, True, index])
                                print("")
                                print(chunk, "has been created")
                            else:
                                fail("Ant with given name already exists, you cannot name a new ant with this name", index)
                                break
                    else:
                        fail("The queen is dead, you cannot run this task", index)
                        break
                elif ("find food" in line):
                    i = 0
                    chunk = ""
                    for i in range(len(line)-1):
                        if (line[i:i+1] == " "):
                            break
                        else:
                            chunk += line[i:i+1]
                    chunk = chunk.strip()
                    
                    valid = False
                    for ant in ants:
                        if (ant[0] == chunk and ant[1]):
                            valid = True
                            break
                    if (valid):
                        food -= 1
                        if (double(chunk)):
                            food -= 1
                        found = random.randint(0, 4)
                        found *= double(chunk)
                        food += found
                        addon = ""
                        if ( found <= 1):
                            addon = ":("
                        elif (found >= 3):
                            addon = ":D"
                        print("")
                        print(chunk, "found", found, "food reserves", addon)
                    else:
                        fail("Could not find given name, ant does not exist or is dead", index)
                        break
                elif ("=" in line):
                    #print("fused" in lines[index] == False)
                    next = lines[index]
                    next = next.strip()
                    #print(next[0:5])
                    if (double(next[0:5].strip()) == 2):
                        count = 0
                        chunk = ""
                        
                        while(line[count:count+1] != "="):
                            chunk += line[count:count+1]
                            count += 1
                        ant1 = chunk.strip()
                        chunk = line[count+1:]
                        ant2 = chunk.strip()
                        fused.append(ant1)
                        fused.append(ant2)
                        i = 0
                        count = 0
                        while i < len(ants):
                            if (ants[i][0] in fused and ants[i][1]):
                                #del ants[i]
                                ants[i][1] = False
                                i += 1
                                count += 1
                            else:
                                i += 1
                        if (count == 0):
                            fail("Neither given ant is alive or has been created", index)
                            break
                        elif (count == 1):
                            fail("One given ant is not alive or has not been created", index)
                            break
                        ants.append(["fused", True, index])
                        print("")
                        print(ant1, "and", ant2, "have been fused")
                    else:
                        fail("Fused ants did not perform a task immediately after being fused", index+1)
                        break
                elif ("*enfin" == line.strip() or line.strip() == ""):
                    pass
                else:
                    valid = False
                    components = []
                    op = ""
                    for i in operators:
                        if (i in line):
                            valid = True
                            op = i
                            break
                    if ("fin" not in line):
                        valid = False
                    if (valid):
                        i = 0
                        comp = ""
                        while i < len(line):
                            if (line[i:i+1] == " "):
                                components.append(comp)
                                comp = ""

                            else:
                                comp += line[i:i+1]
                            i += 1
                        #dev(components)
                        if (components[1] == "var" and components[3] == "est"):
                            components[4] = int(components[4])
                            components[6] = int(components[6])
                            r = -100000000001
                            if (components[5] == "et"):
                                r = components[4] + components[6]
                            elif (components[5] == "sans"):
                                r = components[4] - components[6]
                            else:
                                fail("Syntax error, no mode (+, -) defined, use 'et' or 'sans'", index)
                                break
                            if (r != -100000000001):
                                for k in vars:
                                    if k[0] == components[2]:
                                        k[1] = r
                                        print("")
                                        print("Set var", components[2], "to", r)
                        elif (components[1] == "avecvar" and components[3] == "est"):
                            r = -100000000001
                            v1 = -100000000001
                            v2 = -100000000001
                            for k in vars:
                                if (components[4] == k[0]):
                                    v1 = k[1]
                                elif (components[6] == k[0]):
                                    v2 = k[1]
                            if (v1 == -100000000001 or v2 == -100000000001):
                                fail("Syntax error, given var doesn't exist", index)
                                break
                            if (components[5] == "et"):
                                r = v1 + v2
                            elif (components[5] == "sans"):
                                r = v1 - v2
                            else:
                                fail("Syntax error, no mode (+, -) defined, use 'et' or 'sans'", index)
                                break
                            if (r != -100000000001):
                                for k in vars:
                                    if k[0] == components[2]:
                                        k[1] = r
                                        print("")
                                        print("Set var", components[2], "to", r)
                        
                    else:
                        fail("Syntax error", index)
                        break
                        

                    
                if ("fused" in line):
                    del ants[len(ants)-1]

                if (food <= 0):
                    for ant in ants:
                        ant[1] = False
                    print("")
                    fail("There are no food reserves remaining, all ants have died", index)
                    break
                        





            index += 1


    print("")



filename = sys.argv[1]
varsheet = sys.argv[2]
runScript(filename, varsheet)

# python compile.py script.txt vars.txt

#^^^ run this in powershell/bash