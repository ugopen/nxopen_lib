/*==================================================================================================

    This material contains trade secrets or otherwise confidential information owned by 
    Siemens Industry Software Inc. or its affiliates (collectively, "SISW"), or its licensors.
    Access to and use of this information is strictly limited as set forth in the Customer's 
    applicable agreements with SISW. 

    Unpublished work Copyright 2024 Siemens

====================================================================================================
File description:
    The routines in this file are in the process of being removed from the Open C API product.
    Customers should use the designated replacement routines instead of the routines listed here.
    Once a routine is placed here, it is eligible to be removed after two functional releases of NX.

====================================================================================================

==================================================================================================*/
#ifndef UF_CAM_RETIRING_H
#define UF_CAM_RETIRING_H

#include <uf_defs.h>
#include <uf_cam.h>

#include <libufun_cam_exports.h>

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

/*******************************************************************************

    Return Hole Top of the representative feature object.
    The representative feature is obtained from the geometry
    parent of the operation( which should be of the type FBM_geom ).

    Environment: Internal  and  External

    History: Released in V19.0
             Deprecated in NX2406

    There is no replacement, because the HMOP operation is deprecated.

*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_ask_hole_top
(
    tag_t       hmop_tag,    /* <I> The tag of the hole making operation of interest */
    UF_NCFEAT_t rep_feature, /* <I> A representative feature. */
    tag_t*      smart_point  /* <O> Hole Top of rep_feature. */
);

/*******************************************************************************

    Set Hole Top to the representative feature object. The Hole Top tag must be
    associated to an entity of the representative feature object.
    Otherwise, it will return an error.
    The representative feature is obtained from the geometry
    parent of the operation ( which should be of the type FBM_geom ).

    Environment: Internal  and  External

    History: Released in V19.0
             Deprecated in NX2406

    There is no replacement, because the HMOP operation is deprecated.

*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_set_hole_top
(
    tag_t       hmop_tag,    /* <I> The tag of the hole making operation of interest */
    UF_NCFEAT_t rep_feature, /* <I> A representative feature. */
    tag_t*      smart_point  /* <I> Smart point associated to one of the entities of rep_feature. */
);

/*******************************************************************************

    Return Hole Axis of the representative feature object.
    The representative feature is obtained from the geometry
    parent of the operation( which should be of the type FBM_geom ).

    Environment: Internal  and  External

    History: Released in V19.0
             Deprecated in NX2406

    There is no replacement, because the HMOP operation is deprecated.

*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_ask_hole_axis
(
    tag_t       hmop_tag,    /* <I> The tag of the hole making operation of interest */
    UF_NCFEAT_t rep_feature, /* <I> A representative feature. */
    tag_t*      smart_vector /* <O> Hole Axis of rep_feature. */
);

/*******************************************************************************

    Set Hole Axis to the representative feature object. The Hole Axis tag
    must be associated to an entity of the representative feature object.
    Otherwise, it will return an error.
    The representative feature must be obtained from the geometry
    parent of the operation( which should be of the type FBM_geom ).

    Environment: Internal  and  External

    History: Released in V19.0
             Deprecated in NX2406

    There is no replacement, because the HMOP operation is deprecated.

*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_set_hole_axis
(
    tag_t       hmop_tag,    /* <I> The tag of the hole making operation of interest */
    UF_NCFEAT_t rep_feature, /* <I> A representative feature. */
    tag_t*      smart_vector /* <I> Smart vector associated to one of the entities of rep_feature. */
);

/*******************************************************************************

    Return Hole Depth of of the representative feature object.
    The representative feature must be obtained from the geometry
    parent of the operation( which should be of the type FBM_geom ).

    Environment: Internal  and  External

    History: Released in V19.0
             Deprecated in NX2406

    There is no replacement, because the HMOP operation is deprecated.

*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_ask_hole_depth
(
    tag_t       hmop_tag,    /* <I> The tag of the hole making operation of interest */
    UF_NCFEAT_t rep_feature, /* <I> A representative feature. */
    tag_t*      smart_point  /* <O> Hole Depth of rep_feature. */
);

/*******************************************************************************

    Set Hole Depth to the representative feature object. The Hole Depth tag
    must be associated to an entity of the representative feature object.
    Otherwise, it will return an error.
    The representative feature must be obtained from the geometry
    parent of the operation( which should be of the type FBM_geom ).
    Environment: Internal  and  External

    History: Released in V19.0
             Deprecated in NX2406

    There is no replacement, because the HMOP operation is deprecated.

*******************************************************************************/
extern UFUN_CAMEXPORT int UF_HMOP_set_hole_depth
(
    tag_t       hmop_tag,    /* <I> The tag of the hole making operation of interest */
    UF_NCFEAT_t rep_feature, /* <I> A representative feature. */
    tag_t*      smart_point  /* <I> Smart point associated to one of the entities of rep_feature. */
);


/*****************************************************************************
    This function retrieves a Machine Tool from the current Machine Tool
    Library (as defined in cam_config.dat) and creates an NX Machine Tool
    Object based upon the values received from the library.
    
    Environment: Internal  and  External
    See Also:
    History: Released in V16.0
             Deprecated in NX2406

    Equivalent NXOpen function:
    Please use NXOpen.SIM.MachineLibraryBuilder.GetValue instead.

 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_MCT_retrieve
(
    const char* libref,    /* <I> - the library reference of the desired
                            *     machine tool. Can be gotten from a record
                            *     set or an existing NX object
                            */
    tag_t* ncmct_tag  /* <O> - the NX object created as a result of the
                       *     retrieval
                       */
);

typedef enum
{
    UF_NCMCT_SETUP_REPLACE_NONE = 0,     /* no workpiece replacement        */
    UF_NCMCT_ORIENT_MACHINE_ZERO_TO_MCS, /* orient machine zero to main mcs */
    UF_NCMCT_USE_ASSEMBLY_POSITIONING,   /* use assembly positioning        */
    UF_NCMCT_USE_PART_MOUNT_JUNCTION,    /* use part mount junction         */
    UF_NCMCT_USE_OLD_MACHINE_TRANSFORM,  /* new machine is transformed the same way as the old one, if no old then identity */
    UF_NCMCT_KEEP_ASSEMBLY_CONSTRAINTS   /* new machine is transformed by using the existing assembly constraints */
} UF_NCMCT_setup_replace_mode_t;

/*****************************************************************************
    This function replaces the current Machine Tool with a specified machine
    from the Machine Library (as defined in cam_config.dat) and creates an
    NX Machine Tool Object based upon the values received from the library.
    
    Environment : Internal  and  External
    See Also:
    History: Released in NX3.0
             Deprecated in NX2406

    Equivalent NXOpen function:
    Please use NXOpen.CAM.MachineGroupBuilder.ReplaceMachine instead.

 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_MCT_replace_machine
(
    char* libref,          /* <I> - the library reference of the desired
                            *       machine tool. Can be gotten from a record
                            *       set or an existing NX object
                            */
    int retrieve_opt,        /* <I> - Flag indicating whether tool pocket data
                                      is to be retrieved with new machine:
                                      0 = No
                                      1 = Yes
                              */
    UF_NCMCT_setup_replace_mode_t mounting_opt, /* <I> - Flag indicating how the machine is to be
                                                         located with respect to the part if there
                                                         is a part file associated with the machine:
                                                         0 = No mounting.  Machine is loaded as
                                                                 defined.
                                                         1 = Mount the machine onto the workpiece.
                                                         2 = Mount the workpiece onto the machine.
                                                 */
    tag_t* ncmct_tag  /* <O> - the NX object created as a result of the
                       *       retrieval
                       */
);



//////////////////////////////////////////////////////////////////////////////////
// UF_FBM_GEOM - Deprecated in NX2406

typedef void* UF_FBM_GEOM_classified_crit_t;

typedef enum
{
    UF_FBM_GEOM_crit_value_type_undefined,
    UF_FBM_GEOM_crit_value_type_logical,
    UF_FBM_GEOM_crit_value_type_integer,
    UF_FBM_GEOM_crit_value_type_double,
    UF_FBM_GEOM_crit_value_type_string
} UF_FBM_GEOM_crit_value_type_t;

/*******************************************************************************

   Return all the names of the features that are valid for the FBM_GEOM group

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please use NXOpen.CAM.CAMFeatureCollection and then for each one NXOpen.CAM.CAMFeature.Name instead
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_list_of_feature_names
(
    tag_t fbm_geom_tag,   /* <I> The tag of the fbm_geom group of interest */
    int* count,           /* <O> The number of feature names returned */
    char*** feature_names /* <OF,len:count> The array of the feature names. The memory for the names allocated by this function and must be freed by calling UF_free_string_array. */
);

/*******************************************************************************
   Set the name of the feature in the FBM_GEOM group and create the feature
   objects from the name.

   Environment: Internal  and  External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please use NXOpen.CAM.FeatureGeometryGroup.SetName instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_set_feature_name
(
    tag_t fbm_geom_tag, /*<I> The tag of the fbm_geom group of interest */
    char* feature_name  /*<I> One of the names that is returned by the call to UF_FBM_GEOM_ask_list_of_feature_names */
);

/*******************************************************************************
   Return the name of the feature in the FBM_GEOM group

    Environment: Internal  and  External

    History: Released in V19.0
             Deprecated in NX2406

   Replacement:
     Please use NXOpen.CAM.FeatureGeometryGroup.Type instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int  UF_FBM_GEOM_ask_feature_name
(
    tag_t fbm_geom_tag, /*<I> The tag of the fbm_geom group of interest */
    char** feature_name /*<OF> Name of the feature on which the fbm_geom group is applied. The memory must be freed by calling UF_free */
);

/*******************************************************************************
   Return the feature objects of FBM_GEOM group

    Environment: Internal  and  External

    History: Released in V19.0
             Deprecated in NX2406

   Replacement:
     Please use NXOpen.CAM.FeatureGeometryGroup.GetFeatures instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int  UF_FBM_GEOM_ask_features
(
    tag_t fbm_geom_tag,       /*<I> The tag of the fbm_geom group of interest */
    int* count,               /*<O> The number of feature objects returned */
    UF_NCFEAT_t** ncfeat_objs /*<OF,len:count> The array of ncfeat objects. The memory for the objects allocated by this function and must be freed by calling UF_free */
);

/*******************************************************************************
   Remove the feature object from the FBM_GEOM group. If the feature object
   is not in the FBM_GEOM group, then an error is returned

   Environment: Internal  and  External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please use NXOpen.CAM.FeatureGeometryGroup.RemoveFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_remove_feature
(
    tag_t fbm_geom_tag, /*<I> The tag of the fbm_geom group of interest */
    UF_NCFEAT_t feature /*<I> The feature object to be removed from the fbm_geom group */
);

/*******************************************************************************
   Return the feature objects that represent the all other feature objects
   in FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please use the features return by NXOpen.CAM.FeatureGeometryGroup.GetFeatures instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_representative_features
(
    tag_t fbm_geom_tag,            /*<I> The tag of the fbm_geom group of interest */
    int* count,                    /*<O> The number of representative features in this group */
    UF_NCFEAT_t** rep_feature_list /*<OF,len:count> The array of representative features in this group.
                                         The memory is allocated by this function and has to be freed by calling UF_free */
);

/*******************************************************************************
   Return all the available criteria of the FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     The classification is not exposed from the feature group anymore.
     Please use NXOpen.CAM.CAMFeatureCollection and then for each one NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_available_criteria
(
    tag_t fbm_geom_tag,   /*<I> The tag of the fbm_geom group of interest */
    int* count,           /*<O> The number of criteria */
    char*** criteria_list /*<OF,len:count> The criteria that are available for classification.
                                The memory is allocated by this function and has to be freed by calling UF_free_string_array */
);

/*******************************************************************************
   Return the criteria that has been specified to be used for classification
   of the feature objects in the FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_used_criteria
(
    tag_t fbm_geom_tag,        /*<I> The tag of the fbm_geom group of interest */
    int* count,                /*<O> The number of criteria */
    char*** used_criteria_list /*<OF,len:count> The criteria that will be used for classification.
                                     The memory is allocated by this function and has to be freed by calling UF_free_string_array */
);

/*******************************************************************************
   Return the data type of a criterion of the FBM_GEOM group.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_type_of_criterion
(
    tag_t fbm_geom_tag,                 /*<I> The tag of the fbm_geom group of interest */
    char* criterion,                    /*<I> The criterion for which the type has to be returned */
    UF_FBM_GEOM_crit_value_type_t* type /*<O> The type of the criterion */
);

/*******************************************************************************
   Return the value of a logical type of criteria for a specific feature
   object that is present in the FBM_GEOM group.
   If the feature object is not present in the FBM_GEOM group, an error
   will be returned. Also, if the criteria type does not match, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_logical_of_criteria
(
    tag_t fbm_geom_tag,     /*<I> The tag of the fbm_geom group of interest */
    UF_NCFEAT_t ncfeat_obj, /*<I> The ncfeat_obj object for which the criteria value has to be evaluated*/
    char* criterion,        /*<I> The criterion for which the value is requested */
    logical* value          /*<O> The logical value */
);

/*******************************************************************************
   Return the value of a double type of criteria for a
   specific feature object that is present in the FBM_GEOM group.
   If the feature object is not present in the FBM_GEOM group,
   an error will be returned. Also, if the criteria type does
   not match, an error will be returned.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_double_of_criteria
(
    tag_t fbm_geom_tag,        /*<I> The tag of the fbm_geom group of interest */
    UF_NCFEAT_t ncfeat_object, /*<I> The ncfeat_obj object for which the criteria value has to be evaluated*/
    char* criterion,           /*<I> The criterion for which the value is requested */
    double* value              /*<O> The double value */
);

/*******************************************************************************
   Return the value of a integer type of criteria for a
   specific feature object that is present in the FBM_GEOM group.
   If the feature object is not present in the FBM_GEOM group,
   an error will be returned. Also, if the criteria type does
   not match, an error will be returned.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_integer_of_criteria
(
    tag_t fbm_geom_tag,     /*<I> The tag of the fbm_geom group of interest */
    UF_NCFEAT_t ncfeat_obj, /*<I> The ncfeat_obj object for which the criteria value has to be evaluated*/
    char* criterion,        /*<I> The criterion for which the value is requested */
    int* value              /*<O> The integer value */
);

/*******************************************************************************
   Return the value of a string type of criteria for a
   specific feature object that is present in the FBM_GEOM group.
   If the feature object is not present in the FBM_GEOM group,
   an error will be returned. Also, if the criteria type does
   not match, an error will be returned.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_string_of_criteria
(
    tag_t fbm_geom_tag,     /*<I> The tag of the fbm_geom group of interest */
    UF_NCFEAT_t ncfeat_obj, /*<I> The ncfeat_obj object for which the criteria value has to be evaluated*/
    char* criterion,        /*<I> The criterion whose value has to be evaluated*/
    char** value            /*<OF> The string value. Memory has to be freed by calling UF_free */
);

/*******************************************************************************
   Return the result of the classification based on the given criteria.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_classify_by_criteria
(
    tag_t fbm_geom_tag,                                /*<I> The tag of the fbm_geom group of interest */
    int num_of_criteria,                               /*<I> The number of criteria that have to be considered */
    char** criteria,                                   /*<I,len:num_of_criteria> The criteria to be considered */
    int* num_of_classified_sets,                       /*<O> The count of criteria sets possible */
    UF_FBM_GEOM_classified_crit_t* classified_set_list /*<OF,len:num_of_classified_sets,free:UF_FBM_GEOM_free_classified_set_list> The object containing the results of the classification.
                                                             This has to be freed calling the function UF_FBM_GEOM_free_classified_set_list */
);

/*******************************************************************************
   Set the classified set of feature objects in FBM_GEOM group.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_set_classified_features
(
    tag_t fbm_geom_tag,                                /*<I> The tag of the fbm_geom group of interest */
    UF_FBM_GEOM_classified_crit_t classified_set_list, /*<I> The result of the classification */
    int classified_set_index                           /*<I> The index of the set which should be used */
);

/*******************************************************************************
   Return the integer value of a criterion for the set indicated by the
   classified_set index . If the type of criterion is not an integer, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     No replacement needed.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_int_value_of_classified_crit
(
    tag_t fbm_geom_tag,                                /*<I> The tag of the fbm_geom group of interest */
    char* criterion,                                   /*<I> The criteria for which the value is asked for */
    UF_FBM_GEOM_classified_crit_t classified_set_list, /*<I> The result of the classification */
    int classified_set_index,                          /*<I> The index of the set which should be used */
    int* value                                         /*<O> The value of the criterion */
);

/*******************************************************************************
   Return the double value of a criterion for the set indicated by the
   classified_set index . If the type of criterion is not a double, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_double_value_of_classified_crit
(
    tag_t fbm_geom_tag,                                /*<I> The tag of the fbm_geom group of interest */
    char* criterion,                                   /*<I> The criteria for which the value is asked for */
    UF_FBM_GEOM_classified_crit_t classified_set_list, /*<I> The result of the classification */
    int classified_set_index,                          /*<I> The index of the set which should be used */
    double* value                                      /*<O> The value of the criterion */
);

/*******************************************************************************
   Return the string value of a criterion for the set indicated by the
   classified_set index . If the type of criterion is not a string, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_string_value_of_classified_crit
(
    tag_t fbm_geom_tag,                                /*<I> The tag of the fbm_geom group of interest */
    char* criterion,                                   /*<I> The criteria for which the value is asked for */
    UF_FBM_GEOM_classified_crit_t classified_set_list, /*<I> The result of the classification */
    int classified_set_index,                          /*<I> The index of the set which should be used */
    char** value                                       /*<OF> The value of the criterion. Memory has to be freed by calling UF_free */
);

/*******************************************************************************
   Return the logical value of a criterion for the set indicated by the
   classified_set index . If the type of criterion is not a logical, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_logical_value_of_classified_crit
(
    tag_t fbm_geom_tag,                                /*<I> The tag of the fbm_geom group of interest */
    char* criterion,                                   /*<I> The criteria for which the value is asked for */
    UF_FBM_GEOM_classified_crit_t classified_set_list, /*<I> The result of the classification */
    int classified_set_index,                          /*<I> The index of the set which should be used */
    logical* value                                     /*<O> The value of the criterion */
);

/*******************************************************************************
   Free the classification object.

   Environment: Internal and External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please see UF_FBM_GEOM_ask_available_criteria.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_free_classified_set_list
(
    tag_t fbm_geom_tag,                               /*<I> The tag of the fbm_geom group of interest */
    UF_FBM_GEOM_classified_crit_t classified_set_list /* <I> The object that has to be freed */
);

/*******************************************************************************
   Return the list of entities associated to the feature of the FBM_GEOM group.
   Environment: Internal  and  External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     Please use NXOpen.CAM.CAMFeature.GetFaces on the features return by NXOpen.CAM.FeatureGeometryGroup.GetFeatures instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_feature_entities
(
    tag_t fbm_geom_tag,                 /*<I> The tag of the fbm_geom group of interest */
    UF_NCFEAT_t representative_feature, /*<I> A representative feature object of the group */
    int* count,                         /*<O> The number of entities of the feature object */
    tag_t** entities                    /*<OF,len:count> The array of entities of the feature object. Memory has to be freed by calling UF_free */
);

/*******************************************************************************
   Return the list of accessibility vectors associated to the feature of the
   FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     The accessibility vectors are not exposed anymore.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_accessibility_vectors
(
    tag_t fbm_geom_tag,                 /*<I> The tag of the fbm_geom group of interest */
    UF_NCFEAT_t representative_feature, /*<I> A representative feature object of the group */
    int* count,                         /*<O> The number of accessibility vectors */
    tag_t** smart_vectors               /*<OF,len:count> The array of  accessibility vectors. Memory has to be freed calling UF_free */
);

/*******************************************************************************
   Set the list of accessibility vectors associated to the feature of
   FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     The accessibility vectors are not exposed anymore.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_set_accessibility_vectors
(
    tag_t fbm_geom_tag,                 /*<I> The tag of the fbm_geom group of interest */
    UF_NCFEAT_t representative_feature, /*<I> A representative feature object of the group */
    int count,                          /*<I> The number of accessibility vectors */
    tag_t* smart_vectors                /*<I,len:count> count The array of  accessibility vectors */
);

/*******************************************************************************
   Remove all the accessibility vectors associated to the feature of
   FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
            Deprecated in NX2406

   Replacement:
     The accessibility vectors are not exposed anymore.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_remove_accessibility_vectors
(
    tag_t fbm_geom_tag,                /*<I> The tag of the fbm_geom group of interest */
    UF_NCFEAT_t representative_feature /*<I> A representative feature object of the group */
);

/*******************************************************************************
   Create FBM_GEOM groups from the features in the part geometry of the
   parent group. Only those features in the part geometry that are also in
   the selected list of the Machining Feature Manager are used to create groups.
   Refer to uf_mfm.h for details of selected features in the Machining Feature Manager.

   Environment: Internal  and  External

   History: Released in NX4
            Deprecated in NX2406

   Replacement:
     No replacement needed.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_create
(
    char* type,        /*<I> The template type */
    char* subtype,     /*<I> The template sub-type */
    tag_t parent_geom, /*<I> The parent geometry group of new feature groups */
    tag_t* new_object  /*<O> The first new feature group object */
);



//////////////////////////////////////////////////////////////////////////////////
// UF_MFM - Deprecated in NX2406

typedef enum
{
    UF_MFM_attr_value_type_undefined,
    UF_MFM_attr_value_type_logical,
    UF_MFM_attr_value_type_integer,
    UF_MFM_attr_value_type_double,
    UF_MFM_attr_value_type_string
} UF_MFM_attr_value_type_t;

typedef enum
{
    UF_MFM_source_type_undefined,            /* Unknown type */
    UF_MFM_source_type_user_defined_feature, /* Modeling user-defined feature */
    UF_MFM_source_type_standard_feature,     /* Modeling standard feature */
    UF_MFM_source_type_tagged_edge,          /* Tagged edge object */
    UF_MFM_source_type_tagged_face,          /* Tagged face object */
    UF_MFM_source_type_tagged_point,         /* Tagged point object */
    UF_MFM_source_type_tagged_arc,           /* Tagged arc object */
    UF_MFM_source_type_recognized_feature    /* Recognized feature */
} UF_MFM_source_type_t;

typedef enum
{
    UF_MFM_machined_status_empty,      /* No process is defined */
    UF_MFM_machined_status_regenerate, /* Some tool paths of the process need to regenerate */
    UF_MFM_machined_status_incomplete, /* Some tool paths of the process is not complete */
    UF_MFM_machined_status_complete    /* Tool paths of the process is completed */
} UF_MFM_machined_status_t;

struct UF_MFM_recognize_options_s
{
    logical ignore_cad; /* Ignore CAD features during feature recognition. Set to TRUE if CAD features should be recognized */
};
typedef struct UF_MFM_recognize_options_s UF_MFM_recognize_options_t;


/*******************************************************************************
    Return feature type of the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Type instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_feature_type
(
    UF_NCFEAT_t machining_feature, /* <I>  The pointer of the machining feature */
    char** feature_type_name       /* <OF> Feature type name of the machining feature. The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Set the name of the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.SetName instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_feature_name
(
    UF_NCFEAT_t machining_feature, /* <I> The pointer of the machining feature */
    char* feature_name             /* <I> New feature name */
);

/*******************************************************************************
    Return the name of the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Name instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_feature_name
(
    UF_NCFEAT_t machining_feature, /* <I>  The pointer of the machining feature */
    char** feature_name            /* <OF> The Feature name of the machining feature.
                                           The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Return a list of geometry groups of the machining feature.
    These geometry groups contain the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.GetGroups instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_geometry_groups
(
    UF_NCFEAT_t machining_feature, /*<I>  The pointer of the machining feature */
    int* count,                    /*<O>  The number of geometry groups that the machining feature belongs to */
    tag_t** geometry_groups        /*<OF,len:count> The array of geometry groups that machining feature belongs to.
                                          The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Return the status of the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Status instead.
******************************************************************************/
extern UFUN_CAMEXPORT int  UF_MFM_ask_machined_status
(
    UF_NCFEAT_t machining_feature,   /*<I> The pointer of the machining feature */
    tag_t geometry_group,            /*<I> The gometry group the machining feature */
    UF_MFM_machined_status_t* status /*<O> The machined status */
);

/*******************************************************************************
    Return the source type of the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.SourceType instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int  UF_MFM_ask_source_type
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    UF_MFM_source_type_t* source   /*<O> The source type */
);

/*******************************************************************************
    Return the overridden status of the machining feature.
    The status is TRUE is any attribute or the name is set by the user.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_overridden_status
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    logical* overridden_status     /*<O> The overridden status */
);

/*******************************************************************************
    Return a list of machining features that exist in the part.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeatureCollection instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_machining_features_of_part
(
    tag_t part_tag,                  /*<I>  The part tag */
    int* count,                      /*<O>  The number of machining features in the part*/
    UF_NCFEAT_t** machining_features /*<OF,len:count> The array of machining features in the part.
                                            The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Return a list of the types of machining features that exist in the part.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpenCAM.CAMFeatureCollection and for each NXOpen.CAM.CAMFeature.Type instead
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_machining_feature_types
(
    tag_t part_tag,            /*<I>  The part tag */
    int* count,                /*<O>  The number of machining feature types */
    char*** feature_type_names /*<OF,len:count> The array of machining feature names.
                                      The memory is allocated by this function and must be freed by calling UF_free to the array and for each name string */
);

/*******************************************************************************
    Return a list of machining features of the type in the part.

    Environment: Internal  and  External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_machining_features_of_type
(
    tag_t part_tag,                  /*<I>  The part tag */
    char* type_name,                 /*<I>  The feature type name */
    int* count,                      /*<O>  The number of machining features */
    UF_NCFEAT_t** machining_features /*<OF,len:count> The array of machining features.
                                            The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Return a list of types of machining feature candidates in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_candidate_machining_feature_types
(
    int body_count,              /*<I>  The number of bodies */
    tag_t* body_list,            /*<I,len:body_count>  The list of bodies */
    int* type_count,             /*<O>  The number of candidate types */
    char*** candidate_type_names /*<OF,len:type_count> The array of candidate feature type names.
                                        The memory is allocated by this function and must be freed by calling UF_free to the array and for each name string */
);

/*******************************************************************************
    Create machining features from NX modeling features of the machining
    feature types in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_modeling_features
(
    int body_count,                  /*<I>  The number of bodies */
    tag_t* body_list,                /*<I,len:body_count>  The list of bodies*/
    int type_count,                  /*<I>  The number of feature types */
    char** feature_types,            /*<I,len:type_count>  The list of feature type names */
    int* count,                      /*<O>  The of machining feature */
    UF_NCFEAT_t** machining_features /*<OF,len:count> The array of machining features.
                                            The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Create machining features from NX user defined features (UDF) of the machining
    feature types in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_user_defined_features
(
    int body_count,                  /*<I>  The number of bodies */
    tag_t* body_list,                /*<I,len:body_count>  The list of bodies*/
    int type_count,                  /*<I>  The number of feature types */
    char** feature_types,            /*<I,len:type_count>  The list of feature type names */
    int* count,                      /*<O>  The of machining feature */
    UF_NCFEAT_t** machining_features /*<OF,len:count> The array of machining features.
                                            The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Create machining features from tagged points the current part.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_tagged_points
(
    int* count_of_machining_features, /*<O>  The number of machining features */
    UF_NCFEAT_t** machining_features  /*<OF,len:count_of_machining_features> The array of machining features.
                                             The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Create machining features from tagged arcs in the current part.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_tagged_arcs
(
    int* count,                      /*<O>  The of machining feature */
    UF_NCFEAT_t** machining_features /*<OF,len:count> The array of machining features. The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Create machining features from tagged edges in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_tagged_edges
(
    int body_count,                  /*<I>  The number of bodies */
    tag_t* body_list,                /*<I,len:body_count>  The list of bodies*/
    int* count,                      /*<O>  The of machining feature */
    UF_NCFEAT_t** machining_features /*<OF,len:count> The array of machining features. The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Create machining features from tagged faces in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_tagged_faces
(
    int body_count,                  /*<I>  The number of bodies */
    tag_t* body_list,                /*<I,len:body_count>  The list of bodies*/
    int* count,                      /*<O>  The of machining feature */
    UF_NCFEAT_t** machining_features /*<OF,len:count> The array of machining features. The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Create machining features from recognized features in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_recognized_features
(
    int body_count,                  /*<I>  The number of bodies */
    tag_t* body_list,                /*<I,len:body_count>  The list of bodies*/
    int* count,                      /*<O>  The of machining feature */
    UF_NCFEAT_t** machining_features /*<OF,len:count> The array of machining features. The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Delete machining features.
    If any item in the list is not a machining feature, an error is returned and
    the machining features will not be deleted.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.FeatureRecognitionBuilder.DeleteFeature instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_delete_machining_features
(
    int count,                      /*<I> The number of machining features to be deleted */
    UF_NCFEAT_t* machining_features /*<I,len:count> The array of machining features to be deleted */
);

/*******************************************************************************
    Return a list attribute names of the machining feature.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_attributes
(
    UF_NCFEAT_t machining_feature, /*<I>  The pointer of the machining feature */
    int* count,                    /*<O>  The number of attributes */
    char*** attribute_names        /*<OF,len:count> The array of attribute names. The memory is allocated by this function
                                          and must be freed by calling UF_free to the array and for each name string */
);

/*******************************************************************************
    Return the type of the attribute.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_attribute_type
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    char* attribute,               /*<I> The attribute name */
    UF_MFM_attr_value_type_t* type /*<O> The attribute type */
);

/*******************************************************************************
    Return the original and overridden values of the logical attribute.
    Two values are equal if the attribute is not overridden.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_logical_value_of_attribute
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    char* attribute,               /*<I> The attribute name */
    logical* original_value,       /*<O> The original logical value */
    logical* overridden_value      /*<O> The current logical value */
);

/*******************************************************************************
    Set the value of the logical attribute.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_logical_value_of_attribute
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    char* attribute,               /*<I> The attribute name */
    logical overridden_value       /*<I> The overridden value */
);

/*******************************************************************************
    Return the original and overridden values of the double attribute.
    Two values are equal if the attribute is not overridden.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_double_value_of_attribute
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    char* attribute,               /*<I> The attribute name */
    double* original_value,        /*<O> The original double value */
    double* overridden_value       /*<O> The current double value */
);

/*******************************************************************************
    Set the value of the double attribute.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_double_value_of_attribute
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    char* attribute,               /*<I> The attribute name */
    double overridden_value        /*<I> The overridden value */
);

/*******************************************************************************
    Return the original and overridden values of the integer attribute.
    Two values are equal if the attribute is not overridden.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_integer_value_of_attribute
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    char* attribute,               /*<I> The attribute name */
    int* original_value,           /*<O> The original integer value */
    int* overridden_value          /*<O> The current integer value */
);

/*******************************************************************************
    Set the value of the integer attribute.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_integer_value_of_attribute
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    char* attribute,               /*<I> The attribute name */
    int overridden_value           /*<I> The overridden value */
);

/*******************************************************************************
    Return the original and overridden values of a string attribute.
    Two values are equal if the attribute is not overridden.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_string_value_of_attribute
(
    UF_NCFEAT_t machining_feature, /*<I>  The pointer of the machining feature */
    char* attribute,               /*<I>  The attribute name */
    char** original_value,         /*<OF> The original string value. The memory is allocated by this function and must be freed by calling UF_free. */
    char** overridden_value        /*<OF> The overridden string value. The memory is allocated by this function and must be freed by calling UF_free. */
);

/*******************************************************************************
    Set the value of the string attribute.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_string_value_of_attribute
(
    UF_NCFEAT_t machining_feature, /*<I> The pointer of the machining feature */
    char* attribute,               /*<I> The attribute name */
    char* overridden_value         /*<I> The overridden value */
);

/*******************************************************************************
    Ask whether there are selected features in the list.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.Selection from NXOpen.UI.SelectionManager instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_has_selected_fea_list
(
    logical* result /*<O>:  whether there is selected feature list */
);

/*******************************************************************************
    Clean the memory of selected feature list.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.Selection from NXOpen.UI.SelectionManager  instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_clean_selected_fea_list();

/*******************************************************************************
    Set the selected feature list.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.Selection from NXOpen.UI.SelectionManager  instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_selected_fea_list
(
    UF_NCFEAT_t* machining_features, /*<I,len:count> selected features */
    int count                        /*<I> number of selected features */
);

/*******************************************************************************
    Ask the selected feature list.

    Environment: Internal and External

    History: Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.Selection from NXOpen.UI.SelectionManager  instead.
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_selected_fea_list
(
    UF_NCFEAT_t** machining_features, /*<OF,len:count> selected features */
    int* count                        /*<O>:  number of selected features */
);

/********************************************************************************
    Set NX integer attribute in the specified machining feature, if the attribute
    already exists, then reset the attribute value; otherwise add attribute.

    Environment: Internal and External

    History:  Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_int_ug_attribute
(
    UF_NCFEAT_t machining_feature, /* <I> Machining feature */
    char* attribute,               /* <I> attribute name */
    int value                      /* <I> attribute value */
);

/********************************************************************************
    Set NX double attribute in the specified machining feature, if the attribute
    already exists, then reset the attribute value; otherwise add attribute.

    Environment: Internal and External

    History:  Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_double_ug_attribute
(
    UF_NCFEAT_t machining_feature, /* <I> Machining feature */
    char* attribute,               /* <I> attribute name */
    double value                   /* <I> attribute value */
);

/********************************************************************************
    Set NX string attribute in the specified machining feature, if the attribute
    already exists, then reset the attribute value; otherwise add attribute.

    Environment: Internal and External

    History:  Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.Attributes instead.
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_string_ug_attribute
(
    UF_NCFEAT_t machining_feature, /* <I> Machining feature */
    char* attribute,               /* <I> attribute name */
    char* value                    /* <I> attribute value */
);

/********************************************************************************
    Get list of faces of specified machining feature.

    Environment: Internal and External

    History:  Released in NX3.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.CAMFeature.GetFaces instead.
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_list_of_faces
(
    UF_NCFEAT_t machining_feature, /* <I> Machining feature */
    int* count,                    /* <O> number of faces */
    tag_t** face_list              /* <OF,len:count> face list */
);

/********************************************************************************
    Recognize hole features of the types and from the solid bodies
    provided in the input argument.

    Environment: Internal and External

    History:  Released in NX4.0
             Deprecated in NX2406

    Replacement:
      No replacement needed.
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_recognize_holes
(
    tag_t* body_list,                    /* <I,len:body_count>  list of solid bodies */
    int body_count,                      /* <I>  number of solid bodies */
    char** type_list,                    /* <I,len:type_count>  list of hole types to be recognized nullptr will recognize all types in feature definition file */
    int type_count,                      /* <I>  number of holes types to be recognized Zero will recognize all types in feature definition file */
    UF_MFM_recognize_options_t* options, /* <I>  Options used during recognition */
    int* feature_count,                  /* <O>  number of recognized machining holes */
    UF_NCFEAT_t** machining_features     /* <OF,len:feature_count> list of recognized machining features */
);

/********************************************************************************
    Create a machining feature of UF_MFM_source_type_recognized_feature type
    from a list of faces without setting any feature attributes.
    To set the attributes, call UF_MFM_set_double_ug_attribute.

    Environment: Internal and External

    History:  Released in NX4.0
             Deprecated in NX2406

    Replacement:
      Please use NXOpen.CAM.FeatureRecognitionBuilder.MakeFeature instead.
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_feature
(
    char* feature_type,            /* <I>  The type of machining feature */
    int count,                     /* <I>  The number of faces for a machining feature */
    tag_t* face_list,              /* <I,len:count>  The list of faces for a maching feature */
    UF_NCFEAT_t* machining_feature /* <O>  A new machining feature */
);

#ifdef __cplusplus
}
#endif

#endif // UF_CAM_RETIRING_H
