#ifndef NXOpen_DISPLAY_IRAYPLUSMATATTRFLOAT2_HXX_INCLUDED
#define NXOpen_DISPLAY_IRAYPLUSMATATTRFLOAT2_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_IrayPlusMatAttrFloat2.ja
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
#include <NXOpen/Display_IrayPlusMatAttr.hxx>
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
        class IrayPlusMatAttrFloat2;
    }
    namespace Display
    {
        class IrayPlusMatAttr;
    }
    namespace Display
    {
        class _IrayPlusMatAttrFloat2Builder;
        class IrayPlusMatAttrFloat2Impl;
        /** Represents a IrayPlus Attribute 
                 <br> This class is restricted to being called from a program running during an 
                Interactive NX session.  If run from a non-interactive session it will 
                return NULL. <br> 
                 <br> IrayPlusMatAttributeFloat2 is not supported in KF.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  IrayPlusMatAttrFloat2 : public NXOpen::Display::IrayPlusMatAttr
        {
            private: IrayPlusMatAttrFloat2Impl * m_irayplusmatattrfloat2_impl;
            private: friend class  _IrayPlusMatAttrFloat2Builder;
            protected: IrayPlusMatAttrFloat2();
            public: ~IrayPlusMatAttrFloat2();
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