# Packs of panic

Santa wants to have his elves make toys, but he does not have his administration in order yet. He has a list of parts that sit in each type of toy. The only problem is that some parts again consist of further parts, which makes counting the number of parts difficult.

For example, suppose he gets this list (you can ignore the missing parts for now):

```
Missing 46 parts
Zoink: 9 Oink, 5 Dink
Floep: 2 Flap, 4 Dink
Flap: 4 Oink, 3 Dink
```

In this example, Zoinks are easy: there are a total of 14 (9 + 5) components. A Flap is more cumbersome, because the Flaps in it each also consist of several parts. Each Flap consists of 7 parts. So in a Floep there are 18 (2 * 7 + 4) parts.

[Download the toy list](https://infiaoc.azurewebsites.net/api/aoc/input/2021/4IW9MA8JLE7W)

Given the toy list, find the toy with the largest number of parts. This number is then the answer to part 1 .

Fill in the number of parts below. 
