#ifndef NXOpen_PREFERENCES_ROUTINGLOGICAL_HXX_INCLUDED
#define NXOpen_PREFERENCES_ROUTINGLOGICAL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_RoutingLogical.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class RoutingLogical;
    }
    namespace Preferences
    {
        class RoutingApplicationView;
    }
    namespace Preferences
    {
        /** The RoutingLogical object stores a set of route logical preferences.  <br> To obtain an instance of this class, refer to @link Preferences::RoutingApplicationView Preferences::RoutingApplicationView@endlink  <br> */
        class NXOPENCPPEXPORT RoutingLogical
        {
            /** How to create terminal segments (if creating terminal segments). */
            public: enum FlowArrowEnumType
            {
                FlowArrowEnumTypeOpen/** Open arrow head on flow arrow. */,
                FlowArrowEnumTypeClosed/** Closed arrow head on flow arrow. */,
                FlowArrowEnumTypeFilled/** Filled arrow head on flow arrow. */
            };

            private: NXOpen::Preferences::RoutingApplicationView* m_owner;
            public: explicit RoutingLogical(NXOpen::Preferences::RoutingApplicationView *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the application view flow arrow type  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingLogical::FlowArrowEnumType FlowArrowType
            (
            );
            /**Sets  the application view flow arrow type  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFlowArrowType
            (
                NXOpen::Preferences::RoutingLogical::FlowArrowEnumType flowArrowType /** flow arrow type */ 
            );
            /**Returns  the application view flow arrow parameter A  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double FlowArrowParameterA
            (
            );
            /**Sets  the application view flow arrow parameter A  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFlowArrowParameterA
            (
                double flowArrowParameterA /** flow arrow parameter a */ 
            );
            /**Returns  the application view flow arrow parameter B  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double FlowArrowParameterB
            (
            );
            /**Sets  the application view flow arrow parameter B  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFlowArrowParameterB
            (
                double flowArrowParameterB /** flow arrow parameter b */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
