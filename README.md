# Artificial Intelligence Laboratory

Interactive teaching laboratory for an Artificial Intelligence course.

Instructor:
Sakda Wongadyarin

Technology:
- Python
- Streamlit

## Version 0.1

A Thai-first course menu with 10 teaching units. Selecting a unit displays
its title, learning objective, and “Simulation coming soon” placeholder.
The interface uses a centered, single-column layout with a full-width selector
and responsive text for desktop, tablet, and mobile screens.

Future versions will contain interactive simulations for search algorithms,
machine learning, neural networks, computer vision, NLP, and Edge AI / AIoT.
Version 0.1 does not implement simulations or require large AI packages.

## Run locally

From `C:\Users\ja\ai-lab`, with Python available:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open http://localhost:8501. Stop the server with Ctrl+C in its terminal.
The initial version was tested using Python 3.13.2 and Streamlit 1.56.0.

## Structure

- `app.py`: Streamlit interface and initial course units.
- `requirements.txt`: the single direct dependency, Streamlit.
- `pages/`: reserved for future lab pages.
- `core/`: reserved for shared simulation logic.
- `data/`: reserved for teaching datasets.
- `index.html` and `style.css`: pre-existing static course-menu files;
  the Streamlit application runs independently of them.

## Check the interface

Select each of the 10 units and check its number, title, objective, and
placeholder. Confirm the instructor appears in the introduction and footer.
At desktop, tablet, and mobile widths, check that text wraps and the selector
is easy to use without horizontal scrolling.
