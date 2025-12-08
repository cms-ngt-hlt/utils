NTHREADS=10
GEOM="ExtendedRun4D121"
ERA="Phase2C17I13M9"
CONDS="auto:phase2_realistic_T33"
VALIDSEQ="@hltValidation"
HLTSEQ="NGTScouting" # 75e33 (standard)

# Defaults
NEVENTS=2000
NPARTS=2
PDGID=11
DELTA="XpXX"

### Argument parsing
HELP_STR="Prints this help message."
NEVENTS_STR="(Int) Number of events processed."
NPARTS_STR="(Int) Number of particles generated per event."
PDGID_STR="(Int) PDG ID of the particles being generated."
DELTA_STR="(Float) Distance in centimeters between the particles generated in one event. No effect if \"--nparts 1\"."
function print_usage_submit_skims {
    USAGE="
        Run example: bash $(basename "$0") --nevents 2000 --pdgid 11 --nparts 2 --delta 20p0

	-h / --help	[ ${HELP_STR} ]
	-n / --nevents  [ ${NEVENTS_STR} ]
	--nparts        [ ${NPARTS_STR} ]	
	--pdgid         [ ${PDGID_STR} ]		
	-d / --delta    [ ${DELTA_STR} ]	
"
    printf "${USAGE}"
}

while [[ $# -gt 0 ]]; do
    key=${1}
    case $key in
	-h|--help)
	    print_usage_submit_skims
	    exit 1
	    ;;
	-n|--nevents)
	    NEVENTS=${2}
	    shift; shift;
	    ;;
	-d|--delta)
	    DELTA=${2}
	    shift; shift;
	    ;;
	--nparts)
	    NPARTS=${2}
	    shift; shift;
	    ;;
	--pdgid)
	    PDGID=${2}
	    shift; shift;
	    ;;
	*)  # unknown option
	    echo "Wrong parameter ${1}."
	    exit 1
	    ;;
    esac
done

if [ ${DELTA} == "XpXX" ]; then
    echo "Please provide the `--delta` option."
    exit 1
fi

# step 1
# cmsDriver.py SingleElectronFlatPt2To100_cfi  -s GEN,SIM -n ${NEVENTS} --nThreads ${NTHREADS} \
# 	     --conditions auto:phase2_realistic_T33 --beamspot DBrealisticHLLHC --datatier GEN-SIM \
# 	     --eventcontent FEVTDEBUG --geometry ExtendedRun4D110 --era Phase2C17I13M9 --relval 9000,100

# step 2p1
# cmsDriver.py step2p1 -s DIGI:pdigi_valid,DIGI2RAW,L1,L1TrackTrigger -n ${NEVENTS} --nThreads ${NTHREADS} \
# 	     --conditions auto:phase2_realistic_T33 --datatier GEN-SIM-DIGI-RAW \
# 	     --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 \
# 	     --eventcontent FEVTDEBUG --geometry ExtendedRun4D110 --era Phase2C17I13M9 \
# 	     --hltProcess HLTX --processName HLTX \
# 	     --filein file:SingleElectronFlatPt2To100_cfi_GEN_SIM.root \
# 	     --fileout file:step2p1.root \
# 	     #  --pileup AVE_200_BX_25ns \
# 	     #  --pileup_input das:/RelValMinBias_14TeV/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_STD_MinBias_Run4D110_GenSim-v1/GEN-SIM \
# 	     #  --inputCommands='keep *'

FILE_SUFFIX="${NEVENTS}NEVENTS_${NPARTS}NPARTS_${PDGID}PDGID_${DELTA}DELTA"
INSTEP2p2="Step2_${FILE_SUFFIX}.root"
OUTSTEP2p2="Step2p2_${FILE_SUFFIX}.root"
DQMOUTSTEP2p2="Step2p2_${FILE_SUFFIX}_inDQM.root"
OUTSTEP3="Step3_${FILE_SUFFIX}.root"
DQMOUTSTEP3="DQM_${FILE_SUFFIX}.root"

# step 2p2
cmsDriver.py step2p2 -s L1,L1TrackTrigger,L1P2GT,HLT:75e33,VALIDATION:"${VALIDSEQ}" -n ${NEVENTS} --nThreads ${NTHREADS} \
	     --conditions ${CONDS} \
	     --datatier GEN-SIM-DIGI-RAW,DQMIO \
	     --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2FEVTDEBUGHLT.customisePhase2FEVTDEBUGHLT,L1Trigger/Configuration/customisePhase2TTOn110.customisePhase2TTOn110 \
	     --eventcontent FEVTDEBUGHLT,DQMIO \
	     --geometry ${GEOM} \
	     --era ${ERA} \
	     --hltProcess HLTX --processName HLTXX \
	     --filein file:"${INSTEP2p2}" \
	     --fileout file:"${OUTSTEP2p2}" \
	     --inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' \
	     --outputCommands='keep *_hltParticleFlowCluster*_*_*, keep *_hltParticleFlowTmp_*_HLT' 

# step 3
cmsDriver.py step3 -s HARVESTING:"${VALIDSEQ}" -n -1 \
	     --conditions ${CONDS} --mc --geometry ${GEOM} --era ${ERA} \
	     --filetype DQM --scenario pp \
	     --hltProcess HLTX \
	     --filein file:"${DQMOUTSTEP2p2}" \
	     --fileout file:"${OUTSTEP3}"

# rename output DQM file to avoid overriding it in the future
if [ $? -eq 0 ]; then
    mv DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root ${DQMOUTSTEP3}
else
