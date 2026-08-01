/****************************************************************************

                Copyright (c) 1994-2004 UGS Corp.
                        Unpublished - All rights reserved




File description:

This file contains the UF specific error codes.

 ***************************************************************************/

#ifndef UF_ERROR_BASES_H_INCLUDED
#define UF_ERROR_BASES_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************

  ***************************************************************************/

#define ERROR_UF_base          1105000

#define UF_err_program_not_initialized              ERROR_UF_base
#define UF_err_not_callable_in_internal            (ERROR_UF_base +1)
#define UF_err_cant_init_after_term                (ERROR_UF_base +2)
#define UF_err_cant_free_license                   (ERROR_UF_base +3)
#define UF_err_bad_parameter_number_1              (ERROR_UF_base +4)
#define UF_err_bad_parameter_number_2              (ERROR_UF_base +5)
#define UF_err_bad_parameter_number_3              (ERROR_UF_base +6)
#define UF_err_bad_parameter_number_4              (ERROR_UF_base +7)
#define UF_err_grip_calling_ufun_illegal_use       (ERROR_UF_base +8)
#define UF_err_grip_calling_ufun_counts_dont_agree (ERROR_UF_base +9)
#define UF_err_grip_calling_ufun_types_dont_agree  (ERROR_UF_base +10)
#define UF_err_grip_calling_ufun_sizes_dont_agree  (ERROR_UF_base +11)
#define UF_err_part_not_loaded                     (ERROR_UF_base +12)
#define UF_err_bad_parameter_number_5              (ERROR_UF_base +13)
#define UF_err_bad_parameter_number_6              (ERROR_UF_base +14)
#define UF_err_bad_parameter_number_7              (ERROR_UF_base +15)
#define UF_err_bad_parameter_number_8              (ERROR_UF_base +16)
#define UF_err_invalid_function_type               (ERROR_UF_base +17)
#define UF_err_cant_exit_run_dialog                (ERROR_UF_base +18)
#define UF_err_invalid_library                     (ERROR_UF_base +19)
#define UF_err_no_symbol                           (ERROR_UF_base +20)
#define UF_err_no_memory                           (ERROR_UF_base +21)
#define UF_err_unexpected_load_error               (ERROR_UF_base +22)
#define UF_err_not_supported_this_platform         (ERROR_UF_base +23)
#define UF_err_part_not_fully_loaded               (ERROR_UF_base +24)
#define UF_err_no_work_part                        (ERROR_UF_base +25)
#define UF_err_can_not_get_printerdc               (ERROR_UF_base +26)
#define UF_err_bad_parameter_number_9              (ERROR_UF_base +27)
#define UF_err_bad_parameter_number_10             (ERROR_UF_base +28)
#define UF_err_license_not_available               (ERROR_UF_base +29)
#define UF_err_ugmanager_not_active                (ERROR_UF_base +30)
#define UF_err_text_not_ascii                      (ERROR_UF_base +31)
#define UF_err_operation_aborted                   (ERROR_UF_base +32)
#define UF_err_mc_not_inited                       (ERROR_UF_base +33)
#define UF_err_attr_title_too_big                  (ERROR_UF_base +34)
#define UF_err_attr_value_too_big                  (ERROR_UF_base +35)
#define UF_err_attr_ann_text_found                 (ERROR_UF_base +36)
#define UF_err_attr_is_referenced                  (ERROR_UF_base +36)
#define UF_err_bad_parameter_number_11             (ERROR_UF_base +37)
#define UF_err_bad_parameter_number_12             (ERROR_UF_base +38)
#define UF_err_bad_parameter_number_13             (ERROR_UF_base +39)
#define UF_err_query_udobj_class_id_not_allowed    (ERROR_UF_base +40)
#define UF_err_failure_umg_setting                 (ERROR_UF_base +41)
#define UF_err_invalid_display_part                (ERROR_UF_base +42)
#define UF_err_object_not_smart                    (ERROR_UF_base +43)
#define UF_err_update_link_with_file               (ERROR_UF_base +44)
#define UF_err_redefine_link_without_file          (ERROR_UF_base +45)
#define UF_err_invalid_update_option               (ERROR_UF_base +46)
#define UF_err_file_does_not_exist                 (ERROR_UF_base +47)
#define UF_err_attr_not_found                      (ERROR_UF_base +48)
#define UF_err_invalid_filename                    (ERROR_UF_base +49)
#define UF_err_cant_execute_for_lock_table_content (ERROR_UF_base +50)
#define UF_err_cant_execute_for_lock_table_format  (ERROR_UF_base +51)
#define UF_err_not_in_work_part                    (ERROR_UF_base +52)
#define UF_err_attr_is_locked                      (ERROR_UF_base +53)
#define UF_err_attr_is_reserved                    (ERROR_UF_base +54)
#define UF_err_input_not_utf8                      (ERROR_UF_base +55)
#define UF_err_attr_insufficient_privilege         (ERROR_UF_base +56)
#define UF_err_input_not_locale                    (ERROR_UF_base +57)
#define UF_err_input_is_null                       (ERROR_UF_base +58)
#define UF_err_no_control_permission               (ERROR_UF_base +59)
#define UF_err_attr_duplicate_title                (ERROR_UF_base +60)
#define UF_err_object_not_desired_class            (ERROR_UF_base +61)
#define UF_err_invalid_input                       (ERROR_UF_base +62)
#define UF_err_tag_is_not_tagged_object            (ERROR_UF_base +63)
#define UF_err_tag_not_correct_type                (ERROR_UF_base +64)
#define UF_err_no_matching_record                  (ERROR_UF_base +65)
#define UF_err_already_loaded                      (ERROR_UF_base +66)


/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
}
#endif

#endif /* UF_ERROR_BASES_H_INCLUDED */
