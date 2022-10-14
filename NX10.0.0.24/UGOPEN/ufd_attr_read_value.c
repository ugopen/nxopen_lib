/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_ATTR_read_value                                                 *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example program requires an open part which contains two   *
 *   objects with attribute names of OBJECT1 and OBJECT2 and attribute titles *
 *   of CYL1 and BLOCK1.                                                      *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_attr.h>
#include <uf_obj.h>
#include <uf_disp.h>
#include <uf_ui.h>

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


  tag_t obj1 = NULL_TAG;
  tag_t obj2 = NULL_TAG;

  char title1[ UF_ATTR_MAX_STRING_BUFSIZE ] = "CYL1";
  char title2[ UF_ATTR_MAX_STRING_BUFSIZE ] = "BLOCK1";
  char sval[ UF_ATTR_MAX_STRING_BUFSIZE ];
  char message[ MAX_LINE_BUFSIZE ];
  char buffer[ UF_UI_MAX_STRING_BUFSIZE ];
  char *object_name1 = "OBJECT1";
  char *object_name2 = "OBJECT2";

  UF_ATTR_value_t  value1,value2;

  UF_CALL(UF_UI_open_listing_window());
  

  UF_CALL(UF_OBJ_cycle_by_name(object_name1,&obj1));
  printf("obj1 = %d\n", obj1);
  UF_CALL(UF_OBJ_cycle_by_name(object_name2,&obj2));
  printf("obj2 = %d\n", obj2);

  UF_CALL(UF_ATTR_read_value(obj1, title1, UF_ATTR_any, &value1));
  strcpy(message, "Attribute Title : ");
  strcat(message, title1);

/* Display the attribute's value */
  switch ( value1.type ) {
    case UF_ATTR_integer :
      sprintf(buffer, "Integer Attribute : %d\n",value1.value.integer);
      UF_UI_write_listing_window(buffer);
      break;

    case UF_ATTR_real    :
      sprintf(buffer, "Floating Point Attribute : %f\n", 
                value1.value.real);
      UF_UI_write_listing_window(buffer);
      break;

    case UF_ATTR_time    :
      sprintf(buffer, "Date & Time Attribute : %d, %d\n", 
        value1.value.time[0], 
        value1.value.time[1]);
      UF_UI_write_listing_window(buffer);
      break;

    case UF_ATTR_null    :
      UF_UI_write_listing_window("Null Attribute :\n");
      break;

    case UF_ATTR_string  :
      strcpy(sval, value1.value.string);
      sprintf(buffer, "String Attribute : %s\n", sval);
      UF_UI_write_listing_window(buffer);
      UF_free(value1.value.string);
      break;
    case UF_ATTR_reference :
      strcpy(sval,value1.value.reference);
      sprintf(buffer, "Reference Attribute: %s\n", sval);
      UF_UI_write_listing_window(buffer);
      UF_free(value1.value.reference);
      break;
    default :
      UF_UI_write_listing_window("Attribute Does Not Exist!\n");
      break;
  }

/* Set the attribute value's string pointer to point
   to the 'sval' character array so that the string
   attribute's value is read into 'sval'
*/

  value2.value.string = sval;

  UF_CALL(UF_ATTR_read_value(obj2, title2, UF_ATTR_string, &value2));
    

/* Display the string attribute of second object if it exists. */
  if (value2.type != 0) {
    sprintf(buffer, "String Attribute = %s\n", sval);
    UF_UI_write_listing_window(buffer);
  }
  else
    UF_UI_write_listing_window("String Attribute Does Not Exist for second object!\n");
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
