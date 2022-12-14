#ifndef NXOpen_SKETCHMAKEEQUALBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHMAKEEQUALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchMakeEqualBuilder.ja
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
#include <NXOpen/SketchMakeRelationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SketchMakeEqualBuilder;
    class SketchMakeRelationBuilder;
    class _SketchMakeEqualBuilderBuilder;
    class SketchMakeEqualBuilderImpl;
    /**
        Represents a @link NXOpen::SketchMakeEqualBuilder NXOpen::SketchMakeEqualBuilder@endlink  builder. 
         <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateSketchMakeEqualBuilder  NXOpen::SketchCollection::CreateSketchMakeEqualBuilder @endlink  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchMakeEqualBuilder : public NXOpen::SketchMakeRelationBuilder
    {
        /** equal type */
        public: enum EqualTypes
        {
            EqualTypesRadius/** radius */ ,
            EqualTypesLength/** length */ 
        };

        private: SketchMakeEqualBuilderImpl * m_sketchmakeequalbuilder_impl;
        private: friend class  _SketchMakeEqualBuilderBuilder;
        protected: SketchMakeEqualBuilder();
        public: ~SketchMakeEqualBuilder();
        /**Returns  the equal type as @link NXOpen::SketchMakeEqualBuilder::EqualTypes NXOpen::SketchMakeEqualBuilder::EqualTypes@endlink 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SketchMakeEqualBuilder::EqualTypes EqualType
        (
        );
        /**Sets  the equal type as @link NXOpen::SketchMakeEqualBuilder::EqualTypes NXOpen::SketchMakeEqualBuilder::EqualTypes@endlink 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetEqualType
        (
            NXOpen::SketchMakeEqualBuilder::EqualTypes equalType /** equaltype */ 
        );
    };
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
