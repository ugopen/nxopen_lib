/*==================================================================================================

                       Copyright (c) 1992-1997
                 Electronic Data Systems Corporation
                  Unpublished - All rights reserved

====================================================================================================
File description:                                                                                                              

Definition of error base values.


==================================================================================================*/

#ifndef ERROR_BASES_H_INCLUDED
#define ERROR_BASES_H_INCLUDED


#ifdef __cplusplus
extern "C" {
#endif

/*
    This file is where each module should define the base value
    for the error codes it uses. 
    There should be a spacing of at least 5000 between different bases, that
    should allow each module enough codes.
    Having defined the base value for a module below, include this
    file in the module's main include file and define each error code 
    there based on an offset from the module's error base value.
    e.g for UIT module, ERROR_UI_base is defined as 5000
    Then uit.h will #include error_bases.h and start
    defining UIT error codes:

      #include <error_bases.h>

      #define UI_err_base            ERROR_UI_base
      #define UI_error_not_found     (UI_err_base+1)
      #define UI_error_bad_aid       (UI_err_base+2)
      #define UI_error_no_string     (UI_err_base+3)
    ...

    Error bases start at 510000, this avoids signal values and
    leaves plenty of room any other special ERROR module codes.

    <MRA> 25-Jan-93
    Note that error_decode.c makes use of these values.  As a check, it
    ERROR_notes if two modules overlap in range, or if one module reserves
    a range of numbers over 5000.
*/
    
#define ERROR_OK                 0

/* IMAN (CXX) uses error 1000-51999 */
#define ERROR_IMAN_base       1000

#define ERROR_CMMV_base     510000
#define ERROR_BOM_base      511000
#define ERROR_ATTR_base     512000
#define ERROR_POM_base      515000
#define ERROR_FM_base       520000
#define ERROR_AM_base       525000
#define ERROR_CMMV_bb_base  535000
#define ERROR_XTM_base      540000
#define ERROR_EIM_base      545000
#define ERROR_UI_base       550000
#define ERROR_OM_base       580000
#define ERROR_TAG_base      590000
#define ERROR_UPDATE_base   600000 
#define ERROR_PX_base       610000
#define ERROR_BPM_base      620000
#define ERROR_RM_base       630000
#define ERROR_PART_base     640000
#define ERROR_OCC_base      650000
#define ERROR_ES_base       660000
#define ERROR_CM_base       670000
#define ERROR_ESS_base      680000
#define ERROR_UG_UNDO_base  690000
#define ERROR_PS_base       700000
#define ERROR_CFM_base      710000
#define ERROR_ASSY_base     720000
#define ERROR_DRAFT_base    730000
#define ERROR_ANT_base      740000
#define ERROR_CALLBACK_base 750000
#define ERROR_CLOCK_base    760000
#define ERROR_CONTEXT_base  770000
#define ERROR_CONV_base     780000
#define ERROR_FSM_base      790000
#define ERROR_GNAT_base     800000
#define ERROR_GT_base       810000
#define ERROR_KI_base       820000
#define ERROR_MENU_base     830000
#define ERROR_CSET_base     835000
#define ERROR_SCHEMA_base   840000
#define ERROR_SPATH_base    850000
#define ERROR_UFT_base      860000
#define ERROR_OPL_base      870000
#define ERROR_MODL_base     875000
#define ERROR_WF_base       880000
#define ERROR_LMGR_base     885000
#define ERROR_LM_base       890000
#define ERROR_CLINK_base    895000
#define ERROR_UIGBLFUNC_base 900000 /* <BJS> 16-Apr-93 not really a module but needs a code */
#define ERROR_REPLACE_base  905000
#define ERROR_SK_base       910000 /* <AKN> 07Jun93 Sketcher Errors */
#define ERROR_API_base      920000 /* <TJGC> 28-Sep-1993    UG/IMAN API error codes */
#define ERROR_DSS_base      925000 /* <EMJ> 05-Oct-1993 Display Sub-System  */
#define ERROR_SEL_base      930000 /* <jdl> 13-oct-1993 Selection error base */
#define ERROR_REXP_base     935000
#define ERROR_UGMGR_base    940000 /* <TJGC> 01-Nov-1993    UG specific error codes from UG Hookup */
#define ERROR_ACS_base      945000 /* <VJP> 13-Dec-1993 ACS needs unique code */


/************************ Bases for cam modules **************/
#define ERROR_CAM_base          950000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_RING_base     955000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_GEOM_base     956000 /* <CHL> 07APR94 CAMGEOM errors */
#define ERROR_CAM_HAND_base     957000 /* <CHL> 11MAY94 HANDle errors */
#define ERROR_CAM_SEG_base      960000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_CHAIN_base    965000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_PMRP_base     970000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_PMP_base      975000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_PM_base       980000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_SC_base       985000 /* <OBH> 02SEP93 CAM  surface cont.errors */
#define ERROR_CAM_WE_base       987500 /* <MLY> 09SEP94 CAM Wire EDM errors */
#define ERROR_CAM_MOTION_base   990000 /* <OBH> 02SEP93 CAM motions errors */
#define ERROR_CAM_BND_base      995000 /* <OBH> 02SEP93 CAM boundary errors */
#define ERROR_CAM_FBND_base     997500 /* <MLY> 10OCT94 CAM face boundary errors */
#define ERROR_CAM_MF_base      1000000 /* <OBH> 02SEP93 CAM filters errors */

#define ERROR_CRV_base         1005000 /* <DJC> 08-Feb-1994 curve error base. */
#define ERROR_ABORT_base       1010000 /* <EMJ> 01-Mar-1994 Want a unique code */
#define ERROR_FEM_base         1015000
#define ERROR_CFI_base         1020000 /* cfi error base */
#define ERROR_AQB_base         1025000 /* <RSG> 02-May-1994 FEM Auto Quad Bnda ry */
#define ERROR_DIVCRV_base      1030000 /* <RSG> 04-May-1994 FEM sub-divide curve */
#define ERROR_ENV_base         1035000 /* <KDH> 15-May-1994 ENV Module */
#define ERROR_SYS_base         1040000 /* <KDH> 15-May-1994 SYS Module */
#define ERROR_ARG_base         1045000 /* <KDH> 15-May-1994 ARG Module */
#define ERROR_EXP_base         1050000 /* <AGD> 13-May-1994 EXP API */
#define ERROR_UNDO_UG_base     1055000 /* <FDM> 20-jun-1994 UNDO_UG */
#define ERROR_FLANGE_base      1060000 /* <MJH> 05-Jul-94 Flange feature. */
#define ERROR_FR_PSMARK_base   1065000 /* <FDM> 07-Jul-94 FR_PSMARK */
#define ERROR_SWEEP_base       1070000 /* <KMJ> 17-Jul-94 SWEEP feature. */
#define ERROR_UF_UNDO_base     1075000 /* <FDM> 26-Jul-94 UF_UNDO */
#define ERROR_RPO_base         1080000 /* <DC>  03-aug-1994 RPO API */
#define ERROR_OPER_base        1085000 /* <YFL> 03-aug-1994 CAM OPER errors */
#define ERROR_MFLFOR_base      1090000 /* <TT>  12-Aug-1994 Moldflow Formatting */
#define ERROR_MFLIO_base       1095000 /* <TT>  12-Aug-1994 Moldflow IO */
#define ERROR_UF_CSYS_base     1100000 /* <VTH> 16-Aug-1994 */
#define ERROR_UF_base          1105000 /* <KDH> 12-Sep-1994 UF layer errors */
#define ERROR_TBL_base         1110000 /* <RJF> 05-Aug-1994 TBL RM entity */
#define ERROR_SMDTBL_base      1115000 /* <RJF> 05-Aug-1994 SMD Process Tables*/
#define ERROR_SMDPIP_base      1120000 /* <RJF> 05-Aug-1994 SMD Part in Proc  */
#define ERROR_SMDFLAT_base     1125000 /* <RJF> 05-Aug-1994 SMD Flat Pattens  */
#define ERROR_UF_PLOT_base     1130000 /* <HLC> 04-Nov-1994 UF Plot errors */
#define ERROR_CMSG_base        1135000 /* <WCL> 10-Dec-1994 CMSG errors */
#define ERROR_ES_VDE_base      1140000 /* <DJL> 19-Jan-1995 VDE errors */
#define ERROR_ES_VDG_base      1145000 /* <DJL> 19-Jan-1995 VDG errors */
#define ERROR_USRT_base        1150000 /* <JAP> 07-Feb-1995 User Tools errors */
#define ERROR_UF_OBJ_base      1155000 /* <WCL> 14-Mar-1995 UF_OBJ errors */
#define ERROR_ZONE_base        1160000 /* <GSL> 20-Jun-1995 ZONE errors */
#define ERROR_FACET_base       1165000 /* <MR > 07-Jul-1995 FACET errors */
#define ERROR_UF_VIEW_base     1170000 /* <VTH> 20-Jul-1995 UF_VIEW errors */
#define ERROR_UF_DRF_base      1175000 /* <JA>  24-Jul-1995 UF_DRF errors */
#define ERROR_UGMX_base        1180000 /* <ONM> 27-Jul_1995 UGMX errors */
#define ERROR_CLEAR_base       1185000 /* <BAC> 25-Jul-1995 Clearance Analysis errors */
#define ERROR_UF_UI_base       1190000 /* <ZA > 20-Jul-1995 UF UI errors */
#define ERROR_STACK_base       1195000 /* <ABH> 20 Sep 94 STACK module */
#define ERROR_GRPH_base        1200000 /* <DWL> 11-Oct-94 GRPH module  */
#define ERROR_CPOS_base        1205000 /* <ABH> 18-Jan-95 CPOS module */
#define ERROR_MOTION_base      1210000 /* <ABH> 18-Jan-95 MOTION module */
#define ERROR_SCPOS_base       1215000 /* <ABH> 18-Jan-95 SCPOS module */
#define ERROR_TPC_base         1220000 /* <ABH> 18-Jan-95 TPC module */
#define ERROR_DRPOS_base       1225000 /* <ABH> 18-Jan-95 DRPOS module */
#define ERROR_SCOP_base        1230000 /* <ABH> 18-Jan-95 SCOP module */
#define ERROR_TAX_base         1235000 /* <ABH> 18-Jan-95 TAX module */
#define ERROR_SCPM_base        1240000 /* <ABH> 18-Jan-95 SCPM module */
#define ERROR_SCCPPS_base      1245000 /* <ABH> 18-Jan-95 SCCPPS module */
#define ERROR_SCCV_base        1250000 /* <ABH> 18-Jan-95 SCCV module */
#define ERROR_SCCVPS_base      1255000 /* <ABH> 18-Jan-95 SCCVS module */
#define ERROR_SCOPPM_base      1260000 /* <ABH> 18-Jan-95 SCOPPM module */
#define ERROR_SCPRPS_base      1265000 /* <ABH> 18-Jan-95 SCPRPS module */
#define ERROR_SCPS_base        1270000 /* <ABH> 18-Jan-95 SCPS module */
#define ERROR_UI_GEOM_base     1275000 /* <jck> 21-mar-95 UI_GEOM module */
#define ERROR_TASK_base        1280000 /* <jlh> 24-Apr-95 TASK module */
#define ERROR_TOOL_base        1285000 /* <jlh> 24-Apr-95 TOOL module */
#define ERROR_PMOP_base        1290000 /* <mab> 05-May-95 PMOP module */
#define ERROR_UDOP_base        1295000 /* <fdm> 10-May-95 UDOP module */
#define ERROR_MMCOP_base       1300000 /* <fdm> 10-May-95 MMCOP module */
#define ERROR_LMCOP_base       1305000 /* <fdm> 10-May-95 LMCOP module */
#define ERROR_WEMCOP_base      1310000 /* <fdm> 10-May-95 WEMCOP module */
#define ERROR_DPRC_base        1315000 /* <TRF> 12-May-95 DPRC module */
#define ERROR_SCFC_base        1320000 /* <JA>  17-May-95 SCFC module */
#define ERROR_DPPM_base        1325000 /* <SDT> 18-May-95 DPPM module */
#define ERROR_DPPMV_base       1330000 /* <SDT> 18-May-95 DPPMV module */
#define ERROR_PATH_base        1335000 /* <BCZ> 06-Dec-94 PATH module */
#define ERROR_GEDIT_base       1340000 /* <KDA> 18-Jan-95 GEDIT module */
#define ERROR_UF_CAM_base      1345000
#define ERROR_CAM_EXIT_base    1350000
#define ERROR_UF_UDOP_base     1355000
#define ERROR_UF_OPER_base     1360000
#define ERROR_UF_PATH_base     1365000
#define ERROR_DPUD_base        1370000
#define ERROR_UF_DPUD_base     1375000
#define ERROR_UF_DRPOS_base    1380000
#define ERROR_UDPOS_base       1385000
#define ERROR_UF_DISP_base     1390000 /* <VtH> 18-Aug-1995 UF DISP errors */
#define ERROR_FF_base          1395000 /* <SLS> 24-Aug-95 Freeform Features */
#define ERROR_DD_base          1400000 /* <DF> 03-Jun-1995 DD errors */
#define ERROR_UF_DRAW_base     1405000 /* <MLL> 18-Sep-1995 UF_DRAW errors */
#define ERROR_FILTER_base      1410000
#define ERROR_FLTR_base        1415000
#define ERROR_SCRIPT_base      1420000
#define ERROR_DP_base          1425000 /* <TRF> 28-SEP-1995 DP errors */
#define ERROR_XS_base          1430000 /* <JCS> 04-OCT-1995 XS module */
#define ERROR_UF_FLTR_base     1435000 /* <GSL> 29-Sep-1995 UF_FLTR errors */
#define ERROR_XFER_base        1440000
#define ERROR_QUEUE_base       1445000 /* <ABH> 27-Oct-1995 QUEUE module */
#define ERROR_DPREF_base       1450000 /* <ABH> 10-Nov-1995 DPREF module */
#define ERROR_DPPMR_base       1455000 /* <ABH> 10-Nov-1995 DPPMR module */
#define ERROR_DPSA_base        1460000 /* <DAR> 14-Nov-1995 DPSA module */
#define ERROR_UF_SMD_base      1465000 /* <DVH> 09-Jan-1996 UF_SMD module */
#define ERROR_RT_HASH_base     1470000 /* <FDM> 06-Feb-1996 RT_HASH */
#define ERROR_CAM_GRV_base     1475000 /* <DJM> 19-Feb-1996 GRV module */
#define ERROR_UF_CURVE_base    1480000 /* <Reger> 05-Mar-1996 UF_CURVE module */
#define ERROR_MB_base          1485000 /* <DPF> 21-Sep-1995 MB (menubar errors) */
#define ERROR_STATE_MACH_base  1490000 /* <SBP> 19-Jan-1996 STATE_MACH module (state machine errors) */
#define ERROR_APP_base         1495000 /* <DPF> 29-Jan-1996 APP module (change application errors) */
#define ERROR_ELM_base         1500000 /* <STB> 11-Sep-95 ELM errors */
#define ERROR_GOPT_base        1505000 /* <STB> 17-Apr-96 Optimization errors */
#define ERROR_TEXT_base        1510000 /* <KDH> 17-Jun-96 TEXT Module errors */
#define ERROR_NAME_base        1515000 /* <KDH> 17-Jun-96 NAME Module errors */
#define ERROR_SO_base          1520000 /* <JBT> 01-Jun-1996 SO module */
#define ERROR_ROUTE_base       1525000 /* <Halladay> 29-Apr-1996 ROUTE_module */
#define ERROR_FAM_base         1530000 /* <WIL> 19-Jun-1996 FAM module */
#define ERROR_UDOBJ_base       1535000 /* <Wei Liu> 10-Jul-96 UDOBJ module */
#define ERROR_SFQM_base        1540000 /* <LLU> 19-Jul-1996   SFQM  module */
#define ERROR_GRX_base         1545000 /* <TAS> 05-Aug-1996 GRX module */
#define ERROR_UII_base         1550000 /* JBrennan 29-Jul-96 UI internals */
#define ERROR_UIO_VALUE_base   1555000 /* JBrennan 29-Jul-96 UI values */
#define ERROR_BLD_base         1560000 /* THayata  13-Jan-97 Change to BLD from UIO  */
#define ERROR_GCON_base        1565000 /* <RDH> 16-Mar-1995 GenConnect errors */
#define ERROR_STD_base         1570000 /* standard file interfaces, like STL */

#define ERROR_MODL_RUBB_base   1700000 /* <AGD> 11-Apr-1996 */
#define ERROR_POINT_SEL_base   1705000 /* <AGD> 11-Apr-1996 */
#define ERROR_CURVE_UI_base    1710000 /* <AGD> 11-Apr-1996 */
#define ERROR_CS2_base         1715000 /* <PM>  14-Mar-1996 Constraint Solver Errors */
#define ERROR_SKET_base        1720000 /* <MDE> 22-Mar-1996 SKET module */
#define ERROR_SKET_UI_base     1725000 /* <MDE> 22-Mar-1996 SKET_UI module */
#define ERROR_INSTFLNG_base    1730000 /* <DVH> 30-Jul-96 INSTFLNG module */
#define ERROR_GENFLG_base      1735000 /* <EFK> 19-Aug-1996 GENFLG module */
#define ERROR_MOM_base         1740000 /* <FDM> 30-Aug-1996 */
#define ERROR_MOM_POST_base    1745000 /* <FDM> 30-Aug-1996 */

#define ERROR_PROM_base        1750000 /* <RSS> 09-Sep-1996 Promotions */

#define ERROR_SFASM_base       1755000 /* <RJW> 25-Nov-1996 Auto Solid Mesher */
#define ERROR_SFATM_base       1760000 /* <RJW> 25-Nov-1996 Aries Tet  Mesher */
#define ERROR_UF_SFEM_base     1765000 /* <KJS> 27-Nov-1996 Scenario UF */
#define ERROR_MOM_TCL_base     1770000 /* <FDM> 17-Sep-1996 */
#define ERROR_UF_SFEM_LANG_base  \
                               1775000 /* <KJS> 11-Mar-97 Scenario lang def  */
#define ERROR_PFEDIT_base      1780000 /* <BJS> 11-Mar-1997 Part File EDIT module */
#define ERROR_AP_base          1785000 /* <JAP> 25-Mar-1997 Application Part module */
#define ERROR_UGFONTC_base     1790000 /* <GLG> 14-Mar-1997 */
#define ERROR_SKUTIL_base      1795000 /* <MPE> 04-Apr-1997 Sketch util module*/
#define ERROR_CPROJ_base       1800000 /* <PEH> 17-Apr-1997 */
#define ERROR_UF_SFOPT_base    1805000 /* <MPS> 17-Apr-97 Optima analysis    */

#define ERROR_TOL_FEAT_base    1810000 /* <jdl> 20-Jan-1997 Tolerance Feature */
#define ERROR_ASSOC_base       1815000 /* <jdl> 29-Jan-1997 Association Objects */
#define ERROR_ANNOT_base       1820000 /* <jdl> 29-Jan-1997 Annotation Objects */
#define ERROR_NOTE_base        1825000 /* <nra> 03-Feb-1997 Note objects */
#define ERROR_UF_GDT_base      1830000 /* <jdl> 05-Feb-1997 User Function for Tolerancing */
#define ERROR_EPLIB_base       1835000 /* <ATS> 02-Apr-1997 Part Library View module */
#define ERROR_CSO_base         1840000 /* <jlh> 06-Jun-1997 CAM CSO module */
#define ERROR_PARAM_base       1845000 /* <jlh> 06-Jun-1997 CAM PARAM module */
#define ERROR_OPR_base         1850000 /* <jlh> 06-Jun-1997 CAM new operation module */
#define ERROR_UGFONT_base      1855000 /* <KDH> 15-May-1997 UGFONT module */
#define ERROR_UF_WEIGHT_base   1860000 /* <MRA> 18-Aug-1997 User Function for Weight Management */
#define ERROR_FCF_base         1865000 /* <jdl> 28-May-1997 Feature Control Frames */
#define ERROR_TOL_base         1870000 /* <jdl> 04-Sep-1997 Tolerances */
#define ERROR_IP_base          1875000 /* <DRD> 24-Sep-1997 Interpart References */
#define ERROR_QRY_base         1880000 /* <FDM> 21-Jan-1997 */
#define ERROR_RSET_base        1885000 /* <FDM> 21-Jan-1997 */
#define ERROR_LIB_base         1890000 /* <FDM> 21-Jan-1997 */
#define ERROR_DBC_base         1895000 /* <FDM> 21-Jan-1997 */
#define ERROR_SMHOLE_base      1900000 /* <BAT> 01-Sep-1997 SMHole module */
#define ERROR_BEAD_base        1905000 /* <WSN> 07-Oct-1997 Bead Feature  */
#define ERROR_PLOT_base        1910000 /* <jos> 09-Oct-1997 Plot module errors */
#define ERROR_UF_WAVE_base     1915000 /* <MRA> 18-Aug-1997 User Function for Wave/Interpart extractions */

/*  <DRD> 11-Mar-1994

    Infomanager bases start at 2000000
*/

#define ERROR_WS_base          2000000 /* <MSF> 24-Feb-94 New Workspace */
#define ERROR_CALS_CM_base     2001000 /* <HMK> 16-Nov-94 IAI effectivity */
/*  <BJS> 18-Jun-96
    Only put codes here for IMAN modules.
*/

/* The next code is the largest expected error code ( = largest base + 4999 ),
 * so PLEASE UPDATE IT IF YOU ADD ANOTHER ERROR BASE ! But remember this is
 * for UG and Iman codes combined so most UG codes won't affect this.
 */

#define ERROR_max_error_code   2001999



#ifdef __cplusplus
}
#endif

#endif /* ERROR_BASES_H_INCLUDED */

