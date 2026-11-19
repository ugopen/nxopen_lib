/*==================================================================================================

             Copyright (c) 2003,2004 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

====================================================================================================
File description:

    The NX/Open interface to the VDA Checker comply errors access example
    
    This interface is a set of NX/Open API functions to utilize information on
    violated geometry stored as comply errors in an external 
    *.ceo file ( Comply Error Objects File ) if the VDA - Checker has finished.

    This example demonstrates how to read in *.ceo files and get lists of
    comply error entities to manipulate by using the following functions

        UF_VDAC_load_ceo
        UF_VDAC_free_ceo
        UF_VDAC_ask_log_text_list
        UF_VDAC_ask_class_info
        UF_VDAC_ask_cckey_comply_errors
        UF_VDAC_ask_fo_comply_errors
        UF_VDAC_ask_cckey_fo_list
        UF_VDAC_ask_fo_list
        UF_VDAC_ask_fo_neighbors
        UF_VDAC_delete_list_members

====================================================================================================



==================================================================================================*/

#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <uf.h>
#include <uf_disp.h>
#include <uf_layer.h>
#include <uf_modl.h>
#include <uf_obj.h>
#include <uf_ui.h>
#include <uf_vdac.h>

/*---------------- Internal Data Structure Section ---------------------------*/

typedef char ufd_msg[ 2 *  MAX_FSPEC_BUFSIZE];

/*---------------- Internal Prototypes Section -------------------------------*/

#define UFXLM_is_valid_layer( /*int*/layer ) \
        (((layer) >= UF_LAYER_MIN_LAYER) && ((layer) <= UF_LAYER_MAX_LAYER))

static tag_t UFXLM_create_category
(
    const char* category_name,  /* I: .. maximum of UFX_NAME_LEN characters */
    const char* description,    /* I: optional description string */
    const int*  layer_members,  /* I: array of layer member numbers */
    int         member_count    /* I: number of layer members */
);

static void close_info_window( void );
static int compare_tags ( const void* l, const void* r );

#ifdef _WIN32
#define snprintf  _snprintf
#define vsnprintf _vsnprintf
#endif

static void write_info
( 
    const char* format, /* I: Format specification */
    ...                 /* I: Optional arguments */
);

/*---------------- Static Variables Section ----------------------------------*/

/*
Turn Info Window logging On or Off
*/
static logical sv_log_option = true;

/*---------------- Function Implementation Section ---------------------------*/

/*ARGSUSED*/
extern DllExport void ufusr( char *param, int *retcod, int param_len )
{
    int             error_code = 0;
    int             terminate = 0;
    ufd_msg         line, msg, text;

    do
    {
        UF_VDAC_ceos_p_t    ceos = NULL;
        int                 mode = 0;

        if ( (error_code = UF_initialize() ) )
        {
            write_info( "Error %d in UF_initialize\n", error_code );
            UF_get_fail_message( error_code, msg );
            write_info( "%s", msg );
            break;
        }
        terminate = 1;

        write_info( "\n\nNX/Open UF_VDAC API ufd_vdac_ceo_api_intern  test\n\n" );

        uf3192( &mode );

        if ( mode != 1 )
        {
            write_info( "CEO_API must execute in interactive mode!\n" );
            break;
        }

        do
        {
            UF_VDAC_ce_t            ce;
            UF_VDAC_cckey_fo_t      ce_list;
            UF_VDAC_fo_ce_t         ce_obj;
            UF_VDAC_class_info_t    class_info;
            int                     faulty_nb = 0;
            UF_VDAC_list_pc_t       first;
            int                     icrit;
            int                     layer = 250; /* all the bad guys */
            UF_VDAC_list_pc_t       list_pc;
            int                     ocount;

            /*
            Initialize comply errors evaluator structure 
            Load comply errors from *.ceo file of work part
            */
            error_code = UF_VDAC_load_ceo( NULL, NULL, UF_VDAC_ce_vers_vdac2, &ceos );
            
            if ( 0 != error_code )
            {
                UF_get_fail_message( error_code, msg );
                write_info( "%s", msg );
                break;
            }
            /*
            Get information about the number of face criteria that produced comply errors
            */
            error_code = UF_VDAC_ask_class_info( ceos, UF_VDAC_class_faces, &class_info );
            
            if ( 0 != error_code )
            {
                UF_get_fail_message( error_code, msg );
                write_info( "%s", msg );
                break;
            }
            
            if ( 0 == class_info.num_infos )
            {
                write_info( "No face violations found !\n" );
                break;
            }

            /*
            Get all comply error items of one check criterion key,
            further on this information (values etc.) is not used in this example
            */
            error_code = UF_VDAC_ask_cckey_comply_errors( ceos, &class_info, 0, &ce );
            
            if ( 0 != error_code )
            {
                UF_get_fail_message( error_code, msg );
                write_info( "%s", msg );
            }
            /*
            Get list of faulty object identifiers for one check criterion key
            (index = 0: this is only an example to get some result without doing more
            investigation in class_info before)
            */
            error_code = UF_VDAC_ask_cckey_fo_list( ceos, &class_info, 0, &ce_list );
            
            if ( 0 != error_code )
            {
                UF_get_fail_message( error_code, msg );
                write_info( "%s", msg );
            }
            
            sv_log_option = false; /* temporarily switched off logging (avoid large reports) */ 

            /*
            Move all comply error infected objects to the bad guys layer
            Change color
            */
            UFXLM_create_category( "Bad_guys", "comply error layer", &layer, 1 );
            write_info( "Moving objects to bad guys layer %d", layer );

            for ( list_pc = ce_list.list_head.first; list_pc != NULL; list_pc = list_pc->next )
            {
                tag_t               body = NULL_TAG;
                int                 color = 148; /* Light Red Pink */
                UF_OBJ_disp_props_t dprops;
                char                name[32];
                int                 type, subtype;

                if ( UF_OBJ_ask_status( list_pc->eid ) != UF_OBJ_ALIVE )
                    continue;
                if ( UF_OBJ_ask_type_and_subtype( list_pc->eid, &type, &subtype ) )
                    continue;
                if ( ! UF_OBJ_is_type_displayable( type ) )
                    continue;
                if ( UF_OBJ_ask_display_properties( list_pc->eid, &dprops ) )
                    continue;
                name[0] = 0;
                UF_OBJ_ask_name( list_pc->eid, name );

                write_info( "  tag=%u, type=%d, subtype=%d, layer=%d, color=%d, blank_status=%d"
                            ", line_width=%d, font= %d, name=%s\n", list_pc->eid, type, subtype,
                            dprops.layer, dprops.color, dprops.blank_status,
                            dprops.line_width, dprops.font, name );

                UF_MODL_ask_face_body( list_pc->eid, &body );

                if ( body != NULL_TAG )
                {
                    UF_OBJ_set_layer( body, layer );
                    UF_OBJ_set_color( body, color );
                }
                UF_OBJ_set_color( list_pc->eid, color );

                if ( UF_OBJ_ask_display_properties( list_pc->eid, &dprops ) )
                    continue;
                name[0] = 0;
                UF_OBJ_ask_name( list_pc->eid, name );

                write_info( "  tag=%u, type=%d, subtype=%d, layer=%d, color=%d, blank_status=%d"
                            ", line_width=%d, font= %d, name=%s\n", list_pc->eid, type, subtype,
                            dprops.layer, dprops.color, dprops.blank_status,
                            dprops.line_width, dprops.font, name );

                /*
                Get all comply errors of a faulty object
                */
                error_code = UF_VDAC_ask_fo_comply_errors( ceos, list_pc->eid, &ce_obj );
                
                if ( 0 != error_code )
                {
                    UF_get_fail_message( error_code, msg );
                    write_info( "%s", msg );
                }
                
                for ( icrit = 0; icrit < ce_obj.crit_count; icrit++ )
                {
                    write_info( "tag=%u, cfg_class=%d %s: object_id=( %u %u)", ce_obj.faulty,
                                (int)ce_obj.criteria[icrit].key_info.comply_class,
                                ce_obj.criteria[icrit].key_info.item_name,
                                ce_obj.criteria[icrit].ce_item.object_id,
                                ce_obj.criteria[icrit].ce_item.object_id2 );
                }
            }
            
            write_info( "\nProcess list of all faulty object identifiers" );
            first = NULL;
            ocount = 0;
            /*
            Get a list of all faulty object identifiers
            */
            error_code = UF_VDAC_ask_fo_list( ceos, &first, &ocount );
            
            if ( 0 != error_code )
            {
                UF_get_fail_message( error_code, msg );
                write_info( "%s", msg );
            }
            
            do
            {
                int     i;
                int     k = 0;
                tag_p_t obj_array = NULL;

                if ( NULL == (obj_array = (tag_p_t)malloc( (ocount + 1) * sizeof(tag_t) ) ) )
                    break;

                for ( list_pc = first; list_pc != NULL; list_pc = list_pc->next )
                    obj_array[k++] = list_pc->eid;

                if ( k > 1 )
                    qsort( obj_array, k, sizeof(tag_t), compare_tags );

                for ( i = 0; i < k; i++ )
                {
                    /*
                    Get all comply errors of a faulty object
                    */
                    error_code = UF_VDAC_ask_fo_comply_errors( ceos, obj_array[i], &ce_obj );
                    
                    if ( 0 != error_code )
                    {
                        UF_get_fail_message( error_code, msg );
                        write_info( msg );
                    }
                    write_info( "\nobject=%u has %d comply error(s)", obj_array[i], ce_obj.crit_count );

                    for ( icrit = 0; icrit < ce_obj.crit_count; icrit++ )
                    {
                        write_info( "tag=%u, cfg_class=%d %s: object_id=( %u %u)", ce_obj.faulty,
                                    (int)ce_obj.criteria[icrit].key_info.comply_class,
                                    ce_obj.criteria[icrit].key_info.item_name,
                                    ce_obj.criteria[icrit].ce_item.object_id,
                                    ce_obj.criteria[icrit].ce_item.object_id2 );
                    }
                }
                free (obj_array );

            } while ( 0 );

            /*
            Highlight all faulty objects and their neighbors
            */
            close_info_window();
            sv_log_option = true;

            for ( list_pc = first; list_pc != NULL; list_pc = list_pc->next )
            {
                UF_VDAC_fo_neighbor_pc_t    nb;
                int                         na = 0, nc;
                UF_VDAC_fo_neighbors_t      fo_nb;

                UF_DISP_set_highlight( list_pc->eid, 1 );

                sprintf( line, "Neighbors of %u:", list_pc->eid );

                error_code = UF_VDAC_ask_fo_neighbors( ceos, list_pc->eid, &fo_nb );
                
                if ( 0 != error_code )
                {
                    UF_get_fail_message( error_code, msg );
                    write_info( msg );
                    continue;
                }
                if ( fo_nb.first != NULL )
                    faulty_nb++;

                for ( nb = fo_nb.first, nc = 0; nb != NULL; nb = nb->next, nc = (nc+1) % 10 )
                {
                    UF_DISP_set_highlight( nb->neighbor, 1 );
                    sprintf( text, " %u", nb->neighbor);
                    strcat( line, text );
                    na++;

                    if ( nc == 9 )
                    {
                        write_info( "%s", line );
                        sprintf( line, "Neighbors of %u:", list_pc->eid );
                        na = 0;
                    }
                }
                if ( na > 0 )
                    write_info( "%s", line );
            }
            write_info( "Number of faulty objects with neighbor info: %d", faulty_nb );
            close_info_window();
            uc1601( "Press OK to turn off highlight", 1 );

            /*
            Unhighlight all
            */
            for ( list_pc = first; list_pc != NULL; list_pc = list_pc->next )
            {
                UF_VDAC_fo_neighbor_pc_t    nb;
                UF_VDAC_fo_neighbors_t      fo_nb;

                UF_DISP_set_highlight( list_pc->eid, 0 );

                error_code = UF_VDAC_ask_fo_neighbors( ceos, list_pc->eid, &fo_nb );
                
                if ( 0 != error_code )
                {
                    UF_get_fail_message( error_code, msg );
                    write_info( "%s", msg );
                    continue;
                }
                for ( nb = fo_nb.first; nb != NULL; nb = nb->next )
                {
                    UF_DISP_set_highlight( nb->neighbor, 0 );
                }
            }

            /*
            Delete all members of UG object identifier list
            */
            error_code = UF_VDAC_delete_list_members( ceos, &(ce_list.list_head) );
            
            if ( 0 != error_code )
            {
                UF_get_fail_message( error_code, msg );
                write_info( "%s", msg );
            }
            UF_LAYER_set_status( layer, UF_LAYER_ACTIVE_LAYER );

        } while ( 0 );

        /*
        Before leaving the VDA module:
        Copy VDA module log to info window to report errors occured during work on *.ceo file
        */
        write_info( "\nSummary of VDA module log (possible errors will be reported here):\n" );

        do
        {
            UF_VDAC_text_list_pc_t  first, ptext;

            /*
            Get the log and error log text list of the VDA module
            */
            error_code = UF_VDAC_ask_log_text_list( ceos, &first, NULL );
            
            if ( 0 != error_code )
            {
                UF_get_fail_message( error_code, msg );
                write_info( msg );
                break;
            }

            for ( ptext = first; ptext != NULL; ptext = ptext->next )
            {
                write_info( ptext->text );
            }
        } while ( 0 );

        /*
        Free the comply errors evaluator structure
        */
        if ( ceos != NULL )
            error_code = UF_VDAC_free_ceo( &ceos );

    } while ( 0 );

    close_info_window();

    if ( terminate )
        UF_terminate();
    if ( retcod != NULL )
        *retcod = error_code;
}

/*---------------- Static Function Implementation Section --------------------*/

/*
  Purpose
    Group layers by a category name.
    Assign a category name, member layers, and description.
  Return
    UG category object identifier or NULL_TAG 
*/
static tag_t UFXLM_create_category
(
    const char* category_name,  /* I: .. maximum of UF_OBJ_NAME_NCHARS characters */
    const char* description,    /* I: optional description string */
    const int*  layer_members,  /* I: array of layer member numbers */
    int         member_count    /* I: number of layer members */
)
{
    tag_t   ctag = NULL_TAG;

    do
    {
        UF_LAYER_category_info_t    category_info;
        int                         i;
        int                         layer_count = 0;

        if ( category_name == NULL )
            break;
        else if ( ! category_name[0] )
            break;

        memset( &category_info, 0, sizeof(category_info) );

        /* The following may truncate a multi-byte character in the middle,
           if passed a category_name larger than UF_OBJ_NAME_BUFSIZE.  If
           that is a concern, the calling program should use UF_TEXT_truncate
           to truncate the category name first.
        */
        snprintf ( category_info.name, UF_OBJ_NAME_BUFSIZE, category_name ); 

        if ( (description != NULL) && (*description) )
            snprintf( category_info.descr, UF_OBJ_NAME_BUFSIZE, (char *)description );


        for ( i = 0; i < member_count; i++ )
        {
            int layer = layer_members[i];

            if ( UFXLM_is_valid_layer( layer ) )
            {
                category_info.layer_mask[ layer - 1 ] = TRUE;
                layer_count++;
            }
        }
        if ( layer_count < 1 )
            break;

        if ( UF_LAYER_create_category( &category_info, &ctag ) )
        {
            ctag = NULL_TAG;
        }
    } while ( 0 );

    return ctag;
}

static void close_info_window( void )
{
    logical is_open;

    UF_UI_is_listing_window_open( &is_open );

    if ( is_open )
        UF_UI_close_listing_window();
}

static int compare_tags ( const void* l, const void* r )
{
    const tag_t*    a = (const tag_t*)l;
    const tag_t*    b = (const tag_t*)r;

    if ( *a < *b )
        return -1;
    else if ( *a > *b )
        return 1;
    else
        return 0;
}

/*
  Purpose
    Write to UG Info window
*/
static void write_info
( 
    const char* format, /* I: Format specification */
    ...                 /* I: Optional arguments */
)
{
    logical is_open;

    if ( ! sv_log_option )
        return;
    UF_UI_is_listing_window_open( &is_open );

    if ( !is_open )
    {
        UF_UI_open_listing_window();
        UF_UI_is_listing_window_open( &is_open );
    }
    if ( is_open )
    {
        va_list ap;
        char    msg[1024];
        size_t  sl;

        va_start( ap, format );
        vsnprintf( msg, 1022, format, ap );
        va_end( ap );
        /*
        Terminate Info window string with a new line
        */
        if ( (sl = strlen( msg )) < 1 )
            strcpy( msg,  "\n" );
        else if ( msg[sl - 1] != '\n' )
            strcat( msg, "\n" );

        UF_UI_write_listing_window( msg );
    }
}

extern DllExport int ufusr_ask_unload( void )
{
    return UF_UNLOAD_IMMEDIATELY;
}

extern DllExport void ufusr_cleanup( void )
{
}


