/*******************************************************************************
                Copyright (c) 2001,2004,2005 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
================================================================================
 ******************************************************************************
 *
 * 
 *
 * File description:
 *
 * This file contains the Open API interface to FBM_GEOM in CAM.
 *
 * The CAM FBM_GEOM routines in this file provide an API to the Feature
 * Geometry Groups that are used in the Feature Based Hole Making Module
 *
 ******************************************************************************/
#ifndef UF_FBM_GEOM_H_INCLUDED
#define UF_FBM_GEOM_H_INCLUDED


#include <uf.h>
#include <uf_defs.h>
#include <uf_cam.h>



#include <libufun_cam_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/*
   **************************************************************************
   ***************************     Definitions    ***************************
   **************************************************************************
*/

/*******************************************************************************

   This is the identifier of the object which holds the results of the
   classification applied to a FBM_GEOM group.

   Environment: Internal  and  External

*******************************************************************************/

typedef  void  *UF_FBM_GEOM_classified_crit_t;

/*
   **************************************************************************
   ***************************     Structures     ***************************
   **************************************************************************
*/


/*******************************************************************************

   Types of the classification criteria of the FBM_GEOM group.

   Environment: Internal  and  External

*******************************************************************************/

enum UF_FBM_GEOM_crit_value_type_e
{
       UF_FBM_GEOM_crit_value_type_undefined,
       UF_FBM_GEOM_crit_value_type_logical,
       UF_FBM_GEOM_crit_value_type_integer,
       UF_FBM_GEOM_crit_value_type_double,
       UF_FBM_GEOM_crit_value_type_string
};

typedef enum UF_FBM_GEOM_crit_value_type_e  UF_FBM_GEOM_crit_value_type_t , *UF_FBM_GEOM_crit_value_type_p_t;



/*
   **************************************************************************
   ******************     Functions Relating to FBM_GEOM    *****************
   **************************************************************************
*/


/*******************************************************************************

   Return all the names of the features that are valid for the FBM_GEOM group

       History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_list_of_feature_names
(
   tag_t          fbm_geom_tag,  /* <I> The tag of the fbm_geom group of interest */
   int            *count,        /* <O> The number of feature names returned */
   char           ***feature_names  /* <OF,len:count> The array of the feature names.
                                            The memory for the names allocated
                                            by this function and must be freed
                                            by calling UF_free_string_array. */
);



/*******************************************************************************
   Set the name of the feature in the FBM_GEOM group and create the feature
   objects from the name.

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_set_feature_name
(
   tag_t         fbm_geom_tag,    /*<I> The tag of the fbm_geom group of interest */
   char         *feature_name     /*<I> One of the names that is returned by the call to
                                        UF_FBM_GEOM_ask_list_of_feature_names */
);



/*******************************************************************************

   Return the name of the feature in the FBM_GEOM group

    Environment: Internal  and  External

    History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int  UF_FBM_GEOM_ask_feature_name
(
  tag_t      fbm_geom_tag,          /*<I> The tag of the fbm_geom group of interest */
  char     **feature_name           /*<OF> Name of the feature on which the
                                           fbm_geom group is applied. The
                                           memory must be freed by calling
                                           UF_free */
);



/*******************************************************************************

   Return the feature objects of FBM_GEOM group

    Environment: Internal  and  External

    History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int  UF_FBM_GEOM_ask_features
(
    tag_t         fbm_geom_tag,        /*<I> The tag of the fbm_geom group of interest */
    int           *count,              /*<O> The number of feature objects returned */
    UF_NCFEAT_t   **ncfeat_objs        /*<OF,len:count> The array of  ncfeat objects.
                                              The memory for the objects
                                              allocated by this function
                                              and must be freed by calling
                                              UF_free */
);



/*******************************************************************************

   Remove the feature object from the FBM_GEOM group. If the feature object
   is not in the FBM_GEOM group, then an error is returned


   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_remove_feature
(
   tag_t         fbm_geom_tag,    /*<I> The tag of the fbm_geom group of interest */
   UF_NCFEAT_t   feature          /*<I> The feature object to be removed from the fbm_geom group */
);

/*******************************************************************************

   Return the feature objects that represent the all other feature objects
   in FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_representative_features
(
   tag_t        fbm_geom_tag,               /*<I> The tag of the fbm_geom group of interest */
   int          *count,                     /*<O> The number of representative features in this group */
   UF_NCFEAT_t  **rep_feature_list          /*<OF,len:count> The array of representative
                                                   features in this group.
                                                   The memory is allocated
                                                   by this function and has
                                                   to be freed by calling
                                                   UF_free */
);



/*******************************************************************************
   Return all the available criteria of the FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_available_criteria
(
   tag_t          fbm_geom_tag,       /*<I> The tag of the fbm_geom group of interest */
   int            *count,             /*<O> The number of criteria */
   char           ***criteria_list    /*<OF,len:count> The criteria that are available
                                             for classification. Memory is
                                             allocated by this function and
                                             has to be freed by calling
                                             UF_free_string_array */
);



/*******************************************************************************

   Return the criteria that has been specified to be used for classification
   of the feature objects in the FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_used_criteria
(
   tag_t    fbm_geom_tag,          /*<I> The tag of the fbm_geom group of interest */
   int      *count,                /*<O> The number of criteria */
   char     ***used_criteria_list  /*<OF,len:count> The criteria that will be used
                                          for classification. Memory is
                                          allocated by this function and
                                          has to be freed by calling
                                          UF_free_string_array */
);


/*******************************************************************************

   Return the data type of a criterion of the FBM_GEOM group.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_type_of_criterion
(
   tag_t                             fbm_geom_tag,     /*<I> The tag of the fbm_geom group of interest */
   char                              *criterion,       /*<I> The criterion for which the type has to be returned */
   UF_FBM_GEOM_crit_value_type_p_t   type              /*<O> The type of the criterion */
);



/*******************************************************************************

   Return the value of a logical type of criteria for a specific feature
   object that is present in the FBM_GEOM group.
   If the feature object is not present in the FBM_GEOM group, an error
   will be returned. Also, if the criteria type does not match, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_logical_of_criteria
(
   tag_t          fbm_geom_tag,         /*<I> The tag of the fbm_geom group of interest */
   UF_NCFEAT_t    ncfeat_obj,           /*<I> The ncfeat_obj object for which the criteria value has to be evaluated*/
   char           *criterion,           /*<I> The criterion for which the value is requested */
   logical        *value                /*<O> The logical value */
);



/*******************************************************************************

   Return the value of a double type of criteria for a
   specific feature object that is present in the FBM_GEOM group.
   If the feature object is not present in the FBM_GEOM group,
   an error will be returned. Also, if the criteria type does
   not match, an error will be returned.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_double_of_criteria
(
   tag_t            fbm_geom_tag,     /*<I> The tag of the fbm_geom group of interest */
   UF_NCFEAT_t      ncfeat_object,    /*<I> The ncfeat_obj object for which the criteria value has to be evaluated*/
   char             *criterion,       /*<I> The criterion for which the value is requested */
   double           *value            /*<O> The double value */
);



/*******************************************************************************

   Return the value of a integer type of criteria for a
   specific feature object that is present in the FBM_GEOM group.
   If the feature object is not present in the FBM_GEOM group,
   an error will be returned. Also, if the criteria type does
   not match, an error will be returned.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_integer_of_criteria
(
   tag_t           fbm_geom_tag,   /*<I> The tag of the fbm_geom group of interest */
   UF_NCFEAT_t     ncfeat_obj,     /*<I> The ncfeat_obj object for which the criteria value has to be evaluated*/
   char            *criterion,     /*<I> The criterion for which the value is requested */
   int             *value          /*<O> The integer value */
);



/*******************************************************************************

   Return the value of a string type of criteria for a
   specific feature object that is present in the FBM_GEOM group.
   If the feature object is not present in the FBM_GEOM group,
   an error will be returned. Also, if the criteria type does
   not match, an error will be returned.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_string_of_criteria
(
   tag_t            fbm_geom_tag,    /*<I> The tag of the fbm_geom group of interest */
   UF_NCFEAT_t      ncfeat_obj,      /*<I> The ncfeat_obj object for which the criteria value has to be evaluated*/
   char             *criterion,      /*<I> The criterion whose value has to be evaluated*/
   char             **value          /*<OF> The string value. Memory has to be
                                            freed by calling UF_free */
);



/*******************************************************************************

   Return the result of the classification based on the given criteria.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_classify_by_criteria
(
   tag_t                            fbm_geom_tag,              /*<I> The tag of the fbm_geom group of interest */
   int                              num_of_criteria,           /*<I> The number of criteria that have to be considered */
   char                             **criteria,                /*<I,len:num_of_criteria>
                                                                     The criteria to be considered */
   int                              *num_of_classified_sets,   /*<O> The count of criteria sets possible */
   UF_FBM_GEOM_classified_crit_t     *classified_set_list      /*<OF,len:num_of_classified_sets,free:UF_FBM_GEOM_free_classified_set_list>
                                                                     The object containing the results of the classification.
                                                                     This has to be freed calling the function
                                                                     UF_FBM_GEOM_free_classified_set_list */
);



/*******************************************************************************

   Set the classified set of feature objects in FBM_GEOM group.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_set_classified_features
(
   tag_t                              fbm_geom_tag,            /*<I> The tag of the fbm_geom group of interest */
   UF_FBM_GEOM_classified_crit_t      classified_set_list,     /*<I> The result of the classification */
   int                                classified_set_index     /*<I> The index of the set which should be used */
);


/*******************************************************************************

   Return the integer value of a criterion for the set indicated by the
   classified_set index . If the type of criterion is not an integer, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_int_value_of_classified_crit
(
   tag_t                               fbm_geom_tag,         /*<I> The tag of the fbm_geom group of interest */
   char                                *criterion,           /*<I> The criteria for which the value is asked for */
   UF_FBM_GEOM_classified_crit_t       classified_set_list,  /*<I> The result of the classification */
   int                                 classified_set_index, /*<I> The index of the set which should be used */
   int                                 *value                /*<O> The value of the criterion */
);



/*******************************************************************************

   Return the double value of a criterion for the set indicated by the
   classified_set index . If the type of criterion is not a double, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_double_value_of_classified_crit
(
   tag_t                              fbm_geom_tag,             /*<I> The tag of the fbm_geom group of interest */
   char                               *criterion,               /*<I> The criteria for which the value is asked for */
   UF_FBM_GEOM_classified_crit_t      classified_set_list, /*<I> The result of the classification */
   int                                classified_set_index, /*<I> The index of the set which should be used */
   double                             *value                    /*<O> The value of the criterion */
);


/*******************************************************************************

   Return the string value of a criterion for the set indicated by the
   classified_set index . If the type of criterion is not a string, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_string_value_of_classified_crit
(
   tag_t                             fbm_geom_tag,              /*<I> The tag of the fbm_geom group of interest */
   char                              *criterion,                /*<I> The criteria for which the value is asked for */
   UF_FBM_GEOM_classified_crit_t     classified_set_list,  /* <I> The result of the classification */
   int                               classified_set_index,   /* <I> The index of the set which should be used */
   char                             **value                      /* <OF> The value of the criterion. Memory has to be freed by calling UF_free */
);



/*******************************************************************************

   Return the logical value of a criterion for the set indicated by the
   classified_set index . If the type of criterion is not a logical, an error
   will be returned.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_logical_value_of_classified_crit
(
   tag_t                            fbm_geom_tag,               /*<I> The tag of the fbm_geom group of interest */
   char                             *criterion,                 /*<I> The criteria for which the value is asked for */
   UF_FBM_GEOM_classified_crit_t    classified_set_list,   /*<I> The result of the classification */
   int                              classified_set_index,   /*<I> The index of the set which should be used */
   logical                          *value                      /*<O> The value of the criterion */
);

/*******************************************************************************
   Free the classification object.

   Environment: Internal and External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_free_classified_set_list
(
   tag_t                              fbm_geom_tag,        /*<I> The tag of the fbm_geom group of interest */
   UF_FBM_GEOM_classified_crit_t      classified_set_list   /* <I> The object that has to be freed */
);



/*******************************************************************************

   Return the list of entities associated to the feature of the FBM_GEOM group.
   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_feature_entities
(
   tag_t           fbm_geom_tag,             /*<I> The tag of the fbm_geom group of interest */
   UF_NCFEAT_t     representative_feature,   /*<I> A representative feature object of the group */
   int             *count,                   /*<O> The number of entities of the feature object */
   tag_t           **entities                /*<OF,len:count> The array of entities of the feature object. Memory has to be freed by calling UF_free */
);



/*******************************************************************************

   Return the list of accessibility vectors associated to the feature of the
   FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_ask_accessibility_vectors
(
   tag_t          fbm_geom_tag,              /*<I> The tag of the fbm_geom group of interest */
   UF_NCFEAT_t    representative_feature,    /*<I> A representative feature object of the group */
   int            *count,                    /*<O> The number of accessibility vectors */
   tag_t          **smart_vectors            /*<OF,len:count> The array of  accessibility vectors. Memory has to be freed calling UF_free */
);



/*******************************************************************************

   Set the list of accessibity vectors associated to the feature of
   FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_set_accessibility_vectors
(
   tag_t          fbm_geom_tag,            /*<I> The tag of the fbm_geom group of interest */
   UF_NCFEAT_t    representative_feature,  /*<I> A representative feature object of the group */
   int            count,                   /*<I> The number of accessibility vectors */
   tag_t          *smart_vectors           /*<I,len:count> count
                                                 The array of  accessibility vectors */
);



/*******************************************************************************

   Remove all the accessibility vectors associated to the feature of
   FBM_GEOM group.

   Environment: Internal  and  External

   History: Released in V19.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_remove_accessibility_vectors
(
   tag_t          fbm_geom_tag,             /*<I> The tag of the fbm_geom group of interest */
   UF_NCFEAT_t    representative_feature    /*<I> A representative feature object of the group */
);

/*******************************************************************************
   Create FBM_GEOM groups from the features in the part geometry of the 
   parent group. Only those features in the part geometry that are also in
   the selected list of the Machining Feature Manager are used to create groups. 
   Refer to uf_mfm.h for details of selected features in the Machining Feature Manager.

   Environment: Internal  and  External

   History: Released in NX4
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_FBM_GEOM_create
(
    char   *type,       /*<I> The template type */
    char   *subtype,    /*<I> The template sub-type */
    tag_t  parent_geom, /*<I> The parent geometry group of new feature groups */
    tag_t  *new_object  /*<O> The first new feature group object */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_FBM_GEOM_H_INCLUDED */
