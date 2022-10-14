/*****************************************************************************
             Copyright (c) 2002-2003 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about isets.

*****************************************************************************/

#ifndef UF_MODL_ISETS_H_INCLUDED
#define UF_MODL_ISETS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
Creates a linear instance set feature using the existing work
coordinate system. The values needed are the number in the XC
direction, spacing for the XC direction, number in the YC direction,
spacing in the YC direction, and a list of features to instance. The
output of this function is the object identifier associated to the linear
instance set.

A different instance set will be created for each item in the feature_list.
feature_obj_id will be the identifier of last instance set feature created. 
To query ids of other instance set features, call UF_MODL_ask_instance_iset 
with each item in the feature list as an argument.

To query instances created by this instance set use the function
UF_MODL_ask_instance

The method options correspond to what is available interactively. See
the Modeling User Manual for details.

Environment: Internal  and  External
See Also:UF_MODL_ask_instance
UF_MODL_ask_instance_iset
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_linear_iset(
int method ,/* <I>
            Method:
            0 =  General
            1 = Simple
            2 = Identical
            */
char * number_in_x ,/* <I>
                    Number in XC direction.
                    */
char * distance_x ,/* <I>
                   Spacing in XC direction.
                   */
char * number_in_y ,/* <I>
                    Number in YC direction.
                    */
char * distance_y ,/* <I>
                   Spacing in YC direction.
                   */
uf_list_p_t feature_list ,/* <I>
                          List of selected CMOD features.
                          */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created linear iset
                        */
);

/****************************************************************************
Creates a circular instance set feature using the rotation point,
rotation axis, number of instances, rotational angle and list of selected
features. The output of this function is the object identifier associated
to the circular instance set.

A different instance set will be created for each item in the feature_list.
(except datum axis. See the usage of datum axis below ). feature_obj_id will 
be the identifier of last instance set feature created. To query ids of other 
instance set features, call UF_MODL_ask_instance_iset with each item in the 
feature list as an argument.

You can use a datum axis as a rotation axis. To accomplish this place the tag
of the datum axis at the end of feature_list.  Then initialize the location
and axis array arguments even though they are not used.  Using a datum axis has
the advantage of being associative.

To query instances created by this instance set use the function
UF_MODL_ask_instance

The method options correspond to what is available interactively. See
the Modeling User Manual for details.

Environment: Internal  and  External
See Also:UF_MODL_ask_instance
UF_MODL_ask_instance_iset

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_circular_iset(
int method ,/* <I>
            Method:
            0 = General
            1 = Simple
            2 = Identical
            */
double location[3] ,/* <I>
                   Rotation point.
                   */
double axis[3] ,/* <I>
                Rotation axis.
                */
char * number_str ,/* <I>
                   Number of instances.
                   */
char * angle_str ,/* <I>
                  Rotation angle.
                  */
uf_list_p_t feature_list ,/* <I>
                          List of selected features.
                          */
tag_t * feature_obj_id  /* <O>
                       Feature object identifier of created iset
                        */
);

/********************************************************************
Returns the parameters for a linear instance set.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_linear_iset_parms(
tag_t feature_obj_id ,/* <I>
                      Linear instance set feature identifier.
                      */
int edit ,/* <I>
          This is an unused flag. It normally determines
          whether to return the right-hand side or both sides
          of an expression. Currently, both sides of an
          expression are returned. Set the value of this flag to
          integer value 1.
          */
char ** number_in_x ,/* <OF>
                     Expression containing the number of instances in
                     the X direction.  This must be freed by calling
                     UF_free.
                     */
char ** number_in_y ,/* <OF>
                     Expression containing the number of instances in
                     the Y direction.  This must be freed by calling
                     UF_free.
                     */
char ** distance_x ,/* <OF>
                    The distance between instances in the X direction.
                    This must be freed by calling UF_free.
                    */
char ** distance_y  /* <OF>
                    The distance between instances in the Y direction.
                    This must be freed by calling UF_free.
                    */
);

/********************************************************************
Gets circular instance parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_circular_iset_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int  edit ,/* <I>
           This is an unused flag. It used to determine whether
           to return the right-hand side or both sides of an
           expression. Currently, both sides of an expression
           are returned.
           */
char ** radius ,/* <OF>
                Iset radius.  This must be freed by calling
                UF_free.
                */
char ** number ,/* <OF>
                Number of instances.  This must be freed by calling
                UF_free.
                */
char ** angle  /* <OF>
               Angle between instances.  This must be freed by
               calling UF_free.
               */
);

/****************************************************************************
Edits an instance linear set feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_linear_iset(
tag_t feature_obj_id ,/* <I>
                      Linear instance set feature identifier
                      */
char * number_in_x ,/* <I>
                    Number in XC direction
                    */
char * distance_x ,/* <I>
                   Spacing in XC direction
                   */
char * number_in_y ,/* <I>
                    Number in YC direction
                    */
char * distance_y  /* <I>
                   Spacing in YC direction
                   */
);

/****************************************************************************
Edits an instance circular set feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_circular_iset(
tag_t feature_obj_id ,/* <I>
                      Circular instance set feature identifier
                      */
char * number_str ,/* <I>
                   Number of instances
                   */
char * angle_str ,/* <I>
                  Rotation angle (degrees)
                  */
char * radius_str ,/* <I>
                   Instance set radius
                   */
tag_t rotation_point_id  /* <I>
                         Rotation point identifier:
                         NULL_TAG = Modify Circular Iset without moving it
                         Otherwise modify Circular Iset and move it to new
                         point. If the circular iset feature
                         cannot be moved to the new point,
                         an error code is issued and no
                         modifications are performed.
                         */
);


/********************************************************************
UF_MODL_ask_instance() gets instance feature records of a linear or a 
circular instance set.

The instances of a two dimensional rectangular array are returned in 
column major order. As an example, for a 2x3 rectangular array, the 
instances are serialized in this order:
element 1 - (0,0)
element 2 - (0,1)
element 3 - (0,2)
element 4 - (1,0)
element 5 - (1,1)
element 6 - (1,2)

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_instance(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier of linear_iset or
                      circular_iset
                      */
uf_list_p_t * instances_feature_list  /* <OF,free:UF_MODL_delete_list>
                                      List of instances feature records.
                                      This must be freed by calling
                                      UF_MODL_delete_list.
                                      */
);

/********************************************************************
Gets the master feature of an instance.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_master(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier of the instance.
                      */
tag_t * master_feature_obj_id  /* <O>
                               The object identifier of the master feature
                               */
);

/********************************************************************
Gets the instance set feature of an instance.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_instance_iset(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier of the instance
                      */
tag_t * iset_feature_obj_id  /* <O>
                             Pointer to the iset feature object identifier
                             */
);

/****************************************************************************
Creates a clocking of an instance feature input as the feature object
identifier.
The other inputs are the offset expressions for the X, and Y, directions.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_clock_instance(
tag_t  feature_obj_id ,/* <I>
                       Object identifier of the instance
                       */
char * clock_value1 ,/* <I>
                     X-dir clocking expression
                     */
char * clock_value2  /* <I>
                     Y-dir clocking expression
                     */
);

/****************************************************************************
Unclocks the particular instance feature input as the feature object identifier.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_unclock_instance(
tag_t  feature_obj_id  /* <I>
                       Object identifier for instance
                       */
);

/****************************************************************************
Unclocks the entire instance set input as the feature object identifier.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_unclock_iset(
tag_t  feature_obj_id  /* <I>
                       Object identifier for the instance set
                       */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_ISETS_H_INCLUDED */
