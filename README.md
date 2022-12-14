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
- [ ] FAIL  day seven -- really bad fail on my own. Got it to work on example input  data but not on the full input data. did not take into account the relative directory names  and a recursive file tree the (it would over count).  Got it to work using a stack for recursive summing. But I went to the reddit for help :(

- [X] day eight -- sparked some joy. The challenge was well suited for a graphic visualization and decided to solve it in JavaScrip with p5 library.    

see it here

https://greggelong.github.io/adventOfCode2022/day8/day8js/index

- [X] day nine part one only -- solved by graphing head and tail movements using  p5 vectors then getting an array of all the tail movements and using the new javaScript set to get rid of duplicates.  a covid headache is keeping me from solving the longer tail of part two and constant vpn problems in Beijing have made updating repos super hard. I cant even check my gmail account


- [X]  day 10 part 1 only, should be able to do part 2 with some string manipulation

- [X] day 11 part 1, first time doing some oop. Made a monkey class with data and turn methods then ran initialized all the monkeys and ran twenty rounds.

- [X]  day 12 part 1, working slowly on this one which requires finding a shortest path, so needed to review breadth first search algorithms, which is extra hard without vpn in China now.  I watched a MIT lecture from https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/resources/lecture-4-search-depth-first-hill-climbing-beam/ and reread Grokking algorithms chapter. Also watched the Coding Train coding challenge 68, on billibilli.  and followed the https://infogalactic.com/info/Breadth-first_search  as I cannot use Wiki in china at the moment.

 But much more than than I needed to create a Cell class with to hold data like was visited, height and connections.  I made a simple connection method, and all of the things seem to be connected to each other.  however I needed to change how the connections are made. The key was you are connected to any square your height +1 or lower.  I had miss read thinking you are connected if you are same or one height level different. 
 Then I followed the bfs algorithm and got a list of steps

I am sure this could have been done in a less complicated way. but I really needed to use classes to solve this one.  but as I am also visualizing this, the whole thing becomes more like making a game than writing a script to solve a problem. 


https://greggelong.github.io/adventOfCode2022/day12/index
