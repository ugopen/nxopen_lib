#ifndef NXOpen_ANNOTATIONS_INTERSECTIONSYMBOLBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_INTERSECTIONSYMBOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_IntersectionSymbolBuilder.ja
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
#include <NXOpen/Annotations_IntersectionSymbolBuilder.hxx>
#include <NXOpen/Annotations_BaseSymbolBuilder.hxx>
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
        class IntersectionSymbolBuilder;
    }
    namespace Annotations
    {
        class BaseSymbolBuilder;
    }
    class NXColor;
    class SelectNXObject;
    namespace Annotations
    {
        class _IntersectionSymbolBuilderBuilder;
        class IntersectionSymbolBuilderImpl;
        /** Represents a @link NXOpen::Annotations::IntersectionSymbol NXOpen::Annotations::IntersectionSymbol@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::IntersectionSymbolCollection::CreateIntersectionSymbolBuilder  NXOpen::Annotations::IntersectionSymbolCollection::CreateIntersectionSymbolBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Extension </td> <td> 
         
        3 </td> </tr> 

        <tr><td> 
         
        Width </td> <td> 
         
        Thin </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  IntersectionSymbolBuilder : public NXOpen::Annotations::BaseSymbolBuilder
        {
            /** the types of intersection symbol thickness */
            public: enum Thickness
            {
                ThicknessThin/** Thin */,
                ThicknessNormal/** Normal */,
                ThicknessThick/** Thick  */,
                ThicknessOne/** Width One */ = 6,
                ThicknessTwo/** Width Two */,
                ThicknessThree/** Width Three */,
                ThicknessFour/** Width Four */,
                ThicknessFive/** Width Five */,
                ThicknessSix/** Width Six */,
                ThicknessSeven/** Width Seven */,
                ThicknessEight/** Width Eight */,
                ThicknessNine/** Width Nine */
            };

            private: IntersectionSymbolBuilderImpl * m_intersectionsymbolbuilder_impl;
            private: friend class  _IntersectionSymbolBuilderBuilder;
            protected: IntersectionSymbolBuilder();
            public: ~IntersectionSymbolBuilder();
            /**Returns  the intersection object1 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * IntersectionObject1
            (
            );
            /**Returns  the intersection object2 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * IntersectionObject2
            (
            );
            /**Returns  the extension 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double Extension
            (
            );
            /**Sets  the extension 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetExtension
            (
                double extension /** extension */ 
            );
            /**Returns  the inherit 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * Inherit
            (
            );
            /**Returns  the color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * Color
            (
            );
            /**Sets  the color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetColor
            (
                NXOpen::NXColor * color /** color */ 
            );
            /**Returns  the width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::IntersectionSymbolBuilder::Thickness Width
            (
            );
            /**Sets  the width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetWidth
            (
                NXOpen::Annotations::IntersectionSymbolBuilder::Thickness width /** width */ 
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
