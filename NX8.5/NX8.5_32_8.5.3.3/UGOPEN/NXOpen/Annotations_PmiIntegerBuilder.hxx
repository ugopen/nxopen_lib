#ifndef NXOpen_ANNOTATIONS_PMIINTEGERBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIINTEGERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiIntegerBuilder.ja
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
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/Annotations_PmiIntegerBuilder.hxx>
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
        class PmiIntegerBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class _PmiIntegerBuilderBuilder;
        class PmiIntegerBuilderImpl;
        /** Represents a @link Annotations::PmiInteger Annotations::PmiInteger@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreatePmiIntegerBuilder  Annotations::PmiAttributeCollection::CreatePmiIntegerBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        IntegerValue </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiIntegerBuilder : public Annotations::PmiAttributeBuilder
        {
            private: PmiIntegerBuilderImpl * m_pmiintegerbuilder_impl;
            private: friend class  _PmiIntegerBuilderBuilder;
            protected: PmiIntegerBuilder();
            public: ~PmiIntegerBuilder();
            /**Returns  the str title 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the str title 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Sets  the str title 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            void SetTitle
            (
                const char * title /** title */ 
            );
            /**Returns  the int value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: int IntegerValue
            (
            );
            /**Sets  the int value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetIntegerValue
            (
                int integerValue /** integervalue */ 
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
