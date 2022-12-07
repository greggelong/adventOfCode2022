## a place to hold some code for Advent of code 2022

https://adventofcode.com/2022

I am starting a couple days late.

I have caught up by December 4th
let's see if I can keep it up.

really hacky solutions in python


- [X] day one -- used a dictionary to keep track of elves and calories list. I guess I could have just used a list of lists.
- [X] day two -- rock paper scissors -- some long winded logic checking for wins, losses and ties, and getting a score.
- [X] day three -- used a lookup table (list and index) to keep track of priorities values and "in" to check for duplicates from the first list in second list.
- [X] day four -- tried using strings but ran into edge case problems, then sets, finally used lists and all() and any() to find lists that contain each other or overlap.  And now I see a better solution would be to check for collision of the two the same way I would if the values were coordinates of objects in a game.

- [X] day five -- made something like a simple interpreter to execute movement commands on 2d stacks of boxes, nested lists as stacks.
- [X] day six -- used set() to check for no repeats in a list - of 4 or 14 characters in another list of characters 
- [F] day seven -- really bad fail, got it to work on sample data but not on input. did not take into account the relative directory names the tree (it would over count) 