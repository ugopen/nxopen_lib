/***************************************************************************

               Copyright (c) 1998-2000,2001,2002,2004,2005,2006  Unigraphics Solutions Inc.
                       Unpublished - All rights reserved





File description:

   This file contains all the error codes raised by the UF_DRF module.


****************************************************************************/

#ifndef UF_DRF_ERRORS_H_INCLUDED
#define UF_DRF_ERRORS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/
#define ERROR_UF_DRF_base      1175000 


#ifdef __cplusplus
extern "C" {
#endif

#define UF_DRF_ERROR_BASE                        ERROR_UF_DRF_base
#define UF_DRF_ERROR_RANGE                       5000
#define UF_DRF_NO_ERRORS                         0

#define IS_UF_DRF_ERROR(error)  \
    ((error >=UF_DRF_ERROR_BASE)       && (error <=(UF_DRF_ERROR_BASE + 999)))
#define IS_UF_DRF_WARNING(error) \
    ((error >=UF_DRF_ERROR_BASE + 900) && (error <=(UF_DRF_ERROR_BASE + 999)))

#define UF_DRF_invalid_parameter                (UF_DRF_ERROR_BASE +  1)
#define UF_DRF_null_object_structure            (UF_DRF_ERROR_BASE +  2)
#define UF_DRF_null_object1_structure           (UF_DRF_ERROR_BASE +  3)
#define UF_DRF_null_object2_structure           (UF_DRF_ERROR_BASE +  4)
#define UF_DRF_null_object                      (UF_DRF_ERROR_BASE +  5)
#define UF_DRF_null_object1                     (UF_DRF_ERROR_BASE +  6)
#define UF_DRF_null_object2                     (UF_DRF_ERROR_BASE +  7)
#define UF_DRF_invalid_object                   (UF_DRF_ERROR_BASE +  8)
#define UF_DRF_invalid_object1                  (UF_DRF_ERROR_BASE +  9)
#define UF_DRF_invalid_object2                  (UF_DRF_ERROR_BASE + 10)
#define UF_DRF_invalid_object_assoc_type        (UF_DRF_ERROR_BASE + 11)
#define UF_DRF_invalid_object1_assoc_type       (UF_DRF_ERROR_BASE + 12)
#define UF_DRF_invalid_object2_assoc_type       (UF_DRF_ERROR_BASE + 13)
#define UF_DRF_invalid_object_modifier          (UF_DRF_ERROR_BASE + 14)
#define UF_DRF_invalid_object1_modifier         (UF_DRF_ERROR_BASE + 15)
#define UF_DRF_invalid_object2_modifier         (UF_DRF_ERROR_BASE + 16)
#define UF_DRF_invalid_object_view_id           (UF_DRF_ERROR_BASE + 17)

#define UF_DRF_unable_to_create_crosshatching   (UF_DRF_ERROR_BASE + 18)

#define UF_DRF_invalid_linear_dim_form          (UF_DRF_ERROR_BASE + 19)
#define UF_DRF_invalid_ang_dim_form             (UF_DRF_ERROR_BASE + 20)
#define UF_DRF_invalid_circular_dim_form        (UF_DRF_ERROR_BASE + 21)
#define UF_DRF_invalid_centerline_form          (UF_DRF_ERROR_BASE + 22)

#define UF_DRF_cyl_dim_with_2_margins           (UF_DRF_ERROR_BASE + 23)
#define UF_DRF_invalid_number_of_bounds         (UF_DRF_ERROR_BASE + 24)
#define UF_DRF_invalid_number_of_objects        (UF_DRF_ERROR_BASE + 25)
#define UF_DRF_objects_not_in_same_view         (UF_DRF_ERROR_BASE + 26)
#define UF_DRF_first_object_is_a_point          (UF_DRF_ERROR_BASE + 27)
#define UF_DRF_two_points_in_a_row              (UF_DRF_ERROR_BASE + 28)
#define UF_DRF_too_many_boundaries              (UF_DRF_ERROR_BASE + 29)
#define UF_DRF_invalid_fold_location            (UF_DRF_ERROR_BASE + 30)
#define UF_DRF_invalid_origin                   (UF_DRF_ERROR_BASE + 31)
#define UF_DRF_no_text                          (UF_DRF_ERROR_BASE + 32)
#define UF_DRF_too_many_characters_in_line      (UF_DRF_ERROR_BASE + 33)
#define UF_DRF_too_many_characters_in_text      (UF_DRF_ERROR_BASE + 34)
#define UF_DRF_invalid_leader_mode              (UF_DRF_ERROR_BASE + 35)
#define UF_DRF_invalid_leader_type              (UF_DRF_ERROR_BASE + 36)
#define UF_DRF_invalid_leader_attach_type       (UF_DRF_ERROR_BASE + 37)
#define UF_DRF_invalid_frame_corner             (UF_DRF_ERROR_BASE + 38)
#define UF_DRF_invalid_id_symbol_type           (UF_DRF_ERROR_BASE + 39)
#define UF_DRF_no_objects                       (UF_DRF_ERROR_BASE + 40)
#define UF_DRF_too_many_objects                 (UF_DRF_ERROR_BASE + 41)
#define UF_DRF_form_requires_1_object           (UF_DRF_ERROR_BASE + 42)
#define UF_DRF_form_requires_2_objects          (UF_DRF_ERROR_BASE + 43)
#define UF_DRF_form_requires_3_or_more_objects  (UF_DRF_ERROR_BASE + 44)
#define UF_DRF_coincident_points                (UF_DRF_ERROR_BASE + 45)
#define UF_DRF_point_not_on_centerline          (UF_DRF_ERROR_BASE + 46)
#define UF_DRF_point_coincident_with_center     (UF_DRF_ERROR_BASE + 47)
#define UF_DRF_collinear_points                 (UF_DRF_ERROR_BASE + 48)
#define UF_DRF_invalid_object_type_centerline   (UF_DRF_ERROR_BASE + 49)
#define UF_DRF_invalid_object_type_center_point (UF_DRF_ERROR_BASE + 50)
#define UF_DRF_invalid_object_type_offset_point (UF_DRF_ERROR_BASE + 51)
#define UF_DRF_offset_center_point_requires_arc (UF_DRF_ERROR_BASE + 52)

#define UF_DRF_drawing_is_active                (UF_DRF_ERROR_BASE + 53)
#define UF_DRF_model_objects_on_drawing         (UF_DRF_ERROR_BASE + 54)
#define UF_DRF_dim_not_drawing_object           (UF_DRF_ERROR_BASE + 55)
#define UF_DRF_crosshatch_file_not_found        (UF_DRF_ERROR_BASE + 56)
#define UF_DRF_cannot_close_xhatch_file         (UF_DRF_ERROR_BASE + 57)
#define UF_DRF_material_definition_not_found    (UF_DRF_ERROR_BASE + 58)

#define UF_DRF_unknown_error                    (UF_DRF_ERROR_BASE + 59)
#define UF_DRF_unrecoverable_error              (UF_DRF_ERROR_BASE + 60)
#define UF_DRF_invalid_parameter_value          (UF_DRF_ERROR_BASE + 61)
#define UF_DRF_invalid_view                     (UF_DRF_ERROR_BASE + 62)
#define UF_DRF_tag_is_null                      (UF_DRF_ERROR_BASE + 63)
#define UF_DRF_no_boundary                      (UF_DRF_ERROR_BASE + 64)
#define UF_DRF_no_boundary_members              (UF_DRF_ERROR_BASE + 65)
#define UF_DRF_no_text_found                    (UF_DRF_ERROR_BASE + 66)
#define UF_DRF_ud_symbol_data_not_found         (UF_DRF_ERROR_BASE + 67)
#define UF_DRF_not_a_label                      (UF_DRF_ERROR_BASE + 68)
#define UF_DRF_not_a_id_symbol                  (UF_DRF_ERROR_BASE + 69)
#define UF_DRF_not_a_gdt_symbol                 (UF_DRF_ERROR_BASE + 70)
#define UF_DRF_not_a_dimension                  (UF_DRF_ERROR_BASE + 71)
#define UF_DRF_not_a_centerline                 (UF_DRF_ERROR_BASE + 72)
#define UF_DRF_not_a_folded_radius_dim          (UF_DRF_ERROR_BASE + 73)
#define UF_DRF_not_an_ordinate_origin           (UF_DRF_ERROR_BASE + 74)
#define UF_DRF_not_a_ordinate_margin            (UF_DRF_ERROR_BASE + 75)
#define UF_DRF_invalid_line_assoc_type          (UF_DRF_ERROR_BASE + 76)
#define UF_DRF_object_is_not_a_line             (UF_DRF_ERROR_BASE + 77)
#define UF_DRF_no_margin_to_convert             (UF_DRF_ERROR_BASE + 78)
#define UF_DRF_arc_is_not_in_same_view          (UF_DRF_ERROR_BASE + 79)
#define UF_DRF_error_in_k25h7pa                 (UF_DRF_ERROR_BASE + 80)
#define UF_DRF_not_a_cylindrical_dim            (UF_DRF_ERROR_BASE + 81)
#define UF_DRF_INVALID_SYMBOL_NAME              (UF_DRF_ERROR_BASE + 82)
#define UF_DRF_SYMBOL_NAME_EXISTS               (UF_DRF_ERROR_BASE + 83)
#define UF_DRF_SYMBOL_NAME_DOES_NOT_EXIST       (UF_DRF_ERROR_BASE + 84)
#define UF_DRF_ERROR_OPENING_CURRENT_SBF_FILE   (UF_DRF_ERROR_BASE + 85)
#define UF_DRF_NO_SBF_FILE_NAME                 (UF_DRF_ERROR_BASE + 86)
#define UF_DRF_INVALID_ANCHOR_POINT_OBJECT      (UF_DRF_ERROR_BASE + 87)
#define UF_DRF_COINCIDENT_ANCHOR_ORIENTATION_PT (UF_DRF_ERROR_BASE + 88)
#define UF_DRF_CANNOT_PROCESS_SYMBOL_FONT       (UF_DRF_ERROR_BASE + 89)
#define UF_DRF_INVALID_SYMBOL_FONT_OBJECTS      (UF_DRF_ERROR_BASE + 90)
#define UF_DRF_NOT_DRAFTING_OBJECT              (UF_DRF_ERROR_BASE + 91)
#define UF_DRF_NO_VALID_COMPONENT_FOUND         (UF_DRF_ERROR_BASE + 92)

#define UF_DRF_INVALID_OBJ_FOR_ASSORTED_PARTS   (UF_DRF_ERROR_BASE + 93)
#define UF_DRF_INVALID_CROSSHATCH_FILE_FORMAT   (UF_DRF_ERROR_BASE + 94)
#define UF_DRF_INVALID_TOLERANCE_TYPE           (UF_DRF_ERROR_BASE + 95)
#define UF_DRF_INVALID_TEXT_ARROW_PLACEMENT     (UF_DRF_ERROR_BASE + 96)
#define UF_DRF_INVALID_EXTENSION_LINE_DISPLAY   (UF_DRF_ERROR_BASE + 97)
#define UF_DRF_INVALID_ARROW_DISPLAY            (UF_DRF_ERROR_BASE + 98)
#define UF_DRF_INVALID_DIMENSION_ORIENTATION    (UF_DRF_ERROR_BASE + 99)
#define UF_DRF_INVALID_NUMBER_OF_DECIMAL_PLACES (UF_DRF_ERROR_BASE + 100)
#define UF_DRF_INVALID_FRACTION_DENOMINATOR     (UF_DRF_ERROR_BASE + 101)
#define UF_DRF_INVALID_ARROW_TYPE               (UF_DRF_ERROR_BASE + 102)
#define UF_DRF_INVALID_LEADER_LOCATION          (UF_DRF_ERROR_BASE + 103)
#define UF_DRF_INVALID_COLOR                    (UF_DRF_ERROR_BASE + 104)
#define UF_DRF_INVALID_FONT                     (UF_DRF_ERROR_BASE + 105)
#define UF_DRF_INVALID_WIDTH                    (UF_DRF_ERROR_BASE + 106)
#define UF_DRF_INVALID_ALIGN_POSITION           (UF_DRF_ERROR_BASE + 107)
#define UF_DRF_INVALID_LINEAR_UNITS             (UF_DRF_ERROR_BASE + 108)
#define UF_DRF_INVALID_LINEAR_FRACTION_TYPE     (UF_DRF_ERROR_BASE + 109)
#define UF_DRF_INVALID_DECIMAL_POINT_CHARACTER  (UF_DRF_ERROR_BASE + 110)
#define UF_DRF_INVALID_DIMENSION_TOL_PLACEMENT  (UF_DRF_ERROR_BASE + 111)
#define UF_DRF_INVALID_DIMENSION_ANGULAR_FORMAT (UF_DRF_ERROR_BASE + 112)
#define UF_DRF_INVALID_DUAL_DIMENSION_FORMAT    (UF_DRF_ERROR_BASE + 113)
#define UF_DRF_INVALID_DUAL_DIMENSION_UNITS     (UF_DRF_ERROR_BASE + 114)
#define UF_DRF_INVALID_DUAL_FRACTION_TYPE       (UF_DRF_ERROR_BASE + 115)
#define UF_DRF_INVALID_DIAMETER_SYMBOL_TYPE     (UF_DRF_ERROR_BASE + 116)
#define UF_DRF_INVALID_RADIUS_SYMBOL_TYPE       (UF_DRF_ERROR_BASE + 117)
#define UF_DRF_INVALID_DIAM_RADIUS_PLACEMENT    (UF_DRF_ERROR_BASE + 118)
#define UF_DRF_INVALID_TEXT_PLACEMENT           (UF_DRF_ERROR_BASE + 119)
#define UF_DRF_INVALID_AREA_FILL_MATERIAL       (UF_DRF_ERROR_BASE + 120)
#define UF_DRF_INVALID_ARROW_FILL_STATUS        (UF_DRF_ERROR_BASE + 121)
#define UF_DRF_INVALID_ARROWHEAD_LENGTH         (UF_DRF_ERROR_BASE + 122)
#define UF_DRF_INVALID_DOT_DIAMETER             (UF_DRF_ERROR_BASE + 123)
#define UF_DRF_INVALID_STUB_LENGTH              (UF_DRF_ERROR_BASE + 124)
#define UF_DRF_INVALID_TEXT_TO_LINE_DISTANCE    (UF_DRF_ERROR_BASE + 125)
#define UF_DRF_INVALID_LINE_PAST_ARROW_DISTANCE (UF_DRF_ERROR_BASE + 126)
#define UF_DRF_INVALID_FIRST_POS_TO_EXTENSION_LINE_DISTANCE  \
                                                (UF_DRF_ERROR_BASE + 127)
#define UF_DRF_INVALID_SECOND_POS_TO_EXTENSION_LINE_DISTANCE \
                                                (UF_DRF_ERROR_BASE +128)
#define UF_DRF_INVALID_SYMBOL_TO_DIMENSION_TEXT_DISTANCE  \
                                                (UF_DRF_ERROR_BASE + 129)
#define UF_DRF_INVALID_HATCH_DISTANCE           (UF_DRF_ERROR_BASE + 130)
#define UF_DRF_INVALID_AREA_FILL_SCALE          (UF_DRF_ERROR_BASE + 131)
#define UF_DRF_INVALID_HATCH_TOLERANCE          (UF_DRF_ERROR_BASE + 132)
#define UF_DRF_INVALID_DIMENSION_TEXT_SIZE      (UF_DRF_ERROR_BASE + 133)
#define UF_DRF_INVALID_DIMENSION_TEXT_CHARACTER_SPACE_FACTOR \
                                                (UF_DRF_ERROR_BASE + 134)
#define UF_DRF_INVALID_DIMENSION_TEXT_ASPECT_RATIO           \
                                                (UF_DRF_ERROR_BASE + 135)
#define UF_DRF_INVALID_DIMENSION_TEXT_LINE_SPACE_FACTOR      \
                                                (UF_DRF_ERROR_BASE + 136)
#define UF_DRF_INVALID_APPENDED_TEXT_SIZE       (UF_DRF_ERROR_BASE + 137)
#define UF_DRF_INVALID_APPENDED_TEXT_CHARACTER_SPACE_FACTOR  \
                                                (UF_DRF_ERROR_BASE + 138)
#define UF_DRF_INVALID_APPENDED_TEXT_ASPECT_RATIO            \
                                                (UF_DRF_ERROR_BASE + 139)
#define UF_DRF_INVALID_APPENDED_TEXT_LINE_SPACE_FACTOR       \
                                                (UF_DRF_ERROR_BASE + 140)
#define UF_DRF_INVALID_TOLERANCE_TEXT_SIZE      (UF_DRF_ERROR_BASE + 141)
#define UF_DRF_INVALID_TOLERANCE_TEXT_CHARACTER_SPACE_FACTOR \
                                                (UF_DRF_ERROR_BASE + 142)
#define UF_DRF_INVALID_TOLERANCE_TEXT_ASPECT_RATIO           \
                                                (UF_DRF_ERROR_BASE + 143)
#define UF_DRF_INVALID_TOLERANCE_TEXT_LINE_SPACE_FACTOR      \
                                                (UF_DRF_ERROR_BASE + 144)
#define UF_DRF_INVALID_GENERAL_TEXT_SIZE        (UF_DRF_ERROR_BASE + 145)
#define UF_DRF_INVALID_GENERAL_TEXT_CHARACTER_SPACE_FACTOR   \
                                                (UF_DRF_ERROR_BASE + 146)
#define UF_DRF_INVALID_GENERAL_TEXT_ASPECT_RATIO             \
                                                (UF_DRF_ERROR_BASE + 147)
#define UF_DRF_INVALID_GENERAL_TEXT_LINE_SPACE_FACTOR        \
                                                (UF_DRF_ERROR_BASE + 148)
#define UF_DRF_INVALID_ID_SYMBOL                (UF_DRF_ERROR_BASE + 149)
#define UF_DRF_INVALID_HORIZ_TEXT_JUST          (UF_DRF_ERROR_BASE + 150)
#define UF_DRF_INVALID_GDT_FRAME_FACTOR         (UF_DRF_ERROR_BASE + 151)
#define UF_DRF_INVALID_DIMENSION_ANGULAR_FORMAT_TOLERANCE   \
                                                (UF_DRF_ERROR_BASE + 152)
#define UF_DRF_INVALID_DIMENSION_ANGULAR_SUPPRESS_ZEROS     \
                                                (UF_DRF_ERROR_BASE + 153)
#define UF_DRF_INVALID_SYMBOL_TYPE              (UF_DRF_ERROR_BASE + 154)
#define UF_DRF_INVALID_ROW                      (UF_DRF_ERROR_BASE + 155)
#define UF_DRF_INVALID_COLUMN                   (UF_DRF_ERROR_BASE + 156)
#define UF_DRF_INVALID_NUMBER_OF_FEATURES       (UF_DRF_ERROR_BASE + 157)
#define UF_DRF_INVALID_NUMBER_OF_VIEWS          (UF_DRF_ERROR_BASE + 158)
#define UF_DRF_NO_TEMPLATE_ENV_VAR              (UF_DRF_ERROR_BASE + 159)
#define UF_DRF_TEMPLATE_WONT_LOAD               (UF_DRF_ERROR_BASE + 160)
#define UF_DRF_INVALID_CUSTOM_SYMBOL_PIECE      (UF_DRF_ERROR_BASE + 161)
#define UF_DRF_BAD_SYMBOL_TEXT_OBJECT           (UF_DRF_ERROR_BASE + 162)
#define UF_DRF_DEFAULT_TEXT_OUT_OF_BOUNDS       (UF_DRF_ERROR_BASE + 163)
#define UF_DRF_LEADER_HAS_NO_CONNECTION         (UF_DRF_ERROR_BASE + 164)
#define UF_DRF_INVALID_NARROW_DIMENSION_DISPLAY_TYPE       \
                                                (UF_DRF_ERROR_BASE + 165)
#define UF_DRF_INVALID_NARROW_DIMENSION_LEADER_ANGLE       \
                                                (UF_DRF_ERROR_BASE + 166)
#define UF_DRF_INVALID_NARROW_DIMENSION_TEXT_ORIENTATION   \
                                                (UF_DRF_ERROR_BASE + 167)
#define UF_DRF_NOT_A_CUSTOM_SYMBOL              (UF_DRF_ERROR_BASE + 168)
#define UF_DRF_TEMPLATE_NAME_NOT_FOUND          (UF_DRF_ERROR_BASE + 169)
#define UF_DRF_TEMPLATE_ALREADY_LOADED          (UF_DRF_ERROR_BASE + 170)
#define UF_DRF_INVALID_INHERIT_TAG              (UF_DRF_ERROR_BASE + 171)
#define UF_DRF_INVALID_DIM_APP_TEXT_SPACE_FACTOR           \
                                                (UF_DRF_ERROR_BASE + 172)
#define UF_DRF_INVALID_DIM_TOL_TEXT_SPACE_FACTOR           \
                                                (UF_DRF_ERROR_BASE + 173)
#define UF_DRF_INVALID_DIM_DIM_LINE_SPACE_FACTOR           \
                                                (UF_DRF_ERROR_BASE + 174)
#define UF_DRF_INVALID_DIM_TYPE_FOR_OPERATION   (UF_DRF_ERROR_BASE + 175)

#define UF_DRF_INVALID_CHAMFER_DIMENSION              \
                                                (UF_DRF_ERROR_BASE + 176)
#define UF_DRF_INVALID_CHAMFER_DIMENSION_FORM         \
                                                (UF_DRF_ERROR_BASE + 177)
#define UF_DRF_INVALID_CHAMFER_DIMENSION_STUB_TYPE    \
                                                (UF_DRF_ERROR_BASE + 178)
#define UF_DRF_INVALID_CHAMFER_DIMENSION_LEADER_TYPE  \
                                                (UF_DRF_ERROR_BASE + 179)
#define UF_DRF_INVALID_CHAMFER_DIMENSION_SYMBOL_TYPE  \
                                                (UF_DRF_ERROR_BASE + 180)
#define UF_DRF_INVALID_CHAMFER_DIMENSION_SYMBOL_NAME  \
                                                (UF_DRF_ERROR_BASE + 181)
#define UF_DRF_INVALID_CHAMFER_DIMENSION_SPACE_FACTOR \
                                                (UF_DRF_ERROR_BASE + 182)
#define UF_DRF_INVALID_FACE_ORIENTATION         (UF_DRF_ERROR_BASE + 183)
#define UF_DRF_INVALID_CMP_DWG_BASELINE         (UF_DRF_ERROR_BASE + 184)
#define UF_DRF_INVALID_CMP_DWG_PLOT_OPTIONS     (UF_DRF_ERROR_BASE + 185)
#define UF_DRF_CMP_DWG_DIFF_NOT_PERFORMED       (UF_DRF_ERROR_BASE + 186)
#define UF_DRF_CMP_DWG_DIFF_FOUND               (UF_DRF_ERROR_BASE + 187)
#define UF_DRF_MULTIPLE_PLISTS_NOT_ALLOWED      (UF_DRF_ERROR_BASE + 188)
#define UF_DRF_INVALID_DIM_REFERENCE_TYPE       (UF_DRF_ERROR_BASE + 189)
#define UF_DRF_INVALID_DIM_INSPECTION_TYPE      (UF_DRF_ERROR_BASE + 190)
#define UF_DRF_CONFLICT_BASIC_TOL_AND_INSPECTION_TYPE \
                                                (UF_DRF_ERROR_BASE + 191)
#define UF_DRF_CONFLICT_REF_TOL_AND_REF_SYMBOL_TYPE \
                                                (UF_DRF_ERROR_BASE + 192)

#define UF_DRF_GDT_REQUIRED_FOR_LEADER_TYPE     (UF_DRF_ERROR_BASE + 193)
#define UF_DRF_LEADER_REQUIRED                  (UF_DRF_ERROR_BASE + 194)
#define UF_DRF_NOT_VALID_LEADER_ATTACH_OBJ      (UF_DRF_ERROR_BASE + 195)
#define UF_DRF_CANNOT_ATTACH_TO_OCC             (UF_DRF_ERROR_BASE + 196)
#define UF_DRF_CANNOT_ATTACH_TO_RETAINED_ANNOT  (UF_DRF_ERROR_BASE + 197)
#define UF_DRF_CANNOT_ATTACH_TO_VIEW_LABEL      (UF_DRF_ERROR_BASE + 198)
#define UF_DRF_CANNOT_ATTACH_TO_DISASSOC_DMV_FACET_REP (UF_DRF_ERROR_BASE + 199)
#define UF_DRF_INTERMEDIATE_PTS_NOT_ALLOWED     (UF_DRF_ERROR_BASE + 200)
#define UF_DRF_NOT_VALID_FOR_GB_DAT_DIM         (UF_DRF_ERROR_BASE + 201)
#define UF_DRF_DIM_HAS_NO_EXT_LINES             (UF_DRF_ERROR_BASE + 202)
#define UF_DRF_CANNOT_ATTACH_TO_NON_LINEAR      (UF_DRF_ERROR_BASE + 203)
#define UF_DRF_CANNOT_ATTACH_CANT_FIND_NORMAL   (UF_DRF_ERROR_BASE + 204)
#define UF_DRF_CANNOT_ATTACH_TO_LEADER_WITHOUT_ARROWS (UF_DRF_ERROR_BASE + 205)
#define UF_DRF_TOO_MANY_LEADERS                 (UF_DRF_ERROR_BASE + 206)
#define UF_DRF_LEADER_IS_REQD                   (UF_DRF_ERROR_BASE + 207)
#define UF_DRF_INVALID_TEXT                     (UF_DRF_ERROR_BASE + 208)
#define UF_DRF_NOT_VALID_GDT_TYPE               (UF_DRF_ERROR_BASE + 209)
#define UF_DRF_HAS_NO_LEADER_POS_PARAM          (UF_DRF_ERROR_BASE + 210)
#define UF_DRF_CANNOT_CHANGE_LEADER_POS_PARAM   (UF_DRF_ERROR_BASE + 211)
#define UF_DRF_CANNOT_ATTACH_TO_WELD_SYMBOL     (UF_DRF_ERROR_BASE + 212)
#define UF_DRF_REFILE_PART_FAILURE              (UF_DRF_ERROR_BASE + 213)
#define UF_DRF_INVALID_DATUM_LENGTH_PAST_ARROW  (UF_DRF_ERROR_BASE + 214)
#define UF_DRF_OBJECTS_ARE_NOT_CONSTANT         (UF_DRF_ERROR_BASE + 215)
#define UF_DRF_INVALID_ARROW_OUT_LENGTH_FACTOR  (UF_DRF_ERROR_BASE + 216)
#define UF_DRF_INVALID_TEXT_OVER_STUB_FACTOR    (UF_DRF_ERROR_BASE + 217)
#define UF_DRF_CANNOT_ATTACH_TO_DIM_TYPE        (UF_DRF_ERROR_BASE + 218)
#define UF_DRF_INVALID_TRIM_DIM_LINE_TYPE       (UF_DRF_ERROR_BASE + 219)
#define UF_DRF_INVALID_OFFSET_CURVES            (UF_DRF_ERROR_BASE + 220)
#define UF_DRF_INFINITE_RADIUS                  (UF_DRF_ERROR_BASE + 221)
#define UF_DRF_CANNOT_ATTACH_TO_NON_FACE        (UF_DRF_ERROR_BASE + 222)
#define UF_DRF_INVALID_STACK_VERTICAL_ALIGNMENT (UF_DRF_ERROR_BASE + 223)
#define UF_DRF_INVALID_STACK_HORIZONTAL_ALIGNMENT (UF_DRF_ERROR_BASE + 224)
#define UF_DRF_INVALID_STACK_SPACE_FACTOR       (UF_DRF_ERROR_BASE + 225)
#define UF_DRF_INVALID_DOGLEG_START_OFFSET      (UF_DRF_ERROR_BASE + 226)
#define UF_DRF_INVALID_DOGLEG_END_OFFSET_ZERO   (UF_DRF_ERROR_BASE + 227)
#define UF_DRF_INVALID_DOGLEG_END_OFFSET        (UF_DRF_ERROR_BASE + 228)
#define UF_DRF_INVALID_DOGLEG_ANGLE             (UF_DRF_ERROR_BASE + 229)
#define UF_DRF_INVALID_ORDINATE_MARGIN_SPACING  (UF_DRF_ERROR_BASE + 230)
#define UF_DRF_INVALID_ORDINATE_MARGIN_NUMBER   (UF_DRF_ERROR_BASE + 231)
#define UF_DRF_INVALID_ASSOCIATED_OBJECT        (UF_DRF_ERROR_BASE + 232)
/* Moved these messages out of 300-400 range */
#define UF_DRF_MORE_THAN_7_LEADERS              (UF_DRF_ERROR_BASE + 233)
#define UF_DRF_CANT_REMOVE_LAST_LEADER          (UF_DRF_ERROR_BASE + 234)
#define UF_DRF_INVALID_APPEARANCE_SLANT_ANGLE   (UF_DRF_ERROR_BASE + 235)
#define UF_DRF_INVALID_DATUM_TARGET_LABEL       (UF_DRF_ERROR_BASE + 236)
#define UF_DRF_INVALID_DATUM_TARGET_INDEX       (UF_DRF_ERROR_BASE + 237)
#define UF_DRF_INVALID_INTEGER_INPUT            (UF_DRF_ERROR_BASE + 238)
#define UF_DRF_INVALID_REAL_INPUT               (UF_DRF_ERROR_BASE + 239)
#define UF_DRF_INVALID_STRING_INPUT             (UF_DRF_ERROR_BASE + 240)
#define UF_DRF_UNSUPPORTED_CHARACTER_INPUT      (UF_DRF_ERROR_BASE + 241)
#define UF_DRF_FILENAME_EXISTS                  (UF_DRF_ERROR_BASE + 242)
#define UF_DRF_INVALID_FOLDER_INPUT             (UF_DRF_ERROR_BASE + 243)
#define UF_DRF_INVALID_NOTE_TITLE               (UF_DRF_ERROR_BASE + 244)
#define UF_DRF_SYMBOL_UNSUPPORTED_SKETCH        (UF_DRF_ERROR_BASE + 245)
#define UF_DRF_SYMBOL_IS_ALREADY_IN_EDIT        (UF_DRF_ERROR_BASE + 246)
#define UF_DRF_SYMBOL_INVALID_SYMBOL_NAME       (UF_DRF_ERROR_BASE + 247)
#define UF_DRF_SYMBOL_SELECTED_DIFFERENT_SYMBOLS (UF_DRF_ERROR_BASE + 248)
#define UF_DRF_INVALID_TEXT_OVER_LEADER_GAP_FACTOR (UF_DRF_ERROR_BASE + 249)
#define UF_DRF_UNITS_INVALID_NUMERATOR_FRACTION  (UF_DRF_ERROR_BASE + 250)
#define UF_DRF_UNITS_INVALID_NUMERATOR_DEGREE    (UF_DRF_ERROR_BASE + 251)
#define UF_DRF_UNITS_INVALID_NUMERATOR_MINUTES   (UF_DRF_ERROR_BASE + 252)
#define UF_DRF_UNITS_INVALID_NUMERATOR_SECONDS   (UF_DRF_ERROR_BASE + 253)
#define UF_DRF_UNITS_INVALID_NUMERATOR_AGGERGATE (UF_DRF_ERROR_BASE + 254)
#define UF_DRF_UNITS_INVALID_CELL_SLANT_ANGLE    (UF_DRF_ERROR_BASE + 255)
#define UF_DRF_INVALID_JOG_START_OFFSET      (UF_DRF_ERROR_BASE + 256)
#define UF_DRF_INVALID_JOG_END_OFFSET_ZERO   (UF_DRF_ERROR_BASE + 257)
#define UF_DRF_INVALID_JOG_END_OFFSET        (UF_DRF_ERROR_BASE + 258)
#define UF_DRF_INVALID_JOG_ANGLE             (UF_DRF_ERROR_BASE + 259)
#define UF_DRF_INVALID_JOG_EXTLINE_ANGLE_CONFIG    (UF_DRF_ERROR_BASE + 260)
#define UF_DRF_INVALID_SYMBOL_ASPECT_RATIO    (UF_DRF_ERROR_BASE + 261)

/* error 300-400 reserved for centerline annotations */
#define UF_DRF_CLINE_INVALID_INPUT               (UF_DRF_ERROR_BASE + 301)
#define UF_DRF_CLINE_INCORRECT_NUM_ASSOC_OBJECTS (UF_DRF_ERROR_BASE + 302)
#define UF_DRF_CLINE_INSUFFICIENT_INPUT          (UF_DRF_ERROR_BASE + 303)
#define UF_DRF_CLINE_NON_COLLINEAR_POINTS        (UF_DRF_ERROR_BASE + 304)
#define UF_DRF_CLINE_ALL_POINTS_NOT_COLLINEAR    (UF_DRF_ERROR_BASE + 305)
#define UF_DRF_CLINE_INVALID_INTERSECTION        (UF_DRF_ERROR_BASE + 306)
#define UF_DRF_CLINE_DUPLICATE_POINTS_SELECTED   (UF_DRF_ERROR_BASE + 307)
#define UF_DRF_CLINE_ANGLE_OUT_OF_RANGE          (UF_DRF_ERROR_BASE + 308)
#define UF_DRF_CLINE_POINTS_COLLINEAR            (UF_DRF_ERROR_BASE + 309)
#define UF_DRF_CLINE_UNEQUAL_RADIUS              (UF_DRF_ERROR_BASE + 310)
#define UF_DRF_CLINE_INVALID_OBJECT              (UF_DRF_ERROR_BASE + 311)
#define UF_DRF_CLINE_INVALID_RADIUS              (UF_DRF_ERROR_BASE + 312)
#define UF_DRF_CLINE_INVALID_OFFSET_DISTANCE     (UF_DRF_ERROR_BASE + 313)
#define UF_DRF_CLINE_INVALID_OFFSET_OBJECT       (UF_DRF_ERROR_BASE + 314)
#define UF_DRF_CLINE_INVALID_EXTENSION           (UF_DRF_ERROR_BASE + 315)
#define UF_DRF_CLINE_POINTS_COMPUTATION_FAILURE  (UF_DRF_ERROR_BASE + 316)
#define UF_DRF_CLINE_MEMORY_ALLOCATION_ERROR     (UF_DRF_ERROR_BASE + 317) 
#define UF_DRF_CLINE_UNABLE_TO_CREATE_ERROR      (UF_DRF_ERROR_BASE + 318) 
#define UF_DRF_CLINE_RETAINED_HANDLE_FOUND       (UF_DRF_ERROR_BASE + 319) 
/* Auto centerlines error messages start from 325 */
#define UF_DRF_CLINE_AUTO_NO_VIEWS               (UF_DRF_ERROR_BASE + 325)
#define UF_DRF_CLINE_AUTO_INVALID_VIEW           (UF_DRF_ERROR_BASE + 326) 
#define UF_DRF_CLINE_AUTO_INVALID_CYL_EXTENSION  (UF_DRF_ERROR_BASE + 327)

/* Point type Symbols error messages start from 350 */
#define UF_DRF_SYM_INSUFFICIENT_ASSOC_OBJECTS    (UF_DRF_ERROR_BASE + 350)
#define UF_DRF_SYM_INVALID_INTERSECTION          (UF_DRF_ERROR_BASE + 351)
/* Offset center point */
#define UF_DRF_OFFSET_INVALID_OBJECT             (UF_DRF_ERROR_BASE + 352) 
#define UF_DRF_OFFSET_INVALID_DISTANCE           (UF_DRF_ERROR_BASE + 353) 
#define UF_DRF_OFFSET_INVALID_ARC                (UF_DRF_ERROR_BASE + 354)

#define UF_DRF_INVALID_WELD_LINE_GAP             (UF_DRF_ERROR_BASE + 401)
#define UF_DRF_INVALID_WELD_SPACE_FACTOR         (UF_DRF_ERROR_BASE + 402)
#define UF_DRF_INVALID_WELD_TYPE                 (UF_DRF_ERROR_BASE + 403)
#define UF_DRF_OBJECT_IS_NOT_A_WELD_SYMBOL       (UF_DRF_ERROR_BASE + 404)
#define UF_DRF_INVALID_WELD_SYMBOL_SIZE_FACTOR   (UF_DRF_ERROR_BASE + 405)

/* Limit and Fit messages */
#define UF_DRF_LIMIT_FIT_INVALID_DEVIATION       (UF_DRF_ERROR_BASE + 450)
#define UF_DRF_LIMIT_FIT_INVALID_GRADE           (UF_DRF_ERROR_BASE + 451)
#define UF_DRF_LIMIT_FIT_INVALID_DISPLAY_STYLE   (UF_DRF_ERROR_BASE + 452)
#define UF_DRF_LIMIT_FIT_INVALID_TOL_ALIGNMENT   (UF_DRF_ERROR_BASE + 453)
#define UF_DRF_LIMIT_FIT_INVALID_PAREN_STYLE     (UF_DRF_ERROR_BASE + 454)
#define UF_DRF_LIMIT_FIT_INVALID_HOLE_TYPE       (UF_DRF_ERROR_BASE + 455)

#define UF_DRF_ORIGIN_TYPE_UNSUPPORTED           (UF_DRF_ERROR_BASE + 456)

#define UF_DRF_CANNOT_ATTACH_TO_OBJ_IN_DIFF_VIEW (UF_DRF_ERROR_BASE + 457)

#define UF_DRF_INVALID_TRUE_LENGTH_TEXT_POSITION (UF_DRF_ERROR_BASE + 458)

/* True Type Font */
#define UF_DRF_INVALID_FONT_STYLE (UF_DRF_ERROR_BASE + 459)

#define UF_DRF_INVALID_ALL_AROUND_SYMBOL_SIZE    (UF_DRF_ERROR_BASE + 460)

/* error code for Table PinList */
#define UF_DRF_INVALID_PINLIST_FILTER            (UF_DRF_ERROR_BASE + 461)

/* error code for Table Bill of Material */
#define UF_DRF_INVALID_FABRICATION_NUMBER        (UF_DRF_ERROR_BASE + 462)
#define UF_DRF_INVALID_STOCK_LENGTH_VALUE        (UF_DRF_ERROR_BASE + 463)
#define UF_DRF_INVALID_DETAIL_LEVEL_TYPE         (UF_DRF_ERROR_BASE + 464)

/* more Limit and Fit messages */
#define UF_DRF_LIMIT_FIT_INVALID_ASSY_DISPLAY_STYLE   (UF_DRF_ERROR_BASE + 465)
#define UF_DRF_LIMIT_FIT_INVALID_SPLIT_BY_DIMLINE     (UF_DRF_ERROR_BASE + 466)
#define UF_DRF_LIMIT_FIT_INVALID_SEPARATOR            (UF_DRF_ERROR_BASE + 467)

/* errors 900 - 999 are reserved for warnings */
#define UF_DRF_WARNING                                        (UF_DRF_ERROR_BASE + 900)
#define UF_DRF_CANNOT_DISPLAY_ALL_AROUND_ALL_OVER_CIRCLE      (UF_DRF_ERROR_BASE + 901)
#define UF_DRF_CANNOT_DISPLAY_ALL_AROUND_CIRCLE               (UF_DRF_ERROR_BASE + 902)
#define UF_DRF_CANNOT_DISPLAY_ALL_OVER_CIRCLE                 (UF_DRF_ERROR_BASE + 903)


#ifdef __cplusplus
}
#endif

#endif /* UF_DRF_ERRORS_H_INCLUDED */
