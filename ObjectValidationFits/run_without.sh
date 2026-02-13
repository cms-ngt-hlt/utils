
# Set up
cd /data/evernazz/NanoAOD/2026_01_12/CMSSW_16_0_0_pre4/src
cmsenv

# My own developments for circles here:
https://github.com/elenavernazza/circles/pull/new/PixelTriplets

# Time evolution
cd /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/TimingEvolution_gcc13_16_0
source ../download_phase2.sh 2025 10
source ../download_phase2.sh 2025 11
source ../download_phase2.sh 2025 12
source ../download_phase2.sh 2026 1

python3 ../plotHLTTimingVsDay.py

# Time rescaling GPU-based
cd /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/scripts
cp /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/TimingEvolution_gcc13_16_0/Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-25-1100.json .
cp /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/TimingEvolution_gcc13_16_0/Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100.json .
cp /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/TimingEvolution_gcc13_16_0/Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100.json .
python3 alter_stats.py \
 --input-file Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-25-1100.json \
 --group-file /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json --scale 1.117
python3 alter_stats.py \
 --input-file Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100.json \
 --group-file /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json --scale 1.117
python3 alter_stats.py \
 --input-file Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100.json \
 --group-file /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json --scale 1.117
python3 alter_stats.py \
 --input-file Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100_CPU.json \
 --group-file /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json --scale 1.117
python3 alter_stats.py \
 --input-file Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_CPU.json \
 --group-file /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json --scale 1.117
# Import to web tool for visualization

# Compare two json with bars
# cd /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/scripts
# python3 compare_json_hist.py \
#  Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-25-1100_scaled.json \
#  Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_scaled.json \
#  --map /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json \
#  --colors /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/colours/default.json \
#  --level package --per-event --save stacked_old.png

TYPE=pdf

# Compare three json with bars (GPU-based)
cd /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/scripts
python3 compare_multiple_json_hist.py \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-25-1100_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_scaled.json \
 --group /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json \
 --colors /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/colours/default.json \
 --labels "Legacy" "Patatrack (GPU)" "Extended Patatrack (GPU)" --baseline 0 --label-fontsize 14 --lumi-text "t\\bar{t}+200~PU~|~14~TeV" --cms-text "Simulation Preliminary" \
 --level package --ignore-unassigned --metric-precision 0 --save WithoutNewTrackingBaseline/stacked_GPU.${TYPE}
# Compare three json with bars (GPU-based), splitting pixel triplets
python3 compare_multiple_json_hist.py \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-25-1100_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_scaled.json \
 --group /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt_pixel_trips.json \
 --colors /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/colours/pixel_trips.json \
 --labels "Legacy" "Patatrack (GPU)" "Extended Patatrack (GPU)" --baseline 0 --label-fontsize 14 --lumi-text "t\\bar{t}+200~PU~|~14~TeV" --cms-text "Simulation Preliminary" \
 --level package --ignore-unassigned --metric-precision 0 --save WithoutNewTrackingBaseline/stacked_GPU_Trips.${TYPE}

# Compare three json with bars (CPU-based)
python3 compare_multiple_json_hist.py \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-25-1100_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100_CPU_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_CPU_scaled.json \
 --group /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json \
 --colors /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/colours/default.json \
 --labels "Legacy" "Patatrack (CPU)" "Extended Patatrack (CPU)" --baseline 0 --label-fontsize 14 --lumi-text "t\\bar{t}+200~PU~|~14~TeV" --cms-text "Simulation Preliminary" \
 --level package --ignore-unassigned --metric-precision 0 --save WithoutNewTrackingBaseline/stacked_CPU.${TYPE}
# Compare three json with bars (CPU-based), splitting pixel triplets
python3 compare_multiple_json_hist.py \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-25-1100_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100_CPU_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_CPU_scaled.json \
 --group /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt_pixel_trips.json \
 --colors /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/colours/pixel_trips.json \
 --labels "Legacy" "Patatrack (CPU)" "Extended Patatrack (CPU)" --baseline 0 --label-fontsize 14 --lumi-text "t\\bar{t}+200~PU~|~14~TeV" --cms-text "Simulation Preliminary" \
 --level package --ignore-unassigned --metric-precision 0 --save WithoutNewTrackingBaseline/stacked_CPU_Trips.${TYPE}

# Compare two json with bars (GPU-based vs CPU-based)
python3 compare_multiple_json_hist.py \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100_CPU_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100_scaled.json \
 --group /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json \
 --colors /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/colours/default.json \
 --labels "Patatrack (CPU)" "Patatrack (GPU)" --baseline 0 --label-fontsize 14 --lumi-text "t\\bar{t}+200~PU~|~14~TeV" --cms-text "Simulation Preliminary" \
 --level package --ignore-unassigned --metric-precision 0 --save WithoutNewTrackingBaseline/stacked_2_CPU.${TYPE}
python3 compare_multiple_json_hist.py \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_CPU_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_scaled.json \
 --group /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt.json \
 --colors /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/colours/default.json \
 --labels "Extended Patatrack (CPU)" "Extended Patatrack (GPU)" --baseline 0 --label-fontsize 14 --lumi-text "t\\bar{t}+200~PU~|~14~TeV" --cms-text "Simulation Preliminary" \
 --level package --ignore-unassigned --metric-precision 0 --save WithoutNewTrackingBaseline/stacked_3_CPU.${TYPE}
# Compare two json with bars (GPU-based vs CPU-based), splitting pixel triplets
python3 compare_multiple_json_hist.py \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100_CPU_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-10-30-1100_scaled.json \
 --group /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt_pixel_trips.json \
 --colors /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/colours/pixel_trips.json \
 --labels "Patatrack (CPU)" "Patatrack (GPU)" --baseline 0 --label-fontsize 14 --lumi-text "t\\bar{t}+200~PU~|~14~TeV" --cms-text "Simulation Preliminary" \
 --level package --ignore-unassigned --metric-precision 0 --save WithoutNewTrackingBaseline/stacked_2_CPU_Trips.${TYPE}
python3 compare_multiple_json_hist.py \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_CPU_scaled.json \
 Phase2Timing_resources_NGT_CMSSW_16_0_X_2025-11-10-1100_scaled.json \
 --group /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/groups/hlt_pixel_trips.json \
 --colors /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/circles/web/colours/pixel_trips.json \
 --labels "Extended Patatrack (CPU)" "Extended Patatrack (GPU)" --baseline 0 --label-fontsize 14 --lumi-text "t\\bar{t}+200~PU~|~14~TeV" --cms-text "Simulation Preliminary" \
 --level package --ignore-unassigned --metric-precision 0 --save WithoutNewTrackingBaseline/stacked_3_CPU_Trips.${TYPE}

############################################################################
# Validation of three configurations
############################################################################

cd /data/evernazz/NanoAOD/2026_01_12
cmsrel CMSSW_16_0_0_pre4
cd CMSSW_16_0_0_pre4/src
cmsenv

############ DQM plots
git cms-addpkg DQMServices/Components
git cms-cherrypick-pr 49830
scram b -j
# My own developments here: https://github.com/elenavernazza/cmssw/pull/new/DqmPlots

############ Marco's PR for reproducing Legacy
git remote add ngt git@github.com:cms-ngt-hlt/cmssw.git
git fetch ngt
git switch -c mm_full_legacy --track ngt/mm_full_legacy
scram b -j

############ Marco's PR for vertexing validation
git cms-addpkg Validation/RecoVertex
git cms-cherry-pick-pr 49900
scram b -j 

cd AAA_Test/TTbar_200PU/NGTScouting1
source run.sh
cd ../NGTScouting2
source run.sh
cd ../NGTScouting3
source run.sh

# General Tracks

cd AAA_Test/TTbar_200PU
python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/effic" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/efficPt" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --xlim "0.5,250" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/effic_vs_dxy" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --xlim="-1,1" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/fakerate" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --logy --ylim "0.0002,1" --ylim-ratio "0.,2." \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/fakeratePt" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --logy --xlim "0.5,250" --ylim "0.0002,10" --ylim-ratio "0.,2." \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/ptres_vs_pt_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --xlim "0.5,250" --ylim "0.002,6" --ylim-ratio "0.,3." --logy \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/ptres_vs_eta_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --ylim "0.006,2" --ylim-ratio "0.,2." --no-logx --logy \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/dzres_vs_pt_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --logy --xlim "0.5,250" --ylim "0.0001,1" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/dzres_vs_eta_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --logy --ylim-ratio "0.5,1.5" --ylim "0.001,10" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/dxyres_vs_pt_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --logy --xlim "0.5,250" --ylim-ratio "0.5,1.5" --ylim "0.0001,1" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/dxyres_vs_eta_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --ylim "0.003,0.1" --ylim-ratio "0.8,1.2" --logy \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/ptres_vs_eta_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks/ \
--xlabel-prefix "Simulated Track " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --ylim="-0.05,0.05" --ylim-ratio "0.,3." \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO_original.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO_original.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO_original.root

# # Resolution with RMS

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/ptres_vs_eta_Mean" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks_RMS/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --ylim="-0.05,0.05" --ylim-ratio "0.,3." \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/ptres_vs_pt_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks_RMS/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --xlim "0.5,250" --ylim "0.002,6" --ylim-ratio "0.,3." --logy \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/ptres_vs_eta_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks_RMS/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --ylim "0.006,2" --ylim-ratio "0.,2." --no-logx --logy \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/dzres_vs_pt_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks_RMS/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --logy --xlim "0.5,250" --ylim "0.0001,1" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/dzres_vs_eta_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks_RMS/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --logy --ylim-ratio "0.5,1.5" --ylim "0.001,10" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/dxyres_vs_pt_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks_RMS/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --logy --xlim "0.5,250" --ylim-ratio "0.5,1.5" --ylim "0.0001,1" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/dxyres_vs_eta_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks_RMS/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --logy  --ylim "0.003,0.1" --ylim-ratio "0.8,1.2" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
#  -N "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/ptres_vs_pt_Sigma" \
#  -D "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/ptres_vs_pt_Mean" \
#  --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks_RMS" \
#  --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --xlim "0.5,250" --ylim "0.002,6" --ylim-ratio "0.,3." --logy \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/ptres_vs_pt_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_FullTracks_RMS/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT Final Tracks Performance" --xlim "0.5,250" --ylim "0.002,6" --ylim-ratio "0.,3." --logy \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# PF Jets

cd AAA_Test/QCD_200PU
JETTYPE="hltAK4PFJets"
OUTDIR="QCD200PU_Validation_PFJets"
TITLE="QCD+200PU~(14~TeV)"
JETS="HLT PF Jets Performance"

# cd AAA_Test/QCD_200PU_NoQuality
# JETTYPE="hltAK4PFJets"
# OUTDIR="QCD200PU_NoQuality_Validation_PFJets"
# TITLE="QCD+200PU~(14~TeV)"
# JETS="HLT PFJets Performance"

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/chargedHadronMultiplicity" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Track " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --ylim-ratio "0.5,1.5" --histogram --normalize \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/chargedHadronMultiplicity_" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --ylim-ratio "0.5,1.5" --histogram --normalize \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Eta" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim-ratio "0.95,1.05" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Pt_B" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim-ratio "0.95,1.05" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Pt_E" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim-ratio "0.95,1.05" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Pt_F" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 150, 200" --no-logx \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim-ratio "0.95,1.05" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Eta" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim-ratio "0.5,1.5" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Pt_B" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim="0,1.35" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Pt_E" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim="0,1.35" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Pt_F" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--rebin "40, 60, 80, 100, 150, 200" --no-logx \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim="0,1.35" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenEta_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim "0.,4." --ylim-ratio "0.8,1.2" --histogram --no-logx \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_B_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim "0.,3.5" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_E_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim "0.,3.5" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_F_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 150, 200" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim "0.,3.5" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenEta_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenEta_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim "0.,0.7" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root --no-logx

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_B_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_B_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim "0.,0.5" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_E_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_E_Mean" \
 --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Simulated Jet " --rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
 --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim "0.,0.5" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_F_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_F_Mean" \
 --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Simulated Jet " --rebin "40, 60, 80, 100, 150, 200" --no-logx --histogram \
 --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim "0.,0.5" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# PF Puppi Jets

JETTYPE="hltAK4PFPuppiJets"
OUTDIR="QCD200PU_Validation_PFPuppiJets"
TITLE="QCD+200PU~(14~TeV)"
JETS="HLT PF Puppi Jets Performance"

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/chargedHadronMultiplicity" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --ylim-ratio "0.5,1.5" --ylim "0,3000" --histogram \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/chargedHadronMultiplicity_" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --ylim-ratio "0.5,1.5" --histogram \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Eta" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim-ratio "0.8,1.2" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Pt_B" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim-ratio "0.8,1.2" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Pt_E" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim-ratio "0.8,1.2" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Pt_F" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 150, 200" --no-logx \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim-ratio "0.8,1.2" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Eta" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim-ratio "0.,2." --logy --ylim="0.0001,10" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Pt_B" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --logy --ylim="0.0001,10" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Pt_E" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --logy --ylim="0.0001,10" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Pt_F" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--rebin "40, 60, 80, 100, 150, 200" --no-logx \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --logy --ylim="0.0001,10" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenEta_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim "0.,2." --ylim-ratio "0.8,1.2" --histogram --no-logx \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_B_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim "0.,2." --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_E_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim "0.,2." --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_F_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 150, 200" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim "0.,2." --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenEta_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenEta_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim "0.,0.7" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root --no-logx

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_B_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_B_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim "0.,0.5" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_E_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_E_Mean" \
 --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Simulated Jet " --rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
 --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim "0.,0.5" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_F_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_RecoOverGen_GenPt_F_Mean" \
 --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 150, 200" --no-logx --histogram \
 --xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim "0.,0.5" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# PF Puppi Jets Corrected

JETTYPE="hltAK4PFPuppiJets"
OUTDIR="QCD200PU_Validation_PFPuppiJets_Corrected"
TITLE="QCD+200PU~(14~TeV)"
JETS="HLT PF Puppi Jets Corrected Performance"

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Eta" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim-ratio "0.8,1.2" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Pt_B" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim-ratio "0.8,1.2" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Pt_E" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim-ratio "0.8,1.2" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Eff_vs_Pt_F" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 150, 200" --no-logx \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim-ratio "0.8,1.2" --ylim "0,1.35" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Eta" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim-ratio "0.,2." --logy --ylim="0.0001,10" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Pt_B" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --logy --ylim="0.0001,10" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Pt_E" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --logy --ylim="0.0001,10" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Fake_vs_Pt_F" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --revert \
--rebin "40, 60, 80, 100, 150, 200" --no-logx \
--xlabel-prefix "Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --logy --ylim="0.0001,10" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenEta_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim "0.,2." --ylim-ratio "0.8,1.2" --histogram --no-logx \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenPt_B_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim "0.,2." --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenPt_E_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim "0.,2." --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenPt_F_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 150, 200" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim "0.,2." --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenEta_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenEta_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim "0.,0.7" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root --no-logx

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenPt_B_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenPt_B_Mean" \
--legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim "0.,0.5" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenPt_E_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenPt_E_Mean" \
 --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
 --xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim "0.,0.5" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
 -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenPt_F_Sigma" \
 -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/ResFit_CorrOverGen_GenPt_F_Mean" \
 --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
--rebin "40, 60, 80, 100, 150, 200" --no-logx --histogram \
 --xlabel-prefix "Simulated Jet " --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim "0.,0.5" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# with RMS

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
#  "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenEta_Mean" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
# --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim "0.,2." --ylim-ratio "0.8,1.2" --histogram --no-logx \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
#  "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenPt_B_Mean" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
# --rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
# --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim "0.,2." --ylim-ratio "0.8,1.2" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
#  "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenPt_E_Mean" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
# --rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
# --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim "0.,2." --ylim-ratio "0.8,1.2" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
#  "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenPt_F_Mean" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
# --rebin "40, 60, 80, 100, 150, 200" --no-logx --histogram \
# --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim "0.,2." --ylim-ratio "0.8,1.2" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
#  -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenEta_Sigma" \
#  -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenEta_Mean" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" --histogram \
# --pdf --energy-text "${TITLE}" --legend-title "${JETS}" --web --xlim="-4.,4." --ylim "0.,0.7" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root --no-logx

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
#  -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenPt_B_Sigma" \
#  -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenPt_B_Mean" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
# --rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
# --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Barrel ($ |\eta|<1.5 $)" --web --xlim "25,600" --ylim "0.,0.5" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
#  -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenPt_E_Sigma" \
#  -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenPt_E_Mean" \
#  --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
# --rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
#  --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim "0.,0.5" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot-ratio \
#  -N "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenPt_F_Sigma" \
#  -D "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_CorrOverGen_GenPt_F_Mean" \
#  --legend "Legacy,Patatrack,Extended Patatrack" -o "/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/${OUTDIR}" \
# --rebin "40, 60, 80, 100, 150, 200" --no-logx --histogram \
#  --pdf --energy-text "${TITLE}" --legend-title="${JETS} - Forward ($ |\eta|>3 $)" --web --xlim "25,200" --ylim "0.,0.5" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/Resolution_from_DQMFile_without.py

# Muons

cd AAA_Test/Zuu_200PU
python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Muon/MuonTrack/hltPhase2L3MuonIdTrks/effic_vs_eta" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/Zmumu200PU_Validation_Muons/ \
--pdf --energy-text "Zmumu 200PU (14 TeV)" --web --legend-title "Muons Performance" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root
python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/hltGeneral_hltAssociatorByHits/effic" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/Zmumu200PU_Validation_FullTracks/ \
--pdf --energy-text "Zmumu 200PU (14 TeV)" --web --legend-title "Final Tracks Performance" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# Vertices

cd AAA_Test/TTbar_200PU
# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTsim/hltOfflinePrimaryVertices/effic_vs_Pt2" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_AllVertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "Offline Vertices Performance" --xlim="1,10000" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTsim/hltOfflinePrimaryVertices/effic_vs_Z" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_AllVertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "Offline Vertices Performance" --xlim="-20,20" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTsim/hltOfflinePrimaryVertices/fakerate_vs_Pt2" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_AllVertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "Offline Vertices Performance" --xlim="1,10000" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTsim/hltOfflinePrimaryVertices/fakerate_vs_Z" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_AllVertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "Offline Vertices Performance" --xlim="-20,20" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTsim/hltOfflinePrimaryVertices/PV_purity_vs_Z" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_AllVertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "Offline Vertices Performance" --xlim="-20,20" --ylim="0,1.3" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/effic_vs_Pt2" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--xlabel-prefix "Simulated Vertex " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Vertices Performance" --xlim="2,10000" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/effic_vs_Z" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--xlabel-prefix "Simulated Vertex " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Vertices Performance" --xlim="-19,19" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/fakerate_vs_Pt2" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--xlabel-prefix "Vertex " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Vertices Performance" --xlim="2,10000" --ylim "0,0.4" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/fakerate_vs_Z" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--xlabel-prefix "Vertex " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Vertices Performance" --xlim="-19,19" --ylim "0,0.4" --ylim-ratio "0.,2." \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/PV_purity_vs_Z" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--xlabel-prefix "Simulated Vertex " --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Primary Vertices Performance" --xlim="-19,19" --ylim="0,1.35" --ylim-ratio "0.8,1.2" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/KindOfSignalPV" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Primary Vertices Performance" --xlim="-0.5,5.5" --ylim "0.,1.25" --ylim-ratio "0,2" \
--normalize --histogram --rebin="-0.5,1.5,3.5,5.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# # All resol

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoAllAssoc2GenMatched_ResolPt2_vs_Z_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "DA Primary Vertices Performance" --no-logx --xlim="-19,19" --ylim="0,1.3" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoAllAssoc2GenMatched_ResolPt2_vs_Pt_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "DA Primary Vertices Performance" --logx --xlim="1,1000" --logy --ylim "0.0007,0.07" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoAllAssoc2GenMatched_ResolX_vs_Z_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "DA Primary Vertices Performance" --no-logx --xlim="-19,19" --ylim="0.,0.005" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoAllAssoc2GenMatched_ResolX_vs_Pt_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "DA Primary Vertices Performance" --logx --xlim="1,1000" --logy --ylim "0.0007,0.07" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoAllAssoc2GenMatched_ResolY_vs_Z_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "DA Primary Vertices Performance" --no-logx --xlim="-19,19" --ylim="0.,0.005" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoAllAssoc2GenMatched_ResolY_vs_Pt_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "DA Primary Vertices Performance" --logx --xlim="1,1000" --logy --ylim "0.0007,0.07" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoAllAssoc2GenMatched_ResolZ_vs_Z_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "DA Primary Vertices Performance" --no-logx --xlim="-19,19" --ylim="0.,0.01" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoAllAssoc2GenMatched_ResolZ_vs_Pt_Sigma" \
# --legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
# --pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "DA Primary Vertices Performance" --logx --xlim="1,1000" --logy --ylim "0.0007,0.07" --ylim-ratio "0.5,1.5" \
# NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

# PV resol

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/hltFullVertices/Resolution/PV/res_x_vs_sumpt_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Primary Vertices Performance" --ylim-ratio "0.,2." --xlim="20,1000" --logy \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/hltFullVertices/Resolution/PV/res_y_vs_sumpt_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Primary Vertices Performance" --ylim-ratio "0.,2." --xlim="20,1000" --logy \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/hltFullVertices/Resolution/PV/res_z_vs_sumpt_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Primary Vertices Performance" --ylim-ratio "0.,2." --xlim="20,1000" --logy \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/hltFullVertices/Resolution/PV/res_z_vs_Z_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices/ \
--pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Primary Vertices Performance" --ylim-ratio "0.,2." --xlim="-10,10" --logy \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/Vertexing/hltFullVertices/Resolution/OtherV/res_z_vs_Z_Sigma" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/TTbar200PU_Validation_Vertices_1/ \
--pdf --energy-text="t\bar{t} + 200PU~(14~TeV)" --web --legend-title "HLT DA Primary Vertices Performance" --ylim-ratio "0.,2." --xlim="-10,10" --logy \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root

python3 /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/GaussianFit_from_DQMFile_without.py

DQMData/Run 1/HLT/Run summary/HGCAL/HGCalValidator/hltTiclCandidate/charged_hadrons/eff_charged_hadrons_energy_energy

python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s "DQMData/Run 1/HLT/Run summary/HGCAL/HGCalValidator/hltTiclCandidate/charged_hadrons/eff_charged_hadrons_track_energy" \
--legend "Legacy,Patatrack,Extended Patatrack" -o /eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/QCD200PU_Validation_HGCAL/ \
--pdf --energy-text="QCD + 200PU~(14~TeV)" --web --legend-title "HLT HGCAL Performance" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting2/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root


python3 ${CMSSW_BASE}/src/DQMServices/Components/scripts/dqm-plot -s \
 "DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/${JETTYPE}/Res_RecoOverGen_GenPt_E_Mean" \
--legend "Legacy,Extended Patatrack before,Extended Patatrack after" -o ./ \
--rebin "40, 60, 80, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600" --no-logx --histogram \
--pdf --energy-text "${TITLE}" --legend-title="${JETS} - Endcap ($ 1.5<|\eta|<3 $)" --web --xlim "25,600" --ylim "0.,3.5" --ylim-ratio "0.5,1.5" \
NGTScouting1/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3_TiclBug/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root NGTScouting3/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root
