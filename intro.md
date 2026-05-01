# Introduction

A data visualization curriculum of interactive notebooks, using [Vega-Lite](https://vega.github.io/vega-lite/) and [Altair](https://altair-viz.github.io/). This book contains a series of Python-based Jupyter notebooks. The notebooks are also available as [marimo](https://marimo.io/) notebooks, and a corresponding set of JavaScript notebooks are available online on [Observable](https://observablehq.com/@uwdata/data-visualization-curriculum).

## Getting Started

The visualization curriculum can be used either online or on your local computer. You can view and interact with the plots directly in this Jupyter Book. If you want to modify the code, you have a few different options:

- To read JavaScript notebooks online using [Observable](https://observablehq.com/), navigate to the "Observable" page above and click the corresponding notebook.
- To read Python notebooks online using [Colab](https://colab.research.google.com/), click the corresponding section in this book, hover over the little rocket ship at the top of the page, and select "Colab" from the menu.
- To run [marimo](https://marimo.io/) notebooks online, use [molab](https://marimo.io/for-learners#learn-altair).
- To read Python notebooks locally, follow the instructions below.

### Local Installation

1. [Install Altair and a notebook environment](https://altair-viz.github.io/getting_started/installation.html). The most recent versions of these notebooks use _Altair version 6_.
2. Download the notebooks from the [releases page](https://github.com/uwdata/visualization-curriculum/releases). Typically you will want to use the most recent release.
3. If you are using [Jupyter](https://jupyter.org/), open the `.ipynb` notebooks in your local notebook environment. For example, if you have JupyterLab installed (v1.0 or higher is required), run `jupyter lab` within the directory containing the notebooks. With [uv](https://docs.astral.sh/uv/guides/install-python/), you can run `uv run jupyter lab` (it automatically installs the dependencies).
4. If you are using [marimo](https://marimo.io/), open the `.py` notebooks in the `marimo` directory using either `marimo run marimo/notebook.py` (to use the virtual environment you set up) or `uv run marimo run marimo/notebook.py` (to automatically install the dependencies in the notebook header).

Depending on your programming environment (and whether or not you have a live internet connection), you may want to specify a particular [renderer](https://altair-viz.github.io/user_guide/display_frontends.html) for Altair.

## Credits

Developed at the University of Washington by Jeffrey Heer, Dominik Moritz, Jake VanderPlas, and Brock Craft. Thanks to the [UW Interactive Data Lab](https://idl.cs.washington.edu/) and Arvind Satyanarayan for their valuable input and feedback! Thanks also to the students of [UW CSE512 Spring 2019](https://courses.cs.washington.edu/courses/cse512/19sp/), the first group to use these notebooks within an integrated course curriculum.
