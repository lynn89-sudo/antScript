[![Athena Award Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Faward.athena.hackclub.com%2Fapi%2Fbadge)](https://award.athena.hackclub.com?utm_source=readme)

-- Run this in terminal to init script --
python compile.py script.txt vars.txt

*create le monde
- Creates the world. Nothing can be run till the world is created by you, the creator.

*enfin
- Ends the script. This is required in every antScript at the last line.

queen birth <name>
- Queen ant creates a new ant and assigns it the given name. Only one ant can be created in each cycle

queen list 
- Lists all ants, living and deceased

queen food
- Displays the food reserves

*kill <name>
- Kills a named ant, no questions asked. This can also kill the queen...

<name>=<name>
- Fuses ants together
- Command must immediately be followed by a task, using "fused" as the name (no individual ants can be named "fused")

<name> find food

<name> var <var_name> est <number> et <number> fin
- Creates or edits the value of a variable, the value is the addition of the two numbers
- Yes, "fin" ending is required

<name> avecvar <var_name> est <var_name> et <var_name> fin
- Creates or edits the value of a variable, the value is the addition of the two variables
- Yes, "fin" ending is required

<name> var <var_name> est <number> sans <number> fin
- Creates or edits the value of a variable, the value is the subtraction of the two numbers
- Yes, "fin" ending is required

<name> avecvar <var_name> est <var_name> sans <var_name> fin
- Creates or edits the value of a variable, the value is the subtraction of the two variables
- Yes, "fin" ending is required

