#ifndef NXOpen_ANNOTATIONS_VEHICLEGRIDBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_VEHICLEGRIDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_VehicleGridBuilder.ja
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
#include <NXOpen/Annotations_BaseVehicleGridBuilder.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class VehicleGridBuilder;
    }
    namespace Annotations
    {
        class BaseVehicleGridBuilder;
    }
    namespace Annotations
    {
        class _VehicleGridBuilderBuilder;
        class VehicleGridBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link NXOpen::Annotations::VehicleGridBuilder NXOpen::Annotations::VehicleGridBuilder@endlink .
            This class allows creation of vehicle grid annotations
             <br> To create a new instance of this class, use @link NXOpen::Annotations::VehicleGridCollection::CreateVehicleGridBuilder  NXOpen::Annotations::VehicleGridCollection::CreateVehicleGridBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        GridSpacing </term> <description> 
         
        100 </description> </item> 

        <item><term> 
         
        HorizontalMaximumValue </term> <description> 
         
        500 </description> </item> 

        <item><term> 
         
        HorizontalMinimumValue </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        ShowHorizontalLines </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        ShowVerticalLines </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        VerticalMaximumValue </term> <description> 
         
        500 </description> </item> 

        <item><term> 
         
        VerticalMinimumValue </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  VehicleGridBuilder : public NXOpen::Annotations::BaseVehicleGridBuilder
        {
            private: VehicleGridBuilderImpl * m_vehiclegridbuilder_impl;
            private: friend class  _VehicleGridBuilderBuilder;
            protected: VehicleGridBuilder();
            public: ~VehicleGridBuilder();
        };

        /// \endcond 
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
