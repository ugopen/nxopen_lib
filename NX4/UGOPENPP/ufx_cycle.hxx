/*
================================================================================

          Copyright (c) 1998 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    This file contains the declaration for the Cycle example class.
    To link the internal UG/Open++ version you must link together:
        ufx_cycle_internal.cxx
        ufx_cycle.cxx
        libopenpp.<so sl lib>

    To link the external UG/Open++ version you must link together:
        ufx_cycle_external.cxx
        ufx_cycle.cxx
        libopenpp.<so sl lib>

================================================================================

*/

#ifndef UFX_CYCLE_INCLUDED
#define UFX_CYCLE_INCLUDED

#if defined ( _MSC_VER )

#   if defined ( IMPL_CYCLE )
        // export UG/Open++ classes from their implementation
#       define CLASS_DECL_CYCLE __declspec ( dllexport )
        // define templates at the implementation
#       define TEMPLATE_DECL_CYCLE
#   else
        // import UG/Open++ classes from their implementation
#       define CLASS_DECL_CYCLE __declspec ( dllimport )
        // use templates from the implementation
#       define TEMPLATE_DECL_CYCLE extern
#   endif

#else

#   define CLASS_DECL_CYCLE
#   define TEMPLATE_DECL_CYCLE

#endif

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgPart;

// The Cycle class includes the code that is used by both the internal 
// (ufx_cycle_internal.cxx) and external (ufx_cycle_external.cxx) 
// versions of the "Cycle the Data Model" program. The member functions
// report on the part file history, the part attributes, the customer
// defined area and description and the part status. Also, the objects
// in the part are cycled and their status (alive, condemned, displayable)
// and layer settings are reported.
class CLASS_DECL_CYCLE Cycle {
   
    public:

        // Construct a Cycle object
        Cycle ( );  

        // Destroy a Cycle object
        ~Cycle ( );

        // Prints the part report to the info window.
        static void askPartReport 
        ( 
            const UgPart *part  // <I>
                                // The part to generate the report on.
        );

    private:

        // Prints the part history report to the info window.
        static void askHistoryReport
        ( 
            const UgPart *part  // <I>
                                // The part to generate the report on.
        );

        // Prints the part attribute report to the info window.
        static void askAttributeReport
        ( 
            const UgPart *part  // <I>
                                // The part to generate the report on.
        );

        // Prints the part status, customer area and description report to the info window.
        static void askCustomerReport
        ( 
            const UgPart *part  // <I>
                                // The part to generate the report on.
        );

        // Prints the part object report by type and by layer to the info window.
        static void askObjectReport        
        ( 
            const UgPart *part  // <I>
                                // The part to generate the report on.
        );

};

#endif  // UFX_CYCLE_INCLUDED
