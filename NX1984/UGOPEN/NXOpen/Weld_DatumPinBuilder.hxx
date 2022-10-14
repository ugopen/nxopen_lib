#ifndef NXOpen_WELD_DATUMPINBUILDER_HXX_INCLUDED
#define NXOpen_WELD_DATUMPINBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_DatumPinBuilder.ja
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
#include <NXOpen/Weld_DatumCommonBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class DatumPinBuilder;
    }
    class ScCollector;
    namespace Weld
    {
        class DatumCommonBuilder;
    }
    namespace Weld
    {
        class SelectDatumPin;
    }
    namespace Weld
    {
        class _DatumPinBuilderBuilder;
        class DatumPinBuilderImpl;
        /** Used to create or edit a @link NXOpen::Weld::DatumPin NXOpen::Weld::DatumPin@endlink  feature.  <br> To create a new instance of this class, use @link NXOpen::Weld::WeldManager::CreateDatumPinBuilder  NXOpen::Weld::WeldManager::CreateDatumPinBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        ControlMethod </term> <description> 
         
        PrincipalAxis </description> </item> 

        <item><term> 
         
        CreateDirectionVector </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        CreatePlane </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        CreatePoint </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        Derived </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DirectionLength </term> <description> 
         
        20 (millimeters part), 1.0 (inches part) </description> </item> 

        <item><term> 
         
        ModelingTolerance </term> <description> 
         
        0.0254 </description> </item> 

        <item><term> 
         
        PlaneHeight </term> <description> 
         
        20 (millimeters part), 1.0 (inches part) </description> </item> 

        <item><term> 
         
        PlaneWidth </term> <description> 
         
        20 (millimeters part), 1.0 (inches part) </description> </item> 

        <item><term> 
         
        PrincipalAxisX </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        PrincipalAxisY </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        PrincipalAxisZ </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  DatumPinBuilder : public NXOpen::Weld::DatumCommonBuilder
        {
            private: DatumPinBuilderImpl * m_datumpinbuilder_impl;
            private: friend class  _DatumPinBuilderBuilder;
            protected: DatumPinBuilder();
            public: ~DatumPinBuilder();
            /**Returns  the resting face 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * BoundaryCurve
            (
            );
            /** Moves a point to the center of a circle or slot boundary 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void MoveToCenter
            (
            );
            /**Returns  the derived datum 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::SelectDatumPin * DerivedDatum
            (
            );
            /** Update the axis origin to the center of the slot or circle, and direction to the normal of the boundary.  If the boundary is not planar an approximate direction will be computed from boundary bounding box. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void InitializeAxis
            (
            );
            /** Updates data related to the axis. The origin will be adjusted based on grid snapping, and projection direction.   In addition the control direction information will be updated.  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void UpdateAxisData
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