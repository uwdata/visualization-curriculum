# Data Visualization Curriculum

A data visualization curriculum of interactive notebooks, using [Vega-Lite](https://vega.github.io/vega-lite/) and [Altair](https://altair-viz.github.io/). This repository contains a series of Python-based Jupyter notebooks, a corresponding set of JavaScript notebooks are available online on [Observable](https://observablehq.com/@uwdata/data-visualization-curriculum).

## Curriculum

### Table of Contents

1. Introduction to Vega-Lite / Altair<br/>
   <small>
     [Jupyter Notebook](https://github.com/uwdata/visualization-curriculum/blob/master/altair_introduction.ipynb) |
     [Open in Colab](https://colab.research.google.com/github/uwdata/visualization-curriculum/blob/master/altair_introduction.ipynb) |
     [Open in Observable](https://observablehq.com/@uwdata/introduction-to-vega-lite)
   </small>

2. Data Types, Graphical Marks, and Visual Encoding Channels<br/>
   <small>
     [Jupyter Notebook](https://github.com/uwdata/visualization-curriculum/blob/master/altair_marks_encoding.ipynb) |
     [Open in Colab](https://colab.research.google.com/github/uwdata/visualization-curriculum/blob/master/altair_marks_encoding.ipynb) |
     [Open in Observable](https://observablehq.com/@uwdata/data-types-graphical-marks-and-visual-encoding-channels)
   </small>

3. Data Transformation<br/>
   <small>
     [Jupyter Notebook](https://github.com/uwdata/visualization-curriculum/blob/master/altair_data_transformation.ipynb) |
     [Open in Colab](https://colab.research.google.com/github/uwdata/visualization-curriculum/blob/master/altair_data_transformation.ipynb) |
     [Open in Observable](https://observablehq.com/@uwdata/data-transformation)
   </small>

4. Scales, Axes, and Legends<br/>
   <small>
     [Jupyter Notebook](https://github.com/uwdata/visualization-curriculum/blob/master/altair_scales_axes_legends.ipynb) |
     [Open in Colab](https://colab.research.google.com/github/uwdata/visualization-curriculum/blob/master/altair_scales_axes_legends.ipynb) |
     [Open in Observable](https://observablehq.com/@uwdata/scales-axes-and-legends)
   </small>

5. Multi-View Composition<br/>
   <small>
     [Jupyter Notebook](https://github.com/uwdata/visualization-curriculum/blob/master/altair_view_composition.ipynb) |
     [Open in Colab](https://colab.research.google.com/github/uwdata/visualization-curriculum/blob/master/altair_view_composition.ipynb) |
     [Open in Observable](https://observablehq.com/@uwdata/multi-view-composition)
   </small>

6. Interaction<br/>
   <small><em>coming soon!</em></small>

7. Cartographic Visualization<br/>
   <small><em>coming soon!</em></small>

### Support

- Altair Debugging Guide<br/>
  <small>
     [Jupyter Notebook](https://github.com/uwdata/visualization-curriculum/blob/master/altair_debugging.ipynb) |
     [Open in Colab](https://colab.research.google.com/github/uwdata/visualization-curriculum/blob/master/altair_debugging.ipynb)
  </small>

## Getting Started

The visualization curriculum can be used either online or on your local computer.

- To read JavaScript notebooks online using [Observable](https://observablehq.com/), click the "Observable" links above.
- To read Python notebooks online using [Colab](https://colab.research.google.com/), click the "Colab" links above.
- To read Python notebooks locally, follow the instructions below.

### Local Installation

1. [Install Altair and a notebook environment](https://altair-viz.github.io/getting_started/installation.html).
2. Copy this repository to your local filesystem using `git clone https://github.com/uwdata/visualization-curriculum.git`.
3. Open the notebooks in your local notebook environment. For example, if you have JupyterLab installed, run `jupyter lab` within the directory containing the notebooks.

Depending on your programming environment, you may need to specify a particular [renderer](https://altair-viz.github.io/user_guide/renderers.html) for Altair.

- If you are using __JupyterLab__, __Google Colab__, or __nteract__ you should not need to do anything &mdash; the correct renderer will be enabled by default.
- If you are using __Jupyter Notebook__, you need to enable the notebook renderer by invoking the following code:
  `alt.renderers.enable('notebook')`. If this command fails with a `Value Error: to use the 'notebook' renderer...`, you may need to revert to an older version of vega (the current release v2.0.* is for the upcoming Altair v3.0): `conda install -c conda-forge vega=1.3` or `pip install vega==1.3` (full context [here](https://github.com/altair-viz/altair/issues/1114)).

## Credits

Developed at the University of Washington by Jeffrey Heer, Dominik Moritz, Jake VanderPlas, and Brock Craft. Thanks to the [UW Interactive Data Lab](https://idl.cs.washington.edu/) and Arvind Satyanarayan for their valuable input and feedback!
