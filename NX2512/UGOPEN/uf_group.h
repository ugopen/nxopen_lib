/*******************************************************************************

             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       



   
File Description:

The routines in this file enables you to:
  . Add a member to a group.
  . Get data of a group.
  . Get the tag of the group to which the specified input tag belongs.
  . Create a group from a set of group members.
  . Delete a member from a group.
  . Remove all members of a group, delete the group, and ungroup the immediate 
    group and all subgroups.
  . Remove all members of a group, delete the group, ungroup only the immediate
    group, and allow subgroups to remain.
 ***************************************************************************/

#ifndef UF_GROUP_INCLUDED 
#define UF_GROUP_INCLUDED 


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************
Create a group from a set of group members.

Note: A call to UF_MODL_update may be necessary after creating 
a group for that group to show up correctly in the Part Navigator.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_create_group(
tag_t * group_members ,/* <I,len:count_of_members> count_of_members
                              An array which contains the tags of the group
                              members
                       */
const int count_of_members ,/* <I>
                      number of group members in the group
                      */
tag_t * group_tag  /* <O>
                   the tag of created group
                   */
);

/*****************************************************************************
Queries the members of a group. After you are done using group_members,
deallocate the memory using UF_free.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_ask_group_data(
const tag_t group_tag ,/* <I>
                       The tag of the input group
                       */
tag_t ** group_members ,/* <OF,len:count_of_members>
                        An array which contains the tags of the group
                        members. If the number of the group members is 0,
                        this will be a NULL_TAG. Use
                        UF_free(group_members) to free memory.
                        */
int * count_of_members  /* <O>
                        number of members in the group
                        */
);

/*****************************************************************************
Adds a member to a group.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_add_member_to_group(
tag_t member_tag ,/* <I>
                  Member object identifier to be added to the group.
                  */
tag_t group_tag  /* <I>
                 Group object identifier
                 */
);

/*****************************************************************************
Delete a member from a group.
If Part Navigator is open, deletion wont be reflected immediately.
Please Exit and re-open Part Navigator to see latest change.

Environment: Internal  and  External
See Also: UF_GROUP_del_member_with_refresh
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_del_member_from_group(
tag_t member_tag ,/* <I>
                  Member object identifier to be deleted.
                  */
tag_t group_tag  /* <I>
                 group object identifier
                 This may be NULL_TAG, which means that the member_tag should
                 be deleted from whatever group it is a member of, if any.
                 If group_tag is NULL_TAG and member_tag does not belong to
                 any group, no error is returned.  But if group_tag is
                 not null, an error is returned if member_tag was not a
                 member of group_tag before the call.
                 */
);

/*****************************************************************************
Delete a member from a group and refresh the Part Navigator immediately.
This call may be slow due to refresh of Part Navigator. 

Environment: Internal  and  External

See Also:  UF_GROUP_del_member_from_group

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_del_member_with_refresh(
tag_t member_tag ,/* <I>
                  Member object identifier to be deleted.
                  */
tag_t group_tag  /* <I>
                 group object identifier
                 This may be NULL_TAG, which means that the member_tag should
                 be deleted from whatever group it is a member of, if any.
                 If group_tag is NULL_TAG and member_tag does not belong to
                 any group, no error is returned.  But if group_tag is
                 not null, an error is returned if member_tag was not a
                 member of group_tag before the call.
                 */
);

/*****************************************************************************
Remove all members of a group, deletes the group, ungroups only
the immediate group, and allows subgroups to remain.
If the group specified is a subgroup, all of its members become
members of the ancestor group.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_ungroup_top(
tag_t group_tag  /* <I>
                 Group object identifier of the group to be ungrouped.
                 */
);

/*****************************************************************************
Remove all members of a group, deletes the group, and ungroups the
immediate group and all subgroups.  If the group specified is a 
subgroup, all of its members become members of the ancestor group.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_ungroup_all(
tag_t group_tag  /* <I>
                 Group object identifier
                 */
);

/*****************************************************************************
Queries the tag of the group to which the specified input tag belongs.
If the input tag belongs to more than one group, the first group tag found 
will be returned.  Use UF_GROUP_ask_all_owning_groups to see all groups an 
entity belongs to.

Environment: Internal  and  External

See Also:  UF_GROUP_ask_all_owning_groups

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_ask_group_of_tag(
tag_t tag_of_interest ,/* <I>
                       The object identifier of the object to check.
                       */
tag_t * group_tag  /* <O>
                   The tag of the group to which the tag_of_interest
                   belongs. Returns a NULL_TAG if the
                   tag_of_interest does not belong to any group.
                   */
);

/*****************************************************************************
Sets the group whose tag is passed as input, as non-UMG (Non -Unique Member Group) i.e. its members can be 
members of any other groups (UMG or non-UMG).

Environment: Internal  and  External
See Also:
History: Released in NX3
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_set_non_unique_membership (
tag_t group_tag /* <I>
                 the tag of the group to be set as non_UMG.
                */
);

/*****************************************************************************
Sets the group whose tag is passed as input, as UMG (Unique Member Group)i.e. its members can be 
members of only other non-UMG groups only.

Environment: Internal  and  External
See Also:
History: Released in NX3
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_set_unique_membership (
tag_t group_tag /* <I>
                 the tag of the group to be set as UMG(Unique Member Group).
                */
);

/*****************************************************************************
Queries whether the group whose tag is passed as input, is UMG(Unique Member Group). 
outputs TRUE  - if the group is UMG and 
outputs FALSE - if the group is non-UMG

Environment: Internal  and  External
See Also:
History: Released in NX3
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_is_unique_membership_group (
tag_t group_tag, /* <I>
                 the tag of the group to be checked if it is UMG(Unique Member Group)
                 */
logical *is_UMG  /* <O>
                 TRUE  - if the group is UMG
                 FALSE - if the group is non-UMG
                 */
);

/*****************************************************************************
Queries the owning groups of the given tag and their count. 
The function outputs the count of owning groups and the array that contains the 
tags of owning groups

Environment: Internal  and  External
See Also:
History: Released in NX3
 ****************************************************************************/
extern UFUNEXPORT int UF_GROUP_ask_all_owning_groups (
tag_t member_tag,/* <I>
                  the tag of the member whose owning groups are queried
                 */
int *num_owning_groups, /* <O>
                        The count of owning groups
                        */
tag_p_t *owning_groups_p/* <OF,len:num_owning_groups>
                        The array that contains the tags of owning groups
                        */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif    /*  END UF_GROUP_INCLUDED  */

