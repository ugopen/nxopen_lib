/*==============================================================================
          Copyright (c) 1998 Unigraphics Solutions Inc.
                   Unpublished - All rights reserved

================================================================================
 File Name: ufx_cycle_common.c

 File Description:
   This source file includes the code that is used by both the internal and
   external versions of the "Cycle the Data Model" program. It does all the
   work of getting the part file history, cycling the data Model, and printing
   a report on its results.

================================================================================


*******************************************************************************/


/* Standard header files */
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

/* UFUN header files */
#include <uf.h>
#include <uf_ui.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_defs.h>
#include <uf_attr.h>
#include <uf_cfi.h>

/* Program header file */
#include <ufx_cycle.h>


/* Function prototypes */
static void clean_up_mem(UF_PART_load_status_p_t load_stat);
static void get_history(tag_t part_tag);
static void get_part_attrib(void);
static void get_customer_area(tag_t part_tag);
static void cycle_part(tag_t part_tag);

/* -----------------------------------------------------------------------------
 Function Name: UFX_CYCLE_data

 Function Description:
   Calls the functions that get and print the part file's history, attributes,
   status, customer area, customer description, and the data from cycling
   the part.

 Inputs:
   part_tag - Tag of part file that was opened.

 Outputs:
   None.

 Returns: None.
   -----------------------------------------------------------------------------
*/ 
extern void UFX_CYCLE_data(tag_t part_tag)
{
  int units;
  
  UF_PART_ask_units(part_tag, &units);
  switch (units)
  {
    case UF_PART_METRIC:
      UF_UI_write_listing_window("\nThis part is in Metric units.");
      break;
    case UF_PART_ENGLISH:
      UF_UI_write_listing_window("\nThis part is in English units.");
      break;
    default:
      UF_UI_write_listing_window("\nCould not determine part units.");
      break;
   }
   get_history(part_tag);
   get_part_attrib();
   get_customer_area(part_tag);
   cycle_part(part_tag);
  
}

/* -----------------------------------------------------------------------------
 Function Name: UFX_CYCLE_open_part

 Function Description:
   Opens the part and cleans up memory if required.

 Inputs:
   part - Name of part file to open.

 Outputs:
   part_tag - Tag of part file that was opened.

 Returns: None.
   -----------------------------------------------------------------------------
*/ 
    
extern int UFX_CYCLE_open_part(char *part_name, tag_t *part_tag)
{
  UF_PART_load_status_t load_stat;
  char buffer[132];
  int err_part;
  
  *part_tag = NULL_TAG;

  err_part = UF_PART_open(part_name, part_tag, &load_stat);

  if(*part_tag == NULL_TAG)
  {
    report_err(err_part,"File does not exist. Please enter another name.\n");
  }

  if(err_part && (*part_tag != NULL_TAG))
  {
     if(load_stat.failed)
     {
       sprintf(buffer, "There were %d parts with load errors.",load_stat.n_parts);
       UF_UI_write_listing_window(buffer);
     }
     clean_up_mem(&load_stat);
  }

  return(err_part);
} 

/* -----------------------------------------------------------------------------
 Function Name: clean_up_mem

 Function Description: Deallocates memory if required.

 Inputs:
   load_stat - Pointer to load status data structure.

 Outputs: None.

 Returns: None.
   -----------------------------------------------------------------------------
*/

static void clean_up_mem(UF_PART_load_status_p_t load_stat)
{
  if(load_stat->n_parts)
  {
     UF_free(load_stat->statuses);
     UF_free_string_array(load_stat->n_parts, load_stat->file_names);
  }
} 


/* -----------------------------------------------------------------------------
 Function Name: get_history

 Function Description:
   Gets and prints the part file history to the open listing device.

 Inputs: part_tag
   part_tag - Tag of part from which to get history.

 Outputs: None. 

 Returns: None.
   -----------------------------------------------------------------------------
*/

static void get_history(tag_t part_tag)
{

  char *title0 =
  "\nPart History for part: %s\n";

  char *title1 =
  "Version  Time/Date        Machine  User                  Program";

  char *title2 =
  "-------  ---------------  -------  ----                  -------";

  char *format = "%7d  %-15.15s  %-7.7s  %-20.20s  %s\n";

  char *time_format = "%d %b %y %H:%M";
  char buffer[2* MAX_FSPEC_BUFSIZE ];

  UF_PART_history_list_p_t history_list = NULL;
  char    part_fspec[ MAX_FSPEC_BUFSIZE ];
  char    time_buff[21];
  struct  tm  *time_ptr;
  time_t  displayed_time;
  char    *program, *user, *machine;
  int     vers_num, vers_time;
  int     num_hists, curr_hist;


  UF_PART_create_history_list(&history_list);

  UF_PART_ask_part_name( part_tag, part_fspec );

  sprintf (buffer,"%s%s", title0, part_fspec );
  UF_UI_write_listing_window ( buffer );

  sprintf(buffer,"\n%s\n%s\n", title1, title2);
  UF_UI_write_listing_window(buffer);


  UF_PART_clear_history_list( history_list );

  UF_PART_ask_part_history( part_tag, history_list );

  UF_PART_ask_num_histories( history_list, &num_hists );



  for ( curr_hist=0 ; curr_hist < num_hists ; curr_hist++ )
  {
     UF_PART_ask_nth_history( history_list, curr_hist,
                              &program, &user, &machine,
                              &vers_num, &vers_time );

     displayed_time = (time_t) vers_time;

     time_ptr = localtime (&displayed_time);

     strftime( time_buff, sizeof(time_buff), time_format, time_ptr);

     sprintf(buffer,format,vers_num,time_buff,machine,user,program);
     UF_UI_write_listing_window(buffer);
  }

  
  UF_PART_delete_history_list(history_list);
}


/* -----------------------------------------------------------------------------
 Function Name: get_part_attrib

 Function Description:
   Gets and prints part file attributes to the open listing device if there are
   any.

 Inputs: None.

 Outputs: None.

 Returns: None.
   -----------------------------------------------------------------------------
*/

static void get_part_attrib(void)
{
  char title[51], data[185], attribute[133];
  int err;

  UF_ATTR_value_t attrib;
  tag_t object;

  err = UF_ATTR_ask_part_attribute(&object);
  if (err) report_err(err, "\nUF_ATTR_ask_part_attribute failure.");
  else
  {
    int status = 0;
    do
      {
         attrib.type = UF_ATTR_string;
         attrib.value.string = attribute;
         err = UF_ATTR_cycle(object, &status, UF_ATTR_string, title, &attrib);
         if (err)
         {
           report_err(err, "UF_ATTR_cycle failure:\n");
         }

         if(status)
         {
           sprintf(data,"\nTitle: %s Value: %s",title, attribute);
           UF_UI_write_listing_window(data);
         }
      }while(status != 0);
  }
}

/* -----------------------------------------------------------------------------
 Function Name: get_customer_area

 Function Description:
   Gets and prints the part file status, customer area, and description area
   to the open listing device.

 Inputs: part_tag
   part_tag - Tag of part from which to get history.

 Outputs: None. 

 Returns: None.
   -----------------------------------------------------------------------------
*/

static void get_customer_area(tag_t part_tag)
{
  char *customer    = NULL;
  char *description = NULL;
  char buffer[ UF_UI_MAX_STRING_BUFSIZE ];

  int part_status, err = 0;

  err = UF_PART_ask_status(part_tag, &part_status);
  if(err)
  {
    report_err(err, "UF_PART_ask_status failure:\n");
  }
  else
  {
   sprintf(buffer, "\n\nThe customer status is: %d\n", part_status);
   UF_UI_write_listing_window(buffer);
  }

  err = UF_PART_ask_description(part_tag, &description);
  if(err)
  {
    report_err(err, "UF_PART_ask_description failure:\n");
  }
  else if( description != NULL )
  {
    if(description[0] != '\0')
    {
      sprintf(buffer, "The customer description is: %s\n", description);
      UF_UI_write_listing_window(buffer);
    }
    UF_free(description);
  }

  err = UF_PART_ask_customer_area(part_tag,&customer);
  if(err)
  {
    report_err(err, "UF_PART_ask_customer_area failure:\n");
  }
  else if ( customer != NULL )
  {
    if(customer[0] != '\0')
    {
      sprintf(buffer, "The customer area is: %s\n", customer);
      UF_UI_write_listing_window(buffer);
    }
    UF_free(customer);
  }

}


/* -----------------------------------------------------------------------------
 Function Name: cycle_part

 Function Description:
   Cycles the part and produces a report to the open listing device that
   includes the total count of objects, a count of objects for each object type,
   the total count of condemned objects, the total count of displayable objects,
   and the count of displayable objects on layers accessible to users.

 Inputs:
   part_tag - Tag of part to cycle.

 Outputs: None.

 Returns: None.
   -----------------------------------------------------------------------------
*/

static void cycle_part(tag_t part_tag)
{
  
  UF_OBJ_disp_props_t   disp_props;
  char local_buf[ UF_UI_MAX_STRING_BUFSIZE ];
  char *title1 = "Object Type       Count of Objects";
  char *title2 = "-----------       ----------------";
  char *format = "%-3d               %-d\n";

  char *title3 = "Layer Number      Count of Objects";
  char *title4 = "------------      ----------------";


  int object_count[UF_max_entity_type+1];
  int layer[257];
  int display_count = 0, condemn_count = 0;
  int type, subtype, err, max_count = 0, i;
  logical disp;
  tag_t obj_tag = NULL_TAG;

  UF_UI_write_listing_window("\n\nHere is the object count by type:\n");

  for(type = 0; type < UF_max_entity_type+1; type++)
  {
    object_count[type] = 0;
  }

  for( i = 0; i < 257; i++)
  {
    layer[i] = 0;
  }

  while ((obj_tag = UF_OBJ_cycle_all(part_tag, obj_tag)) != NULL_TAG)
  {
     err = UF_OBJ_ask_type_and_subtype(obj_tag, &type, &subtype);
     if (err) report_err(err, "Couldn't get object type.");
     else
     {
      
       object_count[type]++;
     }

     if(UF_OBJ_ask_status(obj_tag) == UF_OBJ_CONDEMNED) condemn_count++;
     disp = UF_OBJ_is_type_displayable(type);
     if(disp)
     {
       display_count++;
       err = UF_OBJ_ask_display_properties(obj_tag, &disp_props);
       if (err) report_err(err, "Couldn't get display properties.");
       else if (disp_props.layer > 0 && disp_props.layer < 257)
       {
         layer[disp_props.layer]++;
       }
     }
          
  }

  sprintf(local_buf, "\n%s\n%s\n", title1, title2);
  UF_UI_write_listing_window(local_buf);
  for( i = 1; i <= UF_max_entity_type; i++)
  {
     if(object_count[i] != 0)
     {
        max_count += object_count[i];
        sprintf(local_buf,format,i,object_count[i]);
        UF_UI_write_listing_window(local_buf);
     }
  }
  sprintf(local_buf, "\n\nThe total count of objects is: %d", max_count);
  UF_UI_write_listing_window(local_buf);

  sprintf(local_buf, "\nThere are %d displayable objects.", display_count);
  UF_UI_write_listing_window(local_buf);

  sprintf(local_buf, "\nThere are %d condemned objects.", condemn_count);
  UF_UI_write_listing_window(local_buf);

  UF_UI_write_listing_window("\n\nThe following is the object count by");
  UF_UI_write_listing_window("\nLayer. Note that this count does not");
  UF_UI_write_listing_window("\ninclude internal system layers.\n");

  sprintf(local_buf, "\n\n%s\n%s\n", title3, title4);
  UF_UI_write_listing_window(local_buf);

  for( i = 1; i < 257; i++)
  {
     if(layer[i] != 0)
     {
        sprintf(local_buf,format,i,layer[i]);
        UF_UI_write_listing_window(local_buf);
     }
  }

}
