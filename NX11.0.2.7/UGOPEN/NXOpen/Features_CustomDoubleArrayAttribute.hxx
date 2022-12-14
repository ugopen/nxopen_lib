#ifndef NXOpen_FEATURES_CUSTOMDOUBLEARRAYATTRIBUTE_HXX_INCLUDED
#define NXOpen_FEATURES_CUSTOMDOUBLEARRAYATTRIBUTE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CustomDoubleArrayAttribute.ja
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
        class CustomDoubleArrayAttribute;
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
        class CustomDoubleArrayAttributeImpl;
        /**
               Represents a @link Features::CustomDoubleArrayAttribute Features::CustomDoubleArrayAttribute@endlink  class
             <br> An instance of this class can be obtained from @link NXOpen::Features::CustomAttributeCollection::CreateCustomDoubleArrayAttribute NXOpen::Features::CustomAttributeCollection::CreateCustomDoubleArrayAttribute@endlink   <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  CustomDoubleArrayAttribute : public NXOpen::Features::CustomAttribute
        {
            private: CustomDoubleArrayAttributeImpl * m_customdoublearrayattribute_impl;
            /// \cond NX_NO_DOC 
            public: explicit CustomDoubleArrayAttribute(void *ptr);
            /// \endcond 
            /** Set the double values in attribute
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetValues
            (
                const std::vector<double> & doubleValues /** doublevalues */ 
            );
            /** Get the double values in attribute @return  array of doubles
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<double> GetValues
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
