/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_OBJ_cre_mod_versions                                            *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example cycles over the solid objects in the current work  *
 *   part and prints information about their type, subtype, creation version, *
 *   and last modification version numbers.                                   *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_assem.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_part.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_cfi.h>

static  char    title0[] =
  "\nSolid Object Report For Part: %s\n";

static  char    title1[] =
  "Object ID  Type  Subtype  Creation Version  Modified Version";

static  char    title2[] =
  "---------  ----  -------  ----------------  ----------------";

static  char    format[] = 
  "%9d  %4d  %7d      %8d          %8d\n";

static  int print_line( char *buf )
{
    printf("%s", buf );
    return 0;
}

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
  char    line_buff[ MAX_LINE_BUFSIZE ];
  char    part_fspec[ MAX_FSPEC_BUFSIZE ];
  char    *part_buff = NULL;
  int     cre_vers, mod_vers;
  int     type, rtype, subtype;
  tag_t   object;
  tag_t   part;
    
  /* Get the tag of the work part */ 
  part = UF_ASSEM_ask_work_part();
  type = UF_solid_type;
  if  ( part != NULL_TAG )
  {
    char part_buff[2* MAX_FSPEC_BUFSIZE ];
    /* Get the part name of the work part. */
    UF_PART_ask_part_name( part, part_fspec );
    
    sprintf ( part_buff, "%s%s", title0, part_fspec );
    print_line ( part_buff );

    sprintf( line_buff, "\n" );
    print_line( line_buff );
    sprintf( line_buff, "\n%s\n%s\n", title1, title2 );
    print_line( line_buff );
    object = NULL_TAG;

    /* Begin cycling for solid type by passing in a NULL_TAG. */
    UF_OBJ_cycle_objs_in_part(part, type, &object);
    while ( object != NULL_TAG )
    {
      /* Get the type and subtype. */
      UF_OBJ_ask_type_and_subtype( object, &rtype, &subtype );

      /* Get the creation and modification versions. */
      UF_OBJ_ask_cre_mod_versions( object,&cre_vers,&mod_vers);

      /* Print a report. */
      sprintf( line_buff, format, object, rtype, subtype,
                   cre_vers, mod_vers );
      print_line( line_buff );

      /* Continue cycling until object is a NULL_TAG. */
      UF_OBJ_cycle_objs_in_part(part, type, &object);
    }
  }
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
