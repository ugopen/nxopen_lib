#ifndef NXOpen_FEATURES_CUSTOMDOUBLEATTRIBUTE_HXX_INCLUDED
#define NXOpen_FEATURES_CUSTOMDOUBLEATTRIBUTE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CustomDoubleAttribute.ja
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
        class CustomDoubleAttribute;
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
        class CustomDoubleAttributeImpl;
        /**
               Represents a @link Features::CustomDoubleAttribute Features::CustomDoubleAttribute@endlink  class
             <br> An instance of this class can be obtained from @link NXOpen::Features::CustomAttributeCollection::CreateCustomDoubleAttribute NXOpen::Features::CustomAttributeCollection::CreateCustomDoubleAttribute@endlink   <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  CustomDoubleAttribute : public NXOpen::Features::CustomAttribute
        {
            private: CustomDoubleAttributeImpl * m_customdoubleattribute_impl;
            /// \cond NX_NO_DOC 
            public: explicit CustomDoubleAttribute(void *ptr);
            /// \endcond 
            /**Sets  the value from custom double attribute
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetValue
            (
                double doubleValue /** doublevalue */ 
            );
            /**Returns  the value from custom double attribute
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: double Value
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