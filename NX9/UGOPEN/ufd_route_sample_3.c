/*============================================================================

                    Copyright (c) 2001 Unigraphics Solutions
                       Unpublished - All rights reserved
==============================================================================
File description:

This is a sample UG/Routing plug-in program. The UG/Routing module allows
you to define an internal UG/Open program to be invoked at various points 
within UG/Routing to replace the default processing. Currently, a "plug-in"
or replacement routine may been specified for the following Routing
functions:

Compute Bundle diameter (UG/Wiring)

To define a plug-in, modify your Application View file (.apv) to include a 
PLUG_INS section. Shown below is a sample:

PLUG_INS
ROUTE BUNDLE libbates.so compute_bundle
END_OF_PLUG_INS

The above PLUG_INS description tells UG/Routing to execute a user supplied
function whenever UG/Routing needs to determine the information for a
bundle of wires. UG/Routing will try to load the shared library (DLL), 
libbates.so, and then invoke the "compute_bundle" entry point within that
shared library (DLL). It will call the function with a single argument which 
is a pointer to a structure of type UF_ROUTE_bundle_data_s (defined in 
uf_route.h).

struct UF_ROUTE_bundle_data_s
{
    int         num_stock_datas;     I Number of stock data objects
    tag_t      *stock_datas;         I Array of stock data tags
    int         num_cross_sections;  I Number of cross sections
    tag_t      *cross_sections;      I Cross section tags
    int         num_anchors;         O Number of anchors
    tag_t      *anchors;             O Anchor tags
};

Note that the UGII_SHARE environment variable is used to determine the
paths to be searched to locate the libraries referenced by the PLUG_INS
entry.

The compute_bundle function is invoked by UG/Routing whenever the cross
section must be computed for a given set of wires. The input to the plug-in
is the count and an array of tags of the stock_data objects which represent
the wires in the bundle. These stock_data objects may be queried to determine
various Routing characteristics (such as OD or gauge or whatever).

From this information, the plug-in needs to create one or two Routing cross
section objects. These cross section objects define the set of curves which
will be swept along the Routing path to generate the bundle solid. You can
define one or two cross sections, one for Style == SIMPLE and one for Style
== DETAIL. If only one cross section is defined, it will be used for both
styles. Typically, you will define a single cross section object which
will contain a single circle, centered at the origin, and with a diameter
appropriate for the supplied stock_data objects (wire types).

You may optionally define anchors, which are Routing objects which may be 
used to determine an alternate attachment point for the cross section
curves to the segments of the path. Normally, we attach the "center"
(0,0,0) location of the cross section curves to the end of the segment
before sweeping the curves along the path. If you specify that the
stock should use an anchor, its position defines the attachment point.
So, for example, specifying an anchor whose position is (4,0,0) has the
effect of shifting the bundle 4 units to the "left" of the path.

This sample compute_bundle program creates a single cross section
object and no anchors.

==============================================================================
 TEXT ENCLOSED within delete markers will be REMOVED
=============================================================================*/

#include <stdlib.h>
#include <uf.h>
#include <uf_csys.h>
#include <uf_curve.h>
#include <uf_modl_expressions.h>
#include <uf_obj.h>
#include <uf_route.h>
#include <ufd_route_sample.h>

static void get_wire_diameters( int      num_stock_data,
                                tag_t   *stock_data,
                                double **wire_diameters )
{
    int     sx, error;

    *wire_diameters = NULL;
    if  ( num_stock_data )
    {
        *wire_diameters = (double *) UF_allocate_memory( num_stock_data *
                                                         sizeof(double),
                                                         &error );
        for ( sx = 0 ; sx < num_stock_data ; sx ++ )
        {
            int                 num_charx;
            UF_ROUTE_charx_p_t  charx;
            char                od[] = "OD";
            int                 od_indx;

            (*wire_diameters)[sx] = 0.0;
            UF_ROUTE_ask_characteristics( stock_data[sx],
                                          UF_ROUTE_CHARX_TYPE_ANY,
                                          &num_charx, &charx );
            UF_ROUTE_find_title_in_charx( num_charx, charx, od, &od_indx );
            if  ( od_indx >= 0 )
            {
                switch ( charx[od_indx].type )
                {
                  case UF_ROUTE_CHARX_TYPE_INT:
                    (*wire_diameters)[sx] = 
                        (double) charx[od_indx].value.i_value;
                    break;

                  case UF_ROUTE_CHARX_TYPE_REAL:
                    (*wire_diameters)[sx] = charx[od_indx].value.r_value;
                    break;

                  case UF_ROUTE_CHARX_TYPE_STR:
                    (*wire_diameters)[sx] = 
                        strtod( charx[od_indx].value.s_value, NULL );
                    break;

                  default:
                    break;
                }
            }
        }
    }
}

static  void get_bundle_diameter_from_wires( int     num_wires,
                                             double *wire_diameters,
                                             double *bundle_diameter )
{
    int     wx;
    double  total_diameters = 0.0;

    if  ( num_wires > 0 )
    {
        double  factor;

        for ( wx=0 ; wx < num_wires ; wx++ )
        {
            total_diameters += wire_diameters[wx];
        }
        factor = 2.0 / num_wires;
        *bundle_diameter = total_diameters * factor;
    }
    else
        *bundle_diameter = 1.0;
    
}

static  void create_cross( double diameter, tag_t *cross_section )
{
    tag_t               arc;
    tag_t               exprs[2];
    UF_CURVE_arc_t      arc_data;
    double              matrix[9] = { 1,0,0, 0,1,0, 0,0,1 };

    UF_CSYS_create_matrix( matrix, &arc_data.matrix_tag );
    arc_data.radius        = diameter / 2;
    arc_data.start_angle   = 0.0;
    arc_data.end_angle     = TWOPI;
    arc_data.arc_center[0] = 0.0;
    arc_data.arc_center[1] = 0.0;
    arc_data.arc_center[2] = 0.0;

    UF_CURVE_create_arc( &arc_data, &arc );
    UF_OBJ_set_blank_status( arc, UF_OBJ_BLANKED );
    UF_MODL_create_exp_tag( "0.0", &exprs[0] );
    UF_MODL_create_exp_tag( "0.0", &exprs[1] );
    UF_ROUTE_create_cross_section( arc, UF_ROUTE_STYLE_SIMPLE,
                                   exprs, 1, &arc, cross_section );
}

#ifdef __cplusplus
extern "C" {
#endif

extern void DllExport compute_bundle( UF_ROUTE_bundle_data_p_t bundle_data )
{
    int         error ;
    double     *wire_diameters;
    double      bundle_diameter;

    UF_initialize();

    bundle_data->num_anchors        = 0;
    bundle_data->anchors            = NULL;

    get_wire_diameters( bundle_data->num_stock_data, bundle_data->stock_data,
                        &wire_diameters );

    get_bundle_diameter_from_wires( bundle_data->num_stock_data,
                                    wire_diameters,
                                    &bundle_diameter );

    bundle_data->num_cross_sections = 1;
    bundle_data->cross_sections     = (tag_t *)UF_allocate_memory( sizeof(tag_t),
                                                          &error );
    create_cross( bundle_diameter, &bundle_data->cross_sections[0] );

    UF_terminate();
    return;
}

#ifdef __cplusplus
}
#endif
