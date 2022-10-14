/*===========================================================================

                        Copyright (c) 1998 
                Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

 ===========================================================================*/
/*
 ************************************************************************
 *                                                                      *
 * This is a sample C program written for Internal User Function.    *
 * Its intent is a small, prewritten program so users can test        *
 * Internal UFUN on their system to make sure it works.            *
 *                                    *
 *  param     - Parameters                 - Input,  But Not Used       *
 *  retcod    - Return Code                - Output                     *
 *  param_len - Length of 'param' argument - Input                      *
 *                                                                      *
 *           *
 ************************************************************************/

#include <stdio.h>
#include <uf_defs.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_cfi.h>
#include <uf_curve.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_cfi.h>

static void report_error( int error_code, char *msg_text, char *part_name );

#define WAIT 1
#define PART 2

extern void ufusr( char *param, int *retcod, int param_len )
{
    static char title[] =         "CHOOSE OPTION";
    static char menu[6][37+1] = {    "POINT",
                    "LINE",
                    "ARC",
                    "DELETE LAST ENTITY",
                    "CHANGE ARC MODE",
                    "EXIT PROGRAM"        };

    static char mdmenu[2][37+1] = {     "PARTIAL ARC",
                    "FULL CIRCLE"        };

    static char linmsg[2][18] = {    "CHOOSE LINE START",
                       "CHOOSE LINE END"    };

    static char arcmsg[] =         "CHOOSE POINT #";
    static char prtnam[ MAX_FSPEC_BUFSIZE] =         "blank";

    int        choice;        /*  User Choice            */
    int        defalt[2];    /*  Default Point Selection Type*/
    tag_t    entid = 0;    /*  Entity Identifer        */
    int        idum;        /*  Dummy Integer Variable    */
    int        mode = 1;    /*  Arc Creation Mode        */
    double    point1[3];    /*  Point Data Variable        */
    double    point2[3];    /*  Point Data Variable        */
    double    point3[3];    /*  Point Data Variable        */
    int        status;        /*  Status            */
    int        nopart;         /*  No active part flag         */
    int        pos_returned;   /*  Pos returned flag from menu */
    int        rejected = 0;   /*  Reject flag from menu       */
                                /*                              */
    tag_t       part_tag;       /*  Part Tag of Part            */
    UF_PART_load_status_t       /*                              */
                load_status;    /*  Structure to hold any       */
                                /*    errors when loading part  */
    int         num_parts;      /*  Number of parts loaded      */

    UF_initialize();

/*  Check For An Active Part */

    part_tag = UF_ASSEM_ask_work_part();

    if ( part_tag == NULL_TAG )
        {

/*      Ask For A Part To Retrieve or Create */

        nopart = 1;
        while (nopart)
            {
            choice = uc1600("Retrieve/Create part*Enter name", prtnam, &idum);
            if (choice < 3) { return; }
            nopart=((choice != 1) && (choice != 4) && (prtnam[0] != 0)) ? 0 : 1;

/*          Check if the named part already exists on disk */

            status = uc4560(prtnam, PART);
            if ( status == 0 )
                {

/*              Retrieve specified part */
    
                status = UF_PART_open( prtnam, &part_tag, &load_status );

                nopart = 0;
                num_parts = load_status.n_parts;
                if ( status != 0 )
                    {
                    report_error( status, "retrieving part", prtnam );
                    nopart = 1;
                    }
                if ( num_parts > 0 )
                    {
                    int indx = 0;
                    while ( indx < num_parts )
                        {
                        report_error( load_status.statuses[indx],
                                      "retrieving part",
                                      load_status.file_names[indx] );
                        indx++;
                        }
                    UF_free_string_array( num_parts, load_status.file_names );
                    UF_free( load_status.statuses );
                    nopart = 1;
                    }
                }

            else if ( status == 1 )
                {

/*              Create specified part */

                status = UF_PART_new(prtnam, UF_PART_ENGLISH, &part_tag );
                report_error( status, "creating part", prtnam );
                if ( status == 0 )
                    nopart = 0;
                }
            else
                {
                report_error( status, "checking part", prtnam );
                }
            }
        }

/*  We Now Have An Active Part */
/*  Get Next Action Choice (This Section Loops) */

    while (1)
        {
        choice = uc1603(title, 0, menu, 6);

        /*  Should always cancel out of the ufun dialog when the
         *  user selects cancel or back
         */
        if (choice == 1 || choice == 2) 
        {
            UF_terminate();
        }

        choice += -4;
        defalt[0] = 0;
        switch (choice) {
        case 1:  /*  Create Points */
                choice = uc1616("CREATE POINT", defalt, 0, point1);
                while (choice > 4)
                      {
                    UF_CURVE_create_point ( point1 , &entid );
                    choice = uc1616("CREATE POINT", defalt, 0, point1);
                    }
                break;

        case 2:  /*  Create Lines */
                choice = 5;
                while (choice > 4)
                      {
            UF_CURVE_line_t    line_coords;

                    choice = uc1616(linmsg[0], defalt, 0,
              line_coords.start_point );
                    if (choice > 4)
                        {
                        choice = uc1616(linmsg[1], defalt, 0,
              line_coords.end_point );
                        if (choice > 4)
                UF_CURVE_create_line ( &line_coords , &entid );
                        if (choice == 1) 
                            choice = 5; 
                        }
                    }
                break;

        case 3:  /*  Create Arcs/Circles */
                pos_returned = 1;
                while (pos_returned)
                    {
                    arcmsg[13] = '1';
                    choice = uc1616(arcmsg, defalt, 0, point1);
                    pos_returned =  (choice > 4) ? 1 : 0;
                    if (choice > 4)
                        do {
                            arcmsg[13] = '2';
                            choice = uc1616(arcmsg, defalt, 0, point2);
                            if (choice > 4)
                                {
                                arcmsg[13] = '3';
                                choice = uc1616(arcmsg, defalt, 0, point3);
                                rejected = (choice == 1) ? 1 : 0;
                                if (choice > 4)
                                    FTN(uf5063)(&mode,point1,point2,point3,&entid);
                                }
                            else   /* check work */
                                {
                                rejected = (choice == 1) ? 0 : 1;
                                pos_returned = (choice == 1) ? 1 : 0;
                                }
                        } while (rejected);
                    }
                break;

        case 4:  /*  Delete Last Entity Created */
                if (entid != 0)
                    UF_OBJ_delete_object(entid);
                entid = 0;
                break;

        case 5:  /*  Change Arc Mode */
                choice = uc1603("CHOOSE ARC MODE", mode, mdmenu, 2);
                if (choice > 4)
                    mode = choice - 4;
                break;

        default: UF_terminate ( );
             return;
    }
    }
}

/*----------------------------------------------------------------------------*/

static void report_error( int error_code, char *msg_text, char *part_name )
{
    if ( error_code != 0 )
        {
        char error_message[133];
        char local_string[300];

        UF_get_fail_message( error_code, error_message );

        sprintf(local_string, "Error %d   %s: %s - %s",
                error_code, msg_text, part_name, error_message );

        uc1601( local_string, WAIT );
        }
}
