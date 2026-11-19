
/*******************************************************************************

        Copyright (c) 1999 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved

******************************************************************************


File description:

These are the types required for the Open C API interface to the NX user
interface.  The descriptions and typdef's here will only be usable by Internal
Open API programs.

******************************************************************************/

#ifndef UF_UI_TYPES_H_INCLUDED
#define UF_UI_TYPES_H_INCLUDED

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

#include <uf_part_types.h>

/* Data structure that controls standard button configuration on message
   dialogs */
struct UF_UI_message_buttons_s{
    logical button1;              /* flag that specifies whether or not button1
                                     (OK) is required */
    logical button2;              /* flag that specifies whether or not button2
                                     (BACK) is required */
    logical button3;              /* flag that specifies whether or not button3
                                     (CANCEL) is required */
    char    *label1;              /* label for button1 (OK by default) */
    char    *label2;              /* label for button2 (BACK by default) */
    char    *label3;              /* label for button3 (CANCEL by default) */
    int     response1;            /* Response value for button1 */
    int     response2;            /* Response value for button2 */
    int     response3;            /* Response value for button3 */
};
typedef struct UF_UI_message_buttons_s UF_UI_message_buttons_t, *UF_UI_message_buttons_p_t;

typedef enum {
    UF_UI_MESSAGE_ERROR,
    UF_UI_MESSAGE_WARNING,
    UF_UI_MESSAGE_INFORMATION,
    UF_UI_MESSAGE_QUESTION
} UF_UI_MESSAGE_DIALOG_TYPE;



/***************************************************************************
User responses by selecting objects (UF_UI_PICK_RESPONS) or clicking the
button which is labeled ok, cancel, back, apply or help.
****************************************************************************/

#define UF_UI_PICK_RESPONSE    1  /* User response was a selection of objects.*/
#define UF_UI_OK               2  /* OK button was selected. */
#define UF_UI_CANCEL           3  /* Cancel button was selected. */
#define UF_UI_BACK             4  /* Back button was selected. */
#define UF_UI_APPLY            5  /* Apply button was selected. */
#define UF_UI_HELP             6  /* Help button was selected. */
#define UF_UI_OBJECT_SELECTED  7  /* Object was selected. */
#define UF_UI_OBJECT_SELECTED_BY_NAME 8 /* Object was selected by name. */
#define UF_UI_CB_TERMINATE     9  /* Callback routine has terminated. */

/* Constants for saving state info with custom menu */

#ifndef UF_UI_FROM_CUSTOM
#define UF_UI_NO_LOCK          (0)
#define UF_UI_FROM_CUSTOM      (1)
#endif


#define UF_UI_SUCCESS            0
#define UF_UI_FAILURE            1


#define UF_UI_LOCK               2
#define UF_UI_UNLOCK             3
#define UF_UI_ERROR              4
#define UF_UI_LOCK_SET           5
#define UF_UI_LOCK_EXISTS        6
#define UF_UI_LOCK_ERROR         7
#define UF_UI_UNLOCK_SET         8
#define UF_UI_NO_LOCK_EXISTED    9
#define UF_UI_UNLOCK_ERROR       10
#define UF_UI_LOCK_UNNECESSARY   11


typedef int (*UF_UI_change_state_fn_t) (int new_state /* <I> */);

/* Constants for selection scope */

#define UF_UI_SEL_SCOPE_NO_CHANGE        0
#define UF_UI_SEL_SCOPE_WORK_PART        1  /* Allows you to select only objects
                                               which belong to the work part.
                                               This includes immediate
                                               components of the work part. If
                                               you select an object occurrence,
                                               the prototype is returned.  */
#define UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY  3  /* Allows you to select any object
                                               or object occurrence in the
                                               assembly. No scope restrictions
                                               are applied.  */
#define UF_UI_SEL_SCOPE_WORK_PART_AND_OCC 4 /* Allows you to select objects
                                               which belong to the work part or
                                               its subassembly. If you select
                                               an object occurrence, the
                                               prototype is returned.  */
#define UF_UI_SEL_SCOPE_WORK_PART_AND_WP_OCC 5 /* Allows you to select objects
                                               which belong to the work part or
                                               its subassembly. If you select
                                               an object occurrence, the
                                               occurrence of the work part is returned.  */

/* selection mask actions to be used as input to
 UF_UI_set_sel_mask
 */
enum UF_UI_sel_mask_action_e{
    UF_UI_SEL_MASK_ENABLE_ALL,
    UF_UI_SEL_MASK_ENABLE_SPECIFIC,
    UF_UI_SEL_MASK_DISABLE_SPECIFIC,
    UF_UI_SEL_MASK_CLEAR_AND_ENABLE_SPECIFIC,
    UF_UI_SEL_MASK_ALL_AND_DISABLE_SPECIFIC,
    UF_UI_SEL_MASK_COUNT  /* Do not use - not a valid input as a selection mask action */
} ;

typedef enum UF_UI_sel_mask_action_e UF_UI_sel_mask_action_t;

/* selection types to be used as input to UF_UI_set_sel_type */
#define UF_UI_SEL_TYPE_INACTIVE_SELECTION  (0)
#define UF_UI_SEL_TYPE_SINGLE_POSITION     (1 << 0)
#define UF_UI_SEL_TYPE_RECTANGLE_POSITION  (1 << 1)
#define UF_UI_SEL_TYPE_SINGLE_SELECTION    (1 << 2)
#define UF_UI_SEL_TYPE_SINGLE_DESELECTION  (1 << 7)
#define UF_UI_SEL_TYPE_ROBUST_SELECTION    (1 << 5)
/* Note: ROBUST_SELECTION includes single select, single deselect,
 * rectangle select, rectangle deselect, reselect last and chaining */

/* selection descriptors to be used with UF_UI_ask_sel_descriptor */
#define UF_UI_SEL_DESC_SELECTION          (1 << 0)
#define UF_UI_SEL_DESC_DESELECTION        (1 << 1)
#define UF_UI_SEL_DESC_RESELECTION        (1 << 2)
#define UF_UI_SEL_DESC_SINGLE             (1 << 3)
#define UF_UI_SEL_DESC_MULTIPLE           (1 << 4)
#define UF_UI_SEL_DESC_SINGLE_POSITION    (1 << 5)
#define UF_UI_SEL_DESC_RECTANGLE_POSITION (1 << 6)
#define UF_UI_SEL_DESC_NAME_SELECTION     (1 << 7)
#define UF_UI_SEL_DESC_RECTANGLE          (1 << 8)


#define UF_UI_SEL_FAILURE 0
#define UF_UI_SEL_SUCCESS 1

#define UF_UI_CB_EXIT_DIALOG 1
#define UF_UI_CB_CONTINUE_DIALOG 0

#define UF_UI_CB_CONTINUE_SWITCH 0
#define UF_UI_CB_REJECT_SWITCH   1

#define UF_UI_SEL_REJECT 0
#define UF_UI_SEL_ACCEPT 1


/* User Tool routine defines */
#define UF_UI_HIDE  FALSE
#define UF_UI_SHOW  TRUE

/* Non-Modal Message Dialog's positioning methods */
#define UF_UI_MSG_POS_CURSOR       0
#define UF_UI_MSG_POS_CASCADE      1
#define UF_UI_MSG_POS_BOTTOM_RIGHT 2
#define UF_UI_MSG_POS_TOP_LEFT     3
#define UF_UI_MSG_POS_DA1          4
#define UF_UI_MSG_POS_DA2          5

/* Temporary display flag setting for UF_UI_select_conehead */
#define UF_UI_DISP_NONE       0
#define UF_UI_DISP_SELECTED   1
#define UF_UI_DISP_ALL        2

/* Temporary display flag setting for UF_UI_specify_vector */
#define UF_UI_DISP_NO_VECTOR       0
#define UF_UI_DISP_TEMP_VECTOR     1

/* Mode settings for UF_UI_specify_vector
 * (Note: see unsupported modes below) */
#define UF_UI_TWO_POINTS           2
#define UF_UI_TANGENT_TO_CURVE     3
#define UF_UI_XC_AXIS              7
#define UF_UI_NEGATIVE_XC_AXIS     8
#define UF_UI_YC_AXIS              9
#define UF_UI_NEGATIVE_YC_AXIS     10
#define UF_UI_ZC_AXIS              11
#define UF_UI_NEGATIVE_ZC_AXIS     12
#define UF_UI_INFERRED             13
#define UF_UI_AT_ANGLE             14
#define UF_UI_EDGE_CURVE           15
#define UF_UI_FACE_NORMAL          16
#define UF_UI_DATUM_PLANE          17
#define UF_UI_DATUM_AXIS           18

/* Mode settings for the old UF_UI_specify_vector subfunction.
 * These options are no longer supported in their orignal form.
 * When input, the option will be mapped to the closest mode in
 * the new vector subfunction. Output mode will always be from
 * current modes as listed above */
#define UF_UI_ENABLE_OK_NO_DEFAULT (-1)
#define UF_UI_NO_DEFAULT           0
#define UF_UI_LINE_ENDPOINT        1
#define UF_UI_IJK_COMPONENTS       4
#define UF_UI_SPHERICAL_COORDS     5
#define UF_UI_COORD_SYSTEM_AXIS    6


/* Mode settings for UF_UI_ask_iw_decimal_places */
#define UF_UI_SYSTEM_DECIMAL_PLACES  0
#define UF_UI_USER_DECIMAL_PLACES    1

/* Units settings for UF_UI_ask_info_units */
#define UF_UI_POUNDS_INCHES      0
#define UF_UI_POUNDS_FEET        1
#define UF_UI_GRAMS_MILLIMETERS  2
#define UF_UI_GRAMS_CENTIMETERS  3
#define UF_UI_KILOS_METERS       4
#define UF_UI_KILOS_MILLIMETERS  5

/* Constants for FSD directory filter access

*/
enum UF_UI_dialog_filter_id_e{
    UF_UI_EXPORT_PART_FLTR,      /* Specifies *.prt */
    UF_UI_EXPORT_PARASOLID_FLTR, /* Specifies *.xmt_txt */
    UF_UI_EXPORT_CGM_FLTR,       /* Specifies *.cgm */
    UF_UI_EXPORT_DIAGRAM_FLTR,   /* Specifies *.* */
    UF_UI_EXPORT_RPT_FLTR,       /* Specifies *.stl */
    UF_UI_EXPORT_INV_FLTR,       /* Specifies *.iv */
    UF_UI_SYM_FLTR,              /* Specifies *.sym */
    UF_UI_IMPORT_PART_FLTR,      /* Specifies *.prt */
    UF_UI_IMPORT_PARASOLID_FLTR, /* Specifies *.xmt_txt */
    UF_UI_IMPORT_CGM_FLTR,       /* Specifies *.cgm */
    UF_UI_IMPORT_MARKUP_FLTR,    /* Specifies *.mkp */
    UF_UI_IMPORT_UDF_FLTR,       /* Specifies *.udf */
    UF_UI_PART_NEW_FLTR,         /* Specifies *.prt */
    UF_UI_PART_OPEN_FLTR,        /* Specifies *.prt */
    UF_UI_PART_OPEN_VIEWER_FLTR, /* Specifies *.prt */
    UF_UI_PART_SAVEAS_FLTR,      /* Specifies *.prt */
    UF_UI_PART_SAVEAS_STUDENT_FLTR,      /* Specifies *.prt */
    UF_UI_FILE_GRIP_FLTR,        /* Specifies *.grx */
    UF_UI_FILE_UFUN_FLTR,        /* Specifies *.sl, *.so or *.dll depending
                                    on the platform. */
    UF_UI_IMPORT_SYMBOL_FLTR,    /* Specifies *.sym,*.txt, or *.* */
    UF_UI_IMPORT_BLOCK_FLTR,     /* Specifies *.dwg,*.dxf,*.txt */
    UF_UI_IMAGE_QS_FLTR,         /* Specifies *.pix */
    UF_UI_IMAGE_DISP_FLTR,       /* Specifies *.tif and .pix */
    UF_UI_EXPORT_EXPRESSIONS_FLTR, /* Specifies *.exp */
    UF_UI_IMPORT_EXPRESSIONS_FLTR, /* Specifies *.exp */
    UF_UI_MACRO_FLTR,              /* Specifies *.macro */
    UF_UI_LAYOUT_FLTR,             /* Specifies *.win */
    UF_UI_EXPORT_COMPONENT_FLTR,   /* Specifies *.flt */
    UF_UI_IMPORT_COMPONENT_FLTR,   /* Specifies *.flt */
    UF_UI_CAM_MDF_FLTR,       /* Specifies *.md* */
    UF_UI_CAM_GPM_FLTR,       /* Specifies *.* */
    UF_UI_CAM_CLS_FLTR,       /* Specifies *.cls */
    UF_UI_CAM_CL_FLTR,        /* Specifies *.cl */
    UF_UI_CAM_CLF_FLTR,       /* Specifies *.clf */
    UF_UI_CAM_BCL_FLTR,       /* Specifies *.bcl */
    UF_UI_CAM_ISO_FLTR,       /* Specifies *.iso */
    UF_UI_CAM_NCOUT_FLTR,     /* Specifies *.* */
    UF_UI_CAM_LISTOUT_FLTR,   /* Specifies *.* */
    UF_UI_CAM_ACL_FLTR,       /* Specifies *.acl */
    UF_UI_CAM_S_FLTR,         /* Specifies *.*s* */
    UF_UI_CAM_ARC_FLTR,       /* Specifies *.arc */
    UF_UI_CAM_CYC_FILE_FLTR,  /* Specifies *.cyc */
    
    UF_UI_CAM_MTK_FLTR,       /* Specifies *.mtk */
    UF_UI_TRAN_PART_FLTR,     /* Specifies *.prt */
    UF_UI_TRAN_IGS_FLTR,      /* Specifies *.igs */
    UF_UI_TRAN_STP_FLTR,      /* Specifies *.stp */
    UF_UI_TRAN_DXF_FLTR,      /* Specifies *.dxf */
    UF_UI_TRAN_IGES_FLTR,     /* Specifies *.def */
    UF_UI_TRAN_STEP203_FLTR,  /* Specifies *.def */
    UF_UI_TRAN_STEP214_FLTR,  /* Specifies *.def */
    UF_UI_TRAN_DXFTOUG_FLTR,  /* Specifies *.def */
    UF_UI_TRAN_UGTODXF_FLTR,  /* Specifies *.def */
    UF_UI_TRAN_LOG_FLTR,      /* Specifies *.log */
    UF_UI_MB_SYSLOG_FLTR,     /* Specifies *.syslog */
    UF_UI_MISC_DATA_FLTR,     /* Specifies *.dat */
    UF_UI_CAM_TOOLIB_FLTR,    /* Specifies *.prt */
    UF_UI_CAM_LIBLIST_FLTR,   /* Specifies *.prt */
    UF_UI_CAM_DISPAT_FLTR,    /* Specifies *.prt */
    UF_UI_CAM_VCUTS_FLTR,     /* Specifies *.stl */
    UF_UI_CAM_VCUTT_FLTR,     /* Specifies *.txt */
    UF_UI_CAM_TEMPSET_FLTR,   /* Specifies *.opt */
    UF_UI_IMPORT_VRML_FLTR,   /* Specifies *.wrl and *.wrl.gz */
    UF_UI_NLE_FLTR,           /* */
    UF_UI_RLIST_HRN_FLTR,     /* */
    UF_UI_RLIST_CMP_FLTR,     /* */
    UF_UI_IMPORT_SE_FLTR,     /* */
    UF_UI_IMPORT_STL_FLTR,    /* Specifies *.stl and *.stl.gz */
    UF_UI_CAM_CONFIG_FLTR,    /* */
    UF_UI_CAM_SETUP_PRT_FLTR, /* */
    UF_UI_VDAC_CEO_FLTR,      /* */
    UF_UI_VDAC_CFG_FLTR,      /* */
    UF_UI_TBR_FLTR,           /* */
    UF_UI_HATCH_FLTR,         /* */
    UF_UI_BOOKMARK_FLTR,      /* */
    UF_UI_CAM_SHOP_DOC_FLTR,  /* */
    UF_UI_FMBD_FILE_FLTR,     /* */
    UF_UI_LOAD_OPT_FLTR,      /* Specifies *.def */
    UF_UI_TRAN_DWG_FLTR,      /* Specifies *.dwg */
    UF_UI_MENU_DXF_FLTR,      /* Specifies *.dwg and *.dxf */
    UF_UI_IMPORT_ASC_FLTR,      /* Specifies *.asc  and *.dwg*/
    UF_UI_TRAN_CATIA_FLTR,    /* Specifies *.mod and *.exp */
    UF_UI_TRAN_CATMOD_FLTR,   /* Specifies *.mod only */
    UF_UI_CAE_RPT_TEMPLATES_FLTR,   /* Specifies *.htt only */
    UF_UI_CAE_RPT_IMG_FLTR,         /* Specifies *.gif, jpg, mpg, vrml */
    UF_UI_INTEROP_FLTR,             /* Specifies files that contain plm xml context, such as .bkm */
    UF_UI_DRAFTING_IMAGE_FLTR,      /* Specifies *.jpg and *.tif */
    UF_UI_NX2D_FLTR,                /* NX2D File */
    UF_UI_SPRD_FLTR,                /* Specifies *.xls *.csv, *.xs6, *.tsv and *.* */
    UF_UI_SPRDNT_FLTR,              /* Specifies *.xls *.csv, *.tsv and *.* */
    UF_UI_SPRSHT_FLTR,              /* Specifies *.xlsx *xls */
    UF_UI_XESS_FLTR,                /* Specifies *.xs6, etc. */
    UF_UI_CAE_RST_FLTR,             /* Specifies *.op2 *.vdm *.rst *.rth *.des and *.fil */
    UF_UI_CAE_RST_ODB_FLTR,              /* Specifies *.op2 *.vdm *.rst *.rth *.des *.ssndb *.fil and *.odb */
    UF_UI_CAE_ODB_FLTR,                  /* Specifies *.odb */
    UF_UI_CAE_SAMCEF_FLTR,               /* Specifies *.des *.ssndb *.op2 *.vdm *.rst *.rth and *.fil */
    UF_UI_CAE_OP2_FLTR,             /* Specifies *.op2 */
    UF_UI_TRAN_CATIAV5_FLTR,        /* Specifies *.CATPart and *.CATProduct */
    UF_UI_TRAN_CATIAV5_CATPART_FLTR,  /* Specifies *.CATPart */
    UF_UI_IMPORT_AC_FLTR,           /* Specifies *.ac */
    UF_UI_PRT_PART_OPEN_FLTR,       /* Specifies *.prt */
    UF_UI_SFEM_PART_OPEN_FLTR,      /* Specifies *.prt, *.fem *.sim */
    UF_UI_FEM_PART_OPEN_FLTR,       /* Specifies *.fem */
    UF_UI_FEM_PART_NEW_FLTR,        /* Specifies *.fem */
    UF_UI_BOOKMARK_OPEN_FLTR,       /* Specified for open bookmark *.bkm, *.plmxlm */
    UF_UI_BOOKMARK_SAVE_FLTR,       /* Specified for save bookmark *.plmxml */
    UF_UI_CAE_AFU_FLTR,                  /* Specifies *.afu */
    UF_UI_XYPLOT_DISP_TEMPLATE_FLTR,     /* Specifies *.xml */
    UF_UI_FEM_SAVEAS_FLTR,               /* Specifies *.fem */
    UF_UI_SIM_SAVEAS_FLTR,               /* Specifies *.sim */
    UF_UI_MOTION_IMP_EXP_FLTR,           /* Specifies *.xml */
    UF_UI_FTK_NAV_TREE_HISTORY_FLTR,     /* Specifies *.xml */
    UF_UI_SIM_PART_NEW_FLTR,             /* Specifies *.sim */
    UF_UI_SIM_PART_OPEN_FLTR, /* Specifies *.sim */
    UF_UI_FACE_ANALYSIS_REFLECTION_FLTR, /* Specifies *.jpg, *.tif and *.png */
    UF_UI_BACKGROUND_IMAGE_FLTR,         /* Specifies *.jpg, *.tif and *.png */
    UF_UI_TEXTURE_IMAGE_FLTR,            /* Specifies *.jpg, *.tif and *.png */
    UF_UI_IBL_IMAGE_FLTR,                /* Specifies *.lwi, *.jpg, *.tif *.png and *.bmp *hdr and *.exr */
    UF_UI_CAE_RPCIII_FLTR,               /* Specifies *.rsp */
    UF_UI_CAE_DAC_FLTR,                  /* Specifies *.dac */
    UF_UI_CAE_CSV_FLTR,                  /* Specifies *.csv */
    UF_UI_TRAN_PROE_FLTR,                /*Specifies *.asm.* and *.prt.* */
    UF_UI_SE_PART_ASM_FLTR,              /* Specifies *.par and *.asm (Solid Edge files) */
    UF_UI_CAE_EEF_FLTR,                  /* Specifies *.eef */
    UF_UI_CAE_SEF_FLTR,                  /* Specifies *.sef */
    UF_UI_CAE_RS2_FLTR,                  /* Specifies *.rs2 */
    UF_UI_CAM_FEA_EXPORT_FLTR,           /* Specifies *.plmxml for Manufacturing Feature export */
    UF_UI_CAE_MAT_FLTR,                  /* Specifies *.mat */
    UF_UI_MOTION_ADAMS_RES_FLTR,         /* Specifies *.res */
    UF_UI_MOTION_RECURDYN_RAD_FLTR,      /* Specifies *.rad */
    UF_UI_PDF_FLTR,                      /* Specifies *.pdf */
    UF_UI_JPG_FLTR,                      /* Specifies *.jpg */
    UF_UI_TIF_FLTR,                      /* Specifies *.tif */
    UF_UI_EMF_FLTR,                      /* Specifies *.emf */
    UF_UI_PNG_FLTR,                      /* Specifies *.png */
    UF_UI_CAE_UNV58_FLTR,                /* Specifies *.unv(dataset58) */
    UF_UI_ASSY_FEM_PART_OPEN_FLTR,       /* Specifies *.afm */
    UF_UI_ASSY_FEM_PART_NEW_FLTR,        /* Specifies *.afm */
    UF_UI_ASSY_FEM_SAVEAS_FLTR,          /* Specifies *.afm */
    UF_UI_IFEM_PART_OPEN_FLTR,           /* Specifies *.fem, *.afm */
    UF_UI_KF_MISC1_FLTR,                 /* Specifies kf specified file type */
    UF_UI_KF_MISC2_FLTR,                 /* Specifies kf specified file type */
    UF_UI_KF_MISC3_FLTR,                 /* Specifies kf specified file type */
    UF_UI_KF_MISC4_FLTR,                 /* Specifies kf specified file type */
    UF_UI_KF_MISC5_FLTR,                 /* Specifies kf specified file type */
    UF_UI_SIMULINK_MDL_FLTR,             /* Simulink MDL file type */
    UF_UI_SIMULINK_M_FLTR,               /* Simulink M file type */
    UF_UI_MOTION_EXPORT_SDK_RMD_FLTR,    /* Specifies *.sdk and *.rmd */
    UF_UI_STANDARD_FONTS_FLTR,           /* Specifies .ttf and other standard font types */
    UF_UI_SW_PART_ASM_FLTR,              /* Specifies (Solid Works files) */
    UF_UI_IGES_EXPORT_FLTR,              /* Used by File->Export->IGES */
    UF_UI_STEP_EXPORT_FLTR,              /* Used by File->Export->STEP203, STEP214) */
    UF_UI_MOTION_FLEXBODY_RFI_FLTR,      /* Specifies *.rfi for flexible body use*/
    UF_UI_IMAGE_FILE_FLTR,               /* Specifies *.bmp, *.jpg, *.gif, *.png and *.tif*/
    UF_UI_ATTR_CATALOG_FLTR,             /* Specifies *.xml */
    UF_UI_MW_FLTR,                       /* Specifies *.mw for Maple Worksheet*/
    UF_UI_TRUMPF_GEO_FLTR,               /* Specifies .geo for Trumpf bending machines */
    UF_UI_TIRE_SPINDLE_FLTR,             /* Specifies *.spindle */
    UF_UI_STUDIO_IMAGE_FILE_FLTR,        /* Specifies *.tif, *.jpg, *.png, *.gif and *.bmp */
    UF_UI_MOTION_RECURDYN_RAD_RAN_FLTR,  /*Specifies *.rad, *.ran for Motion RecurDyn*/
    UF_UI_MECHDES_RUNTIME_CODE_FLTR,     /* Specifies *.cs and *.dll file type */
    UF_UI_CAE_UNV_FLTR,                  /* Specifies *.unv */
    UF_UI_PAX_FLTR,                      /* Specifies *.pax */
    UF_UI_HDF5_FLTR,                     /* Specifies *.h5 */ 
    UF_UI_LAYUP_FLTR,                     /* Specifies *.Layup */ 
    UF_UI_CAE_BROWSE_FLTR,               /* Specifies *.* */
    UF_UI_CAE_MDF_FLTR,                  /* Specifies *.mdf */
    UF_UI_PART_SAVEAS_WITH_CATPRODUCT_FLTR, /* Specifies *.prt */
    UF_UI_TRAN_CATIAV5_CATPRODUCT_FLTR,  /* Specifies *.CATProduct */
    UF_UI_JT_CONFIG_FLTR,                  /*Specifies *.config file*/
    UF_UI_CAE_CONDSEQ_FLTR,              /* Specifies *.bdd, *.* */
    UF_UI_JPEG_FLTR,                     /* Specifies *.jpeg */
    UF_UI_JPE_FLTR,                     /* Specifies *.jpe */
    UF_UI_TIFF_FLTR,                     /* Specifies *.tiff */
    UF_UI_RASTER_IMAGE_FLTR,            /* Specifies *.jpg,*.jpeg,*.jpe,*.png,*.tif and *.tiff */
    UF_UI_MOTION_LMS_MRES_FLTR,          /* Specifies *.mres for LMS Motion */
    UF_UI_REPORT_TEMPLATE_FLTR,          /* Specifies *.docx */
    UF_UI_REPORT_IMAGES_FLTR,            /* Specifies *.jpg, *.tif, *.png  and *.gif */
    UF_UI_REPORT_ZIP_FLTR,               /* Specifies *.rlfz */
    UF_UI_TRAN_ACIS_IMPORT_FLTR,                /*Specifies *.sat* and *.sab* */
    UF_UI_TRAN_ACIS_EXPORT_FLTR,                /*Specifies *.sat* and *.sab* */
    UF_UI_TRAN_ACIS_SAT_FLTR,                /*Specifies *.sat* */
    UF_UI_TRAN_ACIS_SAB_FLTR,                /*Specifies *.sab* */
    UF_UI_POD_FLTR,                     /* Specifies *.pod */
    UF_UI_IRAYPLUS_MATERIAL_FLTR,        /* Specifies *.xml */
    UF_UI_IRAYPLUS_MATERIAL_SYSTEM_SAVE_FLTR, /* Specifies *.xml */
    UF_UI_PSF_FLTR,                    /*Specifies *.psf* */
    UF_UI_DGML_FLTR,                     /* Specifies *.dgml */
    UF_UI_SIMCENTER_FILE_FLTR,    /* for SimCenter */
    UF_UI_TRAN_STPX_FLTR,
    UF_UI_TRAN_STPZ_FLTR,
    UF_UI_TRAN_STPXZ_FLTR,
    UF_UI_TRAN_STP242_FLTR,
    UF_UI_CAE_LAYOUTSTATE_FLTR,         /* For the layout states *.lsx */
    UF_UI_LIGHT_PROFILE_FILE_FLTR,      /* Specifies light profile files *.ies */
    UF_UI_DIALOG_FILTER_COUNT           /* UF_UI_DIALOG_FILTER_COUNT should
                                      always be defined last */
} ;

typedef enum UF_UI_dialog_filter_id_e UF_UI_dialog_filter_id_t;

/*
*   UF_UI_PART_OPEN_XT_FLTR was added in NX4 at the time when XT files were added
*   to Part Open to be loaded into NX using the XT adapter.  Shortly thereafter it
*   was decided to make that case the default case for Part Open, rendering
*   UF_UI_PART_OPEN_XT_FLTR unnecessary.  However since the value was defined in a UF
*   header there is the potential that NX/Open customers have files that reference the
*   enum value.  This define is to satisfy those customers.  This define will be removed
*   in NX6.
*/
#define UF_UI_PART_OPEN_XT_FLTR  UF_UI_PART_OPEN_FLTR


/* Constants for FSD directory path access.

*/
enum UF_UI_dialog_dir_id_e{
    UF_UI_EXPORT_DIR,  /* This is used by File->Export->Part, File->Export->CGM,
                          File->Export->Parasolid, File->Export->Diagram,
                          File->Export->Rapid-Prototyping, and
                          Assemblies->Component Filters->Define Filter-> Export
                       */
    UF_UI_IMPORT_DIR,  /* This is used by File->Import->Part, File->Import->CGM,
                          File->Import->Parasolid, File->Import->Markup,
                          Toolbox->Feature->User Defined,
                          Toolbox->Expression->Export,
                          Toolbox->Expression->Import,
                          Assemblies->Component Filters->Define Filter->Import
                       */
    UF_UI_PART_DIR,    /* This is used by File->New, File->Open,
                          File->Save->Part As,
                          File->Export->Iges->Specify Part,
                          File->Import->Iges->Specify Part,
                          File->Export->Step203->Specify Part,
                          File->Import->Step203->Specify Part,
                          File->Export->Step214->Specify Part,
                          File->Import->Step214->Specify Part,
                          File->Export->Dxf->Specify Part,
                          File->Import->Dxf->Specify Part
                        */
    UF_UI_GRIP_DIR,     /* This is used by File->Execute->Grip and
                           File->Execute-> Debug Grip. */
    UF_UI_IMAGE_DIR,    /* This is used by
                           View->Visualization->Create Quick Image->Save,
                           View->Visualization->Assembly Hidden Line->Save
                           View->Visualization->Display Image->Save
                        */
    UF_UI_IMPORT_SYMB_DIR,/* This is used by File->Import->Symbol Function.*/

    UF_UI_IMPORT_BLOCK_DIR,/* This is used by File->Import->AutoCAD Block Function.*/

    UF_UI_UFUN_DIR,     /* This is used by File->Execute Open->User Function.
                        */
    UF_UI_MACRO_DIR,    /* This is used by Macro->Playback and
                           Macro->Start Record.
                        */
    UF_UI_LAYOUT_DIR,   /* This is no longer used. */
    UF_UI_CAM_MDF_DIR,  /* This is used by
                           Toolbox->CL Source File->Postprocess->GPM (Specify)
                        */
    UF_UI_CAM_GPM_DIR,  /* */
    UF_UI_CAM_CLF_DIR,  /* This is used by
                           Toolbox->Tool Pth->Postprocess->Generate STD CLF
                        */
    UF_UI_CAM_CL_DIR,   /* This is used by
                           Toolbox->Tool Path->Postprocess->Input File Name
                           (Specify).
                        */
    UF_UI_CAM_CLS_DIR,  /* This is used by Applications->Manufacturing. */
    UF_UI_CAM_BCL_DIR,  /* This is used by
                           Toolbox->Tool Path->Postprocess->Output File Name
                           (Specify). */

    UF_UI_CAM_ISO_DIR,  /* This is used by
                           Toolbox->Tool Path->Postprocess->Generate ISO CLF
                        */
    UF_UI_CAM_NCOUT_DIR, /* This is used by
                   Toolbox->CL Source File->Postprocess->NC Output->Output File
                         */
    UF_UI_CAM_LISTOUT_DIR, /* */
    UF_UI_CAM_ACL_DIR,  /* This is used by
                        Toolbox->CL Source File->Postprocess->Output File Name
                        */
    UF_UI_CAM_S_DIR,    /* This is used by
                           Toolbox->CL Source File->Postprocess->Input File Name
                        */
    UF_UI_CAM_ARC_DIR,  /* This is used by 
                           Machine Tool Builder -> Import NC Archive*/

    UF_UI_CAM_CYC_DIR,  /* This is used by 
                           Program Manager -> Import Cyc Archive*/  

    UF_UI_CAM_MTK_DIR,/* This is used by 
                           Machine Tool Builder -> Import Machine Tool Kit
                        */
    UF_UI_TRAN_IGS_DIR, /* This is used by
                           File->Export->Iges->Specify IGES File
                           File->Import->Iges->Specify IGES File
                        */
    UF_UI_TRAN_STP_DIR, /* This is used by
                           File->Export->Step203->Specify Step203 File
                           File->Import->Step203->Specify Step203 File
                           File->Export->Step214->Specify Step214 File
                           File->Import->Step214->Specify Step214 File
                        */
    UF_UI_TRAN_DXF_DIR, /* This is used by
                           File->Export->Dxf->Specify DXF File
                           File->Import->Dxf->Specify DXF File
                        */
    UF_UI_TRAN_IGES_DIR, /* This is used by
                            File->Export->Iges->Choose Defaults File
                            File->Import->Iges->Choose Defaults File
                         */
    UF_UI_TRAN_STEP203_DIR,/* This is used by
                            File->Export->Step203->Choose Defaults File
                            File->Import->Step203->Choose Defaults File
                         */
    UF_UI_TRAN_STEP214_DIR, /* This is used by
                            File->Export->Step214->Choose Defaults File
                            File->Import->Step214->Choose Defaults File
                         */
    UF_UI_TRAN_DXFTOUG_DIR, /* This is used by
                            File->Import->Dxf->Choose Defaults File
                            */
    UF_UI_TRAN_UGTODXF_DIR, /* This is used by
                            File->Export->Dxf->Choose Defaults File
                            */
    UF_UI_TRAN_LOG_DIR, /* This is used by
                           File->Export->Iges->Specify Log File
                           File->Export->Step203->Specify Log File
                           File->Export->Step214->Specify Log File
                           File->Export->Dxf->Specify Log File
                           File->Import->Iges->Specify Log File
                           File->Import->Step203->Specify Log File
                           File->Import->Step214->Specify Log File
                           File->Import->Dxf->Specify Log File
                           File->Export->Iges->Review Log File
                           File->Export->Step203->Review Log File
                           File->Export->Step214->Review Log File
                           File->Export->Dxf->Review Log File
                           File->Import->Iges->Review Log File
                           File->Import->Step203->Review Log File
                           File->Import->Step214->Review Log File
                           File->Import->Dxf->Review Log File
                         */
    UF_UI_MB_SYSLOG_DIR, /* This is used by
                            Info->Custom MenuBar->File Usage Report
                         */
    UF_UI_MISC_DATA_DIR, /* This is used by
                  Toolbox->Curve->Spline->By Poles->Points From File
                  Toolbox->Curve->Spline->Through Points->Points From File
                  Toolbox->Curve->Spline->Fit->Points From File
                  Toolbox->Free Form Feature->Through Points->Points From File
                  Toolbox->Free Form Feature->From Poles->Points From File
                  Toolbox->Free Form Feature->From Point Cloud->Points From File
                  Toolbox->Free Form Feature->Move Defining Point
                  Toolbox->Free Form Feature->Move Pole
                  Toolbox->Curve->Edit Curve->Edit Curve Parameters->
                       Edit Point->Points From File
                  Toolbox->Curve->Edit Curve->Edit Curve Parameters->
                       Edit Pole->Points From File
                       */

    UF_UI_CAM_TOOLIB_DIR, /* This is used by
                             Toolbox->Tool->LIbrary->Retrieve From Library
                          */
    UF_UI_CAM_LIBLIST_DIR, /* This is used by
                             Toolbox->Tool->LIbrary->List Library Entries
                          */
    UF_UI_CAM_DISPAT_DIR, /* This is used by
                             Applications->Manufacturing->Operation->
                             Edit Display->Specify (Pattern)->Pattern File Name
                          */
    UF_UI_CAM_VCUTS_DIR, /* This is used by
                      Preferences->General CAM->Use Vericut->Toolbox->ToolPath->
                          Vericut->Geometry Definition->OK
                         */
    UF_UI_CAM_VCUTT_DIR, /* This is used by
                      Preferences->General CAM->Use Vericut->Toolbox->ToolPath->
                          Vericut->Geometry Definitions->Output Type (Text)
                         */
    UF_UI_CAM_TEMPSET_DIR, /* */
    UF_UI_NLE_DIR, /* */
    UF_UI_RLIST_HRN_DIR, /* */
    UF_UI_RLIST_CMP_DIR, /* */
    UF_UI_CAM_CONFIG_DIR, /* */
    UF_UI_CAM_SETUP_PRT_DIR, /* */
    UF_UI_VDAC_CEO_DIR, /* */
    UF_UI_VDAC_CFG_DIR, /* */
    UF_UI_TBR_DIR, /* */
    UF_UI_HATCH_DIR, /* */
    UF_UI_BOOKMARK_DIR, /* */
    UF_UI_CAM_SHOP_DOC_DIR, /* */
    UF_UI_FMBD_FILE_DIR,
    UF_UI_TRAN_DWG_DIR, /* This is used by
                           File->Export->DWG->Specify DWG File
                           File->Import->DWG->Specify DWG File
                        */
    UF_UI_MENU_DXF_DIR, /* This is used by
                           File->Import->DWG->Specify DWG File
                        */
    UF_UI_IMPORT_ASC_DIR,               /* Used by File->Import->Ideas ASC/DWG */
    UF_UI_TRAN_CATIA_DIR, /* This is used by
                           ** File->Import->CATIA->Specify MOD or EXP File
                           */
    UF_UI_TRAN_CATMOD_DIR, /* This is used by
                           ** File->Export->CATIA->Specify MOD File
                           */
    UF_UI_CAE_RPT_TEMPLATES_DIR, /* This is used by
                           ** Structures->Tools->Report->Input to define
                              the htt template file of the report.
                           */
    UF_UI_CAE_RPT_IMG_DIR, /* This is used by
                           ** Structures->Tools->Report->Input to define
                              the gif, jpg, mpg, vrml files of the report.
                           */
    UF_UI_INTEROP_FILE_DIR,
    UF_UI_DRAFTING_IMAGE_DIR,/* This is used by
                             ** Insert->Image in Drafting to select an image
                                file to create a drafting image from
                             */
    UF_UI_NX2D_FILE_DIR,

    UF_UI_SPRD_FILE_DIR,
    UF_UI_SPRDNT_FILE_DIR,   /* This is used by Motion Analysis->Spreadsheet Run
                             ** toolbar icon for selecting motion data spreadsheet
                             */
    UF_UI_SPRSHT_FILE_DIR,
    UF_UI_XESS_FILE_DIR,
    UF_UI_CAE_RST_DIR,  /* This is used by
                        ** Strutcures->Solution->Preload Result File
                        */
    UF_UI_CAE_RST_ODB_DIR,
    UF_UI_CAE_ODB_DIR,
    UF_UI_CAE_SAMCEF_DIR,               /*used for *.des */
    UF_UI_TRAN_CATIAV5_DIR,         /* These two are used by CATIA V5 under */
    UF_UI_TRAN_CATIAV5_CATPART_DIR, /* File Open, Save As, Import, and Export */
    UF_UI_CAE_AFU_DIR,                  /* Used by *.afu File */
    UF_UI_XYPLOT_DISP_TEMPLATE_DIR,     /* Used by *.xml File */
    UF_UI_MOTION_IMP_EXP_DIR,           /* Used by *.xml File */
    UF_UI_FTK_NAV_TREE_HISTORY_DIR,     /* Used by *.xml File */
    UF_UI_FACE_ANALYSIS_REFLECTION_DIR, /* Used by Face Analysis -> Reflections: User Specified Image */
    UF_UI_BACKGROUND_IMAGE_DIR,         /* Used by View -> Visualiztion -> Visual Effects: Background */
    UF_UI_TEXTURE_IMAGE_DIR,            /* Used by Materials Editor: Pattern: Simple Decal: Image */
    UF_UI_IBL_IMAGE_DIR,                /* Used by visual effects HDRI */
    UF_UI_CAE_RPCIII_DIR,               /* Used by *.rsp File */
    UF_UI_CAE_DAC_DIR,                  /* Used by *.dac File */
    UF_UI_CAE_CSV_DIR,                  /* Used by *.csv File */
    UF_UI_TRAN_PROE_DIR,                /* Used by PROE */
    UF_UI_CAE_EEF_DIR,                  /* Used by *.eef File */
    UF_UI_CAE_SEF_DIR,                  /* Used by *.sef File */
    UF_UI_CAE_RS2_DIR,                  /* Used by *.rs2 File */
    UF_UI_CAE_MAT_DIR,                  /* Used by *.mat File */
    UF_UI_REPORT_TEMPLATE_DIR,          /* Used by report template file, *.docx */
    UF_UI_REPORT_IMAGES_DIR,            /* Used by report images file, *.tif, *.jpg *.png and *.gif */
    UF_UI_REPORT_ZIP_DIR,               /* Used by *.rlfz File */
    UF_UI_MOTION_ADAMS_RES_DIR,         /* Used by *.res File */
    UF_UI_MOTION_RECURDYN_RAD_DIR,      /* Used by *.rad File */
    UF_UI_PDF_DIR,                      /* Used by *.pdf File */
    UF_UI_JPG_DIR,                      /* Used by *.jpg File */
    UF_UI_TIF_DIR,                      /* Used by *.tif File */
    UF_UI_EMF_DIR,                      /* Used by *.emf File */
    UF_UI_PNG_DIR,                      /* Used by *.png File */
    UF_UI_SYM_DIR,                      /* Used by *.sym File */
    UF_UI_CAE_UNV58_DIR,                /* Used by *.unv(dataset58) File */
    UF_UI_KF_MISC1_DIR,                 /* Used by UI_Comp_KFSelectFile */
    UF_UI_KF_MISC2_DIR,                 /* Used by UI_Comp_KFSelectFile */
    UF_UI_KF_MISC3_DIR,                 /* Used by UI_Comp_KFSelectFile */
    UF_UI_KF_MISC4_DIR,                 /* Used by UI_Comp_KFSelectFile */
    UF_UI_KF_MISC5_DIR,                 /* Used by UI_Comp_KFSelectFile */
    UF_UI_SIMULINK_MDL_DIR,             /* Used by *.mdl File*/
    UF_UI_SIMULINK_M_DIR,               /* Used by *.m File*/
    UF_UI_MOTION_EXPORT_SDK_RMD_DIR,    /* Used by Export->RecurDyn Input in Motion RecurDyn */
    UF_UI_STANDARD_FONTS_DIR,           /* Used by DisplayUI_UICompSelectFontFile */
    UF_UI_IGES_EXPORT_DIR,              /* Used by File->Export->IGES */
    UF_UI_STEP_EXPORT_DIR,              /* Used by File->Export->STEP203, STEP214) */
    UF_UI_MOTION_FLEXBODY_RFI_DIR,      /* Used by *.rfi File*/
    UF_UI_ATTR_CATALOG_DIR,             /* Used by *.xml File*/
    UF_UI_MW_DIR,                       /* Used by *.mw File */
    UF_UI_TRUMPF_GEO_DIR,               /* Used by .geo file */
    UF_UI_TIRE_SPINDLE_DIR,             /* Used by *.spindle File */
    UF_UI_MOTION_RECURDYN_RAD_RAN_DIR,  /* Used by *.ran File */
    UF_UI_MECHDES_RUNTIME_CODE_DIR,     /* Used by *.cs and *.dll file*/
    UF_UI_CAE_UNV_DIR,                  /* Used by *.unv File */
    UF_UI_PAX_DIR,                      /* Used by *.pax file */
    UF_UI_HDF5_DIR,                     /* Used by *.h5 file */ 
    UF_UI_LAYUP_DIR,                    /* Used by *.Layup file */ 
    UF_UI_CAE_BROWSE_DIR,               /*Used by Solution->Browse*/
    UF_UI_CAE_MDF_DIR,                  /* Used for .mdf file */
    UF_UI_TRAN_CATIAV5_CATPRODUCT_DIR, /* File Open, Save As, Import, and Export */
    UF_UI_CAE_CONDSEQ_DIR,              /* Used by *.bdd file */
    UF_UI_MOTION_LMS_MRES_DIR,          /* Used by *.mres file in Motion LMS */
    UF_UI_CAE_RST_XDB_DIR,              /* This is used by PostProcessing import Result File (to be removed)  */
    UF_UI_CAE_RST_XDB_ODB_DIR,          /* This is used by PostProcessing import Result File (to be removed)  */
    UF_UI_TRAN_ACIS_DIR,
    UF_UI_TRAN_ACIS_SAT_DIR,
    UF_UI_TRAN_ACIS_SAB_DIR,
    UF_UI_MOTION_FLEXBODY_OP2_DIR,      /* Used by *.op2 File containing flexible body */
    UF_UI_POD_DIR,                       /* Used by *.pod files Point Cloud ) */
    UF_UI_DGML_DIR,                     /* Used by *.dgml XML-based file format for directed graphs */
    UF_UI_TRAN_STPX_DIR,
    UF_UI_TRAN_STPZ_DIR,
    UF_UI_IRAYPLUS_MATERIAL_DIR,        /* Used by IrayPlus Material Editor Export to *.xml file */
    UF_UI_IRAYPLUS_MATERIAL_SYSTEM_SAVE_DIR, /* Used by IrayPlus Material Editor Save to System Studio Materials *.xml file */
    UF_UI_TRAN_STPXZ_DIR,
    UF_UI_TRAN_STP242_DIR,
    UF_UI_CAE_LAYOUTSTATE_DIR,
    UF_UI_LIGHT_PROFILE_FILE_DIR,       /* Used to specify a light profile file */
   /* 
*/
    UF_UI_DIALOG_DIR_COUNT          /* UF_UI_DIALOG_DIR_COUNT should
                                       always be last */
} ;

typedef enum UF_UI_dialog_dir_id_e UF_UI_dialog_dir_id_t;

/****************************************************************************
* Limit definitions 
* Used within 'UF_UI_write_listing_window' 
* 
* UF_UI_MAX_STRING_LEN is being deprecated because NX is moving to support 
* multibyte characters. User written programs should start using the 
* new definitions for file specifications: 
* UF_UI_MAX_STRING_BUFSIZE should be used for buffer allocations and memory 
* allocations, e.g. char my_string[UF_UI_MAX_STRING_BUFSIZE]; 
* UF_UI_MAX_STRING_NCHARS should be used to limit the number of characters in 
* a buffer. NX code will enforce these limits. 
*
* New routines have been added which will help in this transition: 
* UF_TEXT_count_characters() will count the number of characters in a buffer. 
* UF_TEXT_terminate_chars() will terminate a C string after the given 
* number of characters. 
****************************************************************************/

#define UF_UI_MAX_STRING_NCHARS      1000  /* Maximum number of characters in a UI string excluding the trailing '\0'. These may be multi-byte characters. */ 
#define UF_UI_MAX_STRING_BUFSIZE      NX_BUFSIZE(UF_UI_MAX_STRING_NCHARS)
/*  */
#define UF_UI_MAX_STRING_LEN (UF_UI_MAX_STRING_BUFSIZE - 1) 
/*  */
/* structure used by
 UF_UI_select_point_collection
*/

struct UF_UI_chained_points_s
{
    double pt[3];
    tag_t object;
} ;

typedef struct UF_UI_chained_points_s UF_UI_chained_points_t,
*UF_UI_chained_points_p_t;

/* Constants for selection solid_type */

#define UF_UI_SEL_NOT_A_FEATURE                (-1)
#define UF_UI_SEL_FEATURE_BODY                   0
#define UF_UI_SEL_FEATURE_ANY_EDGE               1
#define UF_UI_SEL_FEATURE_LINEAR_EDGE            2
#define UF_UI_SEL_FEATURE_CIRCULAR_EDGE          3
#define UF_UI_SEL_FEATURE_ELLIPTICAL_EDGE        4
#define UF_UI_SEL_FEATURE_INTERSECTION_EDGE      5
#define UF_UI_SEL_FEATURE_BCURVE_EDGE            6
#define UF_UI_SEL_FEATURE_SPCURVE_EDGE           7
#define UF_UI_SEL_FEATURE_FOREIGN_EDGE           8
#define UF_UI_SEL_FEATURE_CNST_PARM_EDGE         9
#define UF_UI_SEL_FEATURE_ANY_WIRE_OR_EDGE      10

/* 11-18 are reserved for additional solid_type use */

#define UF_UI_SEL_FEATURE_ANY_SHEET             19 /* Do not use this, use _SHEET_BODY or _ANY_FACE */
#define UF_UI_SEL_FEATURE_ANY_FACE              20
#define UF_UI_SEL_FEATURE_PLANAR_FACE           21
#define UF_UI_SEL_FEATURE_CYLINDRICAL_FACE      22
#define UF_UI_SEL_FEATURE_CONICAL_FACE          23
#define UF_UI_SEL_FEATURE_SPHERICAL_FACE        24
#define UF_UI_SEL_FEATURE_TOROIDAL_FACE         25
#define UF_UI_SEL_FEATURE_PARAMETRIC_FACE       26
#define UF_UI_SEL_FEATURE_BLENDING_FACE         27
#define UF_UI_SEL_FEATURE_OFFSET_FACE           28
#define UF_UI_SEL_FEATURE_SWEPT_FACE            29
#define UF_UI_SEL_FEATURE_SWUNG_FACE            30
#define UF_UI_SEL_FEATURE_FOREIGN_FACE          31

#define UF_UI_SEL_FEATURE_ANY_COMPOSITE_BODY    32
#define UF_UI_SEL_FEATURE_ANY_COMPOSITE_FACE    33
#define UF_UI_SEL_FEATURE_ANY_COMPOSITE_EDGE    34

#define UF_UI_SEL_FEATURE_SHEET_BODY            35
#define UF_UI_SEL_FEATURE_SOLID_BODY            36 /* non-sheet-body */
#define UF_UI_SEL_FEATURE_MAX_FEATURE           36

/* 40-90 are reserved for feature type selection use */

/* Special features, no type or subtype is needed. */
#define UF_UI_SEL_FEATURE_ROUTING_CURVE_ONLY    91 /* This should be first of special feature types */
#define UF_UI_SEL_FEATURE_ROUTING_SOLID_ONLY    92
#define UF_UI_SEL_FEATURE_WORK_PART_COMP        93
/*

*/
#define UF_UI_SEL_FEATURE_WELD_RESIS_SPOT       94
#define UF_UI_SEL_FEATURE_WELD_ARC_SPOT         95
#define UF_UI_SEL_FEATURE_WELD_MEC_CLINCH       96
#define UF_UI_SEL_FEATURE_WELD_DOLLOP           97
#define UF_UI_SEL_FEATURE_WELD_NUT              98
#define UF_UI_SEL_FEATURE_WELD_STUD             99
#define UF_UI_SEL_FEATURE_WELD_CUSTOM1          100
#define UF_UI_SEL_FEATURE_WELD_CUSTOM2          101
#define UF_UI_SEL_FEATURE_WELD_CUSTOM3          102
#define UF_UI_SEL_FEATURE_WELD_CUSTOM4          103
#define UF_UI_SEL_FEATURE_WELD_CUSTOM5          104
#define UF_UI_SEL_FEATURE_WELD_GROOVE           105
#define UF_UI_SEL_FEATURE_WELD_FILLET           106
#define UF_UI_SEL_FEATURE_WELD_USER_DEFINED     107
#define UF_UI_SEL_FEATURE_WELD_FILL             108
#define UF_UI_SEL_FEATURE_WELD_BEAD             109
#define UF_UI_SEL_FEATURE_WELD_JOINT            110
#define UF_UI_SEL_FEATURE_WELD_EDGE             111
#define UF_UI_SEL_FEATURE_WELD_RESIS_SEAM       112
#define UF_UI_SEL_FEATURE_WELD_PLUG_SLOT        113
#define UF_UI_SEL_FEATURE_WELD_SURFACE_WELD     114
#define UF_UI_SEL_FEATURE_WELD_JOINTMARK        115
#define UF_UI_SEL_FEATURE_WELD_TRANSFORM        116
/*

*/
#define UF_UI_SEL_FEATURE_WELD_COMPOUND         117
/*

*/
#define UF_UI_SEL_FEATURE_WELD_DATUM_SURFACE    118
#define UF_UI_SEL_FEATURE_WELD_DATUM_PIN        119
#define UF_UI_SEL_FEATURE_WELD_DATUM_CUSTOM1    120
#define UF_UI_SEL_FEATURE_WELD_DATUM_CUSTOM2    121
#define UF_UI_SEL_FEATURE_WELD_DATUM_CUSTOM3    122
/*

*/
#define UF_UI_SEL_FEATURE_WELD_MEASUREMENT_SURFACE      123
#define UF_UI_SEL_FEATURE_WELD_MEASUREMENT_HOLE         124
#define UF_UI_SEL_FEATURE_WELD_MEASUREMENT_STUD         125
#define UF_UI_SEL_FEATURE_WELD_MEASUREMENT_SLOT         126
#define UF_UI_SEL_FEATURE_WELD_MEASUREMENT_TRIM         127
#define UF_UI_SEL_FEATURE_WELD_MEASUREMENT_HEMMED_EDGE  128
#define UF_UI_SEL_FEATURE_WELD_MEASUREMENT_CUSTOM1      129
#define UF_UI_SEL_FEATURE_WELD_MEASUREMENT_CUSTOM2      130
#define UF_UI_SEL_FEATURE_WELD_MEASUREMENT_CUSTOM3      131
#define UF_UI_SEL_FEATURE_MAX_SPECIAL_FEATURE   132 /* This should be last of special feature types */


/* Define UF_pseudo_object_type and corresponsing subtypes and detail types:
 * UF_pseudo_object_type is used for selection only and for object types not defined in uf_object_types.h
 */
#define UF_pseudo_object_type   (-1)

/* The subtypes for UF_pseudo_object_type: */

/* For CAE: */
#define UF_pseudo_CAE_subtype   (1)
#define UF_pseudo_CAE_node      (1) /* first CAE detail type */
#define UF_pseudo_CAE_element   (2) /* second CAE detail type */
#define UF_pseudo_CAE_elemface  (3) /* third CAE detail type */
#define UF_pseudo_CAE_elemedge  (4) /* fourth CAE detail type */


struct UF_UI_mask_s
{
    int object_type; /* This can be one of the object types that are listed in
                        uf_object_types.h or UF_pseudo_object_type */

    int object_subtype; /* This can either be UF_all_subtype (not with UF_pseudo_object_type),
                           or one of the corresponding supported subtypes of the object type specified.
                           This is ignored for certain types like UF_solid_type */

    int solid_type;  /* This should be named detail_type and is only meaningful for certain object_types like
                        UF_solid_type, UF_feature_type or UF_pseudo_type.
                        This should be set to one of the corresponding detail types
                        of the object type and object_subtype specified.
                        This is ignored for UF_all_subtype. */
} ;

typedef struct UF_UI_mask_s UF_UI_mask_t, *UF_UI_mask_p_t;

/* structure used by
 UF_UI_select_single
 UF_UI_select_by_class

*/
struct UF_UI_selection_option_s
{
    int num_mask_triples;
        UF_UI_mask_p_t mask_triples; /* <len:num_mask_triples> */
    int scope; /* scopes are listed in uf_ui.h */
    int other_options; /* initially ignored (set to 0) */
    void *reserved;    /* initially ignore (set to NULL) */
} ;

typedef struct UF_UI_selection_option_s UF_UI_selection_options_t,
*UF_UI_selection_options_p_t;

/* selection ptr which is input to UF_UI selection functions.
   This ptr is a unique identifier for the selection associated with
   a particular dialog. It is assigned by NX and provided to the
   UF programmer when needed. */
typedef void*  UF_UI_selection_p_t;

/* typedef for selection initialization procedure.
   This is an argument to UF_UI_select_with_class_dialog and
   UF_UI_select_with_single_dialog.  It is an optional procedure
   which the user can provide to customize his selection */
typedef int (*UF_UI_sel_init_fn_t)(
    UF_UI_selection_p_t select_, /* <I> ptr to selection */
    void *user_data  /* <I> ptr to user data */
);

/* typedef for application selection filter procedure.
   This procedure and optional user data is specified by calling
   UF_UI_set_sel_procs.
   It is an optional procedure which the user can provide to perform
   application specific filtering when selecting objects.
   It can be used with UF_UI_select_with_single_dialog,
   UF_UI_select_with_class_dialog and
   dialogs created with the UI Styler. */
typedef int (*UF_UI_sel_filter_fn_t)(
    tag_t object,                      /* <I> candidate object */
    int type[3],                       /* <I> object type, object subtype,
                                              solid type */
    void *user_data,                   /* <I> ptr to user's data  */
    UF_UI_selection_p_t select_ /* <I> ptr to selection */);

/* typedef for application selection callback.
   This procedure and optional user data is specified by calling
   UF_UI_set_set_procs.
   It is an optional procedure which the user can provide to perform
   application specific processing for each selection.
   This can be used with  UF_UI_select_with_single_dialog,
   UF_UI_select_with_class_dialog and
   dialogs created with the UI Styler */
typedef int (*UF_UI_sel_cb_fn_t)(
    int num_selected,               /* <I> number of objects just selected */
    tag_p_t selected_objects,       /* <I,len:num_selected>
                                                                                array of selected objects */
    int num_deselected,             /* <I> number of objects just deselected */
    tag_p_t deselected_objects,     /* <I,len:num_deselected>
                                                                                array of deselected objects */
    void *user_data,                /* <I> ptr to user's data */
    UF_UI_selection_p_t select_  /* <I> ptr to selection */);


/* typedefs for motion callbacks, which can be passed to
    UF_UI_specify_screen_position.
 */
struct UF_UI_motion_cb_data_s
{
    tag_t view_tag;            /* The tag of the current view of the
                               crosshairs. */

    double start_position[3];  /* Screen position at the time this "gesture"
                                * was started.  This is the position in
                                * Work Part Absolute Coords obtained by
                                * projecting the cursor position "through the
                                * screen" onto the XY plane of the WCS;
                                * if Grid Snap is on, this is the "snapped"
                                * position.                                */
    tag_t start_view_tag;      /* The view tag of the start position.      */

} ;

typedef struct UF_UI_motion_cb_data_s UF_UI_motion_cb_data_t,
*UF_UI_motion_cb_data_p_t;

typedef void (*UF_UI_motion_fn_t)(
              double  screen_pos[3],  /* <I> The current screen position in
                                       *     Work Part Absolute Coordinates;
                                       *     This is the crosshair position
                                       *     projected "through the screen"
                                       *     onto the XY plane of the WCS;
                                       *     if Grid Snap is on, this is the
                                       *     "snapped" position.            */
              UF_UI_motion_cb_data_p_t motion_cb_data,
                                      /* <I> Ptr to a UF_UI_motion_cb_data_t
                                       *     structure.                     */
              void   *data            /* <I> The client data, provided with
                                       *     the callback.                  */
             );


/* User Function Custom Applications prototypes
   constant definitions and type definitions */

#define UF_UI_END_MENU {UF_UI_END_CUSTOM_MENU,NULL,\
                        NULL,FALSE,NULL,NULL}
#define UF_UI_END_CASCADE_MENU {UF_UI_END_CUSTOM_CASCADE_MENU,\
                        NULL,NULL,FALSE,NULL,NULL}


enum UF_UI_MENU_TYPE_e{
  UF_UI_MENU = 1,                  /* menu item                */
  UF_UI_CASCADE_MENU,              /* cascade pulldown         */
  UF_UI_PUSH,                      /* push button              */
  UF_UI_TOGGLE,                    /* Toggle button for pulldown */
  UF_UI_BUTTON_SEPARATOR,          /* pulldown items separator */
  UF_UI_END_CUSTOM_CASCADE_MENU,   /* end of cascade pulldown  */
  UF_UI_END_CUSTOM_MENU            /* end of menu item         */
} ;

typedef enum UF_UI_MENU_TYPE_e UF_UI_MENU_TYPE;

typedef void            (*UF_UI_cb_proc)(void);
struct UF_UI_menubar_item_s
{
  UF_UI_MENU_TYPE   type;    /* may be any type in UF_UI_MENU_TYPE above */
  char             *text;    /* label to put on the button         */
  char             *name;    /* name of the resource for button    */
  int               state;   /* state of the button                */
  UF_UI_cb_proc     CBproc;  /* activate callback procedure        */
  void             *CBdata;  /* activate callback data             */
};

typedef struct UF_UI_menubar_item_s UF_UI_menubar_item_t,
*UF_UI_menubar_item_p_t;

#define UF_UI_enable_all       1
#define UF_UI_disable_all      2
#define UF_UI_enable_specific  3
#define UF_UI_disable_specific 4


/******************************************************************************
 * Type definitions for UF_UI_<create|open>_part error handling routines
 ******************************************************************************/

/* Structure containing the user data to pass to the error handling function */
struct UF_UI_err_data_s {
    int         size;  /* Size of 'data' in bytes */
    const void *data;  /* Pointer to data to pass to error handling function */
} ;

typedef struct UF_UI_err_data_s UF_UI_err_data_t,
*UF_UI_err_data_p_t;

/******************************************************************************
 logical (*UF_UI_create_part_err_f_t)
 Return:
      TRUE  - Redisplay the File-New dialog (i.e. keep trying to create a
              part)
      FALSE - Exit the File-New dialog (i.e. exit UF_UI_create_part)
 Environment:
 see also:
 History:
 ******************************************************************************/
typedef logical (*UF_UI_create_part_err_f_t)(
  UF_UI_err_data_p_t  error_fn_data, /* <I>
                                     User data
                                     */
  char               *file_name,     /* <I>
                                     File name specified in the File-New dialog
                                     */
  int                 error,         /* <I>
                                     Error code associated with file_name
                                     */
  logical            *skip_error_disp /* <O>
                                      Display standard File-New dialog error i
                                      message indicator
                                      TRUE  - Allow File-New to display the
                                      error message it would normally display
                                      FALSE - Do not allow File-New to display
                                      the message it would normally display
                                      */
);

/******************************************************************************
 logical (*UF_UI_open_part_err_f_t)

 Return:
     TRUE  - Redisplay the File-Open dialog (i.e. keep trying to open a
             part)
     FALSE - Exit the File-Open dialog (i.e. exit UF_UI_open_part)
 Environment:
 See also:
 History:
 ******************************************************************************/
typedef logical (*UF_UI_open_part_err_f_t)(
 UF_UI_err_data_p_t     error_fn_data, /* <I>
                                       User data
                                       */
 char                  *file_name,     /* <I>
                                       File name specified in the File-Open
                                       dialog
                                       */
 int                    error,       /* <I>
                                     Error code associated with file_name
                                     */
 UF_PART_load_status_t *error_status, /* <I>
                                      Structure filled with names and associated
                                      error codes of any parts that did not load
                                      properly.
                                      NOTE: The allocated arrays must be freed.
                                      */
 logical               *skip_error_disp /* <O>
                                        Display standard File-Open dialog error
                                        message indicator
                                        TRUE  - Allow File-Open to display the
                                        error it would normally display
                                        FALSE - Do not allow File-Open to
                                        display the error message it would
                                        normally display
                                        */

);

/* Definitions for type of error handling function */
enum UF_UI_fun_type_e{
    UF_UI_create_part_fun,
    UF_UI_open_part_fun
} ;

typedef enum UF_UI_fun_type_e UF_UI_fun_type_t;

/* General error handling function type */
union UF_UI_err_u {
    UF_UI_create_part_err_f_t create;
    UF_UI_open_part_err_f_t   open;
} ;

typedef union UF_UI_err_u UF_UI_err_u_t;

/* Structure containing error handling function and the user data to pass
 * to it */
struct UF_UI_err_s {
    UF_UI_fun_type_t  type;      /* Type of function in 'fun' */
    UF_UI_err_u_t     fun;       /* UF_UI_<create|open>_part error function */
    UF_UI_err_data_t  fun_data;  /* Pointer to data to pass to 'fun' */
} ;

typedef struct UF_UI_err_s UF_UI_err_t, *UF_UI_err_p_t;


/* Toolbar id returned by UF_UI_create_toolbar() */
typedef struct UF_UI_toolbar_id_s *UF_UI_toolbar_id_t;

/* Toolbar id returned by UF_UI_create_ribbon() */
typedef struct UF_UI_toolbar_id_s *UF_UI_ribbon_id_t;


/* UF feature selection type enum */
enum UF_UI_feat_sel_type_e
{
   UF_UI_FEAT_SEL_TYPE_BROWSEABLE = 0,     /* General browseable feature */
   UF_UI_FEAT_SEL_TYPE_NO_BOOLEAN_UDF,     /* No boolean and udf features */
   UF_UI_FEAT_SEL_TYPE_LAST                /* Last enum mark, don't use this. */
};
typedef enum UF_UI_feat_sel_type_e UF_UI_feat_sel_type_t;


/* enum for UF_UI_point_construct */
enum UF_UI_point_base_method_e
{
    UF_UI_POINT_INFERRED = 0,
    UF_UI_POINT_CURSOR_POS,
    UF_UI_POINT_EXISTING_PT,
    UF_UI_POINT_END_PT,
    UF_UI_POINT_CONTROL_PT,
    UF_UI_POINT_INTERSECT_PT,
    UF_UI_POINT_CENTER_PT,
    UF_UI_POINT_ANGLE_PT,
    UF_UI_POINT_QUADRANT_PT,
    UF_UI_POINT_ON_CURVE_PT,
    UF_UI_POINT_ON_SURFACE_PT,
    UF_UI_POINT_OFFSET_CSYS_PT,
    UF_UI_POINT_DIALOG,
    UF_UI_POINT_NO_METHOD,
    UF_UI_POINT_APPLICATION_METHOD
};
typedef enum UF_UI_point_base_method_e UF_UI_POINT_base_method_t, *UF_UI_POINT_base_method_p_t;

/* Defines for File Operation callback for UI Styler
   created dialogs.  */
#define UF_UI_FILE_NEW              (0)
#define UF_UI_FILE_OPEN             (1)
#define UF_UI_FILE_SAVE             (2)
#define UF_UI_FILE_SAVE_AS          (3)
#define UF_UI_FILE_SAVE_ALL         (4)
#define UF_UI_FILE_CLOSE            (5)
#define UF_UI_FILE_QUIT             (6)
#define UF_UI_FILE_SAVE_AND_EXIT    (7)
#define UF_UI_FILE_CHANGE_PART      (8)
#define UF_UI_FILE_EXECUTE          (9)
#define UF_UI_FILE_REOPEN           (10)
#define UF_UI_FILE_SAVEALL_AND_CLOSE (11)
#define UF_UI_FILE_SAVE_AND_CLOSE   (12)
#define UF_UI_FILE_SAVEAS_AND_CLOSE (13)

struct UF_UI_attachment_s
{
    short center;
    short attach_type_top;
    short attach_type_left;
    short attach_type_right;
    short offset_top;
    short offset_left;
    short offset_right;
    const char *item_id_top;
    const char *item_id_left;
    const char *item_id_right;
};
typedef struct UF_UI_attachment_s UF_UI_attachment_t, *UF_UI_attachment_p_t;

#define UF_UI_ATTACH_DIALOG    (-1)
#define UF_UI_ATTACH_DEFAULT   (-2)
#define UF_UI_ATTACH_NONE      (-3)
#define UF_UI_ATTACH_NO_CHANGE (-4)
#define UF_UI_ATTACH_ITEM      (-5)

/* Option Toggle Data */
struct UF_UI_option_toggle_s
{
    int choice;         /* active option */
    logical is_checked; /* check box state */
};
typedef struct UF_UI_option_toggle_s UF_UI_option_toggle_t, *UF_UI_option_toggle_p_t;

#ifdef __cplusplus
}
#endif

#endif /*  UF_UI_TYPES_H_INCLUDED  */
