# Batch-Scheduling-Model-for-distributed-systems
Implementation of IEEE paper on scheduling of jobs in an distributed environment

[Here](https://ieeexplore.ieee.org/document/7913119) is the link to the paper.

## Aim
The main goal of this project is to schedule given tasks with known sizes to computing nodes whose processing powers are known beforehand. We have implemented the mapping using two metaheuristic algorithms:
1) Genetic Algorithm
2) Bacterial Foraging Algorithm

Results are then displayed and compared. The metrics which were used for comparison are Utilization and Makespan, as explained in the paper.

## Input format
1) Processing power(in MIPS) of nodes must go into the [_nodes_](input/nodes) file in the _input_ folder, comma separated.
2) The sizes of the tasks(in MI) must go into the [_tasks_](input/tasks) file in the _input_ folder, comma separated. 

## Running the code
After placing all the required inputs in their respective files in the right format, run the following command in the terminal.
```python3
python3 scheduler.py
```
