---STORY TREES---
This program is a fun interactive story tree where you simply select "1" or "2" based on which option you like more.
The purpose is... well... for fun!

---HOW TO USE---
Please run the Manager.py file to run the program.
You then have to input a tree file. (Without the extension, that is ".txt" which is added automatically.)

You can create your own tree files, as long as they are in the correct format. 
There are two correct formats:
Either set it up by each possible outcome for each branch:
1
1-1
1-1-1
1-1-2
1-2
1-2-1
1-2-2
Or set it up by each possible outcome based on the "level":
1
1-1
1-2
1-1-1
1-1-2
1-2-1
1-2-2
Etc. 
Each line must have two "|" to separate from "location","option","message."
(So for example 1-1-1 | OPTION | MESSAGE)
The tree also does not have to be balanced.

