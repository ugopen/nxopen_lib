 /*****************************************************************************
  
              Copyright (c) 1998-1999 Unigraphics Solutions Inc.
                         Unpublished - All rights reserved



File description:
   Language Definitions for the Scenario User Function module.
 *****************************************************************************/
#ifndef  UF_SF_LANG_NAMES__H_INCLUDED
#define  UF_SF_LANG_NAMES__H_INCLUDED

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif
 
/* Maximum length of a language name (number of characters)           
   UF_SF_LANG_MAX_NAME_LENGTH is deprecated. Use UF_SF_LANG_MAX_NAME_BUFSIZE instead */
/*  */
#define UF_SF_LANG_MAX_NAME_LENGTH            200
/*  */
#define UF_SF_LANG_MAX_NAME_NCHARS 199
#define UF_SF_LANG_MAX_NAME_BUFSIZE NX_BUFSIZE(UF_SF_LANG_MAX_NAME_NCHARS)

/* The string returned when there is no current language defined yet.   */
#define UF_SF_LANG_NEUTRAL                    "Neutral Lang.  "

/* The string used to wildcard to the current language.                 */
#define UF_SF_LANG_CURRENT                    "Current Lang.  "

/* The string used to wildcard when there is no current language.      */
#define UF_SF_LANG_NO_CURRENT                    "No defined environment"

#define UF_SF_LANG_NOT_DEFINED_OPTION "@@NOT@DEFINED"

#define UF_SF_FREE_VALUE   -777777.0

#define UF_SF_MESH_VISUAL_NO_CHANGE   -7777

/*************************************/
/* define element names for language */
/*************************************/

/* Use UF_SF_CONTACT_ELEMENT for follwing solver elements:
   MSC/NASTRAN - GAP
   ANSYS - CONTAC12
   ANSYS - CONTAC52
*/

#define UF_SF_CONTACT_ELEMENT             "Contact"

/* Use UF_SF_CONTACT_SPRING_ELEMENT for follwing solver elements:
   ANSYS - COMBIN40
*/

#define UF_SF_CONTACT_SPRING_ELEMENT      "Contact-Spring"


/* There are the official names of the environment definitions.         */

#define UF_SF_LANG_MSC_NASTRAN_STR_SIMPLE        "UG/FEA/Linear Statics"
#define UF_SF_LANG_MSC_NASTRAN_STR_SIMPLE_VER    2

#define UF_SF_LANG_MSC_NASTRAN_AXIS        "UG/FEA/Linear Statics/Axisymmetric"
#define UF_SF_LANG_MSC_NASTRAN_AXIS_VER          2

#define UF_SF_LANG_MSC_NASTRAN_THERMAL     "UG/FEA/Steady State Heat Transfer"
#define UF_SF_LANG_MSC_NASTRAN_THERMAL_VER       2

#define UF_SF_LANG_MSC_NASTRAN_THERMAL_AXIS                      \
                           "UG/FEA/Steady State Heat Transfer/Axisymmetric"
#define UF_SF_LANG_MSC_NASTRAN_THERMAL_AXIS_VER  2

#define UF_SF_LANG_MSC_NASTRAN_MODAL             "UG/FEA/Normal Modes"
#define UF_SF_LANG_MSC_NASTRAN_MODAL_VER         2

#define UF_SF_LANG_MSC_NASTRAN_STR_SIMPLE_NL     "MSC/NASTRAN/Nonlinear Statics"
#define UF_SF_LANG_MSC_NASTRAN_STR_SIMPLE_NL_VER 0

/* This is the official name of the MSC/Nastran solver.                 */
#define UF_SF_LANG_MSC_NASTRAN_NAME      "UG/FEA"

/* This is the official name of the Nonlinear MSC/Nastran solver.       */
#define UF_SF_LANG_MSC_NASTRAN_NL_NAME      "MSC/NASTRAN"


#define UF_SF_LANG_FEA_ADAPT_STR_SIMPLE      "UG/FEA p-Adaptive/Linear Statics"
#define UF_SF_LANG_FEA_ADAPT_STR_SIMPLE_VER      0

#define UF_SF_LANG_FEA_ADAPT_MODAL_SIMPLE    "UG/FEA p-Adaptive/Normal Modes"
#define UF_SF_LANG_FEA_ADAPT_MODAL_SIMPLE_VER    0

/* This is the official name of the OPTIMA solver.                    */
#define UF_SF_LANG_FEA_ADAPT_NAME               "UG/FEA p-Adaptive"

/* This is the Linear Buckling Environment for NASTRAN */

#define UF_SF_LANG_MSC_NASTRAN_STR_SIMPLE_LB        "UG/FEA/Linear Buckling"
#define UF_SF_LANG_MSC_NASTRAN_STR_SIMPLE_LB_VER    0

#define UF_SF_LANG_MSC_NASTRAN_AXIS_LB    "UG/FEA/Linear Buckling/Axisymmetric"
#define UF_SF_LANG_MSC_NASTRAN_AXIS_LB_VER          0



/* This is the ANSYS env. definition */

#define UF_SF_LANG_ANSYS_STR_SIMPLE              "ANSYS/Linear Statics Plus"
#define UF_SF_LANG_ANSYS_STR_SIMPLE_VER          2

#define UF_SF_LANG_ANSYS_AXIS          "ANSYS/Linear Statics Plus/Axisymmetric"
#define UF_SF_LANG_ANSYS_AXIS_VER                2

#define UF_SF_LANG_ANSYS_THERMAL       "ANSYS/Steady State Heat Transfer"
#define UF_SF_LANG_ANSYS_THERMAL_VER             2

#define UF_SF_LANG_ANSYS_THERMAL_AXIS                                    \
                       "ANSYS/Steady State Heat Transfer/Axisymmetric"
#define UF_SF_LANG_ANSYS_THERMAL_AXIS_VER        2

#define UF_SF_LANG_ANSYS_MODAL                   "ANSYS/Normal Modes"
#define UF_SF_LANG_ANSYS_MODAL_VER               2

#define UF_SF_LANG_ANSYS_THERM_STR                                       \
                      "ANSYS/Steady State Heat Transfer - Linear Statics Plus"
#define UF_SF_LANG_ANSYS_THERM_STR_VER           2

#define UF_SF_LANG_ANSYS_THERM_STR_AXIS                                  \
         "ANSYS/Steady State Heat Transfer - Linear Statics Plus/Axisymmetric"
#define UF_SF_LANG_ANSYS_THERM_STR_AXIS_VER      2

/* This is the ANSYS env. definition for Linear Buckling */

#define UF_SF_LANG_ANSYS_STR_SIMPLE_LB              "ANSYS/Linear Buckling"
#define UF_SF_LANG_ANSYS_STR_SIMPLE_LB_VER          0

#define UF_SF_LANG_ANSYS_AXIS_LB          "ANSYS/Linear Buckling/Axisymmetric"
#define UF_SF_LANG_ANSYS_AXIS_LB_VER                0


/* This is the official name of the ANSYS solver.                       */
#define UF_SF_LANG_ANSYS_NAME                    "ANSYS"


#ifdef __cplusplus
}
#endif

#endif  /*    UF_SF_LANG_NAMES__H_INCLUDED                              */
