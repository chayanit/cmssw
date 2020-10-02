# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:phase1_2018_realistic --pileup_input das:/RelValMinBias_13/CMSSW_11_2_0_pre6-112X_upgrade2018_realistic_v3-v1/GEN-SIM -n 10 --era Run2_2018 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW --pileup 2018_25ns_UltraLegacy_PoissonOOTPU --geometry DB:Extended --io DigiPU_2018PU.io --python DigiPU_2018PU.py --no_exec --filein filelist:step1_dasquery.log --fileout file:step2.root --nThreads 4
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('HLT',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2018_25ns_UltraLegacy_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/2788AAD5-B7ED-974F-A04A-51D97489D004.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/3353B6EA-90BF-1B4B-8C4F-1E020D3C3DB1.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/36018841-B3FC-D940-BB6C-C1176BC7515F.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/3FF03EC1-BA72-D040-9348-9C9A768D0CD5.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/55BA4BB7-30D6-9847-9604-30263B22414A.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/58812281-5F98-9642-A56A-579723F54B33.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/6D889473-6179-AC40-9623-1E19B5F93A63.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/6FD26244-D20B-F642-B11D-8F2A28924572.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/A68957F7-512F-9740-8B21-6B2F71ECE930.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/CE8AEE4F-723D-EB49-8E05-64316FDC2F7F.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/DB9A15F7-89B7-3649-BE2B-B001A58554E2.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/E81D0B3C-709D-584A-A371-83D4FF281A9F.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/EBC5B25A-F532-8B42-9C88-991A3F0CE575.root', 
        '/store/relval/CMSSW_11_2_0_pre6/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/F8411A44-E530-104F-9E8D-1748A24E23E0.root'
    ),
    inputCommands = cms.untracked.vstring(
        'keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
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
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/121A1783-7DD7-DF43-802E-C78CB2377104.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/63DF706D-C665-0848-A744-017D0D6E346B.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/6BF323E4-0D38-AB44-AFA5-C01719C291A6.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/98485592-239C-D94B-A243-A3AEBD643894.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/A2DA0B0D-D064-D543-9F87-FD29B7E1C030.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/D08314B9-ADEA-7F44-B116-88CF8C2D1949.root', '/store/relval/CMSSW_11_2_0_pre6/RelValMinBias_13/GEN-SIM/112X_upgrade2018_realistic_v3-v1/20000/E1A06B97-1325-A34A-BD50-D6296B9AE4C4.root'])
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
