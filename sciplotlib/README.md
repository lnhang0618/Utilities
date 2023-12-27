```markdown
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
```

### Methods

- `set_title(title, ax=None)`: Sets the title of the plot.
- `set_xlabel(xlabel, ax=None)`: Sets the label for the x-axis.
- `set_ylabel(ylabel, ax=None)`: Sets the label for the y-axis.
- `scatter(...)`: Creates a scatter plot.
- `plot(...)`: Creates a line plot.
- `contourf(...)`: Creates a filled contour plot.
- `enable_scientific_notation(...)`: Enables scientific notation for the specified axis.
- `show()`: Displays the plot.
- `savefig(filename)`: Saves the plot to the specified file.

### Example

Here is an example of how to create a simple line plot:

```python
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot instance
plot = AcademicPlot()

# Plot the data
plot.plot(x, y, label='Sine Wave')

# Customize the plot
plot.set_title('Example Line Plot')
plot.set_xlabel('X Axis')
plot.set_ylabel('Y Axis')

# Display the plot
plot.show()
```

This will create a line plot with a sine wave, properly labeled and styled for academic purposes.

## Customization

You can customize the plot by choosing different themes, setting the number of ticks, and specifying whether to show minor ticks. You can also customize individual plots by passing additional arguments to the `scatter`, `plot`, and `contourf` methods.

## Saving Plots

To save a plot to a file, use the `savefig` method with the desired filename. The plot will be saved in the specified location with the set figure size and layout.

## Dependencies

- Matplotlib
- Seaborn
- Numpy
```
