#ifndef NXOpen_ANNOTATIONS_FRAMEBARBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_FRAMEBARBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_FrameBarBuilder.ja
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
#include <NXOpen/Annotations_BaseFrameBarBuilder.hxx>
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
        class FrameBarBuilder;
    }
    namespace Annotations
    {
        class BaseFrameBarBuilder;
    }
    namespace Annotations
    {
        class _FrameBarBuilderBuilder;
        class FrameBarBuilderImpl;
        /**
            Represents a @link Annotations::FrameBarBuilder Annotations::FrameBarBuilder@endlink .
            This class allows to create frame bar annotation
             <br> To create a new instance of this class, use @link Annotations::FrameBarCollection::CreateFrameBarBuilder  Annotations::FrameBarCollection::CreateFrameBarBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AftPerpendicular </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Axis </td> <td> 
         
        X </td> </tr> 

        <tr><td> 
         
        Baseline </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        BulkHeads </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Centerline </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Decks </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ForwardPerpendicular </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        InterTransverseFrames </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        LongitudinalYFrames </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        LongitudinalZFrames </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        TransveralInsertArea </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        TransverseFrames </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Waterline </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  FrameBarBuilder : public Annotations::BaseFrameBarBuilder
        {
            private: FrameBarBuilderImpl * m_framebarbuilder_impl;
            private: friend class  _FrameBarBuilderBuilder;
            protected: FrameBarBuilder();
            public: ~FrameBarBuilder();
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
