/*******************************************************************************
                Copyright (c) 2001,2004,2005 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
********************************************************************************
 ******************************************************************************
 *
 * 
 *
 * File description:
 *
 * This file contains the Open C API interface to MFM in CAM.  
 *
 * The CAM MFM routines in this file provide an API to manage machining features.
 *
 ******************************************************************************/
#ifndef UF_MFM_H_INCLUDED
#define UF_MFM_H_INCLUDED


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

/*
   **************************************************************************
   ***************************     Structures     ***************************
   **************************************************************************
*/


/*******************************************************************************

   Types of the attribute of the machining feature.

   Environment: Internal  and  External

*******************************************************************************/

enum UF_MFM_attr_value_type_e 
{
       UF_MFM_attr_value_type_undefined,
       UF_MFM_attr_value_type_logical,
       UF_MFM_attr_value_type_integer,
       UF_MFM_attr_value_type_double,
       UF_MFM_attr_value_type_string
};

typedef enum UF_MFM_attr_value_type_e  UF_MFM_attr_value_type_t , *UF_MFM_attr_value_type_p_t; 

/*******************************************************************************

    Types of the source of the machining feature.

    Environment: Internal  and  External

*******************************************************************************/

enum UF_MFM_source_type_e 
{
    UF_MFM_source_type_undefined,               /* Unknown type */
    UF_MFM_source_type_user_defined_feature,    /* Modeling user-defined feature */
    UF_MFM_source_type_standard_feature,        /* Modeling standard feature */
    UF_MFM_source_type_tagged_edge,             /* Tagged edge object */
    UF_MFM_source_type_tagged_face,             /* Tagged face object */
    UF_MFM_source_type_tagged_point,            /* Tagged point object */
    UF_MFM_source_type_tagged_arc,              /* Tagged arc object */
    UF_MFM_source_type_recognized_feature       /* Recognized feature */
};

typedef enum UF_MFM_source_type_e  UF_MFM_source_type_t , *UF_MFM_source_type_p_t; 

/*******************************************************************************

    Machined status of the machining feature.

    Environment: Internal  and  External

*******************************************************************************/
enum UF_MFM_machined_status_e
{
    UF_MFM_machined_status_empty,         /* No process is defined */
    UF_MFM_machined_status_regenerate,    /* Some toolpaths of the process need to regenerate */ 
    UF_MFM_machined_status_incomplete,    /* Some toolpaths of the process is not complete */
    UF_MFM_machined_status_complete       /* Toolpaths of the process is completed */
};

typedef enum UF_MFM_machined_status_e  UF_MFM_machined_status_t, *UF_MFM_machined_status_p_t;

/*******************************************************************************

    The options used in feature recognition.

    Environment: Internal  and  External

*******************************************************************************/

struct UF_MFM_recognize_options_s {

    logical         ignore_cad;     /* Ignore CAD features during feature recognition
                                       Set to TRUE if CAD features should be recognzed */
};

typedef struct UF_MFM_recognize_options_s UF_MFM_recognize_options_t, *UF_MFM_recognize_options_p_t;

/*
   **************************************************************************
   ******************     Functions Relating to MFM    *****************
   **************************************************************************
*/

/*******************************************************************************

    Return feature type of the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_feature_type
(
    UF_NCFEAT_t  machining_feature,  /* <I>  The pointer of the machining feature */
    char         **feature_type_name /* <OF> Feature type name of the machining feature. 
                                             The memory is allocated by this function 
                                             and must be freed by calling UF_free. */
);


/*******************************************************************************

    Set the name of the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_feature_name
(
    UF_NCFEAT_t  machining_feature,  /* <I> The pointer of the machining feature */
    char         *feature_name       /* <I> New feature name */
);


/*******************************************************************************

    Return the name of the machining feature.
 
    Environment: Internal  and  External
 
    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_feature_name
(
    UF_NCFEAT_t  machining_feature,  /* <I>  The pointer of the machining feature */
    char         **feature_name      /* <OF> The Feature name of the machining feature. 
                                             The memory is allocated by this function 
                                             and must be freed by calling UF_free. */
);

 
/*******************************************************************************

    Return a list of geometry groups of the machining feature.
    These geometry groups contain the machining feature. 
   
    Environment: Internal  and  External
       
    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_geometry_groups
(
    UF_NCFEAT_t   machining_feature,          /*<I>  The pointer of the machining feature */
    int           *count,                     /*<O>  The number of geometry groups that the 
                                                     machining feature belongs to */
    tag_t         **geometry_groups           /*<OF,len:count> The array of geometry groups
                                                     that machining feature belongs to. 
                                                     The memory is allocated by this function 
                                                     and must be freed by calling UF_free. */
);

 

/*******************************************************************************

    Return the status of the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
******************************************************************************/
extern UFUN_CAMEXPORT int  UF_MFM_ask_machined_status
(
    UF_NCFEAT_t               machining_feature,        /*<I> The pointer of the machining feature */
    tag_t                     geometry_group,           /*<I> The gometry group the machining feature */
    UF_MFM_machined_status_t  *status                   /*<O> The machined status */
);

      

/*******************************************************************************

    Return the source type of the machining feature.

    Environment: Internal  and  External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int  UF_MFM_ask_source_type
(
    UF_NCFEAT_t            machining_feature,   /*<I> The pointer of the machining feature */
    UF_MFM_source_type_t   *source              /*<O> The source type */
);

 

/*******************************************************************************

    Return the overridden status of the machining feature.
    The status is TRUE is any attribute or the name is set by the user.
   
    Environment: Internal  and  External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_overridden_status
(
    UF_NCFEAT_t   machining_feature,        /*<I> The pointer of the machining feature */
    logical       *overridden_status        /*<O> The overridden status */
);


/*******************************************************************************

    Return a list of machining features that exist in the part.
    

    Environment: Internal  and  External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_machining_features_of_part
(
    tag_t          part_tag,              /*<I>  The part tag */
    int            *count,                /*<O>  The number of machining features in the part*/
    UF_NCFEAT_t    **machining_features   /*<OF,len:count> The array of machining features in the part. 
                                                 The memory is allocated by this function 
                                                 and must be freed by calling UF_free. */
);

/*******************************************************************************

    Return a list of the types of machining features that exist in the part.

    Environment: Internal  and  External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_machining_feature_types
(
    tag_t        part_tag,                /*<I>  The part tag */
    int          *count,                  /*<O>  The number of machining feature types */
    char         ***feature_type_names    /*<OF,len:count> The array of machining feature names. 
                                                 The memory is allocated by this function 
                                                 and must be freed by calling UF_free to
                                                 the array and for each name string */
);


/*******************************************************************************

    Return a list of machining features of the type in the part.

    Environment: Internal  and  External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_machining_features_of_type
(
    tag_t        part_tag,               /*<I>  The part tag */
    char         *type_name,             /*<I>  The feature type name */
    int          *count,                 /*<O>  The number of machining features */
    UF_NCFEAT_t  **machining_features    /*<OF,len:count> The array of machining features. 
                                                The memory is allocated by this function 
                                                and must be freed by calling UF_free. */
);

 
/*******************************************************************************

    Return a list of types of machining feature candidates in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_candidate_machining_feature_types
(
    int      body_count,                /*<I>  The number of bodies */
    tag_t    *body_list,                /*<I,len:body_count>  The list of bodies */
    int      *type_count,               /*<O>  The number of candidate types */
    char     ***candidate_type_names    /*<OF,len:type_count> The array of candidate feature type names.
                                               The memory is allocated by this function 
                                               and must be freed by calling UF_free to
                                               the array and for each name string */
);


/*******************************************************************************

    Create machining features from NX modeling features of the machining 
    feature types in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_modeling_features
(
    int           body_count,                   /*<I>  The number of bodies */
    tag_t         *body_list,                   /*<I,len:body_count>  The list of bodies*/
    int           type_count,                   /*<I>  The number of feature types */
    char          **feature_types,              /*<I,len:type_count>  The list of feature type names */
    int           *count,                       /*<O>  The of machining feature */
    UF_NCFEAT_t   **machining_features          /*<OF,len:count> The array of machining fetures 
                                                       The memory is allocated by this function 
                                                       and must be freed by calling UF_free. */
);

/*******************************************************************************

    Create machining features from NX user defined features (UDF) of the machining 
    feature types in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_user_defined_features
(
    int           body_count,                   /*<I>  The number of bodies */
    tag_t         *body_list,                   /*<I,len:body_count>  The list of bodies*/
    int           type_count,                   /*<I>  The number of feature types */
    char          **feature_types,              /*<I,len:type_count>  The list of feature type names */
    int           *count,                       /*<O>  The of machining feature */
    UF_NCFEAT_t   **machining_features          /*<OF,len:count> The array of machining fetures 
                                                       The memory is allocated by this function 
                                                       and must be freed by calling UF_free. */
);


/*******************************************************************************

    Create machining features from tagged points the current part.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_tagged_points
(
    int           *count_of_machining_features, /*<O>  The number of machining features */
    UF_NCFEAT_t   **machining_features          /*<OF,len:count_of_machining_features> The array of machining features.
                                                       The memory is allocated by this function 
                                                       and must be freed by calling UF_free. */
);


/*******************************************************************************

    Create machining features from tagged arcs in the current part.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_tagged_arcs
(
    int           *count,                       /*<O>  The of machining feature */
    UF_NCFEAT_t   **machining_features          /*<OF,len:count> The array of machining fetures 
                                                       The memory is allocated by this function 
                                                       and must be freed by calling UF_free. */
);


/*******************************************************************************

    Create machining features from tagged edges in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_tagged_edges
(
    int           body_count,                   /*<I>  The number of bodies */
    tag_t         *body_list,                   /*<I,len:body_count>  The list of bodies*/
    int           *count,                       /*<O>  The of machining feature */
    UF_NCFEAT_t   **machining_features          /*<OF,len:count> The array of machining fetures 
                                                       The memory is allocated by this function 
                                                       and must be freed by calling UF_free. */
);


/*******************************************************************************

    Create machining features from tagged faces in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_tagged_faces
(
    int           body_count,                   /*<I>  The number of bodies */
    tag_t         *body_list,                   /*<I,len:body_count>  The list of bodies*/
    int           *count,                       /*<O>  The of machining feature */
    UF_NCFEAT_t   **machining_features          /*<OF,len:count> The array of machining fetures 
                                                       The memory is allocated by this function 
                                                       and must be freed by calling UF_free. */
);


/*******************************************************************************

    Create machining features from recognized features in the bodies.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_features_from_recognized_features
(
    int           body_count,                   /*<I>  The number of bodies */
    tag_t         *body_list,                   /*<I,len:body_count>  The list of bodies*/
    int           *count,                       /*<O>  The of machining feature */
    UF_NCFEAT_t   **machining_features          /*<OF,len:count> The array of machining fetures 
                                                       The memory is allocated by this function 
                                                       and must be freed by calling UF_free. */
);


/*******************************************************************************

    Delete machining features. 
    If any item in the list is not a machining feature, an error is returned and
    the machining features will not be deleted.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_delete_machining_features
(
    int            count,                /*<I> The number of machining features to be deleted */
    UF_NCFEAT_t    *machining_features   /*<I,len:count> The array of machining features to be deleted */
);

 
/*******************************************************************************

    Return a list attribute names of the machining feature.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_attributes
(
    UF_NCFEAT_t     machining_feature,   /*<I>  The pointer of the machining feature */
    int             *count,              /*<O>  The number of attributes */
    char            ***attribute_names   /*<OF,len:count> The array of attribute names. 
                                                The memory is allocated by this function 
                                                and must be freed by calling UF_free to
                                                the array and for each name string */
);

 

/*******************************************************************************

    Return the type of the attribute.
   
    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_attribute_type
(
    UF_NCFEAT_t                   machining_feature,  /*<I> The pointer of the machining feature */
    char                          *attribute,         /*<I> The attribute name */
    UF_MFM_attr_value_type_p_t    type                /*<O> The attribute type */
);

 

/*******************************************************************************

    Return the original and overridden values of the logical attribute.
    Two values are equal if the attribute is not overridden.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_logical_value_of_attribute
(
    UF_NCFEAT_t   machining_feature,     /*<I> The pointer of the machining feature */
    char          *attribute,            /*<I> The attribute name */
    logical       *original_value,       /*<O> The original logical value */ 
    logical       *overridden_value      /*<O> The current logical value */
);


/*******************************************************************************

    Set the value of the logical attribute. 

    Environment: Internal and External
 
    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_logical_value_of_attribute
(
    UF_NCFEAT_t   machining_feature,     /*<I> The pointer of the machining feature */
    char          *attribute,            /*<I> The attribute name */
    logical       overridden_value       /*<I> The overridden value */ 
);

 
/*******************************************************************************

    Return the original and overridden values of the double attribute.
    Two values are equal if the attribute is not overridden.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_double_value_of_attribute
(
    UF_NCFEAT_t   machining_feature,     /*<I> The pointer of the machining feature */
    char          *attribute,            /*<I> The attribute name */
    double        *original_value,       /*<O> The original double value */ 
    double        *overridden_value      /*<O> The current double value */
);


/*******************************************************************************

    Set the value of the double attribute.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_double_value_of_attribute
(
    UF_NCFEAT_t   machining_feature,     /*<I> The pointer of the machining feature */
    char          *attribute,            /*<I> The attribute name */
    double        overridden_value       /*<I> The overridden value */ 
);

 

/*******************************************************************************

    Return the original and overridden values of the integer attribute.
    Two values are equal if the attribute is not overridden.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_integer_value_of_attribute
(
    UF_NCFEAT_t   machining_feature,     /*<I> The pointer of the machining feature */
    char          *attribute,            /*<I> The attribute name */
    int           *original_value,       /*<O> The original integer value */ 
    int           *overridden_value      /*<O> The current integer value */
);


/*******************************************************************************

    Set the value of the integer attribute.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_integer_value_of_attribute
(
    UF_NCFEAT_t   machining_feature,     /*<I> The pointer of the machining feature */
    char          *attribute,            /*<I> The attribute name */
    int           overridden_value       /*<I> The overridden value */ 
);


/*******************************************************************************

    Return the original and overridden values of a string attribute.
    Two values are equal if the attribute is not overridden.

    Environment: Internal and External
 
    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_string_value_of_attribute
(
    UF_NCFEAT_t   machining_feature,     /*<I>  The pointer of the machining feature */
    char          *attribute,            /*<I>  The attribute name */
    char          **original_value,      /*<OF> The original string value.
                                                The memory is allocated by this function 
                                                and must be freed by calling UF_free. */
    char          **overridden_value     /*<OF> The overridden string value.
                                                The memory is allocated by this function 
                                                and must be freed by calling UF_free. */
);


/*******************************************************************************

    Set the value of the string attribute.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_string_value_of_attribute
(
    UF_NCFEAT_t   machining_feature,     /*<I> The pointer of the machining feature */
    char          *attribute,            /*<I> The attribute name */
    char          *overridden_value      /*<I> The overridden value */ 
);


/*******************************************************************************

    Ask whether there are selected features in the list.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_has_selected_fea_list
(
    logical  *result    /*<O>:  whether there is selected feature list */
);


/*******************************************************************************

    Clean the memory of selected feature list.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_clean_selected_fea_list
(
);
 

/*******************************************************************************

    Set the selected feature list.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_selected_fea_list
(
    UF_NCFEAT_t   *machining_features,   /*<I,len:count> selected features */
    int           count                  /*<I> number of selected features */
);

/*******************************************************************************

    Ask the selected feature list.

    Environment: Internal and External

    History: Released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_selected_fea_list
(
    UF_NCFEAT_t   **machining_features,   /*<OF,len:count> selected features */
    int           *count                  /*<O>:  number of selected features */
);
 
/********************************************************************************
     
    Set NX integer attribute in the specified machining feature, if the attribute 
    already exists, then reset the attribute value; otherwise add attribute. 

    Environment: Internal and External 
 
    History:  Released in NX3.0 
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_int_ug_attribute
(  
    UF_NCFEAT_t    machining_feature,                /* <I> Machining feature */
    char           *attribute,                       /* <I> attribute name */ 
    int            value                             /* <I> attribute value */ 
);

/********************************************************************************
     
    Set NX double attribute in the specified machining feature, if the attribute 
    already exists, then reset the attribute value; otherwise add attribute. 

    Environment: Internal and External 
 
    History:  Released in NX3.0 
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_double_ug_attribute
(  
    UF_NCFEAT_t    machining_feature,                /* <I> Machining feature */
    char           *attribute,                       /* <I> attribute name */ 
    double         value                             /* <I> attribute value */ 
);

/********************************************************************************
     
    Set NX string attribute in the specified machining feature, if the attribute 
    already exists, then reset the attribute value; otherwise add attribute. 

    Environment: Internal and External 
 
    History:  Released in NX3.0 
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_set_string_ug_attribute
(  
    UF_NCFEAT_t    machining_feature,                /* <I> Machining feature */
    char           *attribute,                       /* <I> attribute name */ 
    char           *value                            /* <I> attribute value */ 
);

/********************************************************************************
     
    Get list of faces of specified machining feature.

    Environment: Internal and External 
 
    History:  Released in NX3.0 
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_ask_list_of_faces
(  
    UF_NCFEAT_t    machining_feature,                /* <I> Machining feature */
    int            *count,                           /* <O> number of faces */ 
    tag_t          **face_list                       /* <OF,len:count> face list */ 
);

/********************************************************************************
     
    Recognize hole features of the types and from the solid bodies 
    provided in the input argument.

    Environment: Internal and External 
 
    History:  Released in NX4.0 
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_recognize_holes
(  
    tag_t         *body_list,             /* <I,len:body_count>  list of solid bodies */
    int           body_count,             /* <I>  number of solid bodies */
    char          **type_list,            /* <I,len:type_count>  list of hole types to be recognized 
                                           *      NULL will recognize all types in feature definition file */
    int           type_count,             /* <I>  number of holes types to be recognized
                                           *      Zero will recognize all types in feature definition file */
    UF_MFM_recognize_options_p_t options, /* <I>  Options used during recognition */
    int           *feature_count,         /* <O>  number of recognized machining holes */
    UF_NCFEAT_t   **machining_features    /* <OF,len:feature_count> list of recognized machining features */
);

/********************************************************************************
     
    Create a machining feature of UF_MFM_source_type_recognized_feature type
    from a list of faces without setting any feature attributes.
    To set the attributes, call UF_MFM_set_double_ug_attribute.

    Environment: Internal and External 
 
    History:  Released in NX4.0 
**********************************************************************************/
extern UFUN_CAMEXPORT int UF_MFM_create_machining_feature
(  
    char          *feature_type,                /* <I>  The type of machining feature */
    int           count,                        /* <I>  The number of faces for a machining feature */
    tag_t         *face_list,                   /* <I,len:count>  The list of faces for a maching feature */
    UF_NCFEAT_t   *machining_feature            /* <O>  A new machining feature */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_FBM_GEOM_H_INCLUDED */
