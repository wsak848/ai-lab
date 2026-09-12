# Artificial Intelligence Laboratory

Interactive teaching laboratory for an Artificial Intelligence course.

Instructor:
Sakda Wongadyarin

Technology:
- Python
- Streamlit

## Version 0.2

A Thai-first course menu with 10 teaching units. Selecting a unit displays
its title and learning objective. Unit 2 includes a step-by-step BFS / DFS
simulation; the other nine units retain “Simulation coming soon” placeholders.
The interface uses a centered, single-column layout with a full-width selector
and responsive text for desktop, tablet, and mobile screens.

Future versions will contain interactive simulations for search algorithms,
machine learning, neural networks, computer vision, NLP, and Edge AI / AIoT.
No heavy AI packages or Graphviz system installation are required.

### Unit 2: BFS / DFS

Select BFS or DFS, a start node, and a goal node on the fixed undirected tree
with edges A–B, A–C, B–D, B–E, C–F, C–G. Defaults are BFS, A, and G.
Move the slider **below the graph** from step 0 to the final step. Each step
shows the current node, visited set, search order, and queue or stack.
Changing an algorithm or endpoint resets the slider to 0.

Neighbors follow alphabetical adjacency-list order. BFS removes from the
left of the queue; DFS pushes neighbors in reverse order and removes from the
right (stack top), giving left-to-right exploration from A. Nodes are marked
as discovered when added to the frontier, preventing duplicate entries.
Visited means removed from the frontier and processed. Each snapshot is taken
after processing a node and adding neighbors, except at the goal, where search
stops immediately. Step 0 contains only the start in the frontier.

For A to G, BFS visits A, B, C, D, E, F, G; DFS visits A, B, D, E, C, F, G.
Both find A → C → G (2 edges). This tree has only one path between any pair:
it does not demonstrate DFS choosing a longer path. In general, BFS guarantees
a shortest path by edge count in unweighted graphs; DFS does not. DFS order
depends on neighbor ordering and is not universally fixed. Start = goal gives
a one-node path and zero edges when the start is visited at step 1.

## Run locally

From `C:\Users\ja\ai-lab`, with Python available:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open http://localhost:8501. Stop the server with Ctrl+C in its terminal.
Tested using Python 3.13.2 and Streamlit 1.56.0. The development environment
uses a local `.venv` with access to preinstalled system packages; the commands
above create a standalone environment for a fresh installation.

## Structure

- `app.py`: Streamlit interface and initial course units.
- `search_simulation.py`: NetworkX/Matplotlib graph and Streamlit controls.
- `requirements.txt`: Streamlit, NetworkX, and Matplotlib.
- `pages/`: reserved for future lab pages.
- `core/search_algorithms.py`: reusable BFS/DFS functions returning visit order,
  parent map, path, and independent frontier snapshots.
- `tests/test_search.py`: algorithm and Streamlit interaction tests.
- `data/`: reserved for teaching datasets.
- `index.html` and `style.css`: pre-existing static course-menu files;
  the Streamlit application runs independently of them.

## Check the interface

Select each of the 10 units and check its number, title, objective, and
simulation or placeholder. Confirm the instructor appears in the introduction and footer.
At desktop, tablet, and mobile widths, check that text wraps and the selector
is easy to use without horizontal scrolling.

Run automated tests from the project folder with the environment activated:

```powershell
python -m unittest discover -s tests -v
```

Tests cover all 49 start/goal pairs for both algorithms, deterministic order,
frontier states, cycles, disconnected nodes, start = goal, slider reset,
final-path timing, and navigation across all ten units.
