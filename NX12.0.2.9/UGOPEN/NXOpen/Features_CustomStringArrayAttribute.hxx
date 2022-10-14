#ifndef NXOpen_FEATURES_CUSTOMSTRINGARRAYATTRIBUTE_HXX_INCLUDED
#define NXOpen_FEATURES_CUSTOMSTRINGARRAYATTRIBUTE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CustomStringArrayAttribute.ja
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
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class CustomStringArrayAttribute;
    }
    namespace Features
    {
        class CustomAttribute;
    }
    namespace Features
    {
    }
    namespace Features
    {
        class CustomStringArrayAttributeImpl;
        /**
               Represents a @link Features::CustomStringArrayAttribute Features::CustomStringArrayAttribute@endlink  class
             <br> An instance of this class can be obtained from @link NXOpen::Features::CustomAttributeCollection::CreateCustomStringArrayAttribute NXOpen::Features::CustomAttributeCollection::CreateCustomStringArrayAttribute@endlink   <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  CustomStringArrayAttribute : public NXOpen::Features::CustomAttribute
        {
            private: CustomStringArrayAttributeImpl * m_customstringarrayattribute_impl;
            /// \cond NX_NO_DOC 
            public: explicit CustomStringArrayAttribute(void *ptr);
            /// \endcond 
            /** Set the String values in the attribute
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetValues
            (
                std::vector<NXString> & stringValues /** stringvalues */ 
            );
            /** Get the String values in the attribute @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXString> GetValues
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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