/*==================================================================================================

                    Copyright (c) 1998 Unigraphics Solutions Inc. 
                             Unpublished - All rights reserved
====================================================================================================
File description:

     This function is a small sample program that demonstrates
     the invocation of UF_GEXP_edit_length().  It is placed
     directly in our UFUN documentation starting with the
     include statements.

 
==================================================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_ui.h>
#include <uf_defs.h>
#include <uf_obj.h>
#include <uf_gexp.h>
#include <uf_object_types.h>
#include <uf_curve.h>
#include <uf_part.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report( char *file, int line, char *call, int irc)
{
  if (irc)
  {
     char    messg[133];
     printf("%s, line %d:  %s\n", file, line, call);
     (UF_get_fail_message(irc, messg)) ?
       printf("    returned a %d\n", irc) :
       printf("    returned error %d:  %s\n", irc, messg);
  }
  return(irc);
}

static void do_ugopen_api(void)
{
    UF_CURVE_line_t line_coords;
    double block_orig[3] = {0.0,0.0,0.0};
    char *block_len[3] = {"1","2","3"};
    char buf[UF_UI_MAX_STRING_LEN+1];
    tag_t part, feat_tag, exp_tag, solid; 
    tag_t blk_obj, solid_edge, line_tag;
    char *string;
    int type, subtype;
    int i=0;
    

    UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,block_orig,
                                  block_len,&blk_obj));
    UF_CALL(UF_UI_open_listing_window());
    if((part=UF_PART_ask_display_part()) == NULL_TAG)
    {
        UF_UI_write_listing_window("Failed to get part tag\n");
        return;
    }
    solid=NULL_TAG;
    solid_edge=NULL_TAG;
    while (i < 1)
    {
        type=UF_solid_type;    
        UF_OBJ_cycle_objs_in_part( part, type, &solid );
        UF_OBJ_ask_type_and_subtype(solid, &type, &subtype);
        if (!solid_edge && subtype == UF_solid_edge_subtype)
        {
            solid_edge=solid;
            i++;
        }
    }

    UF_CALL(UF_GEXP_create_length(solid_edge, NULL_TAG, 
                                  &feat_tag, &exp_tag));

    UF_CALL(UF_MODL_ask_exp_tag_string(exp_tag,&string));

    sprintf (buf, "Created length expression %s\n", string);
    UF_UI_write_listing_window(buf);

    line_coords.start_point[0] = 5.0;
    line_coords.start_point[1] = 7.0;
    line_coords.start_point[2] = 8.0;

    line_coords.end_point[0] = 10.0;
    line_coords.end_point[1] = 10.0;
    line_coords.end_point[2] = 2.0;

    UF_CALL(UF_CURVE_create_line(&line_coords, &line_tag));
    UF_CALL(UF_GEXP_edit_length(feat_tag, line_tag, NULL_TAG));

    UF_CALL(UF_MODL_update());

    sprintf (buf, "Edited length expression %s\n", string);
    UF_UI_write_listing_window(buf);

    UF_free(string);
}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
  if (!UF_CALL(UF_initialize()))
  {
    do_ugopen_api();
    UF_CALL(UF_terminate());
  }
}


int ufusr_ask_unload(void)
{
  return (UF_UNLOAD_IMMEDIATELY);
}
