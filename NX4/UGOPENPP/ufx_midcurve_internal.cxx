/*
================================================================================

          Copyright (c) 1998 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    This file contains the internal Midcurve example program.

================================================================================

*/

// ****************************************************************************
// Include files for needed types
// ****************************************************************************

#include <ufx_midcurve.hxx>

#include <ug_info_window.hxx>
#include <ug_exception.hxx>
#include <ug_session.hxx>

#include <uf_object_types.h>
#include <uf_exit.h>
#include <uf_ui.h> 
#include <uf.h>

#if !defined(__sgi) && ! (defined(__hpux) && !defined(_HP_NAMESPACE_STD)) || defined(__GNUG__)
#   include <strstream>
    using std::ostrstream;
    using std::endl;
    using std::ends;
#else
#   include <strstream.h>
#endif

static const int N_Points = 100;

static bool selectCurves ( tag_t *curve1_tag, tag_t *curve2_tag );

// The entry point for the Internal UG/Open++ application that creates
// selects two curves and creates a MidCurve object based on those
// curves.
extern void ufusr
(
    char *param,            // <I>
                            // Parameters -- unused
    int *retcod,            // <O>
                            // Return code.  Not used by Internal
                            // UG/Open API.
    int param_len           // <I>
                            // Length of param argument.  Unigraphics
                            // handles this input for you.
)
{   
    try
    {
        UgSession midcurve ( true );
        
        for ( bool more = TRUE; more; )
        { 
            tag_t curve1_tag;
            tag_t curve2_tag;
            
            more = selectCurves ( &curve1_tag, &curve2_tag );
            
            if ( more )
            { 
                UgEvaluatableObject *curve1 = dynamic_cast < UgEvaluatableObject * > ( UgObject::find ( curve1_tag ) );
                UgEvaluatableObject *curve2 = dynamic_cast < UgEvaluatableObject * > ( UgObject::find ( curve2_tag ) );
                
                MidCurve *midcurve = MidCurve::create ( N_Points, curve1, curve2, curve1 );
                
                midcurve->setColor ( Yellow );
                
                curve1->unhighlight ( );
                curve2->unhighlight ( );
            } 
            
        }
    }
    catch ( UgException &exception )
    {
        ostrstream buffer;
        
        buffer << endl << "AN ERROR !!!!" << endl;
        buffer << exception.askErrorText ( ).c_str ( ) << endl << endl << ends;
        
        UgInfoWindow::open ( );
        
        UgInfoWindow::write ( buffer.str ( ) ); // freezes 'buffer'
        buffer.rdbuf ( )->freeze ( 0 );         // unfreeze 'buffer'
    }   
}

/*--------------------------------------------------------------------------------------------------------------------------------*/
static bool selectCurves ( tag_t *curve1_tag, tag_t *curve2_tag )
{
    char curve1_cue [ ] = "Select first curve/edge";
    char curve2_cue [ ] = "Select second curve/edge";

    UF_UI_selection_options_t option;

    int    response;
    double cursor [ 3 ];
    tag_t  view_tag;

    UF_UI_mask_t mask [ ] =
    {
        { UF_line_type,   0,                          0                          },
        { UF_circle_type, 0,                          0                          },
        { UF_conic_type,  UF_conic_ellipse_subtype,   0                          },
        { UF_conic_type,  UF_conic_parabola_subtype,  0                          },
        { UF_conic_type,  UF_conic_hyperbola_subtype, 0                          },
        { UF_spline_type, 0,                          0                          },
        { UF_solid_type,  UF_solid_edge_subtype,      UF_UI_SEL_FEATURE_ANY_EDGE }
    };       

    option.other_options    = 0;
    option.reserved         = NULL;
    option.num_mask_triples = sizeof ( mask ) / sizeof ( mask [ 0 ] );
    option.mask_triples     = mask;
    option.scope            = UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY;
    
    UgException::throwOnFailure ( UF_UI_select_single ( curve1_cue, &option, &response, curve1_tag, cursor, &view_tag ) );
    if ( response < 3 ) 
    {
        return false;
    }

    UgException::throwOnFailure ( UF_UI_select_single ( curve2_cue, &option, &response, curve2_tag, cursor, &view_tag ) );
    if ( response < 3 ) 
    {   

        UF_DISP_set_highlight( *curve1_tag, 0 );

        return false;
    }

    return true;
}
