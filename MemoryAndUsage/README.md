These scripts plot GPU usage and CPU and GPU memory consumption over time.
They require the output CSV file from `patatrack-scripts/benchmark`.
They support an arbitrary number of measurements (one per CSV file).

To plot the occupancy:

```shell
python3 occupancy.py monitor1.csv monitor2.csv --csv_labels "V1" "V2" --outfile . --usage_filter gpu0_usage --xlims 0 3900 --ylims 0 120
```

To plot the memory:

```shell
python3 compareMemoryProfiles.py monitor1.csv monitor2.csv --csv-labels "V1" "V2" --outfile . --ylims 0 300 --major-tick-step 30 --xlims 0 3900 --cms-label Preliminary --info-text "tt + 200 PU (s = 14 TeV)" "2x AMD EPYC 9534 64-Core Processor" "1x NVIDIA L40S GPU (with MPS @ 6%)" "16 jobs with 16 threads/streams each" --ylabel "CPU Memory Usage [GiB]"
```

To plot the memory and the occupancy:

```shell
python3 occupancy_vs_memory.py monitor1.csv monitor2.csv --csv_labels "V1" "V2" --outfile . --memory_filter gpu0_memory --usage_filter gpu0_usage --xlims 0 3900 --ylims 0 120
```

Use the `--help` for more details.