#ifndef NXOpen_ROUTING_ROUTELOGICALASSOCIATION_HXX_INCLUDED
#define NXOpen_ROUTING_ROUTELOGICALASSOCIATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_RouteLogicalAssociation.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class RouteLogicalAssociation;
    }
    class NXObject;
    namespace Routing
    {
        class _RouteLogicalAssociationBuilder;
        /** RouteLogicalAssociation object associates non-electrical components to 
                electrical components. Logical Associations have control objects and 
                target objects.  Meeting control object's condition applies actions to 
                target objects. Example: Control object is a @link ISegment ISegment@endlink 
                and the target object is a clip or clamp which supports the harness. When
                the segment is routed (i.e. condition on control object is satisfied), 
                the action is to suppress the target (clip or clamp) */
        class NXOPENCPPEXPORT RouteLogicalAssociation : public NXObject
        {
            private: friend class  _RouteLogicalAssociationBuilder;
            protected: RouteLogicalAssociation();
            /** Performs the specified action (suppress or unsuppress) on the 
                        RouteLogicalAssociation Object  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: void Perform
            (
            );
            /** Removes the RouteLogicalAssociation object  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: void Remove
            (
            );
            /** Retrieves the control for LogicalAssocition  @return  Control  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: NXOpen::NXObject * GetControl
            (
            );
            /** Sets the control for LogicalAssocition  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: void SetControl
            (
                NXOpen::NXObject * control /** Control */
            );
            /** Get all the targets LogicalAssocition  @return  Targets of current logical association   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: std::vector<NXOpen::NXObject *> GetTargets
            (
            );
            /** Adds target to Logical Assocition  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: void AddTarget
            (
                NXOpen::NXObject * target /** Target to add */
            );
            /** Removes the target from Logical Assocition  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: void RemoveTarget
            (
                NXOpen::NXObject * target /** Target to remove */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif