# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step4 --conditions auto:phase1_2018_realistic -s HARVESTING:@standardValidation+@standardDQM+@ExtraHLT+@miniAODValidation+@miniAODDQM --pileup_input das:/RelValMinBias_13/CMSSW_11_2_0_pre6-112X_upgrade2018_realistic_v3-v1/GEN-SIM -n 10 --era Run2_2018 --scenario pp --pileup 2018_25ns_UltraLegacy_PoissonOOTPU --filetype DQM --geometry DB:Extended --mc --io HARVESTPU_2018PU.io --python HARVESTPU_2018PU.py --no_exec --filein file:step3_inDQM.root --fileout file:step4.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('HARVESTING',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2018_25ns_UltraLegacy_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DQMSaverAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring('file:step3_inDQM.root')
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step4 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/121A1783-7DD7-DF43-802E-C78CB2377104.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/63DF706D-C665-0848-A744-017D0D6E346B.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/6BF323E4-0D38-AB44-AFA5-C01719C291A6.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/98485592-239C-D94B-A243-A3AEBD643894.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/A2DA0B0D-D064-D543-9F87-FD29B7E1C030.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/D08314B9-ADEA-7F44-B116-88CF8C2D1949.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/E1A06B97-1325-A34A-BD50-D6296B9AE4C4.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')

# Path and EndPath definitions
process.genHarvesting = cms.Path(process.postValidation_gen)
process.validationprodHarvesting = cms.Path(process.hltpostvalidation_prod+process.postValidation_gen)
process.validationHarvestingHI = cms.Path(process.postValidationHI)
process.alcaHarvesting = cms.Path()
process.validationHarvestingFS = cms.Path(process.recoMuonPostProcessors+process.postValidationTracking+process.MuIsoValPostProcessor+process.calotowersPostProcessor+process.hcalSimHitsPostProcessor+process.hcaldigisPostProcessor+process.hcalrechitsPostProcessor+process.electronPostValidationSequence+process.photonPostProcessor+process.pfJetClient+process.pfMETClient+process.pfJetResClient+process.pfElectronClient+process.rpcRecHitPostValidation_step+process.makeBetterPlots+process.bTagCollectorSequenceMCbcl+process.METPostProcessor+process.L1GenPostProcessor+process.bdHadronTrackPostProcessor+process.siPixelPhase1OfflineDQM_harvestingV+process.MuonGEMHitsPostProcessors+process.MuonGEMDigisPostProcessors+process.MuonGEMRecHitsPostProcessors+process.postValidation_gen)
process.validationpreprodHarvesting = cms.Path(process.postValidation_preprod+process.hltpostvalidation_preprod+process.postValidation_gen)
process.validationHarvestingNoHLT = cms.Path(process.postValidation+process.postValidation_gen)
process.validationpreprodHarvestingNoHLT = cms.Path(process.postValidation_preprod+process.postValidation_gen)
process.dqmHarvestingPOGMC = cms.Path(process.DQMOffline_SecondStep_PrePOGMC)
process.dqmHarvestingFakeHLT = cms.Path(process.DQMOffline_SecondStep_FakeHLT+process.DQMOffline_Certification)
process.DQMHarvestMiniAOD_step = cms.Path(process.DQMHarvestMiniAOD)
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(process.validationHarvesting,process.dqmHarvesting,process.dqmHarvestingExtraHLT,process.validationHarvestingMiniAOD,process.DQMHarvestMiniAOD_step,process.dqmsave_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
