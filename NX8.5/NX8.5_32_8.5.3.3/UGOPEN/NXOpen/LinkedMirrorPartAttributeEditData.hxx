#ifndef NXOpen_LINKEDMIRRORPARTATTRIBUTEEDITDATA_HXX_INCLUDED
#define NXOpen_LINKEDMIRRORPARTATTRIBUTEEDITDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LinkedMirrorPartAttributeEditData.ja
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
#include <NXOpen/TaggedObject.hxx>
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
    class LinkedMirrorPartAttributeEditData;
    class Part;
    class _LinkedMirrorPartAttributeEditDataBuilder;
    class LinkedMirrorPartAttributeEditDataImpl;
    /** JA interface for LinkedMirrorPartAttributeEditData object  <br> This cannot be created  <br> 
     <br>  Created in NX8.5.0.  <br>  
    */
    class NXOPENCPPEXPORT  LinkedMirrorPartAttributeEditData : public TaggedObject
    {
        private: LinkedMirrorPartAttributeEditDataImpl * m_linkedmirrorpartattributeeditdata_impl;
        private: friend class  _LinkedMirrorPartAttributeEditDataBuilder;
        protected: LinkedMirrorPartAttributeEditData();
        public: ~LinkedMirrorPartAttributeEditData();
        /**Returns  the source part 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Part * SourcePart
        (
        );
        /**Returns  the mirror part 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Part * MirrorPart
        (
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
