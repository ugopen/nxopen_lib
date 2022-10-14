#ifndef NXOpen_ROUTING_ELECTRICAL_CABLEWAYSLAYOUTVIEW_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_CABLEWAYSLAYOUTVIEW_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_CablewaysLayoutView.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Routing_Electrical_CablewaysLayoutView.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class CablewaysLayoutView;
        }
    }
    class NXObject;
    class Xform;
    namespace Routing
    {
        namespace Electrical
        {
            class _CablewaysLayoutViewBuilder;
            class CablewaysLayoutViewImpl;
            /** Represents the CablewaysLayoutView class.  <br> No creator as of now <br> */
            class NXOPENCPPEXPORT  CablewaysLayoutView : public NXObject
            {
                private: CablewaysLayoutViewImpl * m_cablewayslayoutview_impl;
                private: friend class  _CablewaysLayoutViewBuilder;
                protected: CablewaysLayoutView();
                public: ~CablewaysLayoutView();
                /** Condemns the layout view entities.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void CondemnLayoutViewEntities
                (
                );
                /**  Uncondemns the layout view entities.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void UncondemnLayoutViewEntities
                (
                );
                /**  Positions the layout view in the 3D space as per input orientation matrix and origin.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void PositionLayoutView
                (
                    const NXOpen::Matrix3x3 & orientation /** orientation */ ,
                    const NXOpen::Point3d & origin /** origin */ 
                );
                /**  Positions the layout view in the 3D space as per the @link Xform Xform@endlink .  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void PositionLayoutView
                (
                    NXOpen::Xform * toOrientation /** toorientation */ 
                );
                /** Flips the layout view along view direction.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void FlipView
                (
                );
                /** Returns the view direction.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: bool GetViewDirection
                (
                );
                /** Highlights the layout view.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void HighlightView
                (
                );
                /** Unhighlights the layout view.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void UnhighlightView
                (
                );
                /** Returns the orientation matrix and origin associated with the layout view.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void GetViewMatrixAndOrigin
                (
                    NXOpen::Matrix3x3* orientation /** orientation */ ,
                    NXOpen::Point3d* origin /** origin */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif