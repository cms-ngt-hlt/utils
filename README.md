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

## Timing script
`hltTiming.sh` provides an automatic way to run timing measurements of the HLT. 

Some fields inside the script are customisable and should be modified before running the script:

- The configurations to run. The list provided inside the file must correspond to python configuration files named `NAME_config.py`. For example, if the list is `("legacy" "alpaka")` the script expects two configurations files named `legacy_config.py` and `alpaka_config.py` respectively
- The number of jobs, threads and stream to use for the measurement. This can either be a single set of 3 numbers or a list. In the latter case, each HLT configuration will be processed with all provided sets of jobs, threads, and streams.
- GPU memory monitoring can be switched ON/OFF by changing `ENABLE_GPU_MONITORING`

The CMSSW configuration file is produced by the following `cmsDriver` recipe (make sure to copy the input files locally for the best I/O performance)

```bash
cmsDriver.py Phase2 -s L1P2GT,HLT:75e33_timing \
--processName=HLTX \
--conditions auto:phase2_realistic_T33 \
--geometry ExtendedRun4D110 \
--era Phase2C17I13M9 \
--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 \
--eventcontent FEVTDEBUGHLT \
--filein=file:TTbar-PU200_L1_skim_15_1_0_pre1.root \
--mc \
--inputCommands="keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT" \
-n -1 \
--no_exec \
--output={} \
--python_filename legacy_config.py
```

Once the configuration is done, the script can be executed by
```bash
. hltTiming.sh
```