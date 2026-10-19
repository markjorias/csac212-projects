<div align="center">

# CSAC 212 · Introduction to Artificial Intelligence

**Search, logic and probabilistic reasoning exercises in Python, plus a project proposal, from a university AI course.**

![Python 3.12](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
![Programs: 6](https://img.shields.io/badge/programs-6-informational)
![Period: Sep-Oct 2024](https://img.shields.io/badge/period-Sep%E2%80%93Oct%202024-lightgrey)
![Status: coursework archive](https://img.shields.io/badge/status-coursework%20archive-blue)

</div>

## Overview

This repository collects the work I did for **CSAC 212: Introduction to Artificial Intelligence**. It has six small programs and one project proposal:

- **PS1: Search**, four classic search algorithms (breadth-first, depth-first, greedy best-first and an A*-style search) that find a route from Arad to Bucharest on a hand-built Romania road graph;
- **PS2: Knowledge**, which solves four *Knights and Knaves* logic puzzles by writing them as propositional-logic sentences and checking them with a model checker;
- **PS3: Uncertainty**, a Jupyter notebook that builds a Bayesian network with [pgmpy](https://pgmpy.org/) and queries it;
- a **project proposal** (PDF only, no code) for predicting early-stage diabetes risk with XGBoost.

**Skills demonstrated:** uninformed and informed search, knowledge representation in propositional logic, entailment by model checking, Bayesian networks (conditional probability tables, independencies, active trails), exact inference by variable elimination, MAP queries, and writing up a machine-learning project proposal.

## Table of contents

- [Getting started](#getting-started)
- [Repository structure](#repository-structure)
- [Programs](#programs)
- [Methodology](#methodology)
- [Sample results](#sample-results)

## Getting started

**Requirements:** Python 3.12 (the version everything here was run on) and the packages in [requirements.txt](requirements.txt): `networkx`, `matplotlib`, `pgmpy` 1.0 or newer, and `jupyter`. The PS2 program uses only the standard library.

```bash
python3 -m venv .venv
source .venv/bin/activate          # fish shell: source .venv/bin/activate.fish
pip install -r requirements.txt
```

**PS1: Search.** Each script first draws the map in a Matplotlib window. Close the window and the search runs, printing every step to the terminal.

```bash
python 01-problem-sets/ps1-search/bfs.py
python 01-problem-sets/ps1-search/dfs.py
python 01-problem-sets/ps1-search/gbfs.py
python 01-problem-sets/ps1-search/astar.py

# no display available? skip the window:
MPLBACKEND=Agg python 01-problem-sets/ps1-search/bfs.py
```

**PS2: Knowledge** (`logic.py` sits next to the script, so it can be run from anywhere):

```bash
python 01-problem-sets/ps2-knowledge/knights-and-knaves.py
```

**PS3: Uncertainty** (open the notebook, or execute it from the command line):

```bash
jupyter notebook 01-problem-sets/ps3-uncertainty/bayesian-network.ipynb
jupyter nbconvert --to notebook --execute 01-problem-sets/ps3-uncertainty/bayesian-network.ipynb --output-dir /tmp --output bayesian-network-run.ipynb
```

## Repository structure

```text
.
├── 01-problem-sets/
│   ├── ps1-search/
│   │   ├── bfs.py                      # breadth-first search
│   │   ├── dfs.py                      # depth-first search
│   │   ├── gbfs.py                     # greedy best-first search
│   │   └── astar.py                    # A*-style search
│   ├── ps2-knowledge/
│   │   ├── knights-and-knaves.py       # knowledge bases for puzzles 0-3
│   │   ├── logic.py                    # propositional-logic library supplied with the problem set
│   │   └── ps2-instructions.pdf        # problem-set handout
│   └── ps3-uncertainty/
│       ├── bayesian-network.ipynb      # Bayesian network and inference (pgmpy)
│       └── ps3-instructions.pdf        # problem-set handout
├── 02-project-proposal/
│   └── early-diabetes-xgboost-proposal.pdf
├── requirements.txt
└── README.md
```

## Programs

Dates are each file's **last-modified date** (YYYY-MM-DD) taken from the file system before this cleanup. The folder was not under version control, so there is no commit history to check them against. They show when a file was last saved, which is not always when the work was done.

### Problem sets ([01-problem-sets/](01-problem-sets/))

PS1's four search programs all search from Arad to Bucharest, print the frontier and explored set at each step, and draw the graph with `networkx` and `matplotlib`.

| Set | Program | Description | Concept practiced | Date |
|---|---|---|---|---|
| PS1: Search | [bfs.py](01-problem-sets/ps1-search/bfs.py) | Expands the oldest node in the frontier first (FIFO queue) | Breadth-first search, uninformed | 2024-09-13 |
| PS1: Search | [dfs.py](01-problem-sets/ps1-search/dfs.py) | Expands the newest node in the frontier first (LIFO stack) | Depth-first search, uninformed | 2024-09-13 |
| PS1: Search | [gbfs.py](01-problem-sets/ps1-search/gbfs.py) | Expands the frontier node with the lowest heuristic value (`hn`, intended as the straight-line distance to Bucharest) | Greedy best-first search, informed | 2024-09-13 |
| PS1: Search | [astar.py](01-problem-sets/ps1-search/astar.py) | Same graph with edge costs added; ranks frontier nodes by `hn` plus the cost of the last edge | A*-style informed search | 2024-09-13 |
| PS2: Knowledge | [knights-and-knaves.py](01-problem-sets/ps2-knowledge/knights-and-knaves.py) | Encodes four Knights and Knaves puzzles as knowledge bases and prints what can be concluded about each character | Propositional logic, entailment by model checking | 2024-09-20 |
| PS3: Uncertainty | [bayesian-network.ipynb](01-problem-sets/ps3-uncertainty/bayesian-network.ipynb) | Builds a five-variable Bayesian network (`ExamLevel`, `IQLevel`, `Marks`, `Aptiscore`, `Admission`), then examines independencies and active trails, runs variable-elimination queries with and without evidence, and finds most probable states; findings are written up in the notebook's markdown cells | Bayesian networks, exact inference, MAP queries | 2024-10-22 |

Supporting files: [logic.py](01-problem-sets/ps2-knowledge/logic.py) is the library supplied with PS2 (not original work; its date, 2020-04-02, is the original timestamp of the supplied file), and the two `*-instructions.pdf` files are the course handouts (2024-09-16 and 2024-09-26).

### Project proposal ([02-project-proposal/](02-project-proposal/))

| Document | Description | Concept practiced | Date |
|---|---|---|---|
| [early-diabetes-xgboost-proposal.pdf](02-project-proposal/early-diabetes-xgboost-proposal.pdf) | Four-page proposal to predict early-stage diabetes risk with XGBoost from age, sex and symptom data (mostly Yes/No features). Proposal only; no implementation exists | Framing a supervised-learning problem, related work | 2024-10-22 |

## Methodology

### PS1: Search

All four scripts share one structure and differ only in how the next node is chosen from the frontier.

1. **Model the problem.** Each of the 20 cities is a `Node` holding its name (`state`), a `parent`, and a list of successor nodes added with `add_action`. The roads are 24 one-way (directed) edges. The same edges are loaded into a `networkx` `DiGraph` and drawn at hand-set coordinates so the picture resembles a map of Romania. `gbfs.py` and `astar.py` also give each city a heuristic value `hn`, and `astar.py` gives each edge a cost.
2. **Search loop.** Start with Arad in the frontier and an empty explored list. Until the frontier is empty (which raises "no solution"):
   - print the frontier and explored set;
   - remove a node from the frontier and append its name to the `solution` list;
   - stop if it is Bucharest;
   - otherwise add it to the explored set and put its successors into the frontier, skipping explored ones.
3. **The only difference between the scripts** is the frontier's `remove()` method:

   | Script | Node removed from the frontier |
   |---|---|
   | `bfs.py` | the first one added (FIFO queue) |
   | `dfs.py` | the last one added (LIFO stack) |
   | `gbfs.py` | the one with the lowest `hn` |
   | `astar.py` | the one with the lowest `hn` plus the cost of the edge from its parent, as written in the code. The best value found so far is never stored between candidates, so in practice the last node in the frontier is removed |

4. **Output.** The `solution` list is every node removed, in removal order, so it records the order of exploration rather than a path. The frontier-membership check compares a city name with a node object, so it never matches and a city can enter the frontier more than once (visible in the `dfs.py` sample, where `Bucharest` appears twice).

### PS2: Knowledge

1. **Symbols.** Each character gets two propositional symbols, for example `A is a Knight` and `A is a Knave`.
2. **Knowledge base.** For every character the base states that they are exactly one of the two: `And(Or(Knight, Knave), Not(And(Knight, Knave)))`. For each statement a character makes, two implications are added: if the speaker is a knight, the statement is true; if the speaker is a knave, the statement is false (`Implication(Knight, S)` and `Implication(Knave, Not(S))`). Puzzles 0 to 3 are written as `knowledge0` to `knowledge3`.
3. **Inference.** `main()` calls `model_check(knowledge, symbol)` from `logic.py` for all six symbols. `model_check` tries every true/false assignment to the symbols involved and answers yes only if every assignment that makes the knowledge base true also makes the query true (entailment). The program prints the symbols that are entailed, which is the solution to the puzzle.

### PS3: Uncertainty

1. **Structure.** A Bayesian network with five binary variables (states 0 and 1) and four edges: `ExamLevel` → `Marks`, `IQLevel` → `Marks`, `IQLevel` → `Aptiscore`, `Marks` → `Admission`.
2. **Parameters.** Each variable gets a conditional probability table (`TabularCPD`). `ExamLevel` and `IQLevel` have priors (0.7/0.3 and 0.8/0.2). `Aptiscore` depends on `IQLevel`, `Marks` on `ExamLevel` and `IQLevel`, and `Admission` on `Marks`. The tables are attached to the model with `add_cpds`.
3. **Structural analysis.** `get_independencies()` and `local_independencies()` list which variables are independent given others. `active_trail_nodes()` shows which variables an observation can influence, with and without observed evidence.
4. **Inference.** A `VariableElimination` object answers exact queries: single-variable and joint distributions, and conditional distributions given evidence (for example `Admission` given `Marks`, or given `ExamLevel` and `IQLevel`).
5. **Most probable states.** `map_query()` returns the most probable assignment of all variables, then of each variable on its own.
6. **Write-up.** The notebook's markdown cells explain each result.

### How the results were produced

- No version control existed, so the dates in the tables above are file-system last-modified dates recorded before the cleanup.
- Every program was run from a scratch copy of the repository, so no build files were left in it. Environment: Linux, Python 3.12, networkx 3.7, matplotlib 3.11.2, pgmpy 1.1.2.
- The search scripts were run with `MPLBACKEND=Agg` (no plot window). Their output, and PS2's, was compared with the output of the original files before cleanup and matched exactly.
- The notebook was executed end to end with `jupyter nbconvert`. The results shown below come from that run. The outputs saved inside the notebook come from the author's earlier run on an older pgmpy: the probabilities are identical, but pgmpy 1.x prints a shorter independencies list.
- There are no automated tests; correctness was checked by running each program and reading its output.

## Sample results

Real output from running the programs on Python 3.12 (pgmpy 1.1.2 for the notebook). The search scripts were run with `MPLBACKEND=Agg`, so the plot window is skipped.

<details>
<summary><b>bfs.py</b></summary>

```text
***********************************************
Frontier: Arad
Explored: 

Arad was removed from the Frontier.
Arad Added to Explored.
Timisoara Added to Frontier.
Sibiu Added to Frontier.
Zerind Added to Frontier.

***********************************************

Frontier: Timisoara, Sibiu, Zerind
Explored: Arad

Timisoara was removed from the Frontier.
Timisoara Added to Explored.
Lugoj Added to Frontier.

***********************************************

Frontier: Sibiu, Zerind, Lugoj
Explored: Arad, Timisoara

Sibiu was removed from the Frontier.
Sibiu Added to Explored.
Fagaras Added to Frontier.
Rimnicu Vilcea Added to Frontier.

***********************************************

Frontier: Zerind, Lugoj, Fagaras, Rimnicu Vilcea
Explored: Arad, Timisoara, Sibiu

Zerind was removed from the Frontier.
Zerind Added to Explored.
Oradea Added to Frontier.

***********************************************

Frontier: Lugoj, Fagaras, Rimnicu Vilcea, Oradea
Explored: Arad, Timisoara, Sibiu, Zerind

Lugoj was removed from the Frontier.
Lugoj Added to Explored.
Mehadia Added to Frontier.

***********************************************

Frontier: Fagaras, Rimnicu Vilcea, Oradea, Mehadia
Explored: Arad, Timisoara, Sibiu, Zerind, Lugoj

Fagaras was removed from the Frontier.
Fagaras Added to Explored.
Bucharest Added to Frontier.

***********************************************

Frontier: Rimnicu Vilcea, Oradea, Mehadia, Bucharest
Explored: Arad, Timisoara, Sibiu, Zerind, Lugoj, Fagaras

Rimnicu Vilcea was removed from the Frontier.
Rimnicu Vilcea Added to Explored.
Pitesti Added to Frontier.
Craiova Added to Frontier.

***********************************************

Frontier: Oradea, Mehadia, Bucharest, Pitesti, Craiova
Explored: Arad, Timisoara, Sibiu, Zerind, Lugoj, Fagaras, Rimnicu Vilcea

Oradea was removed from the Frontier.
Oradea Added to Explored.

***********************************************

Frontier: Mehadia, Bucharest, Pitesti, Craiova
Explored: Arad, Timisoara, Sibiu, Zerind, Lugoj, Fagaras, Rimnicu Vilcea, Oradea

Mehadia was removed from the Frontier.
Mehadia Added to Explored.
Drobeta Added to Frontier.

***********************************************

Frontier: Bucharest, Pitesti, Craiova, Drobeta
Explored: Arad, Timisoara, Sibiu, Zerind, Lugoj, Fagaras, Rimnicu Vilcea, Oradea, Mehadia

Bucharest was removed from the Frontier.
Bucharest was reached. This is the goal.

Here is the solution: Arad, Timisoara, Sibiu, Zerind, Lugoj, Fagaras, Rimnicu Vilcea, Oradea, Mehadia, Bucharest
```

</details>

<details>
<summary><b>dfs.py</b></summary>

```text
***********************************************
Frontier: Arad
Explored: 

Arad was removed from the Frontier.
Arad Added to Explored.
Timisoara Added to Frontier.
Sibiu Added to Frontier.
Zerind Added to Frontier.

***********************************************

Frontier: Timisoara, Sibiu, Zerind
Explored: Arad

Zerind was removed from the Frontier.
Zerind Added to Explored.
Oradea Added to Frontier.

***********************************************

Frontier: Timisoara, Sibiu, Oradea
Explored: Arad, Zerind

Oradea was removed from the Frontier.
Oradea Added to Explored.
Sibiu Added to Frontier.

***********************************************

Frontier: Timisoara, Sibiu, Sibiu
Explored: Arad, Zerind, Oradea

Sibiu was removed from the Frontier.
Sibiu Added to Explored.
Fagaras Added to Frontier.
Rimnicu Vilcea Added to Frontier.

***********************************************

Frontier: Timisoara, Sibiu, Fagaras, Rimnicu Vilcea
Explored: Arad, Zerind, Oradea, Sibiu

Rimnicu Vilcea was removed from the Frontier.
Rimnicu Vilcea Added to Explored.
Pitesti Added to Frontier.
Craiova Added to Frontier.

***********************************************

Frontier: Timisoara, Sibiu, Fagaras, Pitesti, Craiova
Explored: Arad, Zerind, Oradea, Sibiu, Rimnicu Vilcea

Craiova was removed from the Frontier.
Craiova Added to Explored.
Pitesti Added to Frontier.

***********************************************

Frontier: Timisoara, Sibiu, Fagaras, Pitesti, Pitesti
Explored: Arad, Zerind, Oradea, Sibiu, Rimnicu Vilcea, Craiova

Pitesti was removed from the Frontier.
Pitesti Added to Explored.
Bucharest Added to Frontier.
Bucharest Added to Frontier.

***********************************************

Frontier: Timisoara, Sibiu, Fagaras, Pitesti, Bucharest, Bucharest
Explored: Arad, Zerind, Oradea, Sibiu, Rimnicu Vilcea, Craiova, Pitesti

Bucharest was removed from the Frontier.
Bucharest was reached. This is the goal.

Here is the solution: Arad, Zerind, Oradea, Sibiu, Rimnicu Vilcea, Craiova, Pitesti, Bucharest
```

</details>

<details>
<summary><b>gbfs.py</b></summary>

```text
frontier: Arad, 
remove: Arad
explored: Arad, 
possible action: Timisoara, Zerind, Sibiu, 


frontier: Timisoara, Zerind, Sibiu, 
remove: Sibiu
explored: Arad, Sibiu, 
possible action: Fagaras, Rimnicu Vilcea, 


frontier: Timisoara, Zerind, Fagaras, Rimnicu Vilcea, 
remove: Fagaras
explored: Arad, Sibiu, Fagaras, 
possible action: Bucharest, 


frontier: Timisoara, Zerind, Rimnicu Vilcea, Bucharest, 
remove: Bucharest
[SOLVED]:['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
```

</details>

<details>
<summary><b>astar.py</b></summary>

```text
frontier: Arad, 
remove: Arad
explored: Arad, 
possible action: Timisoara, Zerind, Sibiu, 


frontier: Timisoara, Zerind, Sibiu, 
remove: Sibiu
explored: Arad, Sibiu, 
possible action: Fagaras, Rimnicu Vilcea, 


frontier: Timisoara, Zerind, Fagaras, Rimnicu Vilcea, 
remove: Rimnicu Vilcea
explored: Arad, Sibiu, Rimnicu Vilcea, 
possible action: Pitesti, 


frontier: Timisoara, Zerind, Fagaras, Pitesti, 
remove: Pitesti
explored: Arad, Sibiu, Rimnicu Vilcea, Pitesti, 
possible action: nah
Bucharest, 


frontier: Timisoara, Zerind, Fagaras, Bucharest, 
remove: Bucharest
[SOLVED]:['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
```

</details>

<details>
<summary><b>knights-and-knaves.py</b></summary>

```text
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knave
    B is a Knight
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```

</details>

<details>
<summary><b>bayesian-network.ipynb (selected cells, not the full notebook)</b></summary>

```text
# Active trail nodes
>>> model.active_trail_nodes('Marks')
{'Marks': {'Admission', 'Aptiscore', 'ExamLevel', 'IQLevel', 'Marks'}}

>>> model.active_trail_nodes('Marks', observed=['ExamLevel','IQLevel'])
{'Marks': {'Admission', 'Marks'}}

# Local independencies
>>> model.local_independencies([...all five variables...])
(Admission ⟂ Aptiscore, ExamLevel, IQLevel | Marks)
(Aptiscore ⟂ Admission, ExamLevel, Marks | IQLevel)
(ExamLevel ⟂ Aptiscore, IQLevel)
(IQLevel ⟂ ExamLevel)
(Marks ⟂ Aptiscore | ExamLevel, IQLevel)

# Joint query
>>> model_infer.query(variables=['Marks', 'Admission'])
+----------+--------------+------------------------+
| Marks    | Admission    |   phi(Marks,Admission) |
+==========+==============+========================+
| Marks(0) | Admission(0) |                 0.3780 |
+----------+--------------+------------------------+
| Marks(0) | Admission(1) |                 0.2520 |
+----------+--------------+------------------------+
| Marks(1) | Admission(0) |                 0.3330 |
+----------+--------------+------------------------+
| Marks(1) | Admission(1) |                 0.0370 |
+----------+--------------+------------------------+

# Conditional on evidence
>>> model_infer.query(['Admission'], evidence={'ExamLevel': 0, 'IQLevel': 1})
+--------------+------------------+
| Admission    |   phi(Admission) |
+==============+==================+
| Admission(0) |           0.6300 |
+--------------+------------------+
| Admission(1) |           0.3700 |
+--------------+------------------+

>>> model_infer.query(['Admission'], evidence={'Marks': 0})
+--------------+------------------+
| Admission    |   phi(Admission) |
+==============+==================+
| Admission(0) |           0.6000 |
+--------------+------------------+
| Admission(1) |           0.4000 |
+--------------+------------------+

>>> model_infer.query(['Admission'], evidence={'Marks': 1})
+--------------+------------------+
| Admission    |   phi(Admission) |
+==============+==================+
| Admission(0) |           0.9000 |
+--------------+------------------+
| Admission(1) |           0.1000 |
+--------------+------------------+

# Most probable state of all variables
>>> model_infer.map_query()
{'Admission': 0, 'Marks': 1, 'ExamLevel': 0, 'IQLevel': 0, 'Aptiscore': 0}
```

</details>

