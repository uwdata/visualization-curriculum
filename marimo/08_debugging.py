# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "altair==6.1.0",
#     "marimo",
#     "pandas==3.0.1",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Altair Debugging Guide

    In this notebook we show you common debugging techniques that you can use if you run into issues with Altair.

    You can jump to the following sections:

    * [Installation and Setup](#Installation) when Altair is not installed correctly
    * [Display Issues](#Display-Troubleshooting) when you don't see a chart
    * [Invalid Specifications](#Invalid-Specifications) when you get an error
    * [Properties are Being Ignored](#Properties-are-Being-Ignored) when you don't see any errors or warnings
    * [Asking for Help](#Asking-for-Help) when you get stuck
    * [Reporting Issues](#Reporting-Issues) when you find a bug

    In addition to this notebook, you might find the [Frequently Asked Questions](https://altair-viz.github.io/user_guide/faq.html) and [Display Troubleshooting](https://altair-viz.github.io/user_guide/troubleshooting.html) guides helpful.

    _This notebook is part of the [data visualization curriculum](https://github.com/uwdata/visualization-curriculum)._
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Installation
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These instructions follow [the Altair documentation](https://altair-viz.github.io/getting_started/installation.html) but focus on some specifics for this series of notebooks.

    In every notebook, we will import the [Altair](https://github.com/altair-viz/altair) package. If you are running this notebook on [Colab](https://colab.research.google.com), Altair should be preinstalled and ready to go. The notebooks in this series are designed for Colab but should also work in Jupyter Lab or the Jupyter Notebook (the notebook requires a bit more setup [described below](#Special-Setup-for-the-Jupyter-Notebook)) but additional packages are required.

    If you are running in Jupyter Lab or Jupyter Notebooks, you have to install the necessary packages by running the following command in your terminal.

    ```bash
    pip install altair
    ```

    Or if you use [Conda](https://conda.io)

    ```bash
    conda install -c conda-forge altair
    ```

    You can run command line commands from a code cell by prefixing it with `!`. For example, to install Altair and Vega Datasets with [Pip](https://pip.pypa.io/), you can run the following cell.
    """)
    return


@app.cell
def _():
    # packages added via marimo's package management: altair !pip install altair
    return


@app.cell
def _():
    import altair as alt
    import pandas as pd

    return alt, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Make sure you are Using the Latest Version of Altair
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If you are running into issues with Altair, first make sure that you are running the latest version. To check the version of Altair that you have installed, run the cell below.
    """)
    return


@app.cell
def _(alt):
    alt.__version__
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To check what the latest version of altair is, go to [this page](https://pypi.org/project/altair/) or run the cell below (requires Python 3).
    """)
    return


@app.cell
def _():
    import urllib.request, json 
    with urllib.request.urlopen("https://pypi.org/pypi/altair/json") as url:
        print(json.loads(url.read().decode())['info']['version'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If you are not running the latest version, you can update it with `pip`. You can update Altair and Vega Datasets by running this command in your terminal.

    ```
    pip install -U altair
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try Making a Chart
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now you can create an Altair chart.
    """)
    return


@app.cell
def _(alt, pd):
    cars = pd.read_json("https://cdn.jsdelivr.net/npm/vega-datasets@2/data/cars.json")

    alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Displacement',
        color='Origin'
    )
    return (cars,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Special Setup for the Jupyter Notebook
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If you are running in Jupyter Lab, Jupyter Notebook, or Colab (and have a working Internet connection) you should be seeing a chart. If you are running in another environment (or offline), you will need to tell Altair to use a different renderer;

    To activate a different renderer in a notebook cell:

    ```python
    # to run in nteract, VSCode, or offline in JupyterLab
    alt.renderers.enable('mimebundle')

    ```

    To run offline in Jupyter Notebook you must install an additional dependency, the `vega` package. Run this command in your terminal:

    ```bash
    pip install vega
    ```

    Then activate the notebook renderer:

    ```python
    # to run offline in Jupyter Notebook
    alt.renderers.enable('notebook')

    ```


    These instruction follow [the instructions on the Altair website](https://altair-viz.github.io/getting_started/installation.html#installation-notebook).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Display Troubleshooting

    If you are having issues with seeing a chart, make sure your setup is correct by following the [debugging instruction above](#Installation). If you are still having issues, follow the [instruction about debugging display issues in the Altair documentation](https://iliatimofeev.github.io/altair-viz.github.io/user_guide/troubleshooting.html).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Non Existent Fields

    A common error is [accidentally using a field that does not exist](https://iliatimofeev.github.io/altair-viz.github.io/user_guide/troubleshooting.html#plot-displays-but-the-content-is-empty).
    """)
    return


@app.cell
def _(alt):
    import pandas as pd

    df = pd.DataFrame({'x': [1, 2, 3],
                         'y': [3, 1, 4]})

    alt.Chart(df).mark_point().encode(
        x='x:Q',
        y='y:Q',
        color='color:Q'  # <-- this field does not exist in the data!
    )
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Check the spelling of your files and print the data source to confirm that the data and fields exist. For instance, here you see that `color` is not a valid field.
    """)
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Invalid Specifications

    Another common issue is creating an invalid specification and getting an error.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Invalid Properties

    Altair might show an `SchemaValidationError` or `ValueError`. Read the error message carefully. Usually it will tell you what is going wrong.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, if you forget the mark type, you will see this `SchemaValidationError`.
    """)
    return


@app.cell
def _(alt, cars):
    alt.Chart(cars).encode(
        y='Horsepower'
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or if you use a non-existent channel, you get a `TypeError`.
    """)
    return


@app.cell
def _(alt, cars):
    try:
        alt.Chart(cars).mark_point().encode(
            z='Horsepower'
        )
    except TypeError as e:
        print(f"TypeError: {e}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Properties are Being Ignored

    Altair might ignore a property that you specified. In the chart below, we are using a `text` channel, which is only compatible with `mark_text`. You do not see an error or a warning about this in the notebook. However, the underlying Vega-Lite library will show a warning in the browser console.  Press <kbd>Alt</kbd>+<kbd>Cmd</kbd>+<kbd>I</kbd> on Mac or <kbd>Alt</kbd>+<kbd>Ctrl</kbd>+<kbd>I</kbd> on Windows and Linux to open the developer tools and click on the `Console` tab. When you run the example in the cell below, you will see a the following warning.

    ```
    WARN text dropped as it is incompatible with "bar".
    ```
    """)
    return


@app.cell
def _(alt, cars):
    alt.Chart(cars).mark_bar().encode(
        y='mean(Horsepower)',
        text='mean(Acceleration)'
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If you find yourself debugging issues related to Vega-Lite, you can open the chart in the [Vega Editor](https://vega.github.io/editor/) either by clicking on the "Open in Vega Editor" link at the bottom of the chart or in the action menu (click to open) at the top right of a chart. The Vega Editor provides additional debugging but you will be writing Vega-Lite JSON instead of Altair in Python.

    **Note**: The Vega Editor may be using a newer version of Vega-Lite and so the behavior may vary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Asking for Help

    If you find a problem with Altair and get stuck, you can ask a question on Stack Overflow. Ask your question with the `altair` and `vega-lite` tags. You can find a list of questions people have asked before [here](https://stackoverflow.com/questions/tagged/altair).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reporting Issues

    If you find a problem with Altair and believe it is a bug, please [create an issue in the Altair GitHub repo](https://github.com/altair-viz/altair/issues/new) with a description of your problem. If you believe the issue is related to the underlying Vega-Lite library, please [create an issue in the Vega-Lite GitHub repo](https://github.com/vega/vega-lite/issues/new).
    """)
    return


if __name__ == "__main__":
    app.run()
