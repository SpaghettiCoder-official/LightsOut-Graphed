LightsOut-Graphed
=========
Python implement of graphed lights out game solution &amp; test program

How to execute
==========
Run main.py with files that main.py depends on.
or
Uncomment all.py and run it.

Example
=====
see Tests.md

Code
=====
Program class: Test program
  input_ints(): Get single line and interprete it as int values
  test_by_input(): Get input and test solution.
  main(): call test_by_input.

Graphed_Lights_out: The solution.
  __init__(graph): Create by graph
  try_solve(): Returns onehot list that represents which nodes to be pressed, or None if it isn't solvable
  get_edges_removed(graph, get_whether_remove): Remove edges that make get_whether_remove return true. used in try_solve.
  try_paint(): During dfs, try to paint a linked node. used in try_solve.
