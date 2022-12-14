#ifndef NXOpen_ANNOTATIONS_DRAFTINGDATUMTARGETBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRAFTINGDATUMTARGETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DraftingDatumTargetBuilder.ja
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
#include <NXOpen/Annotations_DraftingDatumTargetBuilder.hxx>
#include <NXOpen/Annotations_ForeshorteningSymbolBuilder.hxx>
#include <NXOpen/Annotations_DatumTargetBuilder.hxx>
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
        class DraftingDatumTargetBuilder;
    }
    namespace Annotations
    {
        class DatumTargetBuilder;
    }
    namespace Annotations
    {
        class ForeshorteningSymbolBuilder;
    }
    namespace Annotations
    {
        class _DraftingDatumTargetBuilderBuilder;
        class DraftingDatumTargetBuilderImpl;
        /**
            Represents a @link NXOpen::Annotations::DraftingDatumTargetBuilder NXOpen::Annotations::DraftingDatumTargetBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::Annotations::AnnotationManager::CreateDraftingDatumTargetBuilder  NXOpen::Annotations::AnnotationManager::CreateDraftingDatumTargetBuilder @endlink  <br> 
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
         
        10 (millimeters part), .1 (inches part) </td> </tr> 

        <tr><td> 
         
        OuterDiameter.Value </td> <td> 
         
        10 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        Width.Value </td> <td> 
         
        10 (millimeters part), 1 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DraftingDatumTargetBuilder : public NXOpen::Annotations::DatumTargetBuilder
        {
            private: DraftingDatumTargetBuilderImpl * m_draftingdatumtargetbuilder_impl;
            private: friend class  _DraftingDatumTargetBuilderBuilder;
            protected: DraftingDatumTargetBuilder();
            public: ~DraftingDatumTargetBuilder();
            /**Returns  the foreshortening symbol builder 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ForeshorteningSymbolBuilder * ForeshorteningSymbol
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
