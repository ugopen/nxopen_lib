/*==================================================================================================

              Copyright (c) 1998 - 2004 Unigraphics Solutions Inc.
                        Unpublished - All rights reserved
====================================================================================================
File description:

    This is an external user function demonstration file for customers.
    Currently it is run from the command line. It takes as arguments a part
    name (following a -p), and an optional list of types (following a -t)
    separated by spaces. The program will open the specified part, and
    cycle through the list of given types to count the number of objects
    of that type, and to display all data associated with the type if
    the type is a point, line, arc or matrix.
    If the -t switch is not specified, or if the types POINT, LINE, ARC,
    or MATRIX are not in the list of user specified types, these types
    are added to the list of types to search during the cycling phase.
    Therefore, if no -t switch is specified, only the above 4 types will
    be searched for.

    If any of the types found within the search are a displayable type,
    then its display attributes are also shown.

    usage : ext_uf_example -p <part_name> [-t <type> [<type> <type> ...] ]


==================================================================================================*/

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <uf.h>
#include <uf_attr.h>
#include <uf_curve.h>
#include <uf_cfi.h>
#include <uf_csys.h>
#include <uf_disp.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>

#define MAX_TYPES       20       /* max # user specified types */

/* prototypes of local routines */
static void error_return(char *msg);
static void arg_error(char *msg, char *prog_name);
static void report_error(int result,char *alt_msg);
static void get_args(int argc, char **argv, char *part_name,
                     int *type_list, int *num_types);
static void add_extratypes(int *type_list,int *num_types);
static void show_point_info(tag_t point, int atts);
static void show_line_info(tag_t line, int atts);
static void show_arc_info(tag_t arc, int atts);
static void show_matrix_info(tag_t matrix,int att);
static void show_display_atts(tag_t object_tag);
static void get_next_matrix_type(tag_t part_tag, tag_t *next_tag);
static void show_attribute_info(tag_t part_tag, int num_types,
                             int type_list[MAX_TYPES]);
static void show_units(tag_t part_tag);

/* called when we encounter an error. an error message is */
/* displayed, and the program is terminated.              */
static void error_return(char *msg)
{
    fprintf(stderr,"\n+++ERROR : %s.\n\n",msg);
    exit(1);
}

/* this routine does the same as the above error_return routine,  */
/* except it displays the usage of the program. only called for   */
/* errors occuring during argument list parsing                   */
static void arg_error(char *msg, char *prog_name)
{
    fprintf(stderr,"\n+++ERROR : %s.",msg);
    fprintf(stderr,"\n\n    usage : %s -p <part_name> ",prog_name);
    fprintf(stderr,"[-t <type> [<type> <type> ...] ]\n\n");
    exit(1);
}

/* this routine receives a UG error code, and uses UF_get_fail_message */
/* to translate the code into a string. this string is passed to the   */
/* ret routine above. if the UG error code could NOT be translated,    */
/* the alternative message which was passed in will be passed to ret.  */
static void report_error(int result,char *alt_msg)
{
    char err_message[200];
    int found = UF_get_fail_message(result,err_message);
    if (found != 0)
        error_return(alt_msg);
    else
        error_return(err_message);
}

/* this routine parses the arguments from the command line */
static void get_args(int argc, char **argv, char *part_name,
                     int *type_list, int *num_types)
{
    int argc_pnt = 1;
    logical part_flag = FALSE, type_flag = FALSE;
    logical limit_exceeded = FALSE;

    while(argc_pnt<argc)
    {
        if(!strcmp(argv[argc_pnt],"-p"))   /* if -p switch */
        {
            if(part_flag)                  /* if already had a -p */
                arg_error("too many -p switches",argv[0]);
            part_flag=TRUE;
            argc_pnt++;
            if(argc_pnt==argc)             /* if no more arguments left */
                arg_error("no part name specified after -p",argv[0]);
            strcpy(part_name,argv[argc_pnt++]);
            if(part_name[0]=='-')          /* if part name is another switch */
                arg_error("no part name specified",argv[0]);
        }
        else if(!strcmp(argv[argc_pnt],"-t"))   /* if -t switch */
        {
            if(type_flag)                       /* if already had a -t */
                arg_error("too many -t switches",argv[0]);
            type_flag=TRUE;
            argc_pnt++;
            while( (argv[argc_pnt][0]!='-') && (argc_pnt<argc) )
                if(*num_types<MAX_TYPES)        /* if not exceeded max types */
                    type_list[(*num_types)++]=atoi(argv[argc_pnt++]); /* add */
                else
                    limit_exceeded = TRUE;
            if(num_types==0)
                arg_error("no types specified after -t switch",argv[0]);
        }
        else
            arg_error("bad arguments",argv[0]);  /* unknown switch */
    }

    if(limit_exceeded)     /* if specified more types than allowed */
    {
        fprintf(stderr,"+++WARNING : number of types specified exceeded ");
        fprintf(stderr,"max number allowed (%d). excess types are ignored",MAX_TYPES);
    }
}

/* the types POINT, LINE, ARC, and MATRIX are added to the list */
/* of user specified types if they are not already specified    */
static void add_extratypes(int *type_list,int *num_types)
{
    int extra_types[] = {UF_point_type,UF_line_type,
                         UF_circle_type,UF_matrix_type};
    int i,j;
    int found;
    int num_extra_types = sizeof(extra_types)/sizeof(int);

    for(i=0;i<num_extra_types;i++)  /* look for each type separately */
    {
        found=0;
        for(j=0;j<*num_types;j++)   /* go through user specified list */
            if(type_list[j]==extra_types[i])
                found=1;
        if(!found)         /* add to end of list if we didn't find it */
            type_list[(*num_types)++]=extra_types[i];
    }
}


/* given a tag for a point, display the data associated with it */
static void show_point_info(tag_t point, int atts)
{
    double point_info[3];
    int result;

    result =  UF_CURVE_ask_point_data (point,point_info);
    if (result) report_error(result,"failed in UF_CURVE_ask_point_data");

    printf("\n      POINT with %d user defined attributes",atts);
    printf("\n      Its coordinates are : [%0.3f , %0.3f , %0.3f]\n",
           point_info[0],point_info[1],point_info[2]);
}

/* given a tag for a line, display the data associated with it */
static void show_line_info(tag_t line, int atts)
{
    UF_CURVE_line_t line_info;
    int result;

    result = UF_CURVE_ask_line_data (line,&line_info);
    if (result) report_error(result,"failed in UF_CURVE_ask_line_data");

    printf("\n      LINE with %d user defined attributes",atts);
    printf("\n      It goes from : [%0.3f , %0.3f , %0.3f]",
           line_info.start_point[0],line_info.start_point[1],line_info.start_point[2]);
    printf("\n              to   : [%0.3f , %0.3f , %0.3f]\n",
           line_info.end_point[0],line_info.end_point[1],line_info.end_point[2]);
}

/* given a tag for an arc, display the data associated with it */
static void show_arc_info(tag_t arc, int atts)
{
    UF_CURVE_arc_t arc_info;
    int result;
    double matrix_info [ 9 ];

    result = UF_CURVE_ask_arc_data (arc,&arc_info);
    if (result) report_error(result,"failed in UF_CURVE_ask_arc_data");

    printf("\n      ARC with %d user defined attributes",atts);
    printf("\n          Its center is at : [%0.3f , %0.3f , %0.3f]",
           arc_info.arc_center[0],arc_info.arc_center[1],arc_info.arc_center[2]);
    printf("\n              radius is : %0.3f with start angle of %0.3f radians",
           arc_info.radius,arc_info.start_angle);
    printf("\n              and end angle of %0.3f radians\n",arc_info.end_angle);
    printf("\n              and end angle of %0.3f radians\n",arc_info.end_angle);
    printf("\n          Its MATRIX consists of:");
    UF_CSYS_ask_matrix_values (arc_info.matrix_tag,matrix_info);
    printf("\n                  : [%0.3f , %0.3f , %0.3f]",
           matrix_info[0],matrix_info[1],matrix_info[2]);
    printf("\n                    [%0.3f , %0.3f , %0.3f]",
           matrix_info[3],matrix_info[4],matrix_info[5]);
    printf("\n                    [%0.3f , %0.3f , %0.3f]\n",
           matrix_info[6],matrix_info[7],matrix_info[8]);
}

/* given a tag for a matrix, display the data associated with it */
static void show_matrix_info(tag_t matrix,int att)
{
    double matrix_info[9];
    int result;

    result = UF_CSYS_ask_matrix_values (matrix,matrix_info);
    if (result) report_error(result,"failed in UF_CYS_ask_matrix_values");

    printf("\n      MATRIX with %d user defined attributes",att);
    printf("\n      Its data is : [%0.3f , %0.3f , %0.3f]",
           matrix_info[0],matrix_info[1],matrix_info[2]);
    printf("\n                    [%0.3f , %0.3f , %0.3f]",
           matrix_info[3],matrix_info[4],matrix_info[5]);
    printf("\n                    [%0.3f , %0.3f , %0.3f]\n",
           matrix_info[6],matrix_info[7],matrix_info[8]);
}

/* this routine is called if a found type is displayable. all of */
/* its display properties are shown here                         */
static void show_display_atts(tag_t object_tag)
{
    char                   *blank_status;
    char                   *color_name;
    UF_OBJ_disp_props_t    disp_props;
    char                   *line_width;
    int                    result;
    double                 rgb_values[3];

    result = UF_OBJ_ask_display_properties (object_tag,&disp_props);
    if (result) report_error(result,"failed in UF_OBJ_ask_display_properties");

    /* translate color from number to string */

    result = UF_DISP_ask_color(
        disp_props.color, UF_DISP_rgb_model, &color_name, rgb_values); 
    if (result) report_error(result,"failed in UF_DISP_ask_color");

    /* translate line width from number to string */
    switch(disp_props.line_width)
    {
        case UF_OBJ_WIDTH_NORMAL : line_width="NORMAL";  break;
        case UF_OBJ_WIDTH_THICK  : line_width="THICK";   break;
        case UF_OBJ_WIDTH_THIN   : line_width="THIN";    break;
        default                  : line_width="UNKNOWN"; break;
    }

    /* translate blank status from number to string */
    if (disp_props.blank_status==UF_OBJ_NOT_BLANKED)
        blank_status="NOT BLANKED";
    else
        blank_status="BLANKED";

    /* display values */
    printf("           ___DISPLAY PROPERTIES___");
    printf("\n              Layer            = %d.",disp_props.layer);
    printf("\n              Color            = %s.",color_name);
    printf("\n              Blank Status     = %s.",blank_status);
    printf("\n              Line Width       = %s.",line_width);
    printf("\n              Font             = %d.",disp_props.font);
    if (disp_props.highlight_status)  /* translate booleans to string */
        printf("\n              Highlight Status = TRUE\n");
    else
        printf("\n              Highlight Status = FALSE\n");

    UF_free(color_name);
}

/* this routine is used to find the next matrix type in a part. */
/* since matrix types' statuses are always CONDEMNED in a       */
/* part, UF_OBJ_cycle_objs_in_part cannot be used since it      */
/* only searches for ALIVE objects. This routine will cycle     */
/* through ALL tags of a part, regardless of their status       */
/* and return the next matrix type it finds. searching is       */
/* started from the beginning of a part, and continued from the */
/* location of the last type found.                             */
static void get_next_matrix_type(tag_t part_tag, tag_t *next_tag)
{
    int type, subtype;

    do
    {
        *next_tag = UF_OBJ_cycle_all(part_tag,*next_tag);
        if(*next_tag!=NULL_TAG)
            UF_OBJ_ask_type_and_subtype(*next_tag,&type,
                                        &subtype);
    } while(*next_tag!=NULL_TAG && type!=UF_matrix_type);
    /* keep cycling until we find our matrix type, or until we */
    /* find a NULL tag meaning that we have reached the end of */
    /* the part                                                */
}

/* this is the main routine that cycles through a part, displaying */
/* data associated with each object within the part                */
static void show_attribute_info(tag_t part_tag, int num_types,
                             int type_list[MAX_TYPES])
{
    int i, status;
    int type_list_count, attr_count;
    int result = 0;
    tag_t next_tag;
    logical displayable;

    for (i=0;i<num_types;i++)      /* loop through each type separately */
    {
        type_list_count = 0;       /* reset counter for this type */
        printf("\n\n\n  --------------------------------------------------\n");
        switch (type_list[i])
        {
            case UF_point_type :
                printf("  --- Searching for POINT objects"); break;
            case UF_line_type :
                printf("  --- Searching for LINE objects"); break;
            case UF_circle_type :
                printf("  --- Searching for ARC objects"); break;
            case UF_matrix_type :
                printf("  --- Searching for MATRIX objects"); break;
            default :
                printf("  --- Searching for objects of type _%d_",type_list[i]);
                break;
        }

        /* Check to see if object is displayable */
        if (UF_OBJ_is_type_displayable(type_list[i])==TRUE)
        {
            printf("\n  *** This object IS displayable");
            displayable=TRUE;
        }
        else
        {
            printf("\n  *** This object is NOT displayable");
            displayable=FALSE;
        }

        next_tag=NULL_TAG;            /* cycle from first object in part */
        do
        {
            /* if the object type if a matrix, we need to cycle the  */
            /* part using get_next_matrix_type. read description for */
            /* get_next_matrix_type() for reasons why.               */
            if (type_list[i]==UF_matrix_type)
                get_next_matrix_type(part_tag,&next_tag);
            else
            {
                /* for any other type, we simply search for the next */
                /* object of our type within the part                */
                result = UF_OBJ_cycle_objs_in_part(part_tag,type_list[i],&next_tag);
                if (result) report_error(result,"failed in UF_OBJ_cycle_objs_in_part");
            }

            /* if an object of this type was found in the part, show its info */
            if(next_tag!=NULL_TAG)
            {
                /* increment the counter for this type */
                type_list_count++;
                /* get its status (ie ALIVE, CONDEMNED etc...) */
                status = UF_OBJ_ask_status(next_tag);
                /* translate status number into a string */
                switch (status)
                {
                    case UF_OBJ_DELETED : 
                        printf("\n  --> DELETED object found :");     break;
                    case UF_OBJ_TEMPORARY : 
                        printf("\n  --> TEMPORARY object found :");   break;
                    case UF_OBJ_CONDEMNED : 
                        printf("\n  --> CONDEMNED object found :");   break;
                    case UF_OBJ_ALIVE : 
                        printf("\n  --> ALIVE object found :");       break;
                    default : 
                        printf("\n  --> Status of object : UNKNOWN"); break;
                }

                /* get number of user defined attributes */
                result = UF_ATTR_count_attributes(next_tag,UF_ATTR_any,&attr_count);
                if (result) report_error(result,"failed in UF_ATTR_count_attributes");

                /* depending on what type we are working with, show */
                /* the data associated with each                    */
                switch (type_list[i])
                {
                    case UF_point_type : show_point_info (next_tag,attr_count);
                        break;
                    case UF_line_type  : show_line_info  (next_tag,attr_count);
                        break;
                    case UF_circle_type: show_arc_info   (next_tag,attr_count);
                        break;
                    case UF_matrix_type: show_matrix_info(next_tag,attr_count);
                        break;
                    default :
                        printf("\n      O - object of type %d ",type_list[i]);
                        printf("with %d user defined attributes.\n",attr_count);
                        break;
                }
                /* if the object is displayable, show its display attributes */
                if (displayable)
                    show_display_atts(next_tag);
            }
        } while (next_tag!=NULL_TAG);  /* keep cycling until no more objects found */

        switch (type_list[i])
        {
            case UF_point_type :
                printf("\n  === Number of POINTs found : %d",type_list_count);
                break;
            case UF_line_type  :
                printf("\n  === Number of LINEs found : %d",type_list_count);
                break;
            case UF_circle_type:
                printf("\n  === Number of ARCs found : %d",type_list_count);
                break;
            case UF_matrix_type:
                printf("\n  === Number of MATRICES found : %d",type_list_count);
                break;
            default :
                printf("\n  === Number of type %d's found : %d",type_list[i],
                       type_list_count);
                break;
        }
        printf("\n  --------------------------------------------------\n");
    }
}

/* this routine shows the units that a part works with */
static void show_units(tag_t part_tag)
{
    int units;
  
    UF_PART_ask_units(part_tag, &units);   

    /* translate units number into a string */
    switch (units)
    {
        case UF_PART_ENGLISH : printf("     UNITS : inches\n");      break;
        case UF_PART_METRIC  : printf("     UNITS : millimeters\n"); break;
        default              : printf("     UNITS : unknown\n");     break;
    }
}
        
/***********************************************************************/
/************                    MAIN                    ***************/
/***********************************************************************/
extern int main(int argc, char **argv)
{
    UF_PART_load_status_t error_status;
    char    part_name[UF_CFI_MAX_PATH_NAME_SIZE];
    int     type_list[MAX_TYPES];
    int     num_types=0, num_parts;
    int     result;
    tag_t   part_tag;

    /* parse command line for part name and optional list of types */
    get_args(argc,argv,part_name,type_list,&num_types);

    /* add point, line, arc, and matrix to list of types (if not there) */
    add_extratypes(type_list,&num_types);

    /* initialize user functions */
    result = UF_initialize();
    if (result) report_error(result,"failed in UF_initialize");

    /* open up specified part */
    result = UF_PART_open(part_name,&part_tag,&error_status);
    if (result) report_error(result,"failed in UF_PART_open");
    num_parts = error_status.n_parts;
    UF_free_string_array(num_parts,error_status.file_names);

    printf("\n*******************************************************\n");
    printf  ("*** PART : %s",part_name);
    show_units(part_tag);
    printf  ("*******************************************************\n");

    /* cycle part, showing data */
    show_attribute_info(part_tag,num_types,type_list);

    printf("\nEND\n");
    return(0);
}
