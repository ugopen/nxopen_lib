#ifndef NXOpen_ANNOTATIONS_PMIDATUMTARGETBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIDATUMTARGETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiDatumTargetBuilder.ja
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
#include <NXOpen/Annotations_AssociatedObjectsBuilder.hxx>
#include <NXOpen/Annotations_PmiDatumTargetBuilder.hxx>
#include <NXOpen/Annotations_DatumTargetBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class PmiDatumTargetBuilder;
    }
    namespace Annotations
    {
        class AssociatedObjectsBuilder;
    }
    namespace Annotations
    {
        class DatumTargetBuilder;
    }
    class SelectDisplayableObject;
    namespace Annotations
    {
        class _PmiDatumTargetBuilderBuilder;
        class PmiDatumTargetBuilderImpl;
        /**
            Represents a @link NXOpen::Annotations::PmiDatumTargetBuilder NXOpen::Annotations::PmiDatumTargetBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::Annotations::AnnotationManager::CreatePmiDatumTargetBuilder  NXOpen::Annotations::AnnotationManager::CreatePmiDatumTargetBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Height.Value </td> <td> 
         
        10 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        InnerDiameter.Value </td> <td> 
         
        1 (millimeters part), .1 (inches part) </td> </tr> 

        <tr><td> 
         
        OuterDiameter.Value </td> <td> 
         
        10 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        Width.Value </td> <td> 
         
        10 (millimeters part), 1 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiDatumTargetBuilder : public NXOpen::Annotations::DatumTargetBuilder
        {
            private: PmiDatumTargetBuilderImpl * m_pmidatumtargetbuilder_impl;
            private: friend class  _PmiDatumTargetBuilderBuilder;
            protected: PmiDatumTargetBuilder();
            public: ~PmiDatumTargetBuilder();
            /**Returns  the region selection 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * RegionSelection
            (
            );
            /**Returns  the associated objects 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::AssociatedObjectsBuilder * AssociatedObjects
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