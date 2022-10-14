/*
===========================================================================
        Copyright (c) 1998 Unigraphics Solutions Corporation
                  Unpublished - All Rights Reserved
===========================================================================
File Description:

    This file is a sample INTERNAL User Function routine that
    demonstrates the use of various UG/Routing functions. It assumes
    that an active (work) part exists.

===========================================================================


===========================================================================*/


#include <string.h>
#include <stdio.h>

#include <uf_defs.h>
#include <uf.h>
#include <uf_assem.h>
#include <uf_curve.h>
#include <uf_part.h>

#include <uf_route.h>
#include <uf_dirpath.h>

#define UF_CALL(X)(report_error( __FILE__, __LINE__, #X, (X)))

static int report_error( char *file, int line, char *call, int irc )
{
    if(irc)
    {
        char err[133],
             msg[133];
        sprintf( msg, "*** ERROR code %d at line %d in %s:\n+++",
            irc, line, file );
        UF_get_fail_message( irc, err );

        UF_print_syslog( msg, FALSE );
        UF_print_syslog( err, FALSE );
        UF_print_syslog( "\n", FALSE );
        UF_print_syslog( call, FALSE );
        UF_print_syslog( ";\n", FALSE );

        if( !UF_UI_open_listing_window() )
        {
            UF_UI_write_listing_window( msg );
            UF_UI_write_listing_window( err );
            UF_UI_write_listing_window( "\n" );
            UF_UI_write_listing_window( call );
            UF_UI_write_listing_window( ";\n" );
        }
    }
    return( irc );
}

/*ARGSUSED*/
void ufusr(char *param, int *retcod, int parm_len)
{
    double     stock_and_part_nps   = 3.0;
    char       *stock_material      = "ASTM A312 TP304(W)";
    char       *stock_schedule      = "80S";
    char       *std_part_material   = "ASTM A403 WP316L(W)";
    char       *std_part_rating     = "10S";
    char       *app_view_name       = NULL;
    const char *app_view_symb       = "UGII_ROUTE_MECH_APP_VIEW";
    const char *part_search_symb    = "UGII_ROUTE_MECH_PART_PATH";
    char       *elbow_node          = "ELBOWS";
    char       *old_app_view_name   = NULL;
    char       full_name[ MAX_FSPEC_BUFSIZE ];

    double  pos1[3] = {  0.0, 0.0, 0.0 };
    double  pos2[3] = { 10.0, 0.0, 0.0 };
    double  pos3[3] = { 10.0, 10.0, 0.0 };
    double  pos4[3] = { 10.0, 10.0, 10.0 };
    double  pos5[3] = { 10.0, 0.0, 10.0 };
    double  origin[3] = { 0.0, 0.0, 0.0 };
    double  csys[6] = { 1.0, 0.0,  0.0, 0.0, 1.0, 0.0 };
    double  radius = 2.0;
    double  ratio = 2.0;

    int     n_stock_charx;
    int     n_stock_matches;
    int     n_std_part_charx;
    int     n_std_part_matches;
    int     inx;
    int     style = UF_ROUTE_STYLE_SIMPLE;
    int     num_segs;
    int     num_places;
    int     part_units;

    tag_t   point;
    tag_t   line;
    tag_t   rcps[5];
    tag_t   segs[7];

    tag_t   stock_data;
    tag_t   anchor;
    tag_t   cross;
    tag_t   corner;
    tag_t   work_part;
    tag_t   fit_part;
    tag_t   inst_id;
    tag_t   occ;
    tag_t   work_part_comp;
    tag_t   work_part_occ;
    tag_t   dir_path;
    tag_t   part_tag;

    UF_CURVE_line_t  line_s;
    UF_ROUTE_charx_t  stock_charx[3];
    UF_ROUTE_charx_t  std_part_charx[4];
    UF_ROUTE_part_lib_part_p_t stock_matches;
    UF_ROUTE_part_lib_part_p_t std_part_matches;
    UF_ROUTE_application_view_p_t old_app_view;
    UF_ROUTE_application_view_p_t app_view;
    UF_PART_load_status_t   error_code ;
    UF_ROUTE_place_solution_p_t *places;

    UF_CALL( UF_initialize() );

    part_tag = UF_PART_ask_display_part();
    if ( part_tag == NULL_TAG ) return;

    UF_PART_ask_units( part_tag, &part_units);

    if ( part_units == UF_PART_METRIC )
    {
        // Use 25 mm NPS instead of 3 inches.
        stock_and_part_nps = 10.0;

        // Change the elbow node to the DIN elbows.
        elbow_node = "DIN_PIP_ELBOW";

        // Change the material and rating to one of the DIN standards.
        stock_material    = "ST37-2";
        std_part_material = "ST37-2";
        std_part_rating   = "16";

        // Update the positions from inch to millimeters
        pos1[0] *= 25.4;
        pos1[1] *= 25.4;
        pos1[2] *= 25.4;

        pos2[0] *= 25.4;
        pos2[1] *= 25.4;
        pos2[2] *= 25.4;

        pos3[0] *= 25.4;
        pos3[1] *= 25.4;
        pos3[2] *= 25.4;

        pos4[0] *= 25.4;
        pos4[1] *= 25.4;
        pos4[2] *= 25.4;

        pos5[0] *= 25.4;
        pos5[1] *= 25.4;
        pos5[2] *= 25.4;
    }

    /* This example must be run from the Routing Mechanical application */
    old_app_view = UF_ROUTE_ask_current_app_view( );
    if ( old_app_view == NULL ) return;

    UF_ROUTE_ask_app_view_name( old_app_view, &old_app_view_name );
    if ( strcmp( old_app_view_name, "Routing Mechanical" ) != 0 )
    {
        UF_print_syslog( "This sample must be run from the Routing Mechanical application.", FALSE );
        return;
    }

    /* Load and set the application view *** Routing -> Base */
    UF_CALL( UF_translate_variable( app_view_symb, &app_view_name ) );
    UF_CALL( UF_ROUTE_load_app_view( app_view_name, &app_view ) );
    UF_CALL( UF_ROUTE_set_current_app_view( app_view ) );

    /* Set the search path for locating Routing (Base) parts / stock */
    UF_CALL( UF_DIRPATH_create_from_env ( part_search_symb, &dir_path ) );
    UF_CALL( UF_ROUTE_set_part_search_path ( dir_path ) );

    /* Create the RCPs at absolute positions */
    UF_CALL( UF_ROUTE_create_rcp_position( pos1, &rcps[0] ) );
    UF_CALL( UF_ROUTE_create_rcp_position( pos2, &rcps[1] ) );

    /* Create RCPs at existing point */
    UF_CALL( UF_CURVE_create_point( pos3, &point ) );
    UF_CALL( UF_ROUTE_create_rcp_point( point, &rcps[2] ) );

    /* Create the Segments through these RCPs */
    UF_CALL( UF_ROUTE_create_seg_thru_rcps( rcps[0], rcps[1], &segs[0] ) );
    UF_CALL( UF_ROUTE_create_seg_thru_rcps( rcps[1], rcps[2], &segs[1] ) );

    /* Create a curve and use this object to create a segment */
    for( inx = 0 ; inx < 3 ; inx++ )
    {
        line_s.start_point[inx] = pos4[inx];
        line_s.end_point[inx]   = pos5[inx];
    }
    UF_CALL( UF_CURVE_create_line( &line_s, &line ) );

    /* Create the Segments through RCPs that follows a curve
       In this case the RCPs should be created along the curve parameter */
    UF_CALL( UF_ROUTE_create_rcp_curve_parm( line, 0, &rcps[3] ) );/* Curve start parm=0 */
    UF_CALL( UF_ROUTE_create_rcp_curve_parm( line, 1, &rcps[4] ) );/* Curve end parm=1 */

    UF_CALL( UF_ROUTE_create_seg_thru_rcps( rcps[2], rcps[3], &segs[2] ) ); /* Connecting
                                                                    Segment */
    UF_CALL( UF_ROUTE_create_seg_on_curve( line, rcps[3], rcps[4], &segs[3] ) );

    /* Set up the characteristics for the stock we wish to assign */

    stock_charx[0].type = UF_EPLIB_CHARX_TYPE_REAL;
    strcpy (stock_charx[0].title, "NPS");
    stock_charx[0].value.r_value = stock_and_part_nps;

    if ( part_units == UF_PART_METRIC )
    {
        stock_charx[1].type = UF_EPLIB_CHARX_TYPE_STR;
        strcpy (stock_charx[1].title, "PIPE_MATERIAL");
        stock_charx[1].value.s_value = stock_material;

        n_stock_charx = 2;
    }
    else
    {
        stock_charx[1].type = UF_EPLIB_CHARX_TYPE_STR;
        strcpy (stock_charx[1].title, "MATERIAL");
        stock_charx[1].value.s_value = stock_material;

        stock_charx[2].type = UF_EPLIB_CHARX_TYPE_STR;
        strcpy (stock_charx[2].title, "SCHEDULE");
        stock_charx[2].value.s_value = stock_schedule;

        n_stock_charx = 3;
    }

    /* Find the stock we want in the Routing Part Library */
    UF_CALL( UF_ROUTE_match_charx_in_plib( "STOCK",
                                           n_stock_charx,
                                           stock_charx,
                                           &n_stock_matches,
                                           &stock_matches ) );
    if ( n_stock_matches == 0 ) return;

    /* Locate (or load) the stock data which matches our criteria */
    UF_CALL( UF_ROUTE_load_stock_by_charx( &stock_matches[0],
                                           "",
                                           style,
                                           &stock_data,
                                           &anchor,
                                           &cross ) );

    UF_CALL( UF_ROUTE_free_match_results( n_stock_matches,
                                          stock_matches ) );

    /* Create a bend corner at one of the RCP junctions */
    UF_CALL( UF_ROUTE_create_bend_by_radius( rcps[1], radius,
                                             &corner, &segs[4] ) );

    /* Assigns the stock data to segments */
    num_segs = 4;
    UF_CALL( UF_ROUTE_assign_stock( stock_data, anchor,
                                    cross, num_segs, segs ) );

    /* Create a bend corner by the ratio of stock dia to the bend radius
       The stock gets automatically updated at the bend */
    UF_CALL( UF_ROUTE_create_bend_by_ratio( rcps[2], ratio,
                                            &corner, &segs[5] ) );

    /* Set up the characteristics for the Standard part we wish to place */

    std_part_charx[0].type = UF_EPLIB_CHARX_TYPE_REAL;
    strcpy (std_part_charx[0].title, "NPS");
    std_part_charx[0].value.r_value = stock_and_part_nps;

    std_part_charx[1].type = UF_EPLIB_CHARX_TYPE_REAL;
    strcpy (std_part_charx[1].title, "ELBOW_ANG");
    std_part_charx[1].value.r_value = 90.0;

    std_part_charx[2].type = UF_EPLIB_CHARX_TYPE_STR;
    strcpy (std_part_charx[2].title, "FITTING_MATERIAL");
    std_part_charx[2].value.s_value = std_part_material;

    std_part_charx[3].type = UF_EPLIB_CHARX_TYPE_STR;
    strcpy (std_part_charx[3].title, "RATING");
    std_part_charx[3].value.s_value = std_part_rating;

    n_std_part_charx = sizeof( std_part_charx ) / sizeof( std_part_charx[0] );

    UF_CALL( UF_ROUTE_match_charx_in_plib( elbow_node, n_std_part_charx,
                                  std_part_charx, &n_std_part_matches,
                                  &std_part_matches ) );
    if ( n_std_part_matches == 0 ) return;

    UF_CALL( UF_ROUTE_load_part_by_charx( std_part_matches[0].num_charx,
                                 std_part_matches[0].charx, &fit_part ) );

    /* Add the elbow as a component of the work part */
    UF_CALL( UF_PART_ask_part_name( fit_part, full_name ) );
    work_part = UF_ASSEM_ask_work_part( );
    UF_CALL( UF_ASSEM_add_part_to_assembly( work_part, full_name,
                                            NULL, NULL, origin,
                                            csys, -1, &inst_id,
                                            &error_code ) );

    /*
        For the following Routing operations of setting the characteristics
        of the fitting part and for placing it within the Routing, we
        use the part occurrence of the fitting in the part occurrence tree
        that is "rooted" at the work part. This is because the Routing
        characteristics and placement functions expect this particular
        part occurrence.
    */
    work_part_comp = UF_ASSEM_ask_parent_of_instance( inst_id );
    work_part_occ = UF_ASSEM_ask_root_part_occ( work_part_comp );
    occ = UF_ASSEM_ask_part_occ_of_inst( work_part_occ, inst_id ) ;

    /*
        We now have the part occurrence of the fitting in the work part's
        part occurrence tree. So we can attach the Routing characteristics
        to this part occurrence and place this occurrence within the
        Routing.
    */
    UF_CALL( UF_ROUTE_set_characteristics( occ, std_part_matches[0].num_charx,
                                           std_part_matches[0].charx ) );

    /* Place the elbow at the fourth RCP */
    num_places = 0; places = NULL;
    UF_CALL( UF_ROUTE_solve_places( rcps[3], occ,
                                    &num_places, &places ) );

    UF_CALL( UF_ROUTE_ask_places_transform( places[0], origin, csys ) );

    UF_CALL( UF_ASSEM_reposition_instance( inst_id, origin, csys ) );

    UF_CALL( UF_ROUTE_free_places( num_places, places ) );

    UF_CALL( UF_ROUTE_set_part_in_stock( occ ) );

    UF_terminate();

    return;
}
