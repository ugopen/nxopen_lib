/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_OBJ_is_type_transferable                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example requires a open work part. The code exports the first 1024  *
 *   transferable objects encountered from the work part to another part.     *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_part.h>
#include <uf_obj.h>
#include <uf_assem.h>

#define MAX_NUM_OBJECTS 1024

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
  tag_t object;
  tag_t work_part = UF_ASSEM_ask_work_part();
  tag_t object_array[MAX_NUM_OBJECTS];
  int num_objects = 0;

  
  for (object = UF_OBJ_cycle_all(work_part, NULL_TAG);
       object != NULL_TAG && num_objects < MAX_NUM_OBJECTS;
       object = UF_OBJ_cycle_all(work_part, object))
  {
    /* Part occurrences cannot be exported because the export
       operation is fundamentally a geometry operation, not an
       assembly operation.

       Non-alive objects cannot be exported because they only exist
       for internal use of the system, usually because an alive object
       depends on it. Non-alive objects are normally only modified by
       the system as a side effect of the user modifying an alive
       object.
    */
    if (UF_OBJ_ask_status(object) == UF_OBJ_ALIVE)  
    {
      logical is_transferable;
      int type;
      int subtype;
 

      if (UF_CALL(UF_OBJ_ask_type_and_subtype(object, &type,
                                           &subtype)))
      {
        return;
      }

      
      /* Transferable types are those object types found in
         uf_object_types.h that are candidates for file export.
         Transferable types include geometry, drafting objects,
         groups, etc. Note that if a transferable type depends on
         an object that is not transferable, then the original
         object cannot be transferred (exported).
      */
         
      if (UF_CALL(UF_OBJ_is_type_transferable(type, &is_transferable)))
      {
        return;
      }

      if (is_transferable)
      {
        object_array[num_objects] = object;
        num_objects++;
      }
    }
 }

 if (num_objects > 0)
 {
    UF_PART_export_options_t export_options;

    export_options.new_part = true;
    export_options.params_mode = UF_PART_maintain_params;
    export_options.expression_mode = UF_PART_copy_exp_deeply;

    UF_CALL(UF_PART_export_with_options("exported_objects", 
                                         num_objects,
                                         object_array, 
                                         &export_options));
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
