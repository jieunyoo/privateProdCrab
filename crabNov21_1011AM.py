import CRABClient
from CRABClient.UserUtilities import config

from WMCore.Configuration import Configuration
#config = Configuration()

config = config()
config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True
config.General.workArea = 'crab_Nov21_1011AM'
config.General.requestName = 'boostedHWWfragmentNov21_1011AM'
config.section_('JobType')
#config.JobType.outputFiles = ['dnntuple.root']
config.JobType.numCores = 1
config.JobType.sendExternalFolder = True
config.JobType.scriptArgs = ['nevent=10', 'nthread=1', 'procname=boostedHWWfragment']
config.JobType.scriptExe = 'exe.sh'
config.JobType.pluginName = 'PrivateMC'
config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = 'FAKEMiniAODv2_cfg.py'
config.JobType.inputFiles = ['FrameworkJobReport.xml', 'inputs']
config.JobType.maxMemoryMB = 2500

config.section_('Data')
config.Data.outputDatasetTag = 'boostedHWWfragmentNov21_1011AM'
config.Data.totalUnits = 5
config.Data.unitsPerJob = 2
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
config.Data.publication = True
config.Data.allowNonValidInputDataset = True
config.Data.outLFNDirBase = '/store/user/jiyoo/'
config.Data.outputPrimaryDataset = 'boostedHWWfragmentNov21_1011AM'
config.Data.publication = False

#config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_US*"]

config.section_('User')
config.section_('Debug')
