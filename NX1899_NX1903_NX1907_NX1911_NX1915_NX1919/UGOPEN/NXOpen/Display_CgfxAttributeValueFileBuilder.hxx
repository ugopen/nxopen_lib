#ifndef NXOpen_DISPLAY_CGFXATTRIBUTEVALUEFILEBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_CGFXATTRIBUTEVALUEFILEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_CgfxAttributeValueFileBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_display_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Display
    {
        class CgfxAttributeValueFileBuilder;
    }
    class Builder;
    namespace Display
    {
        class _CgfxAttributeValueFileBuilderBuilder;
        class CgfxAttributeValueFileBuilderImpl;
        /** Represents a @link NXOpen::Display::CgfxAttributeValueFileBuilder NXOpen::Display::CgfxAttributeValueFileBuilder@endlink  builder 
             <br> This class is restricted to being called from a program running during an 
            Interactive NX session.  If run from a non-interactive session it will 
            return NULL. <br> 
             <br>   <br> 
         <br>  @deprecated Deprecated in NX10.0.0.  No alternative provided for this class. <br>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NX_DEPRECATED("Deprecated in NX10.0.0.  No alternative provided for this class.") NXOPENCPP_DISPLAYEXPORT  CgfxAttributeValueFileBuilder : public NXOpen::Builder
        {
            private: CgfxAttributeValueFileBuilderImpl * m_cgfxattributevaluefilebuilder_impl;
            private: friend class  _CgfxAttributeValueFileBuilderBuilder;
            protected: CgfxAttributeValueFileBuilder();
            public: ~CgfxAttributeValueFileBuilder();
            /** Gets the CgFX material attribute's file name 
             <br>  @deprecated Deprecated in NX10.0.0.  No alternative provided for this class. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  No alternative provided for this class.") NXString GetFilename
            (
            );
            /** Sets the CgFX material attribute's file name 
             <br>  @deprecated Deprecated in NX10.0.0.  No alternative provided for this class. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  No alternative provided for this class.") void SetFilename
            (
                const NXString & filename /** CgFX file name */
            );
            /** Sets the CgFX material attribute's file name 
             <br>  @deprecated Deprecated in NX10.0.0.  No alternative provided for this class. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetFilename
            (
                const char * filename /** CgFX file name */
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