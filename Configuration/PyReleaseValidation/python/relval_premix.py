
# import the definition of the steps and input files:
from  Configuration.PyReleaseValidation.relval_steps import *

# here only define the workflows as a combination of the steps defined above:
workflows = Matrix()

# each workflow defines a name and a list of steps to be done. 
# if no explicit name/label given for the workflow (first arg),
# the name of step1 will be used


# premix at 13 TeV and POSTLS1
workflows[250199]=['',['PREMIXUP15_PU25']]
workflows[500199]=['',['PREMIXUP15_PU50']]
workflows[250199.17]=['',['PREMIXUP17_PU25']]
workflows[250199.18]=['',['PREMIXUP18_PU25']]

# 25ns pile up overlay using premix
workflows[250200]=['',['ZEE_13','DIGIPRMXUP15_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]
workflows[250202]=['',['TTbar_13','DIGIPRMXUP15_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]
workflows[250202.1]=['',['TTbar_13','PREMIXUP15_PU25','DIGIPRMXLOCALUP15_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]
workflows[250202.2]=['',['TTbar_13','DIGIPRMXUP15APVSimu_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]
workflows[250202.3]=['',['TTbar_13','PREMIXUP15_PU25','DIGIPRMXLOCALUP15APVSimu_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]
workflows[250202.4]=['',['TTbar_13','DIGIPRMXUP15APVSimu_PU25','RECOPRMXUP15_HIPM_PU25','HARVESTUP15_PU25']]
workflows[250202.5]=['',['TTbar_13','PREMIXUP15_PU25','DIGIPRMXLOCALUP15APVSimu_PU25','RECOPRMXUP15_HIPM_PU25','HARVESTUP15_PU25']]

workflows[250203]=['',['H125GGgluonfusion_13','DIGIPRMXUP15_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]
workflows[250204]=['',['QQH1352T_13','DIGIPRMXUP15_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]
workflows[250205]=['',['ZTT_13','DIGIPRMXUP15_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]
workflows[250206]=['',['ZMM_13','DIGIPRMXUP15_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]
workflows[250207]=['',['NuGun_UP15','DIGIPRMXUP15_PU25','RECOPRMXUP15_PU25','HARVESTUP15_PU25']]


workflows[250200.17]=['',['ZEE_13UP17','DIGIPRMXUP17_PU25','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]
workflows[250202.17]=['',['TTbar_13UP17','DIGIPRMXUP17_PU25','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]
workflows[250202.171]=['',['TTbar_13UP17','PREMIXUP17_PU25','DIGIPRMXLOCALUP17_PU25','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]
workflows[250202.172]=['',['TTbar_13UP17','DIGIPRMXUP17_PU25_RD','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]
workflows[250203.17]=['',['H125GGgluonfusion_13UP17','DIGIPRMXUP17_PU25','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]
workflows[250204.17]=['',['QQH1352T_13UP17','DIGIPRMXUP17_PU25','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]
workflows[250205.17]=['',['ZTT_13UP17','DIGIPRMXUP17_PU25','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]
workflows[250206.17]=['',['ZMM_13UP17','DIGIPRMXUP17_PU25','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]
workflows[250207.17]=['',['NuGun_UP17','DIGIPRMXUP17_PU25','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]
workflows[250208.17]=['',['SMS-T1tttt_mGl-1500_mLSP-100_13UP17','DIGIPRMXUP17_PU25','RECOPRMXUP17_PU25','HARVESTUP17_PU25']]


workflows[250200.18]=['',['ZEE_13UP18','DIGIPRMXUP18_PU25','RECOPRMXUP18_PU25_L1TEgDQM','HARVESTUP18_PU25_L1TEgDQM']]
workflows[250202.18]=['',['TTbar_13UP18','DIGIPRMXUP18_PU25','RECOPRMXUP18_PU25','HARVESTUP18_PU25']]
workflows[250202.181]=['',['TTbar_13UP18','PREMIXUP18_PU25','DIGIPRMXLOCALUP18_PU25','RECOPRMXUP18_PU25','HARVESTUP18_PU25']]
workflows[250202.182]=['',['TTbar_13UP18','DIGIPRMXUP18_PU25_RD','RECOPRMXUP18_PU25','HARVESTUP18_PU25']]
workflows[250202.183]=['',['TTbar_13UP18_RD_test','DIGIPRMXUP18_PU25_RD_test','RECOPRMXUP18_PU25_RD_test','HARVESTUP18_PU25']]
workflows[250202.184]=['',['TTbar_13UP18_RD','DIGIPRMXUP18_PU25_RD','RECOPRMXUP18_PU25_RD','HARVESTUP18_PU25']]
workflows[250203.18]=['',['H125GGgluonfusion_13UP18','DIGIPRMXUP18_PU25','RECOPRMXUP18_PU25','HARVESTUP18_PU25']]
workflows[250204.18]=['',['QQH1352T_13UP18','DIGIPRMXUP18_PU25','RECOPRMXUP18_PU25','HARVESTUP18_PU25']]
workflows[250205.18]=['',['ZTT_13UP18','DIGIPRMXUP18_PU25','RECOPRMXUP18_PU25','HARVESTUP18_PU25']]
workflows[250206.18]=['',['ZMM_13UP18','DIGIPRMXUP18_PU25','RECOPRMXUP18_PU25_L1TMuDQM','HARVESTUP18_PU25_L1TMuDQM']]
workflows[250206.181]=['',['ZMM_13UP18','PREMIXUP18_PU25','DIGIPRMXLOCALUP18_PU25','RECOPRMXUP18_PU25_L1TMuDQM','HARVESTUP18_PU25_L1TMuDQM']]
workflows[250207.18]=['',['NuGun_UP18','DIGIPRMXUP18_PU25','RECOPRMXUP18_PU25','HARVESTUP18_PU25']]
workflows[250208.18]=['',['SMS-T1tttt_mGl-1500_mLSP-100_13UP18','DIGIPRMXUP18_PU25','RECOPRMXUP18_PU25','HARVESTUP18_PU25']]


# 50ns pile up overlay using premix
workflows[500200]=['',['ZEE_13','DIGIPRMXUP15_PU50','RECOPRMXUP15_PU50','HARVESTUP15_PU50']]
workflows[500202]=['',['TTbar_13','DIGIPRMXUP15_PU50','RECOPRMXUP15_PU50','HARVESTUP15_PU50']]
workflows[500203]=['',['H125GGgluonfusion_13','DIGIPRMXUP15_PU50','RECOPRMXUP15_PU50','HARVESTUP15_PU50']]
workflows[500204]=['',['QQH1352T_13','DIGIPRMXUP15_PU50','RECOPRMXUP15_PU50','HARVESTUP15_PU50']]
workflows[500205]=['',['ZTT_13','DIGIPRMXUP15_PU50','RECOPRMXUP15_PU50','HARVESTUP15_PU50']]
workflows[500206]=['',['ZMM_13','DIGIPRMXUP15_PU50','RECOPRMXUP15_PU50','HARVESTUP15_PU50']]
workflows[500207]=['',['NuGun_UP15','DIGIPRMXUP15_PU50','RECOPRMXUP15_PU50','HARVESTUP15_PU50']]

# develop pile up overlay using premix prod-like!
workflows[250200.1]=['ProdZEE_13_pmx25ns',['ProdZEE_13','DIGIPRMXUP15_PROD_PU25','RECOPRMXUP15PROD_PU25']]
workflows[500200.1]=['ProdZEE_13_pmx50ns',['ProdZEE_13','DIGIPRMXUP15_PROD_PU50','RECOPRMXUP15PROD_PU50']]
workflows[250200.117]=['ProdZEE_13_pmx25ns',['ProdZEE_13UP17','DIGIPRMXUP17_PROD_PU25','RECOPRMXUP17PROD_PU25']]
workflows[250200.118]=['ProdZEE_13_pmx25ns',['ProdZEE_13UP18','DIGIPRMXUP18_PROD_PU25','RECOPRMXUP18PROD_PU25','NANOEDMMC2018_PROD']]
workflows[250206.118]=['ProdZMM_13_pmx25ns',['ProdZMM_13UP18','DIGIPRMXUP18_PROD_PU25','RECOPRMXUP18PROD_PU25','NANOEDMMC2018_PROD']]
workflows[250202.118]=['ProdTTbar_13_pmx25ns',['ProdTTbar_13UP18','DIGIPRMXUP18_PROD_PU25','RECOPRMXUP18PROD_PU25','NANOEDMMC2018_PROD']]
#fastsim, 25ns

## premixed minbias
workflows[250399]=['',['FS_PREMIXUP15_PU25']]
## signal + PU
workflows[250400] = ['ZEE_13',["FS_ZEE_13_PRMXUP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[250402] = ['TTbar_13',["FS_TTbar_13_PRMXUP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[250402.1] = ['TTbar_13',["FS_PREMIXUP15_PU25","FS_TTbar_13_PRMXLOCALUP15_PU25","HARVESTUP15FS"]]
workflows[250403] = ['H125GGgluonfusion_13',["FS_H125GGgluonfusion_13_PRMXUP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[250405] = ['ZTT_13',["FS_ZTT_13_PRMXUP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[250406] = ['ZMM_13',["FS_ZMM_13_PRMXUP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[250407] = ['NuGun_UP15',["FS_NuGun_UP15_PRMXUP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[250408] = ['QCD_FlatPt_15_3000HS_13',["FS_QCD_FlatPt_15_3000HS_13_PRMXUP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[250409] = ['SMS-T1tttt_mGl-1500_mLSP-100_13',["FS_SMS-T1tttt_mGl-1500_mLSP-100_13_PRMXUP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]

#fastsim,  2017 PU50####

## premixed minbias
workflows[250399.17]=['',['FS_PREMIXUP17_PU50']]
## signal + PU
workflows[250400.17] = ['ZEE_13',["FS_ZEE_13_PRMXUP17_PU50","HARVESTUP17FS","MINIAODMCUP17FS"]]
workflows[250402.17] = ['TTbar_13',["FS_TTbar_13_PRMXUP17_PU50","HARVESTUP17FS","MINIAODMCUP17FS"]]
workflows[250402.171] = ['TTbar_13',["FS_PREMIXUP17_PU50","FS_TTbar_13_PRMXLOCALUP17_PU50","HARVESTUP17FS"]]
workflows[250403.17] = ['H125GGgluonfusion_13',["FS_H125GGgluonfusion_13_PRMXUP17_PU50","HARVESTUP17FS","MINIAODMCUP17FS"]]
workflows[250405.17] = ['ZTT_13',["FS_ZTT_13_PRMXUP17_PU50","HARVESTUP17FS","MINIAODMCUP17FS"]]
workflows[250406.17] = ['ZMM_13',["FS_ZMM_13_PRMXUP17_PU50","HARVESTUP17FS","MINIAODMCUP17FS"]]
workflows[250407.17] = ['NuGun_UP17',["FS_NuGun_UP17_PRMXUP17_PU50","HARVESTUP17FS","MINIAODMCUP17FS"]]
workflows[250408.17] = ['QCD_FlatPt_15_3000HS_13',["FS_QCD_FlatPt_15_3000HS_13_PRMXUP17_PU50","HARVESTUP17FS","MINIAODMCUP17FS"]]
workflows[250409.17] = ['SMS-T1tttt_mGl-1500_mLSP-100_13',["FS_SMS-T1tttt_mGl-1500_mLSP-100_13_PRMXUP17_PU50","HARVESTUP17FS","MINIAODMCUP17FS"]]                                   

#fastsim,  2018 PU50####

## premixed minbias
workflows[250399.18]=['',['FS_PREMIXUP18_PU50']]
## signal + PU
workflows[250400.18] = ['ZEE_13',["FS_ZEE_13_PRMXUP18_PU50","HARVESTUP18FS","MINIAODMCUP18FS"]]
workflows[250402.18] = ['TTbar_13',["FS_TTbar_13_PRMXUP18_PU50","HARVESTUP18FS","MINIAODMCUP18FS"]]
workflows[250402.181] = ['TTbar_13',["FS_PREMIXUP18_PU50","FS_TTbar_13_PRMXLOCALUP18_PU50","HARVESTUP18FS"]]
workflows[250403.18] = ['H125GGgluonfusion_13',["FS_H125GGgluonfusion_13_PRMXUP18_PU50","HARVESTUP18FS","MINIAODMCUP18FS"]]
workflows[250405.18] = ['ZTT_13',["FS_ZTT_13_PRMXUP18_PU50","HARVESTUP18FS","MINIAODMCUP18FS"]]
workflows[250406.18] = ['ZMM_13',["FS_ZMM_13_PRMXUP18_PU50","HARVESTUP18FS","MINIAODMCUP18FS"]]
workflows[250407.18] = ['NuGun_UP18',["FS_NuGun_UP18_PRMXUP18_PU50","HARVESTUP18FS","MINIAODMCUP18FS"]]
workflows[250408.18] = ['QCD_FlatPt_15_3000HS_13',["FS_QCD_FlatPt_15_3000HS_13_PRMXUP18_PU50","HARVESTUP18FS","MINIAODMCUP18FS"]]
workflows[250409.18] = ['SMS-T1tttt_mGl-1500_mLSP-100_13',["FS_SMS-T1tttt_mGl-1500_mLSP-100_13_PRMXUP18_PU50","HARVESTUP18FS","MINIAODMCUP18FS"]] 
