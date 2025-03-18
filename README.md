# General utilities for NGT Task 3.1.1

## Plotter 
The plotter in this repository is meant to be used with DQM outputs from CMSSW to superimpose validation plots and compare performance. It is written in python using its ROOT interface. Plots are produced following the instructions provided in one or more `json` files. The basic recipe, thus is:
```bash
python3 plotter.py config.json
```
The configuration files should follow the schema provided in the examples found in the [json folder](/json). The `optiom` field can be used to customize the output plots with the following options:

- `grid`: draws plots with a grid underneath
- `scale`: scales the content of the histograms based on the total integral of the histogram
- `logX`: sets the X axis to logarithmic scale
- `logY`: sets the Y axis to logarithmic scale
- `overrideYLimits`: allows to manually set limits for the Y axis also for plots that are fixed by default. For example, efficiency plots limits are set by default between 0 and 1.4 to show the entire range and legend, with this option the limits can be set arbitrarily

Options should be inserted as a single, comma-separated, string in the `option` field.