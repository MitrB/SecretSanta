# SecretSanta
Create secret santa pairs
Idea by [JinfuC](https://github.com/JinfuC)

## Usage
You should provide a file with all the names of the participants on a different line (look at the names.txt files as reference). 
You can specify the filename with the -f flag. The exact same resulting files will be made given the same seed. 
You should change the seed, as it defaults to 1!
```
$ python santa.py -f [filename] -s [seed]
```
The ouput are named files. The name of the file indicates the person who has to receive this file.
As in each file it is described tho who they should give their present.

