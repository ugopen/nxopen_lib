/*****************************************************************************
 *            Copyright (c) 1998-2001 Unigraphics Solutions, Inc.
 *                      Unpublished - All Rights Reserved
 *
 * Revision History
 *   Revision      Date       Who            Reason
 *      00      31-Sep-2001   Yakove Dayan   initial version
 *      01      24-Mar-2002   Joachim Meyer  define UF_SV_KIM_MAX_NAME_LEN
 *      02      07-Jun-2002   Thomas Schulz  added UF_SIM_KIM_degof_types_t
 *      03      26-Jul-2002   Thomas Schulz  added UF_SIM_ctrl_status_switch_t
 *                                           and UF_SIM_axis_rot_dir_type_t
 *      04      08-Feb-2005   Thomas Schulz  Change the UF_SIM_unit_type_t to
 *                                           reflect changes in SIM_unit_type_t
20-Oct-2006  Elizabeth Ford          Cleaned code to match George Documentation standards
27-Nov-2006  Linda Jeziorski         Back out some of enum format changes - compile issues
08-Mar-2007  Elizabeth Ford          PR 5711211 - doc fixes
05-Mar-2013  Sunil Pillala           Changes for ARCH9354 Internationalization All User Text
14-Mar-2013  Sunil Pillala           Changes for ARCH9354 Internationalization All User Text
 * $HISTORY$
 *
 * File description:
 * This file describes the data types used in the user function
 * S&V commands API defined in uf_sim_commands.h
 *
 ******************************************************************************/

#ifndef UF_SIM_H_INCLUDED
#define UF_SIM_H_INCLUDED

/*************************** Include Files ************************************/
#include <uf.h>
#include <uf_defs.h>
#include <uf_obj_types.h>
#include <libufun_exports.h>


/******************************** Defines *************************************/

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Public Typedefs ********************************/

/* constants for sound play */
#define UF_SV_SND_SYNC         0      /* play synchronously  */
#define UF_SV_SND_ASYNC        1      /* play asynchronously */
#define UF_SV_SND_NOSILENCE    2      /* issue error if sound not found */
#define UF_SV_SND_LOOP         4      /* loop the sound until next SV_play_sound*/
#define UF_SV_SND_NOWAIT       8      /* don't wait if the driver is busy */


/* Defines for component system classes */
#define UF_SIM_KIM_COMP_CLASS_NONE           (0)
#define UF_SIM_KIM_COMP_CLASS_MACHINE        (1<<0)
#define UF_SIM_KIM_COMP_CLASS_TOOL           (1<<1)
#define UF_SIM_KIM_COMP_CLASS_TURRET         (1<<2)
#define UF_SIM_KIM_COMP_CLASS_POCKET         (1<<3)

/*
   UF_SV_KIM_MAX_NAME_LEN is being deprecated because NX is moving to support
   multibyte characters.  User written programs should start using the
   new definitions for object names:
     UF_OBJ_NAME_BUFSIZE should be used for buffer allocations and memory
                         allocations, e.g. char sv_kim_name[UF_OBJ_NAME_BUFSIZE];
     UF_OBJ_NAME_NCHARS  should be used to limit the number of characters in
                         a buffer.  NX code will enforce these limits.
   New routines have been added which will help in this transition:
     UF_TEXT_count_characters() will count the number of characters in a string.
     UF_TEXT_truncate() will terminate a C string such that it will fit in a
                        buffer of a give size and not exceed a character count.
*/
/*  */
#define UF_SV_KIM_MAX_NAME_LEN (UF_OBJ_NAME_BUFSIZE-1)
/*  */

/*
 * This is the object id that is used to access the simulation
 * engine object. The simulation engine object is a transient object
 * and is not stored in the part file.
 */
typedef void   *UF_SIM_engine_p_t;

/*
 * The units of the SIM parameters
 */
typedef enum
{
    UF_SIM_UNIT_NONE=0,
    UF_SIM_UNIT_MM,
    UF_SIM_UNIT_M,
    UF_SIM_UNIT_INCH,
    UF_SIM_UNIT_FEET,
    UF_SIM_UNIT_SEC,
    UF_SIM_UNIT_MIN,
    UF_SIM_UNIT_MM_PER_SEC,
    UF_SIM_UNIT_MM_PER_MIN,
    UF_SIM_UNIT_M_PER_MIN,
    UF_SIM_UNIT_INCH_PER_SEC,
    UF_SIM_UNIT_INCH_PER_MIN,
    UF_SIM_UNIT_FEET_PER_MIN,
    UF_SIM_UNIT_REV_PER_SEC,
    UF_SIM_UNIT_REV_PER_MIN,
    UF_SIM_UNIT_DEG_PER_MIN,
    UF_SIM_UNIT_MM_PER_REV,
    UF_SIM_UNIT_INCH_PER_REV,
    UF_SIM_UNIT_MM_PER_100REV,
    UF_SIM_UNIT_M_PER_SEC_POW2,
    UF_SIM_UNIT_SFM,
    UF_SIM_UNIT_SMM,
    UF_SIM_UNIT_DEG_PER_SEC,
    UF_SIM_UNIT_RAD_PER_SEC,
    UF_SIM_UNIT_RAD_PER_MIN
} UF_SIM_unit_type_t;

/*
 * The units of the SIM tools classifier
 */
typedef enum
{
   UF_SIM_TOOL_CLASS_TOOL_NUMBER=0,
   UF_SIM_TOOL_CLASS_LIBRARY_REF,
   UF_SIM_TOOL_CLASS_CATALOG_NUMBER,
   UF_SIM_TOOL_CLASS_UG_NAME,
   UF_SIM_TOOL_CLASS_COMP_NAME
} UF_SIM_tool_class_t;


typedef enum
{
   UF_SIM_CUTTING_MODE_NONE=0,
   UF_SIM_CUTTING_MODE_CUT,
   UF_SIM_CUTTING_MODE_RAPID
} UF_SIM_cutting_mode_t;


typedef enum
{
   UF_SV_KIM_DEGOF_DIRECTION_NONE=0,
   UF_SV_KIM_DEGOF_DIRECTION_X_POSITIVE=1,
   UF_SV_KIM_DEGOF_DIRECTION_X_NEGATIVE=2,
   UF_SV_KIM_DEGOF_DIRECTION_Y_POSITIVE=3,
   UF_SV_KIM_DEGOF_DIRECTION_Y_NEGATIVE=4,
   UF_SV_KIM_DEGOF_DIRECTION_Z_POSITIVE=5,
   UF_SV_KIM_DEGOF_DIRECTION_Z_NEGATIVE=6
} UF_SV_KIM_degof_direction_t;

typedef enum
{
   UF_SIM_KIM_DEGOF_TYPE_NONE=0,
   UF_SIM_KIM_DEGOF_LINEAR=1,
   UF_SIM_KIM_DEGOF_ROTARY=2
} UF_SIM_KIM_degof_types_t;

typedef enum
{
   UF_SIM_CTRL_STATUS_NONE=0,
   UF_SIM_CTRL_STATUS_SEND_NC_CMD_MSG=2
} UF_SIM_ctrl_status_switch_t;

typedef enum
{
   UF_SIM_AXIS_ROT_NONE=0,
   UF_SIM_AXIS_ROT_MAGNITUDE_DETERMINES_DIRECTION,
   UF_SIM_AXIS_ROT_ALWAYS_SHORTEST,
   UF_SIM_AXIS_ROT_SIGN_DETERMINES_DIRECTION,
   UF_SIM_AXIS_ROT_ALWAYS_CLW,
   UF_SIM_AXIS_ROT_ALWAYS_CCLW
} UF_SIM_axis_rot_dir_type_t;


/************************* Public Function Definitions ************************/

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SIM_H_INCLUDED */
