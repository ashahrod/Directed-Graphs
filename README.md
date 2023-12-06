# Directed Eulerian Paths and Cycles

## Overview
This project focuses on the exploration of directed graphs, specifically Eulerian paths and cycles. The goal is to design an algorithm to find Eulerian paths in directed graphs and prove the existence of a directed Eulerian cycle in strongly connected graphs.

## Part 1: Directed Eulerian Cycles
In a directed graph, Eulerian cycles traverse each edge exactly once, considering the direction of the edges. The project establishes a theorem: In a strongly connected, directed graph where each vertex's in-degree equals its out-degree, a directed Eulerian cycle exists. Provides key observations and insights to guide the proof.

## Part 2: Directed Eulerian Paths
The practical implementation involves designing and implementing an algorithm to find Eulerian paths in directed graphs. The algorithm, written in Python, operates with O(|E|) complexity, utilizing the proof from Part 1. The input graph is provided as an edge list, and the program outputs a directed Eulerian path in a specific format.

### Example Usage
```bash
$ ./compile.sh
$ ./run.sh input_graph.txt
Directed Eulerian path:
0, 4, 3, 4, 1, 2, 0
