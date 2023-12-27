# AcademicPlot Class

`AcademicPlot` is a Python class for generating publication-quality plots using Matplotlib. It provides an easy-to-use interface for creating various types of plots with a consistent style suitable for academic papers.

## Features

- Pre-defined color palettes and styles.
- Support for LaTeX-rendered text for high-quality typography.
- Easy customization of plot size, font size, and tick frequency.
- Minor tick support for detailed axis scales.
- Methods for scatter plots, line plots, and filled contour plots.
- Functionality to enable scientific notation on axes.
- Methods to set figure titles and axis labels with appropriate font sizes.

## Usage

To use the `AcademicPlot` class, first create an instance of the class. You can specify the number of rows and columns for subplots, as well as the figure size and other style-related settings upon initialization.

```python
plot = AcademicPlot(nrows=1, ncols=1, figsize=(8, 6), tick_count=5, fontsize=17, theme='bright', show_minor_ticks=True)
set_title(title, ax=None): Sets the title of the plot.
set_xlabel(xlabel, ax=None): Sets the label for the x-axis.
set_ylabel(ylabel, ax=None): Sets the label for the y-axis.
scatter(...): Creates a scatter plot.
plot(...): Creates a line plot.
contourf(...): Creates a filled contour plot.
enable_scientific_notation(...): Enables scientific notation for the specified axis.
show(): Displays the plot.
savefig(filename): Saves the plot to the specified file.