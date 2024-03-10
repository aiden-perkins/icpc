# ICPC

This is the code that my team and I made to solve problems during the ICPC competition, and I also later solved some of the problems by myself to get more experience. You can read more about the competition [here](https://icpc.global/), and I competed in the [SoCal Regional](http://socalcontest.org/current/index.shtml). 
I am going to try and solve all 11 problems of 2023 before 2024's competition.

### Results

[2023](http://socalcontest.org/history/2023/SCICPC-2023-2024-PreliminaryResults.html) - solved 4/11 problems, placed 33/83 overall and 1/5 for our school.

**_2023 notes:_**

- Easy - ~~1~~, ~~5~~, ~~7~~, ~~8~~, ~~10~~
- Medium - ~~3~~, ~~4~~, ~~6~~
  + 3 stumped me a little during compeition and I decided to ignore it, after doing [AOC](https://adventofcode.com/2023) later in December which had a bunch of graph problems, I realized this was a simple dijkstra's with a few extra lines.
  + 4 was just understanding the instructions, took me ~3 hours one night but due to only having one input I can't confirm my solution will work for all test inputs.
  + 6 required math knowledge, we spent a good 2 hours on this during the competition trying to get it but couldn't, after spending time making a terrible simulation (might try to improve that later) I was able to get an extremely precise answer.
- Hard - 2, 9, 11
  + 2 might not be as bad as I initially thought, just parsing mostly, going to try and time myself doing this one day and see if I can do it under 5 hours.
  + 9 I talked to a professor about solving this, and he said it could be dynamic programming, greedy, or network flow. Although I do not think greedy would apply here, I'm hoping he will help me later on.
  + 11 Thought I had the right idea, only worked for the first and last round. I need to do a lot more work for this and I don't want to put more time into this, see the note at the bottom of my code.

### Running

To run a specific problem just use [run_c++.sh](./run_c++.sh) / [run_python.sh](./run_python.sh) and some arguments as described below.

```
./run_(language).sh (problem set) (problem) [test case]
```
`language` - This can either be `python` or `c++` and it will run the specific shell file, it will automatically compile the c++ file and run that, so you just need to code.

`problem set` - The group of problems you want to select from, currently only `practice` and `2023` are valid.

`problem` - The problem that you want to be run, for practice problems you will probably need double quotes. For the code that was made during the competition, put `-comp` after the number for example `1-comp`.

`test case` - Which test case you want to run, most will only have 2, some only have 1, and some have 3. This is optional, and if you don't provide this argument, then all test cases will be run.

If you notice a `main-comp` file in any of the problems it's because we attempted this during the competition but failed, so that file isn't correct and won't run.
