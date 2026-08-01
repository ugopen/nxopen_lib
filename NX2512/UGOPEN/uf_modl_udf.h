/*****************************************************************************
             Copyright (c) 1998-2009 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about User Defined
    Features (UDF).
    There are two types of UDF features - 1. Old Style Pre-V15 UDF
                                          2. New Style V15 UDF 
    For more information about the two types of UDF please see the online help collection
    under User Defined Feature -> Redefining a UDF.
*****************************************************************************/

#ifndef UF_MODL_UDF_H_INCLUDED
#define UF_MODL_UDF_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Query the features that make up the given UDF.  The UDF is a collection of 
features.
Note:  The features of udfs have the same name as the udf.
       This routine works only with new-style UDFs released in V15

Environment:Internal and External
See Also:
History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_features_of_udf
(
    tag_t udf_tag,       /* <I>
                         The object identifier of either a UDF_INS or UDF_DEF
                         feature.
                         */
    tag_t **features,   /* <OF,len:num_feature>
                        Array of features inside the udf.  This array must
                        be freed by calling UF_free.
                        */
    int   *num_feature  /* <O>
                        Number of features
                        */
);

/****************************************************************************
Imports a user defined feature part.  You must call UF_MODL_boolean_udf for
every UDF that you import.
Note: This routine works only with old-style Pre-V15 UDFs

Environment: Internal  and  External
See Also:
 UF_MODL_export_udf
 UF_MODL_set_udf_parms
 UF_MODL_boolean_udf
 UF_MODL_ask_udf_parms
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_import_udf(
char  * filename ,/* <I>
                  User defined feature file name to import (with .udf
                  extension).
                  */
double dest_csys[9] ,/* <I>
                     CSYS for importing the file.
                     */
double  dest_point[3] ,/* <I>
                       Origin point of the CSYS.
                       */
tag_t  * udf_id  /* <O>
                 Feature obj_id of created user defined feature.
                 */
);

/********************************************************************
Gets the parameters of a User Defined Feature (UDF).
Note: This routine works only with old-style Pre-V15 UDFs

Environment: Internal  and  External
See Also:
 UF_MODL_export_udf
 UF_MODL_import_udf
 UF_MODL_set_udf_parms
 UF_MODL_boolean_udf
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_udf_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
char ** udf_name ,/* <OF>
                  UDF file name. Use UF_free to deallocate memory.
                  */
char *** udf_prompt ,/* <OF,len:num_values> 
                     UDF prompt array. Define this array as
                     char **prompt.  Use UF_free_string_array to
                     deallocate memory.
                     */
char *** udf_values ,/* <OF,len:num_values>
                    UDF expression array. Define this array as
                    char **values. Use UF_free_string_array to
                    deallocate memory.
                    */
int * num_values  /* <O>
                  Number of UDF expressions.
                  */
);

/****************************************************************************
Sets the parameters of a user defined feature part. This function can
only be called once for each udf.
Note: This routine works only with old-style Pre-V15 UDFs

Environment: Internal  and  External
See Also:
 UF_MODL_export_udf
 UF_MODL_import_udf
 UF_MODL_boolean_udf
 UF_MODL_ask_udf_parms
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_set_udf_parms(
tag_t udf_id ,/* <I>
              Feature obj_id.
              */
char  ** prompt ,/* <I,len:number_of_parms>
                 The user defined feature prompt.
                 */
char  ** values ,/* <I,len:number_of_parms>
                 The user defined feature values.
                 */
int number_of_parms  /* <I>
                     Number of parameters in the arrays.
                     */
);

/****************************************************************************
Performs a Boolean on a user defined feature in the active part. The
type of Boolean operation to perform is specified in the sign
parameter of UF_MODL_export_udf. The x-direction, with respect to
the planar tool face, is used to define the coordinate system for the
relative position dimension constraints. The normal to the planar tool
face is the z-direction and is used with the x-direction (axis) to fully
specify the relative position dimension coordinate system.

When specifying trim faces to trim the UDF, the following points
should be noted:
   1. All target faces must come from the same body.
   2. All faces including target and tool faces should be solid
      faces, and neither datum planes nor sheet faces are
      allowed.
   3. Non-planar faces can be used as target faces to trim a
      UDF body. However, if there are n trim faces, and a UDF
      body is cut to more than n+1 pieces, then the trimming
      might not work as expected. So a closed periodical face
      like a cylindrical face is not recommended to trim a UDF.
      However, an open non-planar face like a quarter
      cylindrical face could be used to trim a UDF.
   4. Trimming UDF is not applicable if this UDF's attachment
      mode is creation mode.
   5. Multiple target faces and tool faces can be specified, there
      is no limitation on how many faces can be specified.
   6. This routine should be called after UF_MODL_set_udf_parms.
   7. Once a udf is trimmed, it cannot be instanced to create an
      instance array.
   8. Note that if the trim faces do not completely intersect the
      UDF tool body, trimming might fail. One way to avoid this
      is to specify RPO (relative positioning) constraints by
      calling UF_MODL_register_rpo_routine.
   9. Redefining trim faces of UDF is not supported.


Note: This routine works only with old-style Pre-V15 UDFs
Environment: Internal  and  External
See Also:
 UF_MODL_export_udf
 UF_MODL_import_udf
 UF_MODL_set_udf_parms
 UF_MODL_ask_udf_parms
 UF_MODL_boolean_udf_1
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_boolean_udf(
tag_t udf_id ,/* <I>
              Feature obj_id.
              */
tag_t target_face ,/* <I>
                   Planar face on the target body.
                   */
tag_t tool_face ,/* <I>
                 Planar face on the tool body (of the UDF).
                 */
double tool_dir[3] ,/* <I>
                    Relative position coordinate system x-direction.
                    */
int num_target_faces ,/* <I>
                      number of faces in solid_target_faces array. If not
                      trimming the UDF, set it 0.
                      */
tag_t * solid_target_faces ,/* <I,len:num_target_faces>
                            array of faces on the target used as trim faces to
                            trim the UDF. If not trimming the UDF, set it
                            NULL.
                            */
int num_tool_faces ,/* <I>
                    number of faces in solid_tool_faces array. If not
                    trimming the UDF, set it 0.
                    */
tag_t * solid_tool_faces ,/* <I,len:num_tool_faces>
                          array of faces on the UDF to indicate which
                          portions of the UDF are going to be included or
                          excluded when the UDF is trimmed. If not
                          trimming the UDF, set it to NULL.
                          */
logical included ,/* <I>
                  true if included faces; false if excluded faces.
                  */
tag_t * udf_meta_id  /* <O>
                     Tag to use for all subsequent calls to this udf
                     */
);

/****************************************************************************
This routine is basically the same as UF_MODL_boolean_udf, except
that it allows you to place a UDF on a datum plane. If the target face
is a datum plane, you need to specify which side of the datum plane
you want the udf to be put on. True means to put the udf on the
positive side of the datum plane, false means to put the udf on the
negative side of the datum plane. If a datum plane is a fixed datum,
you need to specify which target body with which the UDF is to be
booleaned.

Note: This routine works only with old-style Pre-V15 UDFs
Environment: Internal  and  External
See Also:
 UF_MODL_export_udf
 UF_MODL_import_udf
 UF_MODL_set_udf_parms
 UF_MODL_ask_udf_parms
 UF_MODL_boolean_udf
History: Original release was in V14.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_boolean_udf_1(
tag_t udf_id ,/* <I>
              udf feature id
              */
tag_t target_face ,/* <I>
                   datum plane id or a face on the target body
                   */
tag_t tool_face ,/* <I>
                 face on the udf tool body
                 */
double tool_dir[3] ,/* <I>
                    X direction of the tool
                    */
int num_target_faces ,/* <I>
                      length of target faces array
                      */
tag_t * target_faces ,/* <I,len:num_target_faces>
                      array of trimming faces on the target body
                      */
int num_tool_faces ,/* <I> 
                    length of  tool faces array
                    */
tag_t * tool_faces ,/* <I,len:num_tool_faces>
                    array of faces on udf body which are included or
                    excluded
                    */
logical included ,/* <I>
                  true for included faces, or false for excluded faces
                  */
tag_t target_body ,/* <I>
                   the target body with which the udf will be
                   booleaned
                   */
logical flip ,/* <I>
              true to accept the datum plane direction, false to
              flip the datum pside
              */
tag_t * udf_meta_id  /* <O>
                     this tag should be used for all subsequent calls to
                     this udf
                     */
);

/****************************************************************************
Exports a user defined feature part. Note that you must use the
UF_MODL_boolean_udf to actually perform the Boolean operation
specified by the sign parameter.

User Defined Features (UDFs) allow you to define the shape and
function of features. This gives you the ability to create a library of
features tailored to your needs.

Four Open API routines provide support for the creation of User
Defined Features. These routines generally reflect the interactive
UDF functionality. Please see user-defined features in the Modeling
User Manual for more information and examples. The Open API
routines are UF_MODL_export_udf, UF_MODL_import_udf, UF_MODL_set_udf_parms
and UF_MODL_boolean_udf.  In addition, there is one inquiry routine
UF_MODL_ask_udf_parms.

All UDFs must be predefined (created) and saved as a user-defined
feature file. You use the UF_MODL_export_udf to create the file. You
retrieve a UDF using UF_MODL_import_udf and use UF_MODL_set_udf_parms
to change the predefined feature parameters and UF_MODL_boolean_udf to
make the UDF part of your model. You can also use the relative position
routines (see UF_MODL_register_rpo and UF_MODL_unregister_rpo) to position
your UDF on your part.

To create a UDF file, you must first create a model using the existing
functions (Open API, GRIP, or interactively). This entire model,
including expressions, is the new UDF you wish to define. The UDF
must be created in the absolute coordinate space. The origin (0,0,0) is
considered the feature's origin.

After the geometry is defined, you use UF_MODL_export_udf to
create a user feature output file. The UDF file contains the geometry
as well as information on the input parameters (i.e. those parameters
that you let other users change when the UDF is brought into their
parts) and the attachment method.

The UDF file has the same name as the part name but with the ".udf"
extension. For example, if your part name were "name_of_file.prt",
then the udf file name would be "name_of_file.udf".  Input parameters
are those parameters you wish to be entered during the creation of a
model as a feature. The input parameters are specified by the ip_prompts,
ip_names, and number_of_elements arguments.

All variables not entered as input variables become constants or they
can be controlled using expressions established before saving the
UDF file. For example, let's say your UDF consists of a block where
p0 represents the width, p1 represents the length, and p2 represents
the height. You have determined that you wish the width and length to
be specified when bringing in the UDF, but you wish the height to
always be the width plus twice the length.

In your creation of the block, you would have predefined p2 = p0 +
2*p1. But you need to specify to the UFD file that p0 and p1 are the
input parameters. You specify the variables or expressions in the
ip_names argument. You can alias these expressions using the
ip_prompts arguments.

When specifying the input parameters when importing the UDF, you
set the parameters using the alias prompt name. An error occurs if
you specify variables that do not exist in the model and the UDF file
is not created. In our preceding example, you would specify the inputs
parameters as follows:
    int number2 = number_of_elements = 2;
    char *ip_prompts[number2] = {"width", "length"};
    char *ip_names[number2]  = {"p0", "p1"};

You specify the attachment method that the UDF is to perform when
brought into your model. The options are create, add, subtract, and
intersect (UF_NULLSIGN, UF_POSITIVE, UF_NEGATIVE, and UG_UNSIGNED
respectively).

After the feature is saved, you need to specify data when bringing the
UDF into your part. With UF_MODL_import_udf, you specify the udf
part file name and the destination csys and point. The routine returns
the tag of the UDF.  The destination csys is the orientation in which
the feature is brought into the part. The destination point is the
location at which the system places the origin of the UDF.

UF_MODL_set_udf_parms sets the values for UDF predefined parameter names
(prompts).  An error results if you provide an incorrect parameter name.
You can use UF_MODL_ask_udf_parms to inquire the names and current
setting of the input parameters.

Finally, you use UF_MODL_boolean_udf to specify the planar face on the UDF
(tool body) that is to be placed directly on the planar body (target body).
You also need to determine what is the x-direction on the planar tool face
to define the coordinate system for the relative positioning constraints.
The normal to the planar tool face is the z-axis and is used with the
x-direction to fully specify the relative positioning dimension coordinate
system. Before applying the boolean, you may wish to register the relative
position to allow you to specify the position of the udf. If the attachment
method is "create," then you do not need to specify the planar faces.
However, you must call UF_MODL_boolean_udf for every imported UDF regardless
of the type of Boolean operation performed.

Note: This routine works only with old-style Pre-V15 UDFs
Environment: Internal  and  External
See Also:
 UF_MODL_export_udf
 UF_MODL_import_udf
 UF_MODL_set_udf_parms
 UF_MODL_boolean_udf
 UF_MODL_ask_udf_parms
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_export_udf(
char  ** ip_prompts ,/* <I,len:number_of_elements>
                     Pointer to array of pointers to ip prompts.
                     */
char  ** ip_names ,/* <I,len:number_of_elements>
                   Pointer to array of pointers to ip variable names.
                   */
int number_of_elements ,/* <I>
                        Number of elements in array.
                        */
UF_FEATURE_SIGN sign  /* <I>
                      The attachment method sign. Valid options:
                      UF_NULLSIGN = 0, create new target solid
                      UF_POSITIVE = 1, add to target solid
                      UF_NEGATIVE = 2, subtract from target solid
                      UF_UNSIGNED = 3 intersect with target solid
                      */
);

/******************************************************************************
Query the external references that make up the UDF definition.

Note: This routine works only with new-style UDFs released in V15
Environment:Internal and External
See Also:
History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_udf_definition
(
    tag_t udf_tag,                /* <I>
                                  Object identifier of a UDF feature definition,
                                  UDF_DEF.
                                  */
    tag_t **parents,              /* <OF,len:num_parents>
                                  Array of external parents of the udf.
                                  This must be freed by calling UF_free.
                                  */
    char  ***parents_prompt,      /* <OF,len:num_parents> 
                                  Array of prompts.  This must be freed by
                                  calling UF_free_string_array.
                                  */
    int   *num_parents,           /* <O>
                                  Number of external parents
                                  */
    tag_t **expression,           /* <OF,len:num_expression> 
                                  Array of expressions.  This must be freed by
                                  calling UF_free.
                                  */
    char  ***expression_prompt,   /* <OF,len:num_expression>
                                  Array of prompt.  This must be freed by
                                  calling UF_free_string_array.
                                  */
    int   *num_expression         /* <O>
                                  NUmber of expressions
                                  */
);

/******************************************************************************
Create a new UDF instantiation in the current part.  The steps to instantiate a
new UDF are as follows:

1) Open the UDF definition file using UF_PART_open_quiet().
2) Find the UDF feature definition.
3) Ask for the UDF definition to get all the external references.
4) Change part to the instantiation part
5) For each external reference you need to select a new reference in the
   instantiation part.
6) Get new values for the expressions.
7) Use UF_MODL_create_instantiated_udf to create a UDF instantiation.

There is a newer version of this API - UF_MODL_create_instantiated_udf1
It is recommended to use the newer version for the following cases -
1. The inputs to a UDF consist of selection-intent objects. 
2. One needs to use a UDF input in the reverse sense.
3. One wants provide specific mapping when dealing with selection-intent inputs.

For more details about mapping see the documentation for UF_MODL_create_instantiated_udf1

Note: This routine works only with new-style UDFs released in V15
Environment:Internal and External
See Also:

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_instantiated_udf
(
    tag_t udf_definition_tag,     /* <I>
                                  The object identifier of the udf feature
                                  definition, UDF_DEF.
                                  */
    char  *cgm_file_name,         /* <I>
                                  Cgm file
                                  */
    tag_t *old_parents,           /* <I,len:num_parents>
                                  Array of old parents
                                  */
    tag_t *new_parents,           /* <I,len:num_parents>
                                  Array of new parents
                                  */
    int   num_parents,            /* <I>
                                  Number of parents
                                  */
    tag_t *old_expression,        /* <I,len:num_expression>
                                  Array of udf definition expression
                                  */
    char  **new_expression_value, /* <I,len:num_expression>
                                  Array of new expression new values only
                                  the right hand side
                                  */
    int   num_expression,         /* <I>
                                  Number of expressions.
                                  */
    tag_t *new_udf                /* <O>
                                  New udf instantiated feature, a
                                  UDF_INS feature.
                                  */
);

/******************************************************************************
If the udf contains a single sweep along guide, returns this sweep. If
the udf does not contain any sweep which is the type of sweep along
the guide, or the udf contains more than one sweep which is the type
of sweep along guide, then the routine returns NULL_TAG.


Note: This routine works only with old-style Pre-V15 UDFs
Environment: Internal  and  External
See Also: UF_MODL_ask_sweep_curves  
          UF_MODL_edit_sweep_curves 
History:
 ******************************************************************************/
extern UFUNEXPORT int  UF_MODL_ask_sweep_of_udf(
tag_t udf_eid ,/* <I>
               udf object identifier
               */
tag_t * sweep_eid  /* <O>
                   sweep object identifier within the udf
                   */
);

/*******************************************************************************
This function gets the data of a given UDFS feature.
To free the members of the data structure UF_MODL_udfs_def_data_p_t, please
call function UF_MODL_free_udfs_def_data.
Note:  The features of udfs have the same name as the udf.
       This routine works only with new-style UDFs released in V15
Environment:Internal and External
See Also:
History: 
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_udfs_ask_def_data
(
   tag_t feature_tag, /* <I> feature tag - Tag of UDFS feature */
   UF_MODL_udfs_def_data_p_t udfs_data /* <OF> - Data for redefinition */
);
/*******************************************************************************
This function frees the definition data of a UDF.

Note: This routine works only with new-style UDFs released in V15
Environment:Internal and External
See Also:
History: 
*******************************************************************************/
extern UFUNEXPORT void UF_MODL_free_udfs_def_data
(
  UF_MODL_udfs_def_data_p_t udfs_data /* <I> - Data to be freed */
); /* <NEC> */

/*******************************************************************************
This function creates a new udfs feature by given data.

Note: This routine works only with new-style UDFs released in V15
Environment:Internal and External
See Also:
History: 
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_udfs_create_def
(
   tag_t *feature_tag,/* <I> feature tag - Tag of UDFS feature */
   UF_MODL_udfs_def_data_p_t udfs_data/* <I> - Data for redefinition */
);

/*******************************************************************************
 This function redefines a given UDFS feature. It also reorders the
 feature as the "youngest" one in the file.

Note: This routine works only with new-style UDFs released in V15
Environment:Internal and External
See Also:
History: 
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_udfs_redefine_def
(
   tag_t feature_tag,/* <I> feature tag - Tag of UDFS feature */
   UF_MODL_udfs_def_data_p_t udfs_data/* <I> - Data for redefinition */
);

/******************************************************************************
Respecifies trim faces for a UDF. All the old trim faces are replaced
by new trim faces. The UDF should have been trimmed when it was
originally imported.

Note: This routine works only with old-style Pre-V15 UDFs
Environment: Internal  and  External
See Also: UF_MODL_boolean_udf
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_redefine_trim_faces(
tag_t udf_id ,/* <I>
              udf id which is returned from UF_MODL_boolean_udf()
              */
int n_trim_faces ,/* <I>
                  number of trim faces
                  */
tag_t trim_faces[] ,/* <I,len:n_trim_faces>
                    array of trim faces
                    */
logical delete_rpo  /* <I>
                    flag to indicate whether to delete rpo or not
                    */
);

/***********************************************************************
 * Function description:
 *
 *   User function for initializing UDF instantiation data from
 *   a UDF definition feature. Note that the following attributes are only 
 *   filled out (i.e. memory and content).
 *
 *   num_exps              (UF_MODL_udf_exp_data_t)
 *   old_exps              (UF_MODL_udf_exp_data_t)
 *   num_refs              (UF_MODL_udf_ref_data_t)
 *   old_refs              (UF_MODL_udf_ref_data_t)
 *   reverse_refs_dir      (UF_MODL_udf_ref_data_t)
 *   num_mapping_objs      (UF_MODL_udf_mapping_data_t) 
 *   reverse_objs_dir      (UF_MODL_udf_mapping_data_t)
 *   old_output_objs       (UF_MODL_udf_mapping_data_t) 
 *   old_output_objs_index (UF_MODL_udf_mapping_data_t) 
 * 
 *   The memory of the following attributes must be allocated by the user 
 *   and their contents must be inputted by the user for further applications 
 *   such as the instantiation of a UDF feature and etc.
 *   
 *   new_exp_values        (UF_MODL_udf_exp_data_t)
 *   new_refs              (UF_MODL_udf_ref_data_t)
 *   new_output_objs       (UF_MODL_udf_mapping_data_t) 
 *   new_output_objs_index (UF_MODL_udf_mapping_data_t) 
 *
 *
 * Environment: Internal  and  External
 *
 * It can accept single UDF references and Smart Collectors and Sections in
 * UF_MODL_udf_ref_data_t.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * See Also: UF_MODL_ask_instantiated_udf
 *
 * History: This function was originally released in NX3.
 ***********************************************************************/

extern UFUNEXPORT int UF_MODL_udf_init_insert_data_from_def
( 
    tag_t                  udf_define_tag, /* <I>  Tag of UDF definition feature */
    UF_MODL_udf_exp_data_t *exp_data,      /* <OF> Expression data */
    UF_MODL_udf_ref_data_t *ref_data       /* <OF> Parent data */
);

/***********************************************************************
 * Function description:
 *   User function for instantiating a UDF feature.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * It can accept single UDF references and Smart Collectors and Sections in
 * UF_MODL_udf_ref_data_t.
 *
 * There is a newer version of this API - UF_MODL_create_instantiated_udf1
 * It is recommended to use the newer version for the following cases -
 * 1. The inputs to a UDF consist of selection-intent objects. 
 * 2. One needs to use a UDF input in the reverse sense.
 * 3. One wants provide specific mapping when dealing with selection-intent inputs.
 * 
 * A simple example where mapping is required while instantiating a UDF is as follows:
 * 1. A UDF comprises of an extrude feature and a blend feature
 * 2. The blend feature blends one edge of the extrude feature
 * 3. The extrude feature's input is a selection-intent section. 
 * 4. In the UDF definition, the section comprised of four curves. One of the
 *    curves produces an extrude lateral face. One edge of the lateral face 
 *    was blended by the blend feature.
 * 5. Hence the blend feature is a downstream child of one of the curves of the
 *    input section of the UDF definition.
 * 6. While instantiating, the new input section can have any number of curves.
 * 7. Hence while instantiating, the output blend feature will get created based
 *    on which curve of the instantiation input selection-intent section maps to the 
 *    corresponding curve of definition selection-intent section.   
 *
 * The following steps describe how to instantiate a UDF with mapping using the Open C API:
 *  as an Internal User Function program
 * 
 * Run the user function program
 * 
 * Then select the sketch(8)
 * Select "Sketch Section" on the next dialog
 * For smart-dir, select the sketch(8) again
 * OK through all other dialogs to create the UDF
 * 
 * To run see how this works interactively in NX two files have been provided.  They are
 * 
 * 
 *
 * See Also: UF_MODL_udf_init_insert_data_from_def
 * History: This function was originally released in NX3.
 ***********************************************************************/

extern UFUNEXPORT int UF_MODL_create_instantiated_udf1
( 
    tag_t                  udf_define_tag,  /* <I> Tag of UDF definition feature */
    UF_MODL_udf_exp_data_t *exp_data,       /* <I> Expression data */
    UF_MODL_udf_ref_data_t *ref_data,       /* <I> Parent data */
    tag_t                  *udf_insert_tag  /* <O> Tag of UDF instantiated feature */
);

/***********************************************************************
 * Function description:
 *   User function for requiring a UDF instantiated feature defining data.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * It can accept single UDF references and Smart Collectors and Sections in
 * UF_MODL_udf_ref_data_t.
 *
 * See Also: UF_MODL_udf_init_insert_data_from_def and 
 *           UF_MODL_create_instantiated_udf1
 * 
 * History: This function was originally released in NX3.
 *
 ***********************************************************************/

extern UFUNEXPORT int UF_MODL_ask_instantiated_udf
(
    tag_t                  udf_insert_tag,/* <I>  Tag of UDF instantiated feature */
    UF_MODL_udf_exp_data_t *exp_data,     /* <OF> Expression data */
    UF_MODL_udf_ref_data_t *ref_data      /* <OF> Parent data */
);

/**********************************************************************
 * Function description:
 *   User function for editing a UDF instantaited feature.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * It can accept single UDF references and Smart Collectors and Sections in
 * UF_MODL_udf_ref_data_t.
 *
 * Note that a Smart Section in ref_data must be deleted when a Smart Section is
 * created as a new UDF parent for the editing purpose.
 *
 * See Also: UF_MODL_ask_instantiated_udf
 *
 * History: This function was originally released in NX3.
 ********************************************************************/

extern UFUNEXPORT int UF_MODL_edit_instantiated_udf
(   
    tag_t                  udf_insert_tag,/* <I> Tag of UDF instantiated feature */
    logical                explosion,     /* <I> Flag of explosion */
    UF_MODL_udf_exp_data_t *exp_data,     /* <I> Expression data */
    UF_MODL_udf_ref_data_t *ref_data      /* <I> Parent data */
);

/************************************************************************
 * This function is to initialize the expression data of a UDF.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment:Internal and External
 *
 * See Also: UF_MODL_create_instantiated_udf1, UF_MODL_edit_instantiated_udf
 *
 * History: This function was originally released in NX3.
 ***********************************************************************/

extern UFUNEXPORT void UF_MODL_udf_init_exp_data
(
    UF_MODL_udf_exp_data_p_t exp_data /* <I/O> The UDF expression data to be initialized */
);

/************************************************************************
 * This function is to initialize the mapping data of a UDF.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment:Internal and External
 *
 * See Also: UF_MODL_create_instantiated_udf1, UF_MODL_edit_instantiated_udf
 *
 * History: This function was originally released in NX3.
 ***********************************************************************/

extern UFUNEXPORT void UF_MODL_udf_init_mapping_data
(
    UF_MODL_udf_mapping_data_p_t mapping_data /* <I/O> The UDF mapping data to be initialized */
);

/************************************************************************
 * This function is to initialize the reference data of a UDF.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment:Internal and External
 *
 * See Also: UF_MODL_create_instantiated_udf1, UF_MODL_edit_instantiated_udf 
 *
 * History: This function was originally released in NX3.
 ***********************************************************************/

extern UFUNEXPORT void UF_MODL_udf_init_ref_data
(
    UF_MODL_udf_ref_data_p_t ref_data /* <I/O> The UDF reference data to be initialized */
);

/************************************************************************
 * This function frees the expression data of a UDF.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment:Internal and External
 *
 * See Also: UF_MODL_ask_instantiated_udf
 *
 * History: This function was originally released in NX3.
 ***********************************************************************/

extern UFUNEXPORT void UF_MODL_udf_free_exp_data
(
    UF_MODL_udf_exp_data_p_t exp_data /* <I> - The UDF expression data to be freed */
);

/************************************************************************
 * This function frees the mapping data of a UDF.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment:Internal and External
 *
 * See Also: UF_MODL_ask_instantiated_udf
 *
 * History: This function was originally released in NX3.
 ***********************************************************************/

extern UFUNEXPORT void UF_MODL_udf_free_mapping_data
(
    UF_MODL_udf_mapping_data_p_t mapping_data /* <I> - The UDF mapping data to be freed */
);

/************************************************************************
 * This function frees the reference data of a UDF.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment:Internal and External
 *
 * See Also: UF_MODL_ask_instantiated_udf
 *
 * History: This function was originally released in NX3.
 ***********************************************************************/

extern UFUNEXPORT void UF_MODL_udf_free_ref_data
(
    UF_MODL_udf_ref_data_p_t ref_data /* <I> - The UDF reference data to be freed */
);

/****************************************************************************
 * Register a routine for UDF obtaining mapping data. This allows you to register
 * a routine into the Open API environment so that you can select some
 * objects that need to be mapped at UDF instantiation or editing if a mapping 
 * between old UDF parents and new UDF parents is necessary. Subsequently, 
 * every time a UDF feature is instantiated or edited, this registered routine 
 * is called. To register a routine named user_udf_mapping_routine(), the call 
 * is:
 *
 * UF_MODL_register_udf_mapping_routine(user_udf_mapping_routine)
 * where user_udf_mapping_routine is defined as:
 * int user_udf_mapping_routine()
 *
 * Calling this function will prevent an internal Open shared library from 
 * being unloaded, and overrides the setting of the user supplied function, 
 * ufusr_ask_unload.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * See Also: UF_MODL_unregister_udf_mapping_routine
 *
 * History: This function was originally released in NX3.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_register_udf_mapping_routine
(
    UF_MODL_udf_mapping_f_p_t routine /* <I>
                                         Routine name. You define the routine.  
                                         The system calls the routine like this:
                                         UF_MODL_udf_mapping_f_p_t routine
                                         (tag_t       udf_feature_tag,
                                          UF_MODL_udf_ref_data_t *ref_data)
  
                                         where udf_feature_tag is a tag of the enquiring 
                                         UDF defintion feature (for instantiation)
                                         or instantiated feature (for editing), 
                                         and ref_data is the output of this UDF parent 
                                         data including mapping data that the user needs 
                                         to obtain. 

                                         The routine returns an error if it failed. 
                                         If the returned error is != 0, then it is
                                         successful.
                                      */
);

/*******************************************************************************
 * Returns the currently specified UDF mapping data routine as a function pointer 
 * of type UF_MODL_udf_mapping_f_p_t.  If no routine is specified, zero is returned.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * See Also: UF_MODL_register_udf_mapping_routine
 *
 * History: This function was originally released in NX3.
********************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_udf_mapping_routine
(
    UF_MODL_udf_mapping_f_p_t *user_udf_mapping_routine 
                              /* <I>
                                 Function pointer to the currently
                                 specified UDF mapping data routine.
                              */
);

/****************************************************************************
 * Unregisters a routine for relative positioning.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * See Also: UF_MODL_register_udf_mapping_routine
 *           UF_MODL_unregister_udf_mapping_routine
 *
 * History: This function was originally released in NX3.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_unregister_udf_mapping_routine
( 
    void 
);

/****************************************************************************
 * Ask the UDF mapping data at instantiation.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * See Also: UF_MODL_register_udf_mapping_routine
 *           UF_MODL_unregister_udf_mapping_routine
 *
 * History: This function was originally released in NX3.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_udf_mapping_for_insert
(
    tag_t                  udf_define_tag,      /* <I>  Tag of UDF definition feature */
    UF_MODL_udf_ref_data_t *ref_data            /* <OF> Parent data */
);

/****************************************************************************
 * Ask the UDF mapping data at editing.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * See Also: UF_MODL_register_udf_mapping_routine
 *           UF_MODL_unregister_udf_mapping_routine
 *
 * History: This function was originally released in NX3.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_udf_mapping_for_edit
(
    tag_t                  udf_insert_tag,      /* <I>  Tag of UDF instantiated feature */
    UF_MODL_udf_ref_data_t *ref_data            /* <OF> Parent data */
);

/****************************************************************************
 * Ask if a mapping between old UDF parents and new parents is needed at instantiation.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * See Also: UF_MODL_register_udf_mapping_routine
 *           UF_MODL_unregister_udf_mapping_routine
 *
 * History: This function was originally released in NX3.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_require_udf_mapping_for_insert
(
    tag_t udf_define_tag,           /* <I> Tag of UDF definition feature */
    logical *mapping_is_required,   /* <O> TRUE: a mapping is required */
    int *mapping_num_objects,       /* <O> Number of mapping objects */
    tag_t **mapping_objects         /* <OF,len:mapping_num_objects> Array of mapping objects */ 
);

/****************************************************************************
 * Ask if a mapping between old UDF parents and new parents is needed at editing.
 *
 * Note: This routine works only with new-style UDFs released in V15
 * Environment: Internal  and  External
 *
 * See Also: UF_MODL_register_udf_mapping_routine
 *           UF_MODL_unregister_udf_mapping_routine
 *
 * History: This function was originally released in NX3.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_require_udf_mapping_for_edit
(
    tag_t udf_insert_tag,           /* <I> Tag of UDF instantiated feature */
    logical *mapping_is_required,   /* <O> TRUE: a mapping is required */
    int *mapping_num_objects,       /* <O> Number of mapping objects */
    tag_t **mapping_objects         /* <OF,len:mapping_num_objects> Array of mapping objects */ 
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_UDF_H_INCLUDED */
