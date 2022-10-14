/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_FLTR_create_box_zone                                            *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The code in the following example creates a box zone and a plane zone.   *
 *   The code also edits the zones created, and inquires about their          *
 *   parameters.
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h> 
#include <uf.h> 
#include <uf_part.h> 
#include <uf_fltr.h>
#include <uf_obj_types.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static void zone_function(void);

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
  zone_function();

}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
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
static void zone_function(void) 
{ 
  tag_t box_zone_tag; 
  tag_t plane_zone_tag; 
  tag_t part_tag; 
  tag_t displayed_part_tag; 
   
  int uf_stat=UF_FLTR_OK; 
  double centroid[3]; 
  double corner[3]; 
  double orientation[9]; 
  double origin[3];
  /*<Devansh Desai> : DES11050 :Refer to UF_OBJ_NAME_LEN instead of hard coded value */
  //+1 for null byte.
  char name[ UF_OBJ_NAME_BUFSIZE ]="";
  char newname[] = "newzonename";

  /* open part file and create some zones */
  printf("Creating part... \n");

  UF_CALL(UF_PART_new("zone_example.prt", 
                        2,  /* english units = 2 */ 
                        &part_tag)); 

  centroid[0] = 1.0; 
  centroid[1] = 2.0; 
  centroid[2] = 3.0;

  corner[0]   = 1.0; 
  corner[1]   = 1.0; 
  corner[2]   = 1.0;

  orientation[0]   = 1.0; 
  orientation[1]   = 0.0; 
  orientation[2]   = 0.0; 
  orientation[3]   = 0.0; 
  orientation[4]   = 1.0; 
  orientation[5]   = 0.0; 
  orientation[6]   = 0.0; 
  orientation[7]   = 0.0; 
  orientation[8]   = 1.0;

  displayed_part_tag = UF_PART_ask_display_part();

  /*********** Create Box Zone    **************/

  UF_CALL(UF_FLTR_create_box_zone(displayed_part_tag, 
                                  "ZONE_BOX1", centroid,
                                  corner, orientation,
                                  &box_zone_tag));

  printf ("Created box zone 'ZONE_BOX1' \n:" 
           "Tag is %u status is %d\n ", 
           box_zone_tag, uf_stat );

  /*********** Create Plane Zone    **************/

  UF_CALL(UF_FLTR_create_plane_zone(displayed_part_tag,
                                    "ZONE_PLANE1", origin, 
                                    orientation,
                                    &plane_zone_tag));

  printf ("Created plane zone 'ZONE_PLANE1': \n"
           "Tag is %u status is %d\n ", 
           plane_zone_tag, uf_stat );

  /*********** Modify Box Zone    **************/ 
  centroid[0] = -5.0; 
  centroid[1] = -10.0; 
  centroid[2] = -20.0;

  corner[0] = 2.0; 
  corner[1] = 4.0; 
  corner[2] = 7.0;

  orientation[0] = 0.5; 
  orientation[1] = 0.5; 
  orientation[2] = 0.5; 
  orientation[3] = 0.5; 
  orientation[4] = 0.5; 
  orientation[5] = 0.5; 
  orientation[6] = 0.5; 
  orientation[7] = 0.5; 
  orientation[8] = 0.5;

  UF_CALL(UF_FLTR_edit_box_zone( box_zone_tag, newname,
                                    centroid, corner, 
                                    orientation));
  /*********** Modify Plane Zone    **************/

  origin[0] = 10.0; 
  origin[1] = -20.0; 
  origin[2] = 30.0;

  UF_CALL(UF_FLTR_edit_plane_zone(plane_zone_tag, newname, 
                                  origin, orientation));

  /*********** Ask about zones *****************/ 
  UF_CALL(UF_FLTR_ask_plane_zone( plane_zone_tag, 
                                  name, origin, 
                                  orientation));

  UF_CALL(UF_FLTR_ask_box_zone( box_zone_tag, name, 
                                centroid, corner, 
                                orientation));

  printf("\n New name: %s\n", name);
 
}
