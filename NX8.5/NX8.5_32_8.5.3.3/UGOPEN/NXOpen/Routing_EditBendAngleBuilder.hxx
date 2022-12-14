#ifndef NXOpen_ROUTING_EDITBENDANGLEBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_EDITBENDANGLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_EditBendAngleBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Routing_EditBendAngleBuilder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class EditBendAngleBuilder;
    }
    class Builder;
    class TaggedObject;
    namespace Routing
    {
        class _EditBendAngleBuilderBuilder;
        class EditBendAngleBuilderImpl;
        /** 
             <br> To create a new instance of this class, use @link Routing::RouteManager::CreateEditBendAngleBuilder  Routing::RouteManager::CreateEditBendAngleBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  EditBendAngleBuilder : public Builder
        {
            private: EditBendAngleBuilderImpl * m_editbendanglebuilder_impl;
            private: friend class  _EditBendAngleBuilderBuilder;
            protected: EditBendAngleBuilder();
            public: ~EditBendAngleBuilder();
            /** Set the Bend RCP to edit. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetRCP
            (
                NXOpen::TaggedObject * bendRcp /** Bend Rcp */
            );
            /** Set the vector the defines the new bend angle.. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void UpdateAngle
            (
                double angle /** The new angle. */
            );
            /** Move all attached geometry as a rigid set. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetMoveAttachedFlag
            (
                bool moveAttached /** Whether or not to move the geometry as a rigid set. */
            );
            /** Swap the free and anchor segments. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SwapAnchorSegment
            (
            );
            /** Returns information about the angle being changed.  @return  Teh angle between the two segments 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: double GetSelectedBendData
            (
                NXOpen::Vector3d* anchorSegDir /** The anchor Segment */,
                NXOpen::Point3d* rcpPos /** The position of the bend rcp */,
                NXOpen::Vector3d* planeNormal /** The normal of the plane the arc lies in. */
            );
            /** Commits the current edit operation. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void CommitCurrentEdit
            (
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
