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
    # Multi-View Composition

    When visualizing a number of different data fields, we might be tempted to use as many visual encoding channels as we can: `x`, `y`, `color`, `size`, `shape`, and so on. However, as the number of encoding channels increases, a chart can rapidly become cluttered and difficult to read. An alternative to "over-loading" a single chart is to instead _compose multiple charts_ in a way that facilitates rapid comparisons.

    In this notebook, we will examine a variety of operations for _multi-view composition_:

    - _layer_: place compatible charts directly on top of each other,
    - _facet_: partition data into multiple charts, organized in rows or columns,
    - _concatenate_: position arbitrary charts within a shared layout, and
    - _repeat_: take a base chart specification and apply it to multiple data fields.

    We'll then look at how these operations form a _view composition algebra_, in which the operations can be combined to build a variety of complex multi-view displays.

    _This notebook is part of the [data visualization curriculum](https://github.com/uwdata/visualization-curriculum)._
    """)
    return


@app.cell
def _():
    import pandas as pd
    import altair as alt

    return alt, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Weather Data

    We will be visualizing weather statistics for the U.S. cities of Seattle and New York. Let's load the dataset and peek at the first and last 10 rows:
    """)
    return


@app.cell
def _():
    weather = 'https://cdn.jsdelivr.net/npm/vega-datasets@1/data/weather.csv'
    return (weather,)


@app.cell
def _(pd, weather):
    df = pd.read_csv(weather)
    df.head(10)
    return (df,)


@app.cell
def _(df):
    df.tail(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We will create multi-view displays to examine weather within and across the cities.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Layer
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One of the most common ways of combining multiple charts is to *layer* marks on top of each other. If the underlying scale domains are compatible, we can merge them to form _shared axes_. If either of the `x` or `y` encodings is not compatible, we might instead create a _dual-axis chart_, which overlays marks using separate scales and axes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Shared Axes
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start by plotting the minimum and maximum average temperatures per month:
    """)
    return


@app.cell
def _(alt, weather):
    alt.Chart(weather).mark_area().encode(
      alt.X('month(date):T'),
      alt.Y('average(temp_max):Q'),
      alt.Y2('average(temp_min):Q')
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _The plot shows us temperature ranges for each month over the entirety of our data. However, this is pretty misleading as it aggregates the measurements for both Seattle and New York!_

    Let's subdivide the data by location using a color encoding, while also adjusting the mark opacity to accommodate overlapping areas:
    """)
    return


@app.cell
def _(alt, weather):
    alt.Chart(weather).mark_area(opacity=0.3).encode(
      alt.X('month(date):T'),
      alt.Y('average(temp_max):Q'),
      alt.Y2('average(temp_min):Q'),
      alt.Color('location:N')
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _We can see that Seattle is more temperate: warmer in the winter, and cooler in the summer._

    In this case we've created a layered chart without any special features by simply subdividing the area marks by color. While the chart above shows us the temperature ranges, we might also want to emphasize the middle of the range.

    Let's create a line chart showing the average temperature midpoint. We'll use a `calculate` transform to compute the midpoints between the minimum and maximum daily temperatures:
    """)
    return


@app.cell
def _(alt, weather):
    alt.Chart(weather).mark_line().transform_calculate(
      temp_mid='(+datum.temp_min + +datum.temp_max) / 2'
    ).encode(
      alt.X('month(date):T'),
      alt.Y('average(temp_mid):Q'),
      alt.Color('location:N')
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _Aside_: note the use of `+datum.temp_min` within the calculate transform. As we are loading the data directly from a CSV file without any special parsing instructions, the temperature values may be internally represented as string values. Adding the  `+` in front of the value forces it to be treated as a number.

    We'd now like to combine these charts by layering the midpoint lines over the range areas. Using the syntax `chart1 + chart2`, we can specify that we want a new layered chart in which `chart1` is the first layer and `chart2` is a second layer drawn on top:
    """)
    return


@app.cell
def _(alt, weather):
    tempMinMax = alt.Chart(weather).mark_area(opacity=0.3).encode(
      alt.X('month(date):T'),
      alt.Y('average(temp_max):Q'),
      alt.Y2('average(temp_min):Q'),
      alt.Color('location:N')
    )

    tempMid = alt.Chart(weather).mark_line().transform_calculate(
      temp_mid='(+datum.temp_min + +datum.temp_max) / 2'
    ).encode(
      alt.X('month(date):T'),
      alt.Y('average(temp_mid):Q'),
      alt.Color('location:N')
    )

    tempMinMax + tempMid
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _Now we have a multi-layer plot! However, the y-axis title (though informative) has become a bit long and unruly..._

    Let's customize our axes to clean up the plot. If we set a custom axis title within one of the layers, it will automatically be used as a shared axis title for all the layers:
    """)
    return


@app.cell
def _(alt, weather):
    tempMinMax_1 = alt.Chart(weather).mark_area(opacity=0.3).encode(alt.X('month(date):T', title=None, axis=alt.Axis(format='%b')), alt.Y('average(temp_max):Q', title='Avg. Temperature °C'), alt.Y2('average(temp_min):Q'), alt.Color('location:N'))
    tempMid_1 = alt.Chart(weather).mark_line().transform_calculate(temp_mid='(+datum.temp_min + +datum.temp_max) / 2').encode(alt.X('month(date):T'), alt.Y('average(temp_mid):Q'), alt.Color('location:N'))
    tempMinMax_1 + tempMid_1
    return tempMid_1, tempMinMax_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _What happens if both layers have custom axis titles? Modify the code above to find out..._

    Above used the `+` operator, a convenient shorthand for Altair's `layer` method. We can generate an identical layered chart using the `layer` method directly:
    """)
    return


@app.cell
def _(alt, tempMid_1, tempMinMax_1):
    alt.layer(tempMinMax_1, tempMid_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that the order of inputs to a layer matters, as subsequent layers will be drawn on top of earlier layers. _Try swapping the order of the charts in the cells above. What happens? (Hint: look closely at the color of the `line` marks.)_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dual-Axis Charts
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _Seattle has a reputation as a rainy city. Is that deserved?_

    Let's look at precipitation alongside temperature to learn more. First let's create a base plot the shows average monthly precipitation in Seattle:
    """)
    return


@app.cell
def _(alt, weather):
    alt.Chart(weather).transform_filter(
      'datum.location == "Seattle"'
    ).mark_line(
      interpolate='monotone',
      stroke='grey'
    ).encode(
      alt.X('month(date):T', title=None),
      alt.Y('average(precipitation):Q', title='Precipitation')
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To facilitate comparison with the temperature data, let's create a new layered chart. Here's what happens if we try to layer the charts as we did earlier:
    """)
    return


@app.cell
def _(alt, weather):
    tempMinMax_2 = alt.Chart(weather).transform_filter('datum.location == "Seattle"').mark_area(opacity=0.3).encode(alt.X('month(date):T', title=None, axis=alt.Axis(format='%b')), alt.Y('average(temp_max):Q', title='Avg. Temperature °C'), alt.Y2('average(temp_min):Q'))
    _precip = alt.Chart(weather).transform_filter('datum.location == "Seattle"').mark_line(interpolate='monotone', stroke='grey').encode(alt.X('month(date):T'), alt.Y('average(precipitation):Q', title='Precipitation'))
    alt.layer(tempMinMax_2, _precip)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _The precipitation values use a much smaller range of the y-axis then the temperatures!_

    By default, layered charts use a *shared domain*: the values for the x-axis or y-axis are combined across all the layers to determine a shared extent. This default behavior assumes that the layered values have the same units. However, this doesn't hold up for this example, as we are combining temperature values (degrees Celsius) with precipitation values (inches)!

    If we want to use different y-axis scales, we need to specify how we want Altair to *resolve* the data across layers. In this case, we want to resolve the y-axis `scale` domains to be `independent` rather than use a `shared` domain. The `Chart` object produced by a layer operator includes a `resolve_scale` method with which we can specify the desired resolution:
    """)
    return


@app.cell
def _(alt, weather):
    tempMinMax_3 = alt.Chart(weather).transform_filter('datum.location == "Seattle"').mark_area(opacity=0.3).encode(alt.X('month(date):T', title=None, axis=alt.Axis(format='%b')), alt.Y('average(temp_max):Q', title='Avg. Temperature °C'), alt.Y2('average(temp_min):Q'))
    _precip = alt.Chart(weather).transform_filter('datum.location == "Seattle"').mark_line(interpolate='monotone', stroke='grey').encode(alt.X('month(date):T'), alt.Y('average(precipitation):Q', title='Precipitation'))
    alt.layer(tempMinMax_3, _precip).resolve_scale(y='independent')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _We can now see that autumn is the rainiest season in Seattle (peaking in November), complemented by dry summers._

    You may have noticed some redundancy in our plot specifications above: both use the same dataset and the same filter to look at Seattle only. If you want, you can streamline the code a bit by providing the data and filter transform to the top-level layered chart. The individual layers will then inherit the data if they don't have their own data definitions:
    """)
    return


@app.cell
def _(alt, weather):
    tempMinMax_4 = alt.Chart().mark_area(opacity=0.3).encode(alt.X('month(date):T', title=None, axis=alt.Axis(format='%b')), alt.Y('average(temp_max):Q', title='Avg. Temperature °C'), alt.Y2('average(temp_min):Q'))
    _precip = alt.Chart().mark_line(interpolate='monotone', stroke='grey').encode(alt.X('month(date):T'), alt.Y('average(precipitation):Q', title='Precipitation'))
    alt.layer(tempMinMax_4, _precip, data=weather).transform_filter('datum.location == "Seattle"').resolve_scale(y='independent')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    While dual-axis charts can be useful, _they are often prone to misinterpretation_, as the different units and axis scales may be incommensurate. As is feasible, you might consider transformations that map different data fields to shared units, for example showing [quantiles](https://en.wikipedia.org/wiki/Quantile) or relative percentage change.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Facet
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *Faceting* involves subdividing a dataset into groups and creating a separate plot for each group. In earlier notebooks, we learned how to create faceted charts using the `row` and `column` encoding channels. We'll first review those channels and then show how they are instances of the more general `facet` operator.

    Let's start with a basic histogram of maximum temperature values in Seattle:
    """)
    return


@app.cell
def _(alt, weather):
    alt.Chart(weather).mark_bar().transform_filter(
      'datum.location == "Seattle"'
    ).encode(
      alt.X('temp_max:Q', bin=True, title='Temperature (°C)'),
      alt.Y('count():Q')
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _How does this temperature profile change based on the weather of a given day – that is, whether there was drizzle, fog, rain, snow, or sun?_

    Let's use the `column` encoding channel to facet the data by weather type. We can also use `color` as a redundant encoding, using a customized color range:
    """)
    return


@app.cell
def _(alt, weather):
    _colors = alt.Scale(domain=['drizzle', 'fog', 'rain', 'snow', 'sun'], range=['#aec7e8', '#c7c7c7', '#1f77b4', '#9467bd', '#e7ba52'])
    alt.Chart(weather).mark_bar().transform_filter('datum.location == "Seattle"').encode(alt.X('temp_max:Q', bin=True, title='Temperature (°C)'), alt.Y('count():Q'), alt.Color('weather:N', scale=_colors), alt.Column('weather:N')).properties(width=150, height=150)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _Unsurprisingly, those rare snow days center on the coldest temperatures, followed by rainy and foggy days. Sunny days are warmer and, despite Seattle stereotypes, are the most plentiful. Though as any Seattleite can tell you, the drizzle occasionally comes, no matter the temperature!_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In addition to `row` and `column` encoding channels *within* a chart definition, we can take a basic chart definition and apply faceting using an explicit `facet` operator.

    Let's recreate the chart above, but this time using `facet`. We start with the same basic histogram definition, but remove the data source, filter transform, and column channel. We can then invoke the `facet` method, passing in the data and specifying that we should facet into columns according to the `weather` field. The `facet` method accepts both `row` and `column` arguments. The two can be used together to create a 2D grid of faceted plots.

    Finally we include our filter transform, applying it to the top-level faceted chart. While we could apply the filter transform to the histogram definition as before, that is slightly less efficient. Rather than filter out "New York" values within each facet cell, applying the filter to the faceted chart lets Vega-Lite know that we can filter out those values up front, prior to the facet subdivision.
    """)
    return


@app.cell
def _(alt, weather):
    _colors = alt.Scale(domain=['drizzle', 'fog', 'rain', 'snow', 'sun'], range=['#aec7e8', '#c7c7c7', '#1f77b4', '#9467bd', '#e7ba52'])
    alt.Chart().mark_bar().encode(alt.X('temp_max:Q', bin=True, title='Temperature (°C)'), alt.Y('count():Q'), alt.Color('weather:N', scale=_colors)).properties(width=150, height=150).facet(data=weather, column='weather:N').transform_filter('datum.location == "Seattle"')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given all the extra code above, why would we want to use an explicit `facet` operator? For basic charts, we should certainly use the `column` or `row` encoding channels if we can. However, using the `facet` operator explicitly is useful if we want to facet composed views, such as layered charts.

    Let's revisit our layered temperature plots from earlier. Instead of plotting data for New York and Seattle in the same plot, let's break them up into separate facets. The individual chart definitions are nearly the same as before: one area chart and one line chart. The only difference is that this time we won't pass the data directly to the chart constructors; we'll wait and pass it to the facet operator later. We can layer the charts much as before, then invoke `facet` on the layered chart object, passing in the data and specifying `column` facets based on the `location` field:
    """)
    return


@app.cell
def _(alt, weather):
    tempMinMax_5 = alt.Chart().mark_area(opacity=0.3).encode(alt.X('month(date):T', title=None, axis=alt.Axis(format='%b')), alt.Y('average(temp_max):Q', title='Avg. Temperature (°C)'), alt.Y2('average(temp_min):Q'), alt.Color('location:N'))
    tempMid_2 = alt.Chart().mark_line().transform_calculate(temp_mid='(+datum.temp_min + +datum.temp_max) / 2').encode(alt.X('month(date):T'), alt.Y('average(temp_mid):Q'), alt.Color('location:N'))
    alt.layer(tempMinMax_5, tempMid_2).facet(data=weather, column='location:N')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The faceted charts we have seen so far use the same axis scale domains across the facet cells. This default of using *shared* scales and axes helps aid accurate comparison of values. However, in some cases you may wish to scale each chart independently, for example if the range of values in the cells differs significantly.

    Similar to layered charts, faceted charts also support _resolving_ to independent scales or axes across plots. Let's see what happens if we call the `resolve_axis` method to request `independent` y-axes:
    """)
    return


@app.cell
def _(alt, weather):
    tempMinMax_6 = alt.Chart().mark_area(opacity=0.3).encode(alt.X('month(date):T', title=None, axis=alt.Axis(format='%b')), alt.Y('average(temp_max):Q', title='Avg. Temperature (°C)'), alt.Y2('average(temp_min):Q'), alt.Color('location:N'))
    tempMid_3 = alt.Chart().mark_line().transform_calculate(temp_mid='(+datum.temp_min + +datum.temp_max) / 2').encode(alt.X('month(date):T'), alt.Y('average(temp_mid):Q'), alt.Color('location:N'))
    alt.layer(tempMinMax_6, tempMid_3).facet(data=weather, column='location:N').resolve_axis(y='independent')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _The chart above looks largely unchanged, but the plot for Seattle now includes its own axis._

    What if we instead call `resolve_scale` to resolve the underlying scale domains?
    """)
    return


@app.cell
def _(alt, weather):
    tempMinMax_7 = alt.Chart().mark_area(opacity=0.3).encode(alt.X('month(date):T', title=None, axis=alt.Axis(format='%b')), alt.Y('average(temp_max):Q', title='Avg. Temperature (°C)'), alt.Y2('average(temp_min):Q'), alt.Color('location:N'))
    tempMid_4 = alt.Chart().mark_line().transform_calculate(temp_mid='(+datum.temp_min + +datum.temp_max) / 2').encode(alt.X('month(date):T'), alt.Y('average(temp_mid):Q'), alt.Color('location:N'))
    alt.layer(tempMinMax_7, tempMid_4).facet(data=weather, column='location:N').resolve_scale(y='independent')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _Now we see facet cells with different axis scale domains. In this case, using independent scales seems like a bad idea! The domains aren't very different, and one might be fooled into thinking that New York and Seattle have similar maximum summer temperatures._

    To borrow a cliché: just because you *can* do something, doesn't mean you *should*...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concatenate
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Faceting creates [small multiple](https://en.wikipedia.org/wiki/Small_multiple) plots that show separate subdivisions of the data. However, we might wish to create a multi-view display with different views of the *same* dataset (not subsets) or views involving *different* datasets.

    Altair provides *concatenation* operators to combine arbitrary charts into a composed chart. The `hconcat` operator (shorthand `|` ) performs horizontal concatenation, while the `vconcat` operator (shorthand `&`) performs vertical concatenation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with a basic line chart showing the average maximum temperature per month for both New York and Seattle, much like we've seen before:
    """)
    return


@app.cell
def _(alt, weather):
    alt.Chart(weather).mark_line().encode(
      alt.X('month(date):T', title=None),
      alt.Y('average(temp_max):Q'),
      color='location:N'
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _What if we want to compare not just temperature over time, but also precipitation and wind levels?_

    Let's create a concatenated chart consisting of three plots. We'll start by defining a "base" chart definition that contains all the aspects that should be shared by our three plots. We can then modify this base chart to create customized variants, with different y-axis encodings for the `temp_max`, `precipitation`, and `wind` fields. We can then concatenate them using the pipe (`|`) shorthand operator:
    """)
    return


@app.cell
def _(alt, weather):
    base = alt.Chart(weather).mark_line().encode(alt.X('month(date):T', title=None), color='location:N').properties(width=240, height=180)
    temp = base.encode(alt.Y('average(temp_max):Q'))
    _precip = base.encode(alt.Y('average(precipitation):Q'))
    wind = base.encode(alt.Y('average(wind):Q'))
    temp | _precip | wind
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Alternatively, we could use the more explicit `alt.hconcat()` method in lieu of the pipe `|` operator. _Try rewriting the code above to use `hconcat` instead._

    Vertical concatenation works similarly to horizontal concatenation. _Using the `&` operator (or `alt.vconcat` method), modify the code to use a vertical ordering instead of a horizontal ordering._

    Finally, note that horizontal and vertical concatenation can be combined. _What happens if you write something like `(temp | precip) & wind`?_

    _Aside_: Note the importance of those parentheses... what happens if you remove them? Keep in mind that these overloaded operators are still subject to [Python's operator precedence rules](https://docs.python.org/3/reference/expressions.html#operator-precedence), and so vertical concatenation with `&` will take precedence over horizontal concatenation with `|`!

    As we will revisit later, concatenation operators let you combine any and all charts into a multi-view dashboard!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Repeat
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The concatenation operators above are quite general, allowing arbitrary charts to be composed. Nevertheless, the example above was still a bit verbose: we have three very similar charts, yet have to define them separately and then concatenate them.

    For cases where only one or two variables are changing, the `repeat` operator provides a convenient shortcut for creating multiple charts. Given a *template* specification with some free variables, the repeat operator will then create a chart for each specified assignment to those variables.

    Let's recreate our concatenation example above using the `repeat` operator. The only aspect that changes across charts is the choice of data field for the `y` encoding channel. To create a template specification, we can use the *repeater variable* `alt.repeat('column')` as our y-axis field. This code simply states that we want to use the variable assigned to the `column` repeater, which organizes repeated charts in a horizontal direction. (As the repeater provides the field name only, we have to specify the field data type separately as `type='quantitative'`.)

    We then invoke the `repeat` method, passing in data field names for each column:
    """)
    return


@app.cell
def _(alt, weather):
    alt.Chart(weather).mark_line().encode(
      alt.X('month(date):T',title=None),
      alt.Y(alt.repeat('column'), aggregate='average', type='quantitative'),
      color='location:N'
    ).properties(
      width=240,
      height=180
    ).repeat(
      column=['temp_max', 'precipitation', 'wind']
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Repetition is supported for both columns and rows. _What happens if you modify the code above to use `row` instead of `column`?_

    We can also use `row` and `column` repetition together! One common visualization for exploratory data analysis is the [scatter plot matrix (or SPLOM)](https://en.wikipedia.org/wiki/Scatter_plot#Scatterplot_matrices). Given a collection of variables to inspect, a SPLOM provides a grid of all pairwise plots of those variables, allowing us to assess potential associations.

    Let's use the `repeat` operator to create a SPLOM for the `temp_max`, `precipitation`, and `wind` fields. We first create our template specification, with repeater variables for both the x- and y-axis data fields. We then invoke `repeat`, passing in arrays of field names to use for both `row` and `column`. Altair will then generate the [cross product (or, Cartesian product)](https://en.wikipedia.org/wiki/Cartesian_product) to create the full space of repeated charts:
    """)
    return


@app.cell
def _(alt, weather):
    alt.Chart().mark_point(filled=True, size=15, opacity=0.5).encode(
      alt.X(alt.repeat('column'), type='quantitative'),
      alt.Y(alt.repeat('row'), type='quantitative')
    ).properties(
      width=150,
      height=150
    ).repeat(
      data=weather,
      row=['temp_max', 'precipitation', 'wind'],
      column=['wind', 'precipitation', 'temp_max']
    ).transform_filter(
      'datum.location == "Seattle"'
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _Looking at these plots, there does not appear to be a strong association between precipitation and wind, though we do see that extreme wind and precipitation events occur in similar temperature ranges (~5-15° C). However, this observation is not particularly surprising: if we revisit our histogram at the beginning of the facet section, we can plainly see that the days with maximum temperatures in the range of 5-15° C are the most commonly occurring._

    *Modify the code above to get a better understanding of chart repetition. Try adding another variable (`temp_min`) to the SPLOM. What happens if you rearrange the order of the field names in either the `row` or `column` parameters for the `repeat` operator?*

    _Finally, to really appreciate what the `repeat` operator provides, take a moment to imagine how you might recreate the SPLOM above using only `hconcat` and `vconcat`!_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A View Composition Algebra
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Together, the composition operators `layer`, `facet`, `concat`, and `repeat` form a *view composition algebra*: the various operators can be combined to construct a variety of multi-view visualizations.

    As an example, let's start with two basic charts: a histogram and a simple line (a single `rule` mark) showing a global average.
    """)
    return


@app.cell
def _(alt, weather):
    basic1 = alt.Chart(weather).transform_filter(
      'datum.location == "Seattle"'
    ).mark_bar().encode(
      alt.X('month(date):O'),
      alt.Y('average(temp_max):Q')
    )

    basic2 = alt.Chart(weather).transform_filter(
      'datum.location == "Seattle"'
    ).mark_rule(stroke='firebrick').encode(
      alt.Y('average(temp_max):Q')
    )

    basic1 | basic2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can then combine the two charts using a `layer` operator, and then `repeat` that layered chart to show histograms with overlaid averages for multiple fields:
    """)
    return


@app.cell
def _(alt, weather):
    alt.layer(
      alt.Chart().mark_bar().encode(
        alt.X('month(date):O', title='Month'),
        alt.Y(alt.repeat('column'), aggregate='average', type='quantitative')
      ),
      alt.Chart().mark_rule(stroke='firebrick').encode(
        alt.Y(alt.repeat('column'), aggregate='average', type='quantitative')
      )
    ).properties(
      width=200,
      height=150
    ).repeat(
      data=weather,
      column=['temp_max', 'precipitation', 'wind']
    ).transform_filter(
      'datum.location == "Seattle"'
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Focusing only on the multi-view composition operators, the model for the visualization above is:

    ```
    repeat(column=[...])
    |- layer
       |- basic1
       |- basic2
    ```

    Now let's explore how we can apply *all* the operators within a final [dashboard](https://en.wikipedia.org/wiki/Dashboard_%28business%29) that provides an overview of Seattle weather. We'll combine the SPLOM and faceted histogram displays from earlier sections with the repeated histograms above:
    """)
    return


@app.cell(hide_code=True)
def _(alt, weather):
    splom = alt.Chart().mark_point(filled=True, size=15, opacity=0.5).encode(
      alt.X(alt.repeat('column'), type='quantitative'),
      alt.Y(alt.repeat('row'), type='quantitative')
    ).properties(
      width=125,
      height=125
    ).repeat(
      row=['temp_max', 'precipitation', 'wind'],
      column=['wind', 'precipitation', 'temp_max']
    )

    dateHist = alt.layer(
      alt.Chart().mark_bar().encode(
        alt.X('month(date):O', title='Month'),
        alt.Y(alt.repeat('row'), aggregate='average', type='quantitative')
      ),
      alt.Chart().mark_rule(stroke='firebrick').encode(
        alt.Y(alt.repeat('row'), aggregate='average', type='quantitative')
      )
    ).properties(
      width=175,
      height=125
    ).repeat(
      row=['temp_max', 'precipitation', 'wind']
    )

    tempHist = alt.Chart(weather).mark_bar().encode(
      alt.X('temp_max:Q', bin=True, title='Temperature (°C)'),
      alt.Y('count():Q'),
      alt.Color('weather:N', scale=alt.Scale(
        domain=['drizzle', 'fog', 'rain', 'snow', 'sun'],
        range=['#aec7e8', '#c7c7c7', '#1f77b4', '#9467bd', '#e7ba52']
      ))
    ).properties(
      width=115,
      height=100
    ).facet(
      column='weather:N'
    )

    alt.vconcat(
      alt.hconcat(splom, dateHist),
      tempHist,
      data=weather,
      title='Seattle Weather Dashboard'
    ).transform_filter(
      'datum.location == "Seattle"'
    ).resolve_legend(
      color='independent'
    ).configure_axis(
      labelAngle=0
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The full composition model for this dashboard is:

    ```
    vconcat
    |- hconcat
    |  |- repeat(row=[...], column=[...])
    |  |  |- splom base chart
    |  |- repeat(row=[...])
    |     |- layer
    |        |- dateHist base chart 1
    |        |- dateHist base chart 2
    |- facet(column='weather')
       |- tempHist base chart
    ```

    _Phew!_ The dashboard also includes a few customizations to improve the layout:

    - We adjust chart `width` and `height` properties to assist alignment and ensure the full visualization fits on the screen.
    - We add `resolve_legend(color='independent')` to ensure the color legend is associated directly with the colored histograms by temperature. Otherwise, the legend will resolve to the dashboard as a whole.
    - We use `configure_axis(labelAngle=0)` to ensure that no axis labels are rotated. This helps to ensure proper alignment among the scatter plots in the SPLOM and the histograms by month on the right.

    _Try removing or modifying any of these adjustments and see how the dashboard layout responds!_

    This dashboard can be reused to show data for other locations or from other datasets. _Update the dashboard to show weather patterns for New York instead of Seattle._
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Summary

    For more details on multi-view composition, including control over sub-plot spacing and header labels, see the [Altair Compound Charts documentation](https://altair-viz.github.io/user_guide/compound_charts.html).

    Now that we've seen how to compose multiple views, we're ready to put them into action. In addition to statically presenting data, multiple views can enable interactive multi-dimensional exploration. For example, using _linked selections_ we can highlight points in one view to see corresponding values highlight in other views.

    In the next notebook, we'll examine how to author *interactive selections* for both individual plots and multi-view compositions.
    """)
    return


if __name__ == "__main__":
    app.run()
