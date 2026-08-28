#!/bin/bash -ex
LOCALPATH='/eos/cms/store/relval/CMSSW_20_0_0_pre1/RelValMinBias_14TeV/GEN-SIM-DIGI-RAW/PU_150X_mcRun4_realistic_v1_STD_D121_RegeneratedGS_PU-v1/2590000/'

# Filter mode: which module decides the L1 skim accept/reject.
#   pathstatus -> process.L1skimFilter = PathStatusFilter (logicalExpression over l_pathname) (TIMING MENU)
#   l1gt       -> process.L1skimFilter = L1GTAcceptFilter (algoBlocksTag/decision) (NGT MENU)
# Select at runtime with -f, or via env var FILTER_MODE. Defaults to l1gt.
#
# run with: /rerunL1_skim.sh -f pathstatus or ./rerunL1_skim.sh -f l1gt
#

FILTER_MODE="${FILTER_MODE:-l1gt}"

while getopts "f:h" opt; do
    case "${opt}" in
        f) FILTER_MODE="${OPTARG}" ;;
        h)
            echo "Usage: $0 [-f pathstatus|l1gt]"
            exit 0
            ;;
        *)
            echo "Usage: $0 [-f pathstatus|l1gt]" >&2
            exit 1
            ;;
    esac
done

case "${FILTER_MODE}" in
    pathstatus|l1gt) ;;
    *)
        echo "Invalid -f value '${FILTER_MODE}': must be 'pathstatus' or 'l1gt'" >&2
        exit 1
        ;;
esac

echo "L1 skim filter mode: ${FILTER_MODE}"

# Read all files into a bash array
mapfile -t FILES < <(find "${LOCALPATH}" -maxdepth 1 -type f | sort)

CHUNK=128
NFILES=${#FILES[@]}

#CHUNK=50
#NFILES=50

echo "Found ${NFILES} input files"

for ((i=0; i<NFILES; i+=CHUNK)); do

    CFG=$(printf "rerunL1_chunk_%03d_cfg.py" $((i/CHUNK)))
    OUT=$(printf "output_chunk_%03d_%s.root" $((i/CHUNK)) "${FILTER_MODE}")

    # Build the comma-separated file list
    FILELIST=""
    for ((j=i; j<i+CHUNK && j<NFILES; ++j)); do
        FILELIST+="file:${FILES[j]},"
    done
    FILELIST="${FILELIST%,}"

    cmsDriver.py Phase2 -s L1P2GT \
		 --processName=SKIM \
		 --conditions auto:phase2_realistic_T35 \
		 --geometry ExtendedRun4D121 \
		 --era Phase2C22I13M9 \
		 --eventcontent FEVTDEBUGHLT \
		 --datatier GEN-SIM-DIGI-RAW \
		 --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring \
		 --filein "${FILELIST}" \
		 --fileout "file:/cms-hlt-nfs/data/relValMinBiasL1Skim_200PU/CMSSW_20_0_0_pre1/${OUT}" \
		 --python_filename "${CFG}" \
		 -n -1 --nThreads 46 \
		 --mc \
		 --no_exec

### the list of products to be retained in the skim has been obtained by running
### cmsRun -e hlt.py (obtained from cmsDriver)
### and then running getKeepStatements.py --xml jobReport.xml (from this repository)
cat <<EOF >> "${CFG}"
myOutputCommands = cms.untracked.vstring(
    'drop *_*_*_HLT',
    'drop *_*_*_SIM',
    'keep CSCDetIdCSCStripDigiMuonDigiCollection_simMuonCSCDigis_MuonCSCStripDigi_HLT',
    'keep CSCDetIdCSCWireDigiMuonDigiCollection_simMuonCSCDigis_MuonCSCWireDigi_HLT',
    'keep DTLayerIdDTDigiMuonDigiCollection_simMuonDTDigis__HLT',
    'keep DetIdHGCSampleHGCDataFramesSorted_simHGCalUnsuppressedDigis_EE_HLT',
    'keep DetIdHGCSampleHGCDataFramesSorted_simHGCalUnsuppressedDigis_HEback_HLT',
    'keep DetIdHGCSampleHGCDataFramesSorted_simHGCalUnsuppressedDigis_HEfront_HLT',
    'keep EcalTimeDigisSorted_mix_EBTimeDigi_HLT',
    'keep FEDRawDataCollection_rawDataCollector__HLT',
    'keep GEMDetIdGEMDigiMuonDigiCollection_simMuonGEMDigis__HLT',
    'keep GEMDetIdGEMRecHitedmIdToHitRange_gemRecHits__HLT',
    'keep Phase2TrackerDigiedmDetSetVectorPhase2TrackerDigiPhase2TrackerDigiedmrefhelperFindForDetSetVectoredmRefTTTracks_l1tTTTracksFromTrackletEmulation_Level1TTTracks_HLT',
    'keep Phase2TrackerDigiedmDetSetVector_mix_Tracker_HLT',
    'keep PixelDigiedmDetSetVector_simSiPixelDigis_Pixel_HLT',
    'keep RPCDetIdRPCDigiMuonDigiCollection_simMuonRPCDigis__HLT',
    'keep int_addPileupInfo_bunchSpacing_HLT',
    'keep l1tEGammaBXVector_l1tEGammaClusterEmuProducer__HLT',
    'keep l1tEGammaBXVector_l1tLayer1EG_L1EgEE_HLT',
    'keep l1tEGammaBXVector_l1tLayer1HF_L1Eg_HLT',
    'keep l1tEGammaBXVector_l1tLayer1HGCalExtended_L1Eg_HLT',
    'keep l1tEGammaBXVector_l1tLayer1HGCalNoTK_L1Eg_HLT',
    'keep l1tEGammaBXVector_l1tLayer1HGCal_L1Eg_HLT',
    'keep l1tEGammaBXVector_l1tLayer2EG_L1CtEgEE_HLT',
    'keep l1tEGammaBXVector_l1tPhase2L1CaloEGammaEmulator_GCTEGammas_HLT',
    'keep l1tEtSums_l1tMETPFProducer__HLT',
    'keep l1tEtSums_l1tSC4PFL1PuppiCorrectedEmulatorMHT__HLT',
    'keep l1tEtSums_l1tTrackerEmuEtMiss_L1TrackerEmuEtMiss_HLT',
    'keep l1tEtSums_l1tTrackerEmuHTMissExtended_L1TrackerEmuHTMissExtended_HLT',
    'keep l1tEtSums_l1tTrackerEmuHTMiss_L1TrackerEmuHTMiss_HLT',
    'keep l1tJetBXVector_l1tCaloJet_L1CaloJetCollectionBXV_HLT',
    'keep l1tMuonStubs_l1tStubsGmt_tps_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_CL2Electrons_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_CL2EtSum_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_CL2HtSum_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_CL2JetsSC4_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_CL2JetsSC8_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_CL2Photons_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_CL2Taus_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_GMTSaDisplacedMuons_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_GMTSaPromptMuons_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_GMTTkMuons_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_GTTDisplacedHtSum_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_GTTDisplacedJets_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_GTTEtSum_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_GTTPrimaryVert_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_GTTPromptHtSum_HLT',
    'keep l1tP2GTCandidates_l1tGTProducer_GTTPromptJets_HLT',
    'keep l1tPFJets_l1tSC4PFL1PuppiCorrectedEmulator__HLT',
    'keep l1tPFJets_l1tSC4PFL1PuppiExtendedCorrectedEmulator__HLT',
    'keep l1tPFJets_l1tSC8PFL1PuppiCorrectedEmulator__HLT',
    'keep l1tPFTaus_l1tHPSPFTauProducer__HLT',
    'keep l1tPFTaus_l1tNNTauProducerPuppi_L1PFTausNN_HLT',
    'keep l1tPFTracks_l1tLayer1BarrelExtended_DecodedTK_HLT',
    'keep l1tPFTracks_l1tLayer1Barrel_DecodedTK_HLT',
    'keep l1tPFTracks_l1tLayer1HF_DecodedTK_HLT',
    'keep l1tPFTracks_l1tLayer1HGCalExtended_DecodedTK_HLT',
    'keep l1tPFTracks_l1tLayer1HGCalNoTK_DecodedTK_HLT',
    'keep l1tPFTracks_l1tLayer1HGCal_DecodedTK_HLT',
    'keep l1tSAMuons_l1tSAMuonsGmt_displaced_HLT',
    'keep l1tSAMuons_l1tSAMuonsGmt_prompt_HLT',
    'keep l1tTauBXVector_l1tCaloJet_L1CaloTauCollectionBXV_HLT',
    'keep l1tTauBXVector_l1tNNCaloTauEmulator_L1NNCaloTauCollectionBXV_HLT',
    'keep l1tTauBXVector_l1tNNCaloTauProducer_L1NNCaloTauCollectionBXV_HLT',
    'keep l1tTkElectrons_l1tLayer1BarrelExtended_L1TkEle_HLT',
    'keep l1tTkElectrons_l1tLayer1Barrel_L1TkEle_HLT',
    'keep l1tTkElectrons_l1tLayer1EG_L1TkEleEB_HLT',
    'keep l1tTkElectrons_l1tLayer1EG_L1TkEleEE_HLT',
    'keep l1tTkElectrons_l1tLayer1HF_L1TkEle_HLT',
    'keep l1tTkElectrons_l1tLayer1HGCalExtended_L1TkEle_HLT',
    'keep l1tTkElectrons_l1tLayer1HGCalNoTK_L1TkEle_HLT',
    'keep l1tTkElectrons_l1tLayer1HGCal_L1TkEle_HLT',
    'keep l1tTkElectrons_l1tLayer2EG_L1CtTkElectron_HLT',
    'keep l1tTkEms_l1tLayer1BarrelExtended_L1TkEm_HLT',
    'keep l1tTkEms_l1tLayer1Barrel_L1TkEm_HLT',
    'keep l1tTkEms_l1tLayer1EG_L1TkEmEB_HLT',
    'keep l1tTkEms_l1tLayer1EG_L1TkEmEE_HLT',
    'keep l1tTkEms_l1tLayer1HF_L1TkEm_HLT',
    'keep l1tTkEms_l1tLayer1HGCalExtended_L1TkEm_HLT',
    'keep l1tTkEms_l1tLayer1HGCalNoTK_L1TkEm_HLT',
    'keep l1tTkEms_l1tLayer1HGCal_L1TkEm_HLT',
    'keep l1tTkEms_l1tLayer2EG_L1CtTkEm_HLT',
    'keep l1tTkJetWords_l1tTrackJetsEmulation_L1TrackJets_HLT',
    'keep l1tTkJetWords_l1tTrackJetsExtendedEmulation_L1TrackJetsExtended_HLT',
    'keep l1tTrackerMuons_l1tTkMuonsGmt__HLT',
    'keep l1tVertexWords_l1tVertexFinderEmulator_L1VerticesEmulation_HLT',
    'keep recoCaloJets_l1tPhase1JetCalibrator9x9_Phase1L1TJetFromPfCandidates_HLT',
    'keep recoCaloJets_l1tPhase1JetCalibrator9x9trimmed_Phase1L1TJetFromPfCandidates_HLT',
    'keep recoCaloJets_l1tPhase1JetProducer9x9_UncalibratedPhase1L1TJetFromPfCandidates_HLT',
    'keep recoCaloJets_l1tPhase1JetProducer9x9trimmed_UncalibratedPhase1L1TJetFromPfCandidates_HLT'
)

process.FEVTDEBUGHLToutput.outputCommands = myOutputCommands

## L1A skimm part

l_pathname = [
 "pDoubleEGEle37_24",
 "pDoubleIsoTkPho22_12",
 "pDoublePuppiJet112_112",
 "pDoublePuppiTau52_52",
 "pDoubleTkEle25_12",
 "pDoubleTkMuon15_7",
 "pIsoTkEleEGEle22_12",
 # the following two are in AND in pPuppiHT400_pQuadJet70_55_40_40
 #"pPuppiHT400",
 #"pQuadJet70_55_40_40",
 "(pPuppiHT400 and pQuadJet70_55_40_40)",
 "pPuppiHT450",
 "pPuppiMET200",
 "pPuppiTauTkIsoEle45_22",
 "pPuppiTauTkMuon42_18",
 "pSingleEGEle51",
 "pSingleIsoTkEle28",
 "pSingleIsoTkPho36",
 "pSinglePuppiJet230",
 "pSingleTkEle36",
 "pSingleTkMuon22",
 "pTripleTkMuon5_3_3"
# MISSING pDoublePuppiJet160_35_mass620
# MISSING pDoubleTkElePuppiHT_8_8_390
# MISSING pDoubleTkMuPuppiHT_3_3_300
# MISSING pDoubleTkMuPuppiJetPuppiMet_3_3_60_130
# MISSING pDoubleTkMuonTkEle5_5_9
# MISSING pDoubleTkMuon_4_4_OS_Dr1p2
# MISSING pDoubleTkMuon_4p5_4p5_OS_Er2_Mass7to18
# MISSING pDoubleTkMuon_OS_Er1p5_Dr1p4
# MISSING pNNPuppiTauPuppiMet_55_190
# MISSING pPuppiMHT140
# MISSING pTkEleIsoPuppiHT_26_190
# MISSING pTkElePuppiJet_28_40_MinDR
# MISSING pTkEleTkMuon10_20
# MISSING pTkMuPuppiJetPuppiMet_3_110_120
# MISSING pTkMuTriPuppiJet_12_40_dRMax_DoubleJet_dEtaMax
# MISSING pTkMuonDoubleTkEle6_17_17
# MISSING pTkMuonPuppiHT6_320
# MISSING pTkMuonTkEle7_23
# MISSING pTkMuonTkIsoEle7_20
# MISSING pTripleTkMuon_5_3_0_DoubleTkMuon_5_3_OS_MassTo9
# MISSING pTripleTkMuon_5_3p5_2p5_OS_Mass5to17
]

l_path = []

logExpStr = None

for pathname in l_pathname :
    if (logExpStr is None) :
        logExpStr = pathname
    else :
        logExpStr += f" or {pathname}"

EOF

    # Filter selection is decided at bash level (\${FILTER_MODE}) rather than
    # hardcoded in the generated python config, so the two implementations
    # never both land in the same _cfg.py file.
    if [ "${FILTER_MODE}" == "pathstatus" ]; then
        cat <<EOF >> "${CFG}"
process.L1skimFilter = cms.EDFilter("PathStatusFilter",
    logicalExpression = cms.string(logExpStr)
)
EOF
    else
        cat <<EOF >> "${CFG}"
process.L1skimFilter = cms.EDFilter("L1GTAcceptFilter",
			            algoBlocksTag = cms.InputTag("l1tGTAlgoBlockProducer"),
                        	    decision = cms.string("final")                                    
                                   )
EOF
    fi

    cat <<EOF >> "${CFG}"

process.L1skimPath = cms.Path(process.L1skimFilter)
l_path.append(process.L1skimPath)
EventSelection = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring("L1skimPath")
    )
)

process.FEVTDEBUGHLToutput.SelectEvents = EventSelection.SelectEvents
EOF

    echo "" >> "${CFG}"
    echo "# Add L1 skim path to the schedule" >> "${CFG}"
    echo "process.schedule.append(process.L1skimPath)" >> "${CFG}"

    edmConfigDump  "${CFG}"  > dump_"${CFG}"
    python3 dump_"${CFG}"
    
    cmsRun dump_"${CFG}" >& "${CFG}".log
done
