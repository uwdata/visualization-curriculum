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
   <small>
     [Jupyter Notebook](https://github.com/uwdata/visualization-curriculum/blob/master/altair_interaction.ipynb) |
     [Open in Colab](https://colab.research.google.com/github/uwdata/visualization-curriculum/blob/master/altair_interaction.ipynb) |
     [Open in Observable](https://observablehq.com/@uwdata/interaction)
   </small>

7. Cartographic Visualization<br/>
   <small>
     [Jupyter Notebook](https://github.com/uwdata/visualization-curriculum/blob/master/altair_cartographic.ipynb) |
     [Open in Colab](https://colab.research.google.com/github/uwdata/visualization-curriculum/blob/master/altair_cartographic.ipynb) |
     [Open in Observable](https://observablehq.com/@uwdata/cartographic-visualization)
   </small>

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

1. [Install Altair and a notebook environment](https://altair-viz.github.io/getting_started/installation.html). The notebooks are written for _Altair v3.2 or later_.
2. Copy the curriculum repository to your local filesystem using `git clone https://github.com/uwdata/visualization-curriculum.git`.
3. Open the notebooks in your local notebook environment. For example, if you have JupyterLab installed (v1.0 or higher is required), run `jupyter lab` within the directory containing the notebooks.

Depending on your programming environment, you may need to specify a particular [renderer](https://altair-viz.github.io/user_guide/renderers.html) for Altair.

- If you are using __JupyterLab__, __Google Colab__, or __nteract__ you should not need to do anything &mdash; the correct renderer will be enabled by default.
- If you are using __Jupyter Notebook__, you need to enable the notebook renderer by invoking the following code: `alt.renderers.enable('notebook')`.

## Credits

Developed at the University of Washington by Jeffrey Heer, Dominik Moritz, Jake VanderPlas, and Brock Craft. Thanks to the [UW Interactive Data Lab](https://idl.cs.washington.edu/) and Arvind Satyanarayan for their valuable input and feedback! Thanks also to the students of [UW CSE512 Spring 2019](https://courses.cs.washington.edu/courses/cse512/19sp/), the first group to use these notebooks within an integrated course curriculum.
