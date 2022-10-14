/*==================================================================================================

                    Copyright (c) 1998 Unigraphics Solutions Inc. 
                             Unpublished - All rights reserved
====================================================================================================
File description:

     This function is a small sample program that demonstrates
     the invocation of UF_GEXP_edit_distance().  It is placed
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
    double block_orig1[3] = {5.0,5.0,5.0};
    char *block_len[3] = {"1","2","3"};
    char buf[ UF_UI_MAX_STRING_BUFSIZE ];
    char *string;
    tag_t part=NULL_TAG, feat_tag=NULL_TAG, exp_tag=NULL_TAG, solid=NULL_TAG, 
        solid_body[2]={NULL_TAG}, line_tag=NULL_TAG; 
    tag_t blk_obj,blk_obj1;
    int type, subtype;
    int i=0;
    
    UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,block_orig,
                                  block_len,&blk_obj));
    UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,block_orig1,
                                  block_len,&blk_obj1));
    UF_CALL(UF_UI_open_listing_window());
    if((part=UF_PART_ask_display_part()) == NULL_TAG)
    {
        UF_UI_write_listing_window("Failed to get part tag\n");
        return;
    }
    solid=NULL_TAG;
    while (i < 2)
    {
        type=UF_solid_type;    
        UF_OBJ_cycle_objs_in_part( part, type, &solid );
        UF_OBJ_ask_type_and_subtype(solid, &type, &subtype);
        if (subtype == UF_solid_body_subtype)
            solid_body[i++]=solid;
    }

    UF_CALL(UF_GEXP_create_distance(solid_body[0], 
                                    NULL_TAG, 
                                    solid_body[1],  
                                    NULL_TAG, 
                                    &feat_tag, 
                                    &exp_tag));

    UF_CALL(UF_MODL_ask_exp_tag_string(exp_tag,&string));

    sprintf (buf, "Created distance expression %s\n", string);
    UF_UI_write_listing_window(buf);

    line_coords.start_point[0] = 5.0;
    line_coords.start_point[1] = 7.0;
    line_coords.start_point[2] = 8.0;

    line_coords.end_point[0] = 10.0;
    line_coords.end_point[1] = 10.0;
    line_coords.end_point[2] = 2.0;

    UF_CALL(UF_CURVE_create_line (&line_coords, &line_tag));
    UF_CALL(UF_GEXP_edit_distance(feat_tag, 
                                  solid_body[0], 
                                  NULL_TAG, 
                                  line_tag, 
                                  NULL_TAG));

    UF_CALL(UF_MODL_update());

    sprintf (buf, "Edited distance expression %s\n", string);
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

