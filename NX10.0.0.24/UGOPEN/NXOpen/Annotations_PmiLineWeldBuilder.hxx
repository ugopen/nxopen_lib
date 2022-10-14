#ifndef NXOpen_ANNOTATIONS_PMILINEWELDBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMILINEWELDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiLineWeldBuilder.ja
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
#include <NXOpen/Annotations_PmiLineWeldBuilder.hxx>
#include <NXOpen/Annotations_LineWeldBuilder.hxx>
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
        class PmiLineWeldBuilder;
    }
    namespace Annotations
    {
        class AssociatedObjectsBuilder;
    }
    namespace Annotations
    {
        class LineWeldBuilder;
    }
    namespace Annotations
    {
        class _PmiLineWeldBuilderBuilder;
        class PmiLineWeldBuilderImpl;
        /** Represents a @link NXOpen::Annotations::PmiLineWeld NXOpen::Annotations::PmiLineWeld@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::WeldCollection::CreatePmiLineWeldBuilder  NXOpen::Annotations::WeldCollection::CreatePmiLineWeldBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        FieldWeld </td> <td> 
         
        Plain </td> </tr> 

        <tr><td> 
         
        FlipDirection </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        FlipHorizontal </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        FlipVertical </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        IdLine </td> <td> 
         
        Plain </td> </tr> 

        <tr><td> 
         
        Scale </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        StaggeredWeld </td> <td> 
         
        NoStaggeredSymbol </td> </tr> 

        <tr><td> 
         
        Tail </td> <td> 
         
        NoTail </td> </tr> 

        <tr><td> 
         
        WeldAlongContour </td> <td> 
         
        None </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiLineWeldBuilder : public NXOpen::Annotations::LineWeldBuilder
        {
            private: PmiLineWeldBuilderImpl * m_pmilineweldbuilder_impl;
            private: friend class  _PmiLineWeldBuilderBuilder;
            protected: PmiLineWeldBuilder();
            public: ~PmiLineWeldBuilder();
            /**Returns  the @link NXOpen::Annotations::AssociatedObjectsBuilder NXOpen::Annotations::AssociatedObjectsBuilder@endlink   for weld symbol 
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