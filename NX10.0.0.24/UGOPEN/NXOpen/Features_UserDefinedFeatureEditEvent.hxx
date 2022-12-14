#ifndef NXOpen_FEATURES_USERDEFINEDFEATUREEDITEVENT_HXX_INCLUDED
#define NXOpen_FEATURES_USERDEFINEDFEATUREEDITEVENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_UserDefinedFeatureEditEvent.ja
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
        class UserDefinedFeatureEditEvent;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _UserDefinedFeatureEditEventBuilder;
        class UserDefinedFeatureEditEventImpl;
        /** JA interface for the UserDefinedFeatureEditEvent object  <br> This calls cannot be created  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  UserDefinedFeatureEditEvent : public NXOpen::TaggedObject
        {
            private: UserDefinedFeatureEditEventImpl * m_userdefinedfeatureeditevent_impl;
            private: friend class  _UserDefinedFeatureEditEventBuilder;
            protected: UserDefinedFeatureEditEvent();
            public: ~UserDefinedFeatureEditEvent();
            /**Returns  the related UDF 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::Feature * Feature
            (
            );
            /**Returns  the response 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: int Response
            (
            );
            /**Sets  the response 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetResponse
            (
                int response /** response */ 
            );
            /**Returns  the class name 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ClassName
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
