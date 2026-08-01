/*******************************************************************************
             Copyright (c) 1998-2004 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       



File description:

    Open API interface to families.

    Object Family Terminology
    -------------------------

    Family table - A table which describes various attributes of an
    object.  Each row in the table is called a family member.  Each family
    member defines a set of attribute values(represented by text) for the
    attributes in the object family.

    Family member instance - An object, which when created, applies a set
    of attribute values to the attributes in the object family.

    Family - The family table and family member instances.
    The routines in this file allow you to:
    .   add a family member
    .   query attribute data, class count, class data, class name,
        family data, instance data, member column data, or member
        row data.
    .   check attribute status, family status, or member status.
    .   create an attribute or a family.
    .   delete an instance or a member.
    .   edit an attribute, a family or a member.
    .   evaluate intent data.
    .   free attribute data, class data, family data, or member data.

Terminology: 
-----------
    part family       -            a set of parts defined by a template part,
                                   table of attributes, and family members.
                                   Also referred to as a family of parts.
    template part     -            A part file that contains a table of the
                                   family members and attributes
                                   (parameters) associated with each
                                   member of a part family.
    family member     -            is a part file which belongs to a part
                                   family and is enumerated in the template
                                   part's table of members and attributes.
    family attribute class  -      is a subtype of a family attribute such as
                                   a character string, expression, etc. See
                                   the description for the "subtype" field in
                                   the structure UF_FAM_class_data_s.

Concepts:
--------
    A family is defined by a set of family attributes and a table of family
    members which define the values of the attributes. For example the
    following family has two attributes. The first attribute is a name
    attribute. The second attribute is an expression attribute. A part file
    containing a family is known as a family template part.
  
    NAME           P1
    member1        1.0
    member2        2.0
    member3        3.0
 
    By creating an instance of a family member at the UF_FAM level, the
    attribute values of that member are applied to the template part. In
    the example above, you would set the value of the NX expression P1
    to 2.0 in order to create an instance of member2.
    
    If you create an instance of a family member at the UF_PART level,
    you are creating an instance of the member inside of a new part which
    is a copy of the template part. The new part inherits the name of the
    member name, e.g. in this case it would be called member2.prt.

    At the UF_FAM level, a family member select intent is a set of rules
    which allow the system to automatically select a family member from
    a family. Using the example above, an intent might look like "P1 >
    1.0" or "P1 == 3.0" or "NAME == member3".

    At the UF_ASSEM level, an instance intent is a UF_FAM intent rule
    associated with an assembly instance. This allows the system to
    automatically select a new part family member based upon the rules
    which specify the member selection intent.
  
****************************************************************************/

#ifndef UF_FAM_H_INCLUDED
#define UF_FAM_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_fam_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************
Returns the number of available family attribute classes.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_ask_class_count(
int *  class_count  /* <O>
                    Number of available family attribute classes.
                    */
);

/***************************************************************************
Returns the name of a family attribute class.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_ask_class_name(
int  subtype ,/* <I>
              Attribute subtype of class
              UF_fam_attr_text_subtype:
              UF_fam_attr_numeric_subtype:
              UF_fam_attr_integer_subtype,
              UF_fam_attr_double_subtype,
              UF_fam_attr_string_subtype,
              UF_fam_attr_part_subtype,
              UF_fam_attr_name_subtype,
              UF_fam_attr_instance_subtype,
              UF_fam_attr_exp_subtype,
              UF_fam_attr_mirror_subtype,
              UF_fam_attr_density_subtype,
              UF_fam_attr_feature_subtype,
              */
char **  name  /* <OF>
               Name of the attribute class.  This must be freed
               by calling UF_free.
               */
);

/***************************************************************************
Returns the data associated with a family attribute class.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_ask_class_data(
int  subtype ,/* <I>
              Attribute subtype of class
              UF_fam_attr_text_subtype:
              UF_fam_attr_numeric_subtype:
              UF_fam_attr_integer_subtype,
              UF_fam_attr_double_subtype,
              UF_fam_attr_string_subtype,
              UF_fam_attr_part_subtype,
              UF_fam_attr_name_subtype,
              UF_fam_attr_instance_subtype,
              UF_fam_attr_exp_subtype,
              UF_fam_attr_mirror_subtype,
              UF_fam_attr_density_subtype,
              UF_fam_attr_feature_subtype,
              */
UF_FAM_class_data_p_t class_data  /* <O>
                                  Data of the attribute class.
                                  */
);

/***************************************************************************
Frees data returned from UF_FAM_ask_class_data.

Environment: Internal  and  External

See Also:  UF_FAM_ask_class_data

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_free_class_data(
UF_FAM_class_data_p_t class_data  /* <I>
                                  Data of the attribute class.
                                  */
);

/***************************************************************************
Creates a family attribute.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_create_attribute(
UF_FAM_attribute_data_p_t attribute_data ,/* <I>
                                          Data for the attribute.
                                          */
tag_t *attribute  /* <O>
                  Object identifier of attribute.
                  */
);

/***************************************************************************
Edits a family attribute.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_edit_attribute(
tag_t attribute ,/* <I>
                 Object identifier of the attribute.
                 */
UF_FAM_attribute_data_p_t attribute_data  /* <I>
                                          New data for the attribute.
                                          */
);

/***************************************************************************
Returns the data of a family attribute.

Environment: Internal  and  External

See Also:  UF_FAM_free_attribute_data

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_ask_attribute_data(
tag_t attribute ,/* <I>
                 Object identifier of the attribute.
                 */
UF_FAM_attribute_data_p_t attribute_data  /* <OF,free:UF_FAM_free_attribute_data>
                                          Data of the attribute.  A 
                                          UF_FAM_attribute_data_t structure 
                                          must must be allocated by the user. 
                                          This routine will then fill that
                                          structure with data that must be 
                                          freed by the caller by calling
                                          UF_FAM_free_attribute_data.
                                          */
);

/***************************************************************************
Frees data returned from UF_FAM_ask_attribute_data.

Environment: Internal  and  External

See Also:  UF_FAM_ask_attribute_data

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_free_attribute_data(
UF_FAM_attribute_data_p_t attribute_data  /* <I>
                                          Data of the attribute.
                                          */
);/*<NON_NXOPEN>*/

/***************************************************************************
Performs an update validity check on a family attribute object.
If the attribute object is valid, 0 is returned.  If any problems are found 
with the attribute object, an appropriate error code is returned.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_check_attribute_status(
tag_t attribute  /* <I>
                 Object identifier of the attribute.
                 */
);


/***************************************************************************
Creates a family.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_create_family(
UF_FAM_family_data_p_t family_data ,/* <I>
                                    Data for the family.
                                    */
tag_t * family  /* <O>
                Object identifier of family.
                */
);


/***************************************************************************
Edits the data of a family.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_edit_family(
tag_t family ,/* <I>
              Object identifier of the family.
              */
UF_FAM_family_data_p_t family_data  /* <I>
                                    New data for the family.
                                    */
);

/***************************************************************************
Returns the data of a family.

Environment: Internal  and  External

See Also:  UF_FAM_free_family_data

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_ask_family_data(
tag_t family ,/* <I>
              Object identifier of the family.
              */
UF_FAM_family_data_p_t family_data  /* <OF,free:UF_FAM_free_family_data>
                                    Data of the family.  The 
                                    UF_FAM_family_data_t structure must be
                                    allocated by the user, and a pointer 
                                    passed to this routine.  This routine
                                    returns data in the structure which
                                    must be freed by calling 
                                    UF_FAM_free_family_data.
                                    */
);


/***************************************************************************
Frees data returned from UF_FAM_ask_family_data.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_free_family_data(
UF_FAM_family_data_p_t family_data  /* <I>
                                    Data of the family.
                                    */
);/*<NON_NXOPEN>*/

/***************************************************************************
Performs an update validity check on a family object.
If the family object is valid, 0 is returned.  If any problems are found 
with the family object, an appropriate error code is returned.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_check_family_status(
tag_t family  /* <I>
              Object identifier of the family.
              */
);


/***************************************************************************
Adds a member to a family. When all the members have been added to the
family, call UF_MODL_update to perform an update. 

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_add_member(
tag_t family ,/* <I>
              Object identifier of the family.
              */
UF_FAM_member_data_p_t member_data ,/* <I>
                                    Data for the member.
                                    */
int * member_index  /* <O>
                    Index of the family member.
                    */
);


/***************************************************************************
Edits the data of a family member. When all the editing has been done,
call UF_MODL_update to perform an update.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_edit_member(
tag_t family ,/* <I>
              Object identifier of the family.
              */
int member_index ,/* <I>
                  Index of the family member.
                  */
UF_FAM_member_data_p_t member_data  /* <I>
                                    New data for the family member.
                                    */
);

/***************************************************************************
Returns family member row data.

Environment: Internal  and  External

See Also:  UF_FAM_free_member_data

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_ask_member_row_data(
tag_t family ,/* <I>
              Object identifier of the family.
              */
int member_index ,/* <I>
                  Index of the family member.
                  */
UF_FAM_member_data_p_t member_data  /* <OF,free:UF_FAM_free_member_data>
                                    Row data of the object.  The 
                                    UF_FAM_member_data_t structure must be
                                    allocated by the user, and a pointer 
                                    passed to this routine.  This routine
                                    returns data in the structure which
                                    must be freed by calling 
                                    UF_FAM_free_member_data.
                                    */
);


/***************************************************************************
Returns family member column data.

Environment: Internal  and  External

See Also:  UF_FAM_free_member_data

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_ask_member_column_data(
tag_t family ,/* <I>
              Object identifier of the family.
              */
int attribute_index ,/* <I>
                     Index of the family attribute.
                     */
UF_FAM_member_data_p_t member_data  /* <OF,free:UF_FAM_free_member_data>
                                    Column data of the object.  The 
                                    UF_FAM_member_data_t structure must be
                                    allocated by the user, and a pointer 
                                    passed to this routine.  This routine
                                    returns data in the structure which
                                    must be freed by calling 
                                    UF_FAM_free_member_data.
                                    */
);

/***************************************************************************
Frees data returned from UF_FAM_ask_member_row_data and
UF_FAM_ask_member_column_data.

Environment: Internal  and  External

See Also:  UF_FAM_ask_member_row_data 
           UF_FAM_ask_member_column_data

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_free_member_data(
UF_FAM_member_data_p_t member_data  /* <I>
                                    Data of the family member.
                                    */
);/*<NON_NXOPEN>*/

/***************************************************************************
Performs an update validity check on a family member.
If the family member is valid, 0 is returned.  If any problems are 
found with the family member, an appropriate error code is returned.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_check_member_status(
tag_t family ,/* <I>
              Object identifier of the family.
              */
int member_index  /* <I>
                  Index of the family member.
                  */
);

/***************************************************************************
Deletes a family member.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_delete_member(
tag_t family ,/* <I>
              Object identifier of the family.
              */
int member_index  /* <I>
                  Index of the family member.
                  */
);


/***************************************************************************
Creates an instance of a family member in the work part. This effectively
turns the work part into a part family member. This is unlike
UF_PART_create_family_instance, which creates a new part to use instead of
the work part.

May be called on the template part, which is the equivalent of applying the
family member attributes to the template part. On doing this, the instance
must be deleted afterwards using UF_FAM_delete_instance otherwise the
template part will stay as a part member of itself.

Environment: Internal  and  External

See Also: UF_PART_create_family_instance
          UF_FAM_delete_instance

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_create_instance(
tag_t family ,/* <I>
              Object identifier of the family.
              */
int member_index ,/* <I>
                  Index of the family member.
                  */
tag_t * instance  /* <O>
                  Object identifier of the family instance.
                  */
);

/***************************************************************************
Returns the data of a family instance.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_ask_instance_data(
tag_t  instance ,/* <I>
                 Object identifier of the family instance.
                 */
tag_t * family ,/* <O>
                Object identifier of the family.
                */
int * member_index  /* <O>
                    Index of the family member.
                    */
);

/***************************************************************************
Deletes a family instance.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_delete_instance(
tag_t  instance  /* <I>
                 Object identifier of the family instance.
                 */
);


/***************************************************************************
Evaluate intent data and return indices of matching family members.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_FAM_evaluate_intent_data
(
UF_FAM_intent_data_p_t intent_data ,/* <I>
                                    Data of the intent.
                                    */
int * match_count ,/* <O>
                   Number of matching family members
                   */
int ** match_indices  /* <OF,len:match_count>
                      Indices of matching family members
                      */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_FAM_H_INCLUDED */
