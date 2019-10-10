import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
	args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2018/13TeV/madgraph/V5_2.6.0/exo_diboson/Spin-2/BulkGraviton_VBF_WW_inclu_narrow/BulkGraviton_VBF_WW_inclu_narrow_M2000_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
	nEvents = cms.untracked.uint32(5000),
	numberOfParameters = cms.uint32(1),
	outputFile = cms.string('cmsgrid_final.lhe'),
	scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

from Configuration.Generator.Pythia8CommonSettings_cfi import *
#from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
 
generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
	#pythia8CUEP8M1SettingsBlock,
        pythia8CP5SettingsBlock,
        parameterSets = cms.vstring('pythia8CommonSettings',
				    #'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    'pythia8CP5Settings',
                                    )
    )
)
