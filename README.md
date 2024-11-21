# ICPC

This is the code that my team and I made to solve problems during the ICPC competition, and I also later solved some of the problems by myself to get more experience. You can read more about the competition [here](https://icpc.global/), and I competed in the [SoCal Regional](http://socalcontest.org/current/index.shtml). 

### Results

2023 - [Problem Set](http://socalcontest.org/history/2023/SCICPC-2023-2024-ProblemSet.pdf) - [Standings](http://socalcontest.org/history/2023/SCICPC-2023-2024-PreliminaryResults.html) - solved 4/11 problems, placed 33/83 overall and 1/5 for our school.
2024 - [Problem Set](http://socalcontest.org/history/2024/SCICPC-2024-2025-ProblemSet.pdf) - [Standings](http://socalcontest.org/history/2024/SCICPC-2024-2025-PreliminaryResults.html) - solved 3/12 problems, placed 37/83 overall and 1/5 for our school.

**_notes:_**

2024 competition, what a huge disappointment. It had been a whole entire year since the last competition and I had done so much to prepare.
I had solved all problems from 2023, solved all of AOC 2023, took 36 units of upper division CS classes, solved 20+ leetcode problems and solved 20+ online problems (spoj, online judge, etc.).
On top of all of that, I had printed pretty much anything I would need, I read part of the competitive programming textbook, I was super confident going in. And... I solved 1 less problem than before.
I don't know what to do, this destroyed me. From here on out I am ditching python and I am only going to use c++ to solve programming puzzles.
After AOC 2024 my goal is going to be to solve as many kattis problems as possible that are recommended in the CP4 textbook, using only c++, and I will try and do one everyday.
By the time next the next competition comes, I want to have solved at least 200, all in c++, all from the textbook.


### Running

To run a specific problem just use [run_c++.sh](./run_c++.sh) / [run_python.sh](./run_python.sh) and some arguments as described below.

```
./run_(language).sh (problem set) (problem) [test case]
```
`language` - This can either be `python` or `c++` and it will run the specific shell file, it will automatically compile the c++ file and run that, so you just need to code.

`problem set` - The group of problems you want to select from, currently `2023`, `2024`, `goldstein`, & `online judge` are valid.

`problem` - The problem that you want to be run, for practice problems you will probably need double quotes. For the code that was made during the competition, put `-comp` after the number for example `1-comp`.

`test case` - Which test case you want to run, most will only have 2, some only have 1, and some have 3. This is optional, and if you don't provide this argument, then all test cases will be run.

If you notice a `main-comp` file in any of the problems it's because we attempted this during the competition but failed, so that file isn't correct and won't run.
