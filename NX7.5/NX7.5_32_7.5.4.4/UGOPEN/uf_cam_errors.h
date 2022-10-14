/*****************************************************************************
 *            Copyright (c) 1998-2004 Unigraphics Solutions, Inc.
 *                      Unpublished - All Rights Reserved                       
 * File Name: uf_cam_errors.h
 *
 * 
 *
 *
 * File Description:
 *  This file defines those error codes which are specific to the CAM User
 *  Function API. They do not duplicate any error codes of the NX CAM core
 *  modules. A CAM User Function might return any NX core module error code
 *  as well as any of the error codes defined here.
 *
 *  This file contains all such CAM User Function error codes regardless of
 *  what CAM User Function module they pertain to. In this way, the programmer
 *  has access to all CAM User Function error codes by including this one
 *  file instead of including a separate file for each CAM User Function module.
 *
 ******************************************************************************/
#ifndef UF_CAM_ERRORS_H_INCLUDED
#define UF_CAM_ERRORS_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif


/***************************** Include Files **********************************/

/******************************** Defines *************************************/

/*  */

#define ERROR_UF_CAM_base      1345000
#define UF_CAM_ERROR_INVALID_INPUT                (ERROR_UF_CAM_base)
#define UF_CAM_ERROR_NO_CURRENT_OPT               (ERROR_UF_CAM_base + 1)
#define UF_OPER_ERROR_NO_TEMPLATE                 (ERROR_UF_CAM_base + 2)
#define UF_OPER_ERROR_TEMPLATE_NAME_NOT_FOUND     (ERROR_UF_CAM_base + 3)
#define UF_CAM_SESSION_ERROR_NO_SESSION           (ERROR_UF_CAM_base + 4)
#define UF_CAM_ERROR_OBJECT_NOT_DESIRED_CLASS     (ERROR_UF_CAM_base + 5)
#define UF_CAM_ERROR_TAG_IS_NOT_TAGGED_OBJECT     (ERROR_UF_CAM_base + 6)
#define UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE         (ERROR_UF_CAM_base + 7)
#define UF_CAM_ERROR_OBJECT_IS_NOT_TAGGED_OBJECT  (ERROR_UF_CAM_base + 8)
#define UF_SETUP_ERROR_USE_NEW_POST_FUNCTION      (ERROR_UF_CAM_base + 9)
#define UF_PARAM_ERROR_CHECK_FAILED               (ERROR_UF_CAM_base + 10)
#define UF_UI_ONT_ERROR_ONT_DOES_NOT_EXIST        (ERROR_UF_CAM_base + 11)
#define UF_PARAM_ERROR_MAP_FAILED                 (ERROR_UF_CAM_base + 12)
#define UF_PARAM_ERROR_LICENSE_FAILURE            (ERROR_UF_CAM_base + 13)
#define UF_UDE_PARAM_NOT_INTEGER_TYPE             (ERROR_UF_CAM_base + 14)
#define UF_UDE_PARAM_NOT_DOUBLE_TYPE              (ERROR_UF_CAM_base + 15)
#define UF_UDE_PARAM_NOT_STRING_OR_OPTION_TYPE    (ERROR_UF_CAM_base + 16)
#define UF_UDE_PARAM_NOT_BOOLEAN_TYPE             (ERROR_UF_CAM_base + 17)
#define UF_UDE_PARAM_NOT_POINT_TYPE               (ERROR_UF_CAM_base + 18)
#define UF_UDE_PARAM_NOT_VECTOR_TYPE              (ERROR_UF_CAM_base + 19)
#define UF_UDE_PARAM_DOES_NOT_EXIST               (ERROR_UF_CAM_base + 20)
#define UF_UDE_PARAM_IS_NOT_OPTIONAL              (ERROR_UF_CAM_base + 21)
#define UF_UDE_NOT_VALID_SET                      (ERROR_UF_CAM_base + 22)
#define UF_CAM_ERROR_NO_SETUP                     (ERROR_UF_CAM_base + 23)
#define UF_CAM_ERROR_NOT_PLANAR_FACE              (ERROR_UF_CAM_base + 24)
#define UF_CAM_ERROR_INVALID_INPUT_ENTITY         (ERROR_UF_CAM_base + 25)
#define UF_CAM_ERROR_INVALID_APP_DATA             (ERROR_UF_CAM_base + 26)
#define UF_CAM_ERROR_FROM_TURNING_PROCESSOR       (ERROR_UF_CAM_base + 27)
#define UF_CAM_ERROR_SAVE_SPINNING_IPW_AS_PART    (ERROR_UF_CAM_base + 28)
#define UF_CAM_ERROR_NOT_AUTO_BLANK               (ERROR_UF_CAM_base + 29)
#define UF_CAM_ERROR_PLANE_NOT_DEFINED            (ERROR_UF_CAM_base + 30)
#define UF_CAM_ERROR_DATA_NOT_CORRECT_TYPE        (ERROR_UF_CAM_base + 31)
#define UF_CAM_ERROR_PREFERENCE_NOT_DEFINED       (ERROR_UF_CAM_base + 32)
#define UF_CAM_ERROR_DUPLICATE_NAME               (ERROR_UF_CAM_base + 33)
#define UF_CAM_ERROR_INVALID_GROUP_DATA           (ERROR_UF_CAM_base + 34)
#define UF_CAM_ERROR_INVALID_INHERITED_ENTITY     (ERROR_UF_CAM_base + 35)
#define UF_CAM_ERROR_INVALID_INDEX                (ERROR_UF_CAM_base + 36)
#define UF_CAM_ERROR_IPW_DOES_NOT_EXIST           (ERROR_UF_CAM_base + 37)
#define UF_CAM_ERROR_INCONSISTENT_IPW_BOX         (ERROR_UF_CAM_base + 38)
#define UF_CAM_ERROR_POINT_NOT_FOUND              (ERROR_UF_CAM_base + 39)
#define UF_CAM_ERROR_INVALID_RADIUS               (ERROR_UF_CAM_base + 40)
#define UF_CAM_ERROR_INVALID_DIAMETER             (ERROR_UF_CAM_base + 41)
#define UF_CAM_ERROR_INVALID_LENGTH               (ERROR_UF_CAM_base + 42)
#define UF_CAM_ERROR_INVALID_TAPER                (ERROR_UF_CAM_base + 43)
#define UF_CAM_ERROR_UNDEFINED_TURN_WORKPIECE_TYPE         (ERROR_UF_CAM_base + 44)
#define UF_CAM_ERROR_INVALID_TYPE_OF_WORKPIECE             (ERROR_UF_CAM_base + 45)
#define UF_CAM_ERROR_INVALID_TURN_WORKPIECE_LENGTH         (ERROR_UF_CAM_base + 46)
#define UF_CAM_ERROR_INVALID_TURN_WORKPIECE_DIAMETER       (ERROR_UF_CAM_base + 47)
#define UF_CAM_ERROR_INVALID_TURN_WORKPIECE_INNER_DIAMETER (ERROR_UF_CAM_base + 48)
#define UF_CAM_ERROR_INVALID_TURN_WORKPIECE_DIRECTION      (ERROR_UF_CAM_base + 49)
#define UF_CAM_ERROR_INVALID_TURN_WORKPIECE_STOCK          (ERROR_UF_CAM_base + 50)
#define UF_CAM_ERROR_READ_ONLY_PARAM              (ERROR_UF_CAM_base + 51)
#define UF_CAM_ERROR_INVALID_DRIVE_METHOD         (ERROR_UF_CAM_base + 52)
#define UF_CAM_ERROR_INVALID_DRIVE_GEOMETRY       (ERROR_UF_CAM_base + 53)
#define UF_CAM_ERROR_CUT_LEVELS_NOT_SUPPORTED     (ERROR_UF_CAM_base + 54)
#define UF_CAM_ERROR_CUT_LEVEL_CHANGE_NOT_MADE    (ERROR_UF_CAM_base + 55)
#define UF_CAM_ERROR_INVALID_CUT_LEVEL_ENTITY     (ERROR_UF_CAM_base + 56)
#define UF_CAM_ERROR_SINGLE_RANGE_NOT_CHANGED     (ERROR_UF_CAM_base + 57)
#define UF_CAM_ERROR_INVALID_CUSTOM_POINT_TYPE    (ERROR_UF_CAM_base + 58)
#define UF_CAM_ERROR_NO_MATCHING_RECORD           (ERROR_UF_CAM_base + 59)
#define UF_CAM_ERROR_GOUGE_CHECK_NOT_SUPPORTED    (ERROR_UF_CAM_base + 60)
#define UF_CAM_ERROR_NO_FEEDS_SPEEDS_LIBRARY      (ERROR_UF_CAM_base + 61)
#define UF_CAM_ERROR_NO_PART_MATERIAL             (ERROR_UF_CAM_base + 62)
#define UF_CAM_ERROR_NO_TOOL_MATERIAL             (ERROR_UF_CAM_base + 63)
#define UF_CAM_ERROR_NO_CUT_METHOD                (ERROR_UF_CAM_base + 64)
#define UF_CAM_ERROR_DATA_MATCH                   (ERROR_UF_CAM_base + 65)
#define UF_CAM_ERROR_DATA_NOT_AVAILABLE           (ERROR_UF_CAM_base + 66)
#define UF_CAM_ERROR_LIBRARY_NOT_FOUND            (ERROR_UF_CAM_base + 67)
#define UF_CAM_ERROR_NOT_LIBRARY_TOOL             (ERROR_UF_CAM_base + 68)
#define UF_CAM_ERROR_TOOLS_NOT_SAME_TYPE          (ERROR_UF_CAM_base + 69)
#define UF_CAM_ERROR_INSPECTION_SETUP             (ERROR_UF_CAM_base + 70)
#define UF_CAM_ERROR_MANUFACTURING_SETUP          (ERROR_UF_CAM_base + 71)
#define UF_CAM_ERROR_INSPECTION_TEMPLATE          (ERROR_UF_CAM_base + 72)
#define UF_CAM_ERROR_MANUFACTURING_TEMPLATE       (ERROR_UF_CAM_base + 73)
#ifdef __cplusplus
}
#endif


#endif /* UF_CAM_ERRORS_H_INCLUDED */
