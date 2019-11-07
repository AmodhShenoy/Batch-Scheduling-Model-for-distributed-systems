# Batch-Scheduling-Model-for-distributed-systems
Implementation of IEEE paper on scheduling of jobs in an distributed environment

[Here](https://ieeexplore.ieee.org/document/7913119) is the link to the paper.

## Input format
1) Processing power(in MIPS) of nodes must go into the [_nodes_](input/nodes) file in the _input_ folder, comma separated.
2) The sizes of the tasks(in MI) must go into the [_tasks_](input/tasks) file in the _input_ folder, comma separated. 

## Running the code
After placing all the required inputs in their respective files in the right format, run the following command in the terminal.
```python3
python3 scheduler.py
```
