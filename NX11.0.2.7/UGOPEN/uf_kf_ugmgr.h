/*******************************************************************************


                     Copyright 2007 UGS Corp.
                       All Rights Reserved.



File description:

Open API interface to KF in NX Manager mode. These calls are not available when
using NX without NX Manager. These functions do the work of getting
KF data from the Teamcenter Engineering database.

Throughout this file a folder is input to a number of the API's.  To ensure
that a unique folder is specified use the form <user>:<folder>[:<folder>...].

*****************************************************************************/

#ifndef UF_KF_UGMGR_H_INCLUDED
#define UF_KF_UGMGR_H_INCLUDED

/***************************************************************************

***************************************************************************/

#include <uf_defs.h>
#include <uf_ugmgr_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


#define UF_KF_UGMGR_EXPORT_DFA_IN_PART       1
#define UF_KF_UGMGR_EXPORT_DFA_IN_ASSEMBLY   2

/****************************************************************************
This function gets the user defined KF classes stored in the Teamcenter Engineering database.
If there is more than one folder having the same name then all the KF classes 
defined in those folders are returned.

Environment: Internal  and  External
See Also:

History: Originally released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_KF_UGMGR_ask_user_dfa_classes(
    const char*               folder_name, /* <I>  
                                             Name of the folder */
    char***                   user_dfa_classes, /* <OF,len:num_classes> 
                                                  list of KF classes in the
                                                  specified folder. The list
                                                  should be freed by calling
                                                  UF_free_string_array */
    int*                      num_classes       /* <O>  
                                                  number of KF classes */
    );

/****************************************************************************
This function gets the user defined KF functions stored in the Teamcenter Engineering database.
If there is more than one folder having the same name then all the KF funcs 
defined in those folders are returned.

Environment: Internal  and  External
See Also:

History: Originally released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_KF_UGMGR_ask_user_dfa_funcs(
    const char*               folder_name, /* <I>
                                             Name of the folder */
    char***                   user_dfa_funcs, /* <OF,len:num_funcs>
                                                list of KF functions file in the
                                                  specified folder. The list
                                                  should be freed by calling
                                                  UF_free_string_array */
    int*                      num_funcs       /* <O>
                                                  number of KF funcs */
    );


/***************************************************************************
This function checks whether the specified KF class exists in the Teamcenter Engineering database.
Environment: Internal  and  External
See Also:

History: Originally released in V18.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_UGMGR_is_user_dfa_class_exists(
    const char*               dfa_class_name, /* <I>
                                                 Name of the KF class to
                                                 search for */
    logical*                  class_exists  /* <O> 
                                                 True if exists, else FALSE*/
    );

/***************************************************************************
This function checks whether the specified KF function exists in the Teamcenter Engineering database.
Environment: Internal  and  External
See Also:

History: Originally released in V18.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_UGMGR_is_user_dfa_func_exists(
    const char*               dfa_func_name, /* <I>
                                                 Name of the KF functions to
                                                 search for */
    logical*                  func_exists  /* <O> 
                                                 True if exists, else FALSE*/
    );

/***************************************************************************
This function checks whether the specified folder exists in Teamcenter Engineering.

Environment: Internal  and  External
See Also:

History: Originally released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_KF_UGMGR_is_folder_exists(
    const char*               folder_name,/* <I>
                                             Name of the folder to search for
                                             in the Teamcenter Engineering Database.*/
    logical*                  folder_exists /* <O> 
                                             TRUE if exists, else FALSE*/
    );

/***************************************************************************
This function gets all the user KF classes referenced in the part file.

Environment: Internal  and  External
See Also:

History: Originally released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_KF_UGMGR_list_user_classes_referenced(
    tag_t                     part_tag,/* <I>  
                                          tag of the part */
    char***                   user_classes_list, /* <OF,len:num_classes> 
                                                 List of classes referenced
                                                 by the part specified. This
                                                 list has to be freed by calling
                                                 UF_free_string_array*/
    int*                      num_classes/* <O>  
                                           Number of KF classes referenced in
                                           the part file*/
    );
/***************************************************************************
This function gets all the user KF funcs referenced in the part file.

This function always returns 0 functions as references to functions
are not maintained in Teamcenter.

Environment: Internal  and  External
See Also:

History: Originally released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_KF_UGMGR_list_user_funcs_referenced(
    tag_t                     part_tag,/* <I>  
                                          tag of the part */
    char***                   user_funcs_list, /* <OF,len:num_funcs> 
                                                List of functions referenced
                                                by the part specified. This
                                                list has to be freed by calling
                                                UF_free_string_array*/
    int*                      num_funcs/* <O>  
                                           Number of KF functions referenced in
                                           the part file
                                       */
    );

/***************************************************************************
This function checks whether the item is DFA
Environment: Internal  and  External
See Also:

History: Originally released in NX2
****************************************************************************/ 
extern UFUNEXPORT int UF_KF_UGMGR_is_item_dfa_type(
    char*    item_name, /* <I>
                         Item Name
                    */
    logical* dfa_type /* <O>
                         TRUE = Item is a DFA else FALSE
                      */
);

/***************************************************************************
This function sets the options for export of DFA files in command line mode
Environment: Internal  and  External
See Also:

History: Originally released in NX2
****************************************************************************/
extern UFUNEXPORT int UF_KF_UGMGR_initialize_export(
    int option          /* <I>
                           Use UF_KF_UGMGR_EXPORT_DFA_IN_PART to export
                           DFA files in individual part
                           Use UF_KF_UGMGR_EXPORT_DFA_IN_ASSEMBLY to export
                           DFA files used by entire assembly
                        */
);

/***************************************************************************
This function exports DFA classes and functions that are referenced in
a part file
Environment: Internal  and  External
See Also:

History: Originally released in NX2
****************************************************************************/
extern UFUNEXPORT int UF_UGMGR_KF_export_dfa_in_part(
    const char* part_name     /* <I>
                                  CLI Name of part
                              */
);

/***************************************************************************
This function sets the options for import of DFA files in command line mode
Environment: Internal  and  External
See Also:

History: Originally released in NX2
****************************************************************************/
extern UFUNEXPORT int UF_KF_UGMGR_initialize_import(
    logical is_dfa_list /* <I>
                           True if input is a file containing the names of files to import.
                           If true the value of the -part switch is a file containing a list of 
                           DFA files to import (1 per line).
                           Otherwise the value of the -part switch is assumed to be the DFA file to import.
                        */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_KF_UGMGR_H_INCLUDED */
