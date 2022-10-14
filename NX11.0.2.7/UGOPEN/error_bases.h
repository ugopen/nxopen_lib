/*================================================================================================

       Copyright 1990 Siemens Product Lifecycle Management Software Inc.
                             All Rights Reserved.

==================================================================================================
File description:
    Definition of error base values.

@
=================================================================================================*/

#ifndef ERROR_BASES_H_INCLUDED
#define ERROR_BASES_H_INCLUDED

/* <JLM> 13-Nov-98 Restrict nesting of this file */
#ifdef __lint
#pragma uginclude only_in_error "error_decode_privileged.h", "*.c*";
#endif


/*
    This file is where each module should define the base value
    for the error codes it uses.
    There should be a spacing of at least 5000 between different bases, that
    should allow each module enough codes.

    Having defined the base value for a module below, include the identical
    definition in the module's main include file and define each error code
    there based on an offset from the module's error base value.
    e.g for UIT module, ERROR_UI_base is defined as 550000
    Then uit.h will also use the same definition for ERROR_UI_base
    and start defining UIT error codes:

      #define UI_err_base            550000
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

    <JLM> 04-Jan-99
    Revise instructions above to reflect desire that this header not
    be nested.  The full set of modifications performed at this time are:

    1) The prototype for ERROR_register_decoder_fn, ERROR_decoder_fn_t,
       ERROR_decode_in_table and other symbols required to register error
       decoder functions have moved to new header error_decode_privileged.h.
       This new header includes error_bases.h.

    2) error_bases.h is to be included only in C source files and in
       error_decode_privileged.h.  This is accomplished via qaz pragmas.

    3) Every header that needs one of the ERROR_<module>_base definitions
       from error_bases.h should instantiate the definition there *AND* in
       the module header that defines the other error codes which depend on
       ERROR_<module>_base.  The two definitions will be validated against each
       other by virtue of being included in the source file that registers the
       error decoder function.  ANSI C specifies that if both definitions are
       identical then it is considered a "benign redefinition" and no warning
       is issued.  Therefore this results in no compiler warnings and we do not
       issue a qaz warning or error.  However if the definitions differ then a
       compiler warning and qaz error result.

 */

#if 0
/* Example: */

/******** error_bases.h ****************/

#define ERROR_FOO_base 4200000 /* <JLM> 25-Dec-98 Error base for FOO module */

/******** foo_error_codes.h ************/

#define ERROR_FOO_base 4200000 /* <JLM> 01-Jan-99 Error base for FOO module */
#define FOO_situation_normal    ERROR_FOO_base
#define FOO_situation_abnormal  ERROR_FOO_base+1

/******** foo_error_codes.c ***************/

#include <error_decode_privileged.h> /* For ERROR_register_decoder_fn proto */
#include <foo_error_codes.h>         /* For ERROR_FOO_base, FOO__error_table */

extern void FOO__init_error_table(void)
{
    ERROR_register_decoder_fn(ERROR_FOO_base, 5000,
                              (ERROR_decoder_fn_t) ERROR_decode_in_table,
                              (void *)FOO__error_table);
}

/*
 * ERROR_FOO_base is defined in both foo_error_codes.h and in error_bases.h,
 * which is indirectly included via the required inclusion of
 * error_decode_privileged.h.  If the two definitions do not match (ignoring
 * white space and comments) then the compiler and qaz will issue warnings.
 */

/******************************************/
#endif

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
#define ERROR_MT_base       550000
#define ERROR_UI_QP_base    560000 /* Arch4008: Quick Pick errors */
#define ERROR_OM_base       580000
#define ERROR_TAG_base      590000
#define ERROR_UPDATE_base   600000
#define ERROR_DUC_base      601000 // <hansen> 04-Jun-2008 DelayedUpdateController errors
#define ERROR_PX_base       610000
#define ERROR_BPM_base      620000
#define ERROR_RM_base       630000
#define ERROR_PART_base     640000
#define ERROR_OCC_base      650000
#define ERROR_BKM_base      659000 /* <JMF> 18-Mar-99 borrow some OCC space for bookmarks */
#define ERROR_ES_base       660000
#define ERROR_CM_base       670000
#define ERROR_ESS_base      680000
#define ERROR_CMOD_base     690000 /* <SCH> 30-Sep-1999 borrow ERROR_UG_UNDO_base for expanded
                                      CMOD since ERROR_UG_UNDO_base is not used when
                                      ERROR_UNDO_UG_base was created */
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
#define ERROR_BASE_base     810000
#define ERROR_KI_base       820000
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
#define ERROR_UGMGR_base    940000 /* <TJGC> 01-Nov-1993 UG specific error codes from UG Hookup */
#define ERROR_LICENSE_base  945000 /* <VJP>   13-Dec-1993 ACS needs unique code;
                                      <Reger> 03-Sep-2008 Rename ACS to LICENSE */


/************************ Bases for cam modules **************/
#define ERROR_CERR_base         950000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_RING_base     955000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_GEOM_base     956000 /* <CHL> 07APR94 CAMGEOM errors */
#define ERROR_CAM_SEG_base      960000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_CHAIN_base    965000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_PMRP_base     970000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_PMP_base      975000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_PM_base       980000 /* <OBH> 02SEP93 General CAM errors */
#define ERROR_CAM_TCM_base      984000 /* <JLH> 09MAR05 CAM Teamcenter Mfg errors */
#define ERROR_CAM_SC_base       985000 /* <OBH> 02SEP93 CAM  surface cont.errors */
#define ERROR_CAM_WE_base       987500 /* <MLY> 09SEP94 CAM Wire EDM errors */
#define ERROR_CAM_BND_base      995000 /* <OBH> 02SEP93 CAM boundary errors */
#define ERROR_CAM_FBND_base     997500 /* <MLY> 10OCT94 CAM face boundary errors */
#define ERROR_CAM_PROC1_base    1000000 /* <Toon VanderKooi> library camsproc1 errors */

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
#define ERROR_MODL_COMPATIBILITY_base 1080500 /* <HGD> 2-May-2016 */
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
#define ERROR_TOOL_HOLDER_base 1287500 /* <rlm> 11-Jan-2005 HOLDER module */
#define ERROR_PMOP_base        1290000 /* <mab> 05-May-95 PMOP module */
#define ERROR_PMOP_fc_base     1291000 /* <mab> 08-Apr-98 PMOP_fc module */
#define ERROR_UDOP_base        1295000 /* <fdm> 10-May-95 UDOP module */
#define ERROR_MMCOP_base       1300000 /* <fdm> 10-May-95 MMCOP module */
#define ERROR_MEOP_base        1304000 /* <HCW> 19-Aug-98 MEOP module */
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
#define ERROR_DPMITP_base      1464000 /* <WLV> 24-May-2006 DPMITP module */
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
#define ERROR_REG_base         1555000 /* THayata  21-Oct-98 REG values */
#define ERROR_BLD_base         1560000 /* THayata  13-Jan-97 Change to BLD from UIO  */
#define ERROR_GCON_base        1565000 /* <RDH> 16-Mar-1995 GenConnect errors */
#define ERROR_STD_base         1570000 /* standard file interfaces, like STL */
#define ERROR_TURN_base        1575000 /* <JWA> 20-Oct-1998 TURN modules */
#define ERROR_FA_base          1580000 /* <PEH> 29-Jan-2001 Claim space for FA module -
                                                               next available 1585000*/
#define ERROR_INT_GRID_MAP_base \
                               1585000 /* <DML> 10-Feb-2004 INT GRID MAP module -
                                                               next available 1585010 */
#define ERROR_MODL_RUBB_base   1700000 /* <AGD> 11-Apr-1996 */
#define ERROR_POINT_SEL_base   1705000 /* <AGD> 11-Apr-1996 */
#define ERROR_CURVE_base       1710000 /* <AGD> 11-Apr-1996 */
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
#define ERROR_VHOST_base       1812500 /* <jdl> 02-Mar-1999 Add VHOST error codes */
#define ERROR_ASSOC_base       1815000 /* <jdl> 29-Jan-1997 Association Objects */
#define ERROR_ANNOT_base       1820000 /* <jdl> 29-Jan-1997 Annotation Objects */
#define ERROR_NOTE_base        1825000 /* <nra> 03-Feb-1997 Note objects */
#define ERROR_UF_GDT_base      1830000 /* <jdl> 05-Feb-1997 User Function for Tolerancing */
#define ERROR_EPLIB_base       1835000 /* <ATS> 02-Apr-1997 Part Library View module */
#define ERROR_PX_BREP_base     1838000 /* <MPS> 25-Jun-1998 Boundary Rep module */
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
#define ERROR_UF_WAVE_base     1915000 /* <MRA> 18-Aug-1997 User Function for Wave/Interpart
                                                                              extractions */
#define ERROR_SURF_REG_base    1920000 /* <TRF> 20-Oct-1997 SURF REG module*/
#define ERROR_UF_SURF_REG_base 1925000 /* <TRF> 20-Oct-1997 UF SURF REG module*/
#define ERROR_CAM_PREPRO_base  1930000 /* <MRP> 20-Oct-1997 UF_CAM_PREPRO module */
#define ERROR_SMSLOT_base      1935000 /* <WSN> 01-Dec-1997 SMSlot module */
#define ERROR_SMCUTOUT_base    1937000 /* <WSN> 03-Aug-1998 SMCutout module */
#define ERROR_ROUTE_TCL_base   1940000 /* <HHalladay> 29-Jan-1998 ROUTE TCL module */
#define ERROR_RLIST_base       1945000 /* <TWB> 23-Mar-1998 RLIST module errors*/
#define ERROR_KEYWORD_base     1950000 /* <SBP> 12-Feb-1998 KEYWORD module */
#define ERROR_FEAT_base        1955000 /* <SBP> 07-Apr-1998 FEAT module */
#define ERROR_SMBRIDGE_base    1960000 /* <DLB> 27-Jan-1998 SMBridge module */
#define ERROR_UI_LIB_base      1970000 /* <MW>  18-Mar-1998 UI_LIB (UG/Library UI) */
#define ERROR_MOM_INFO_base    1975000 /* <gbs> 17-Apr-98*/
#define ERROR_OPTM_base        1980000 /* <bcz> 30-jul-1997 CAM OPTM module */
#define ERROR_OPT_base         1981000 /* <bcz> 26-jan-1998 CAM OPT module, exclusive with
                                                                              OPTM module */
#define ERROR_MOM_DOC_base     1984000 /* <gsl> 20-Nov-1997 MOM */
#define ERROR_UI_ONT_base      1986000 /* <mw>  06-Jan-1998 UI_ONT (operation navigation tool) */
#define ERROR_UI_PARAM_base    1989000 /* <DWL> 09-Feb-1998 UI_PARAM */
#define ERROR_CAM_SESSION_base 1990000 /* <j_l> 20-Apr-1998 CAM_session */
#define ERROR_NCMCT_base       1991000 /* <gbs> 23-Sep-1998 NCMCT */
#define ERROR_UF_SO_base       1995000 /* <JBT> 28-May-1998 User Function for Smart Objects */

/*  <JLM> 04-Jan-99 The UG space resumes after the IMAN space below */

/*  <DRD> 11-Mar-1994

    Infomanager bases start at 2000000
*/

#define ERROR_WS_base          2000000 /* <MSF> 24-Feb-94 New Workspace */
#define ERROR_CALS_CM_base     2001000 /* <HMK> 16-Nov-94 IAI effectivity */
/*  <BJS> 18-Jun-96
    Only put codes here for IMAN modules.
*/

/*  <JLM> 04-Jan-99 The UG space resumes here: */
#define ERROR_UGW_base         3000000 /* <JLM> 04-Jan-1999 */
#define ERROR_UF_GFEM_base     3005000 /* <LLU> 29-Jan-1999 GFEM User Function */
#define ERROR_CAM_FILE_base    3010000 /* <fdm> 13-Oct-1998 */
#define ERROR_UI_WIZD_base     3015000 /* <obh> 27-Oct-1998 */

#define ERROR_SMSTRAIN_base    3020000 /* <DLB> 09-Mar-1999 SMSTRAIN Module */

/* <APB> 15-Feb-1999
  user function for clone and clone based import export
*/

#define ERROR_UF_CLONE_base    3025000

#define ERROR_DIEENG_base      3030000 /* Die Engineering Applications */
#define ERROR_VDAC_base        3035000 /* <EEC> 24-Mar-1999 VDA Checker */

#define ERROR_TBR_base         3045000

#define ERROR_SMBRACKET_base   3050000 /* <RRM> 05-Apr-1999 SMBRACKET module */
#define ERROR_SMRELIEF_base    3052000 /* <RRM> 03-May-1999 SMRELIEF module */

#define ERROR_SMBEND_base      3055000 /* <ARE> 20-Apr-1999 SMBEND Module */

/*  <RSS> 16-Mar-1999
    error bases for the alternates module
*/
#define ERROR_ALT_base         3060000

#define ERROR_SMPUNCH_base     3065000 /* <DCL> 18-Jun-1999 SMPUNCH Module */

#define ERROR_INTEROP_base     3070000

#define ERROR_UGINTEROP_base   3075000

#define ERROR_SMJOGGLE_base    3080000 /* <SAK> 24-Aug-1999 SMJOGGLE Module */

#define ERROR_XMLS_base        3085000 /* <JMF> 13-Sep-99 SYSS xml parser */

/********************************************************************************/
/* IMPORTANT: PLEASE NOTE THAT IF MERGED THIS BKM/QPL VALUE MUST NOT BE CHANGED */
/********************************************************************************/
#define ERROR_BKM_QPL_base     3090000 /* <JMF> 13-Sep-99 QPL/BKM/PV cross-product error codes */


#define ERROR_IM_base          3095000
#define ERROR_ANN_ORIGIN_base  3100000
#define ERROR_METAFORM_base    3105000 /* <DLB> 26-Sep-2002 Renamed as MetaForm Error-base */
#define ERROR_SMCORNER_base    3110000 /* <SYED> 17Apr2000 SMCorner */
#define ERROR_SMMACH_base      3115000 /* <SYED> 17Apr2000 SMMachinery Corner */
#define ERROR_COLOR_base       3120000 /* <TLH> 17Apr2000 COLOR module */
#define ERROR_ERROR_KBE_base   3125000 /* <FDM> 22-Feb-2000 */
#define ERROR_KFP_base         3130000 /* <RRM> 29-Jun-2000 pipeline module */
#define ERROR_UGSEBKM_base     3135000 /* <MR> 24-Aug-2000 for SolidEdge bookmark translation */
#define ERROR_SEQ_base_unused  3140000  //<alex> 05-Oct-2015 No longer used - feel free to reuse this one (but note that it only allows for 1000 errors!)
#define ERROR_PLM2NX_base      3141000 /* Since SEQ is not really used any more steal some off that */
#define ERROR_PVT_base         3145000 /* <AGD> 1-Sept-2000 Preview display */
#define ERROR_SMMBB_base       3150000 /* <A K Sheju, 31 Jun 2000  */
#define ERROR_WELD_SYM_base    3155000 /* <SKL> 19-Jun-2000 Weld Symbols module */
#define ERROR_KFF_base         3160000 /* <Rami Reuveni> */
#define ERROR_BODYDES_base     3165000 /* <Rami Reuveni> */
#define ERROR_GDT_FILE_base    3170000 /* <GD> 18-oct-2000 for GDT FILE module */
#define ERROR_LIM_FITS_base    3175000 /* <GD> 18-Oct-2000 for Limits and Fits module */
#define ERROR_SMMITER_base     3180000 /* <SAJ> 07Dec2000 SMMiter Feature */
#define ERROR_KMC_base         3185000 /* <RG> 01-Sep-2000 KMC module */
#define ERROR_DFO_base         3190000 /* <FG>  07-Dec-2000 Direct Modeling */
#define ERROR_MOTO_base        3195000 /* <GDS> 10-Jan-2000 Assembly Motion Manager */
#define ERROR_NXKINEO_base     3198000 /* <AW> 26-Feb-2006 NXKineo Path Planning */
#define ERROR_FABFLAT_base     3200000 /* <MXU>  16-Jan-2001 Fabric Flat Pattern */
#define ERROR_CLASH_base       3205000 /* <SP>  30-Jan-2001 Dynamic Collision Detection */
#define ERROR_MATING_base      3210000 /* <SP>  30-Jan-2001 Dynamic Mating */
#define ERROR_SV_base          3215000 /* <Yakove Dayan>  17-Jan-2001 simulation engine */
#define ERROR_CAM_SIM_base     3220000 /* <Yakove Dayan>  17-Jan-2001 machine tool simulation */
#define ERROR_HMOP_base        3225000 /* <LUF>  29-Jan-2001 Hole-making operation */
#define ERROR_VISUALIZE_base   3230000 /* <DK> 23-Jan-2001 UI_Visualize */
#define ERROR_SMSP_base        3235000 /* <JW> 26-Jan-2001 Smart models */
#define ERROR_CLIPBOARD_base   3240000 /* <JMF> 11-Feb-2001 CLIPBOARD module error for
                                                           UG object cut/copy/paste */
#define ERROR_TRUSHAPE_base    3245000 /* <jrr> */
#define ERROR_PIPNAV_base      3250000 /* <WSNiblack 28Feb01> Part in Process Navigator */
#define ERROR_CAM_CTR_base     3255000 /* <TEH> 26-Mar-2001 CAM CTR module */
#define ERROR_MQC_base         3260000 /* <SCH> 25-Jun-2001 Model Quality check module */
#define ERROR_UF_MQC_base      3265000 /* <SCH> 25-Jun-2001 MQC UF module */
#define ERROR_FUSION_base      3270000 /* <CAN> 21-Aug-2001 FUSION module */
#define ERROR_FLEX_base        3275000 /* <A Dylla> 18-Jul-2001 Flex module */
#define ERROR_TASK_ENV_base    3280000 /* <DPF> 29-Jun-2001 Task Environments */
#define ERROR_TRANCAT_base     3285000 /* <WSNiblack 08-Oct-2001> CATIA       */
#define ERROR_GS_POPUP_base    3290000 /* <GD>  11-Oct-2001 Obj.Specific popup*/
#define ERROR_NCHSC_base       3295000 /* <DK> 21-Sep-2001 NCHSC module */
#define ERROR_SMSPUNCH_base    3300000 /* <AJS 15-Oct-2001>  */
#define ERROR_ANIM_EXP_base    3305000 /* <RG> 08-Oct-2001 ANIM_EXP module */
#define ERROR_MOT_ANLPP_base   3310000 /* <RG> 24-oct-2001 MOT_ANLPP module */
#define ERROR_QAF_base         3315000 /* <RSS> 21-Aug-2001 */
#define ERROR_NCE3D_base       3320000 /* <MF>  18-Nov-2001 nce3d library */
#define ERROR_COLLAB_base      3325000 /* <SDK> 11-Dec-2001 Add UG/Collaborate */
#define ERROR_SMRT_MODEL_base  3330000 /* <jdl> 12-Nov-2001 */
#define ERROR_WNT_base         3335000 /* <Pengk 7-Dec-2001> waveint library for Wave diagram*/
#define ERROR_UGXML_base       3340000 /* <JLM> 10-Dec-2001 */
#define ERROR_UI_PREV_base     3345000 /* <TJGC> 16-Jan-2002 */
#define ERROR_SMD_BEND_base    3350000 /* <DLB> 11-Jan-2002 */
#define ERROR_IDEAS_base       3355000 /* <AW> 04-Feb-2002 */
#define ERROR_PAL_base         3360000 /* <JMF> 31-Jan-2002 */
#define ERROR_ANN_USRSYM_base  3365000 /* <jdl> 19-Feb-2002 */
#define ERROR_SSP_base         3370000 /* <FDM> 25-Feb-2002 */
#define ERROR_SMPROFLNG_base   3375000 /* <RRM> 12-Mar-2002 */
#define ERROR_INSET_base       3380000 /* <KPS> 28-Mar-2002 */
#define ERROR_KF_CAM_FN_base   3385000 /* <FDM> 10-Apr-2002 */
#define ERROR_SMD_PK_base      3390000 /* <DLB> 26-Sep-2002 */
#define ERROR_IDIXML_base      3395000 /* <jdl> 13-Sep-2002 */
#define ERROR_ANN_IMAGE_base   3400000 /* <SPaladini> 24-Oct-2002 */
#define ERROR_IMAGE_IO_base    3405000 /* <SPaladini> 24-Oct-2002 */
#define ERROR_IGES_base        3410000 /* <WSNiblack> 11-Nov-2002 */
#define ERROR_STEP_base        3415000 /* <WSNiblack> 11-Nov-2002 */
#define ERROR_DXFDWG_base      3420000 /* <WSNiblack> 11-Nov-2002 */
#define ERROR_UGTO2D_base      3425000 /* <WSNiblack> 11-Nov-2002 */
#define ERROR_DSTAPER_base     3430000 /* <SVD> 23-Nov-2002 */
#define ERROR_SPSD_base        3435000 /* <SSrivastava> 09-Dec-2002 */
#define ERROR_WIZSTR_base      3440000 /* <SSrivastava> 09-Dec-2002 */
#define ERROR_UNITSCONV_base   3445000 /* <ADylla 12-Dec-2002 */
#define ERROR_CONFG_base       3450000 /* <MS> 14-Jan-2003 */
#define ERROR_NX2D_base        3455000 /* <jdl> 30-Jul-2002 */
#define ERROR_RIP_EDGE_base    3460000 /* <shahk> 26-Jan-2002 */
#define ERROR_GROUP_base       3465000 /* <JMF> 15-Nov-2002 */
#define ERROR_WIZARD_base      3470000 /* <Ken Snyder> 05-Jul-2003 */
#define ERROR_DMM_base         3475000 /* <jdl> 06-Feb-2003 */
#define ERROR_IDEAS_MIG_base   3480000 /* <RG> 11-Feb-2002 */
#define ERROR_IDEAS_FEAT_base  3485000 /* <RG> 11-Feb-2002 */
#define ERROR_ADVFEM_base      3490000 /* <Mike Walsh> 06-Mar-2003 */
#define ERROR_KLINK_base       3495000 /* <jdl> 22-Apr-2003 */
#define ERROR_UF_TABNOT_base   3500000 /* <ale> 23-Apr-2003 */
#define ERROR_TREX_base        3505000 /* <Tom Thompson 11-Mar-2003> */
#define ERROR_MSEQ_base        3510000 /* <MEL> 30-Jul-2003 */
#define ERROR_LAYER_base       3515000 /* <VL> 20-Mar-2003 */
#define ERROR_JA_base          3520000 /* <VL> 21-Mar-2003 */
#define ERROR_DELETE_base      3525000 /* <VL> 25-Mar-2003 */
#define ERROR_UF_MOTION_base   3530000 /* <Matt Staten> 05-Sep-2003 Mot.Scen UF */
#define ERROR_CAM_CLV_base     3535000 /* <David Lettis 01-Oct-2003> */
#define ERROR_CAE_ABS_base     3540000 /* <Vasa M. Reddy 18-Nov-2003 CAE abstract> */
#define ERROR_ACUT_base        3545000 /* <ADylla> Nov-7-2003  */
#define ERROR_PMAN_base        3550000 /* <Pavramenko> 14-Nov-2003 */
#define ERROR_CGME_base        3555000 /* <WIL 21-Nov-2003> */
#define ERROR_CGMI_base        3560000 /* <WIL 21-Nov-2003> */
#define ERROR_CGM_base         3565000 /* <WIL 29-Dec-2003> */
#define ERROR_IPWDSP_base      3570000 /* <Dieter Krach> 03-Jan-2004 */
#define ERROR_WIZCAM_base      3575000 /* <Markus Wilmsen> 12-Feb-2004> */
#define ERROR_DRAW_BASE        3580000 /* <PTO 11-FEB-2004>   */
#define ERROR_VIEW_base        3585000 /* <Guangchao Dong> 25-Jan-2004 */
#define ERROR_SDI_base         3590000 /* <KDH 24-Feb-2004> */
#define ERROR_CAM_XTP_base     3595000 /* <Olaf Kaltz> 02-Feb-2004 */
#define ERROR_LDR_base         3600000 /* <BJS> 26-Mar-2004 */
#define ERROR_LAYOUT_base      3605000 /* <RDB> 19-Apr-2004 */
#define ERROR_CSF_base         3610000 /* <Mandar Mahajani> 12-Apr-2004 */
#define ERROR_JAM_base         3615000 /* <BJS> 04-Jun-2004 */
#define ERROR_BLEND_base       3620000 /* <Sunil Bapat> 27-May-2004 */
#define ERROR_HM_base          3625000 /* <Lingyun Lu 02-Dec-2003> */
#define ERROR_FILLWELD_base    3630000 /* <Tom Thompson 29-Jun-2004> */
#define ERROR_MW_base          3635000 /* <Chee-Keong Chong 19-Aug-2004 Moldwizard> */
#define ERROR_VARSWEEP_base    3640000 /* <Sameer Parasnis 28-Sep-2004> */
#define ERROR_BKMPLM_base      3645000 /* <Drew Dylla Nov 24-Nov-2004> */
#define ERROR_SPACEMAP_base    3650000 /* <Srinivasa Reddy 01-Dec-2004> */
#define ERROR_PMI_base         3655000 /* <Shrinivas Soman 12-Dec-2004> */
#define ERROR_GENPOS_base      3660000 /* <MS>  04-Jan-2005 */
#define ERROR_COMPOS_base      3665000 /* <MS>  04-Jan-2005 */
#define ERROR_TLINE_base       3670000 /* <Gary Smethers 08-Dec-2004> */
#define ERROR_SBSM_base        3675000 /* <N. Gopi Krishna 13-Dec-2004> */
#define ERROR_PGS_base         3680000 /* <Pierre Sheehy 17-Jan-2005> */
#define ERROR_SHIP_base        3685000 /* <Ameer Syed> 18-Jan-2005 */
#define ERROR_AEROSM_base      3690000 /* <Rishi R Mishra> 03-Feb-2005 */
#define ERROR_FIELD_base       3695000 /* <Ken Mraz> 09-Feb-2005 */
#define ERROR_OTPUB_base       3700000 /* <Nader Askari> 05-Mar-2005 */
#define ERROR_LIGHT_base       3705000 /* <RDB> 07-Mar-2005 */
#define ERROR_SPDSHT_base      3710000 /* <Bob Zhang 14-Mar-2005 Spreadsheet> */
#define ERROR_TRIMBODY_base    3715000 /* <Ameer Syed> 18-Jan-2005 */
#define ERROR_UICOMP_PMI_base  3720000 /* <jdl> 29-Mar-2005 */
#define ERROR_SPUNOUTLINE_base 3725000 /* <J. Wartmann> 27-May-2005 */
#define ERROR_RASTER_IMAGE_base \
                               3730000 /* <RDB> 01-May-2005 */
#define ERROR_NXPOS_base       3735000 /* <MS>  28-Jun-2005 */
#define ERROR_AIWEB_base       3740000 /* <MR>  14-Aug-2005 */
#define ERROR_XYPLOT_base      3745000 /* <Eric Fan> 05-Aug-2005 */
#define ERROR_TRANPROE_base    3750000 /* <Anil Suryawanshi> 31-Aug-2005 */
#define ERROR_TRANCATV5_base   3755000 /* <Sterling Hyland>  31-Aug-2005 */
#define ERROR_BIW_base         3760000 /* <Jerry Hu> 08-Sep-2005 */
#define ERROR_PROPERTY_base    3765000 /* <Tracy Rees> Jan-7-2006*/
#define ERROR_VD_base          3770000 /* <Shufeng Chen> 23-Feb-2006 */
#define ERROR_CAM_BUILDER_base 3775000 /* <Markus Wilmsen> 10-Apr-2006 */
#define ERROR_PIO_base         3780000 /* <Ed Jagodzinski> 11-Apr-2006 */
#define ERROR_PATHPLAN_base    3785000 /* <AW> 26-Feb-2006  path planner */
#define ERROR_STAMPING_base    3790000 /* <Glaser> 18-Apr-2006 */
#define ERROR_System_Threading_base \
                               3795000 /* <BJS> 3-May-2006 for classes in System::Threading */
#define ERROR_OP2_base         3800000 /* <Jeff Ma> 09-May-2006 */
#define ERROR_IDEASUNV_base    3805000 /* <Kevin Morgan> 30-May-2006 */
#define ERROR_SHOWHIDE_base    3810000 /* <RSS> Show Hide dialog errors */
#define ERROR_FILENEW_base     3815000 /* <RSS> 16-Jun-2006 */
#define ERROR_CAMERA_base      3820000 /* <RDB> 17-Jun-2006 */
#define ERROR_RA_base          3825000 /* <Paul Benson> 30-Jun-2006 */
#define ERROR_TRIMSHEET_base   3830000 /* <Yogesh Kulkarni> 12-Jul-2006 trimsheet_error_codes.h */
#define ERROR_VOXELMODEL_base  3835000 /* <Bob Zhang> 12-Jul-2006 VoxelModel*/
#define ERROR_TOOLING_base     3840000 /* <Hongfan Jiang> 11-Jul-2006 libtoolingutils */
#define ERROR_NXSTYLER_base    3845000 /* <Abhishek> 30-Jul-2006 */
#define ERROR_PKP_base         3850000 /* <AVS> PKPlus error codes */
#define ERROR_Facet_JT_base    3855000 // <RG> 14-Aug-2006 Facet::JT error codes
#define ERROR_KRU_base         3860000 /* <Jianyong Wen> 12-Jun-2006 */

#define ERROR_AUTOPOPULATE_base \
                               3865000 /* <Steve Kunkee> 26-Apr-2006 */
#define ERROR_SIA_base         3870000 /* <Nilesh Joshi>  10-Nov-2006*/

#define ERROR_CAMNCM_base      3875000 /* <Juergen Wartmann> 06-Nov-2006 */
#define ERROR_CAM_DIAG_base    3880000 /* <Tim Fithian> 05-Jan-2007 */
#define ERROR_XFORM_base       3885000 /* <AdrianB> 30-Apr-2007 */
#define ERROR_PDQC_base        3890000 /* <SD Tang> 06-Jun-2007 */
#define ERROR_DYNAMIC_SECTION_base \
                               3895000 /* <SRK> 14-Jun-2007 */
#define ERROR_DYNAMIC_SECTIONCUT_base \
                               3900000 /* <SRK> 27-Jul-2007 */
#define ERROR_TCCIF_base       3905000 /* <Yunfei Wu> 20-Aug-2007 */
#define ERROR_SHAPESEARCH_base 3910000 /* <Bob Zhang> 20-Jun-2007 */
#define ERROR_VTK_base         3915000 /* <Rami Reuveni> 12-Jun-2007 */
#define ERROR_SPLITBODY_base   3920000 /* <ZGU> 20-Aug-2007 */
#define ERROR_BOOLEANTOOL_base 3925000 /* <ZGU> 20-Aug-2007 */
#define ERROR_ISSUE_base       3930000 /* <Yunfei Wu> 05-Sep-2007 */
#define ERROR_CAMSFTR_base     3935000 /* <Hans Scheerder> 17-Sep-2007 */
#define ERROR_PHYMAT_base      3940000 /* <witcpale> 10-Oct-2007 phymat module errors*/
#define ERROR_PROPTABLE_base   3945000 /* <witcpale> 10-Oct-2007 property table errors*/
#define ERROR_MOVIE_CREATION_base 3950000  /* <ak> Movie creation */
#define ERROR_UNITS_base          3955000  /* <golfisd> 29-Aug-2008 units errors */
#define ERROR_CAEPOST_base     3960000     /*agarwala 4 dec-2008 caepost errors */
#define ERROR_REFSET_ANALYSIS_base 3965000 /* <pandeyon> 09-Feb-2009 Refset Analysis errors*/
#define ERROR_FRO_base         3970000 /* <armbrust> 05-Mar-2009 feed rate optimization errors */
#define ERROR_SIM_JA_base      3975000 /* <krach> 13-May-2009 SIM JA errors */
#define ERROR_CMMINSPECT_base  3980000 /* <gigear> 23-Jun-2009 CMM Inspection errors */
#define ERROR_COND_FORMAT_base 4000000 //Conditional Formatting
#define ERROR_CGP_base         4005000 /* <longwint> 02-Aug-2009 */
#define ERROR_VIRTUAL_CURVE_base 4010000 /* hartliep 22-Jul-2009 virtual curve errors */
#define ERROR_MODLMATH_base    4015000 /* <John Fisher> 17-Aug-2009 */
#define ERROR_TRIMBODY2_base   4020000    /* <Kishore Nimmagadda> 08-Jul-2009 */
#define ERROR_ICS_base         4025000 /*<rajhans> Interactive Curve Selection errors.*/
#define ERROR_DURABILITY_base  4030000 /*Mukund Rajamony/MAYA CaeSim_Durability_Errors.h */
#define ERROR_MDPHYS_base      4035000 /*<Jack Yu> 10-Jul-2009 Added ERROR_MDPHYS_base*/
#define ERROR_MDFT_base        4040000 /*<Michael Li> 10-May-2009 Added ERROR_MDFT_base*/
#define ERROR_LIBRARY_CALLBACK_base        4045000 /*<Jay Desai> 29-Jun-2010 Added for library callback module*/
#define ERROR_Drafting_Automation_base \
                               4050000 // <darrow> 24-May-2010 Added
#define ERROR_Memory_base      4055000 /* <SRK> 16-Aug-2010 */
#define ERROR_CAMVM_BASE       4060000
#define ERROR_OIF_base         4065000 // <subhedar 08-Dec-2010> Object Identification Framework error codes
#define ERROR_PENETRATION_base 4070000 /* <Anurag Anurag> 23-Mar-2011 Added for Penetration Management project KDA156008 */
#define ERROR_DCM3_base        4075000 //  <Michael Abbott> 10-Aug-2011 Errors for the DCM3 library interface
#define ERROR_Isolate_base     4080000 // <gulhane> 11-Nov-2011 Errors for Isolate Feature
#define ERROR_DataManagement_Application_base 4085000 //  Errors for the DataManagement::Application module <austin> 02-Dec-2011 
#define ERROR_BOOLEAN_base     4090000  // Boolean feature/component errors
#define ERROR_SmartVolumeProfile_base 4095000 // Kishore Nimmagadda - DES11064 - Open Profile Smart Volume project
#define ERROR_CONFIGURATION_SYSTEM_base 4100000  /*<Krushnan Mahalingam> 28-May-2012 Added for Configuration System module*/
#define ERROR_MANIFEST_READER_SYSTEM_base 4105000  /*<Jitender Kumar> 25-June-2012 Added for Manifest Reader module*/
#define ERROR_NXSTARTUPMANAGER_SYSTEM_base 4110000  /*<Prashant Sisodiya> 14-Aug-2012 Added for NXStartup Manager module*/
#define ERROR_ORDER_CREATION_base    4115000 // <kumarash> 30-Oct-2012: Added for reordering functionality 
#define ERROR_SWEPTVOLUME_base 4120000       //Huang He DES12040 Swept Volume project
#define ERROR_PACKAGE_MANAGER_base   4125000 // /*<Krushnan Mahalingam> 17-Jan-2013 Added for Packaging module*/
#define ERROR_PART_MIGRATION_base    4130000 // <Umar> 11-Jan-2013: Added for part migration  
#define ERROR_LASERTEACHMODE_base    4135000 // Yuan Liu Laser Teachmode
#define ERROR_SUBOP_COMMAND_base     4140000 // <Tom Hayes> 08-Feb-2013 cammill9021 User Assisted Workflow project
#define ERROR_DIAGRAMMING_base       4145000 // <Haifeng Xu> 26-Sep-2013 Added ERROR_DIAGRAMMING_base*/
#define ERROR_PART_IMPORTER_base     4150000 // <x_shindm> 03-Oct-2013: Added for part importer module.
#define ERROR_SC03_base              4155000 // <Troy Shagena> 09-Dec-2013 Added ERROR_SC03_base*/
#define ERROR_MIRRORCOPY_base        4160000 // <Andy Gong> Added ERROR_MIRRORCOPY_base for DES13023 & KDA156047
#define ERROR_SAMCEF_base            4165000 // <Frederic Bair> 06-Feb-2014 Added ERROR_SAMCEF_base*/
#define ERROR_LAYOUT2D_BASE          4170000 // <Maggie Li/Maya> 18-Mar-2013 Added for layout2d module 
#define ERROR_UserDefinedTemplate_base 4175000 //<sridhara> 13-Jan-2014 For User-Defined-Template functionality
#define ERROR_PM_base                  4180000 // <borse> 12-Mar-2014 For Part modules
#define ERROR_BREPFACET_base         4185000 // <zgu> 13-Jan-2014  Added ERROR_BREPFACET_base
#define ERROR_MARKUP_base            4190000 // <zhengxj> 26-Jan-2014 Added ERROR_MARKUP_base
#define ERROR_ADVPB_base             4195000 // <Wilson Kurniawan> Added for advanced postbuilder module
#define ERROR_ROUT_MECH_base         4200000 // <Sarang.Baheti> added for Routing Mechanical
#define ERROR_ASSY_PLACEMENT_base    4205000 // <Ambar.Soman 12-Dec-2014> Added for Assy Placement
#define ERROR_NXOPENXML_base         4210000 // <Jimmy Pan 28-Feb-2015> added for NX openxml module
#define ERROR_NXREPORTFW_base        4215000 // <jimmy Pan 28-Feb-2015> added for NX template based report framework
#define ERROR_CAEREPORT_base         4220000 // <jimmy Pan 28-Feb-2015> added for CAE report framework
#define ERROR_SYSNOISEDATABASE_base  4225000 // <Costin Nila> 10-Mar-2015 Added ERROR_SYSNOISEDATABASE_base*/
#define ERROR_ROUTING_CORE_base      4230000 // <sena> 09-Mar-2015 Added for Routing Core
#define ERROR_SH_LWKS2_base          4235000 // <Greg Fenner> Added for high end rendering
#define ERROR_MTU_base               4240000 // <Paul Wilbrandt> Added for Machine Tool Utility module
#define ERROR_INSTALL_base           4245000 // <Smit Agrawal 13-Mar-2015> Added for Install Errors
#define ERROR_DRAWTO3D_base          4250000 // <Janardan Gaikwad> Added for Drawing to 3D functionality
#define ERROR_ACIS_base              4255000 // <khodke 17-Apr-2015> Added for ACIS import export
#define ERROR_WORK_INSTRUCTION_base  4260000 // <David Cheung> cmm10021 Added for work instructions.
#define ERROR_SYSNOISEBEM_base       4265000 // <Costin Nila> 25-Mar-2015 Added ERROR_SYSNOISEBEM_base*/
#define ERROR_FEATURESERVICE_base    4270000 // <Hese Nitin> 27-May-2015 Added ERROR_FEATURESERVICE_base*/
#define ERROR_POINT_CLOUD_base       4275000 // <Jackie Zhang 01-Jun-2015> Added for Point Cloud Errors
#define ERROR_MFG_MLP_base           4280000 // <Michiel Popma> 25-Jun-2015 cam11036 Added for Machining Line Planner errors
#define ERROR_ROUT_JA_MECH_base      4285000 // <Sourabh.Agrawal> added for RoutingJA Mechanical
#define ERROR_PLAS_base              4290000 // <Billy Wang> 25-Sep-2015 added for PLAS library
#define ERROR_FTK_base               4295000 // <Fredo Yang> 11-Nov-2015 added for FTK module
#define ERROR_MFG_AM_base            4300000 // <Hans Scheerder> 17-Mar-2016 CAM11097 Additive Manufacturing
#define ERROR_INTERPOL_base          4305000 // <Andrey Chernolutskiy> 11-May-2016
#define ERROR_IMW_base               4310000 // <Nancy O'Brien-Bodo> 29-Apr-2016 added for Imageware integration
#define ERROR_CAM_SERVICES_base      4315000 // <Arto Saari> 12-Jul-2016 CAM11036 Added for CAM services module
#define ERROR_CAM_TEMP_DIAG_base     4320000 // <Chunsik Yi> 08-Feb-2017 PR8261089 Added for CAM temporary diagnostics
#define ERROR_GFXBUILDER_base        4325000 // <Dirk Brennecke> Added for Graphics Builder

/* The next code is the largest expected error code ( = largest base + 4999 ),
 * so PLEASE UPDATE IT IF YOU ADD ANOTHER ERROR BASE !
 */
#define ERROR_max_error_code   4329999


/* <gechung> 19-Jun-2008 
 * Added ERROR_Teamcenter_base & ERROR_max_Tc_error_code for offsetted errors 
 * returned from Teamcenter. The same #define exists in DataManagement_Errors.h. 
 * At present, Teamcenter has up to 1000000 error numbers. We intentionally not 
 * bumping up the ERROR_max_error_code below to avoid perturbing processing
 * of normal NX errors.
 */
#define ERROR_Teamcenter_base    100000000
#define ERROR_max_Tc_error_code  101000000

/*
  Error application are error which assign to external application
*/
#define ERROR_aplication_base         70000000
#define ERROR_AUTOMATION_DESIGN_base  70000000
#define ERROR_LINE_DESIGN_base        70050000
#define ERROR_PID_base                70055000
#define ERROR_max_AP_error_code       80000000



#endif /* ERROR_BASES_H_INCLUDED */


