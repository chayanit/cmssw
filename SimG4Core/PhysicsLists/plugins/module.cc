#include "SimG4Core/Physics/interface/PhysicsListFactory.h"

#include "DummyPhysics.h"
#include "FTFCMS_BIC.h"
#include "FTFPCMS_BERT.h"
#include "FTFPCMS_BERT_EML.h"
#include "FTFPCMS_BERT_EMM.h"
#include "FTFPCMS_BERT_EMN.h"
#include "FTFPCMS_BERT_EMM_TRK.h"
#include "FTFPCMS_BERT_HP_EMM.h"
#include "FTFPCMS_BERT_HP_EML.h"
#include "FTFPCMS_BERT_XS_EML.h"
#include "FTFPCMS_BERT_EMY.h"
#include "FTFPCMS_BERT_EMZ.h"
#include "FTFPCMS_INCLXX_EMM.h"
#include "FTFPCMS_INCLXX_HP_EMM.h"
#include "QBBCCMS.h"
#include "QGSPCMS_BERT_EML.h"
#include "QGSPCMS_BERT_HP_EML.h"
#include "QGSPCMS_FTFP_BERT.h"
#include "QGSPCMS_FTFP_BERT_EML.h"
#include "QGSPCMS_FTFP_BERT_EMM.h"
#include "QGSPCMS_FTFP_BERT_EMN.h"
#include "QGSPCMS_FTFP_BERT_EMY.h"
#include "QGSPCMS_FTFP_BERT_EMZ.h"

DEFINE_PHYSICSLIST(DummyPhysics);
typedef FTFCMS_BIC FTF_BIC;
DEFINE_PHYSICSLIST(FTF_BIC);
typedef FTFPCMS_BERT FTFP_BERT;
DEFINE_PHYSICSLIST(FTFP_BERT);
typedef FTFPCMS_BERT_EML FTFP_BERT_EML;
DEFINE_PHYSICSLIST(FTFP_BERT_EML);
typedef FTFPCMS_BERT_EMM FTFP_BERT_EMM;
DEFINE_PHYSICSLIST(FTFP_BERT_EMM);
typedef FTFPCMS_BERT_EMN FTFP_BERT_EMN;
DEFINE_PHYSICSLIST(FTFP_BERT_EMN);
typedef FTFPCMS_BERT_EMM_TRK FTFP_BERT_EMM_TRK;
DEFINE_PHYSICSLIST(FTFP_BERT_EMM_TRK);
typedef FTFPCMS_BERT_HP_EMM FTFP_BERT_HP_EMM;
DEFINE_PHYSICSLIST(FTFP_BERT_HP_EMM);
typedef FTFPCMS_BERT_HP_EML FTFP_BERT_HP_EML;
DEFINE_PHYSICSLIST(FTFP_BERT_HP_EML);
typedef FTFPCMS_BERT_XS_EML FTFP_BERT_XS_EML;
DEFINE_PHYSICSLIST(FTFP_BERT_XS_EML);
typedef FTFPCMS_BERT_EMY FTFP_BERT_EMY;
DEFINE_PHYSICSLIST(FTFP_BERT_EMY);
typedef FTFPCMS_BERT_EMZ FTFP_BERT_EMZ;
DEFINE_PHYSICSLIST(FTFP_BERT_EMZ);
typedef FTFPCMS_INCLXX_EMM FTFP_INCLXX_EMM;
DEFINE_PHYSICSLIST(FTFP_INCLXX_EMM);
typedef FTFPCMS_INCLXX_HP_EMM FTFP_INCLXX_HP_EMM;
DEFINE_PHYSICSLIST(FTFP_INCLXX_HP_EMM);
typedef QBBCCMS QBBC;
DEFINE_PHYSICSLIST(QBBC);
typedef QGSPCMS_BERT_EML QGSP_BERT_EML;
DEFINE_PHYSICSLIST(QGSP_BERT_EML);
typedef QGSPCMS_BERT_HP_EML QGSP_BERT_HP_EML;
DEFINE_PHYSICSLIST(QGSP_BERT_HP_EML);
typedef QGSPCMS_FTFP_BERT QGSP_FTFP_BERT;
DEFINE_PHYSICSLIST(QGSP_FTFP_BERT);
typedef QGSPCMS_FTFP_BERT_EML QGSP_FTFP_BERT_EML;
DEFINE_PHYSICSLIST(QGSP_FTFP_BERT_EML);
typedef QGSPCMS_FTFP_BERT_EMM QGSP_FTFP_BERT_EMM;
DEFINE_PHYSICSLIST(QGSP_FTFP_BERT_EMM);
typedef QGSPCMS_FTFP_BERT_EMN QGSP_FTFP_BERT_EMN;
DEFINE_PHYSICSLIST(QGSP_FTFP_BERT_EMN);
typedef QGSPCMS_FTFP_BERT_EMY QGSP_FTFP_BERT_EMY;
DEFINE_PHYSICSLIST(QGSP_FTFP_BERT_EMY);
typedef QGSPCMS_FTFP_BERT_EMZ QGSP_FTFP_BERT_EMZ;
DEFINE_PHYSICSLIST(QGSP_FTFP_BERT_EMZ);
//
