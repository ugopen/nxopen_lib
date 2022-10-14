#ifndef NXOpen_FEATURES_USERDEFINEDFEATUREAPPLICATIONFIELD_HXX_INCLUDED
#define NXOpen_FEATURES_USERDEFINEDFEATUREAPPLICATIONFIELD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_UserDefinedFeatureApplicationField.ja
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
        class UserDefinedFeatureApplicationField;
    }
    class TaggedObject;
    namespace Features
    {
        class _UserDefinedFeatureApplicationFieldBuilder;
        class UserDefinedFeatureApplicationFieldImpl;
        /** JA interface for UserDefinedFeatureApplicationField object 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  UserDefinedFeatureApplicationField : public TaggedObject
        {
            private: UserDefinedFeatureApplicationFieldImpl * m_userdefinedfeatureapplicationfield_impl;
            private: friend class  _UserDefinedFeatureApplicationFieldBuilder;
            protected: UserDefinedFeatureApplicationField();
            public: ~UserDefinedFeatureApplicationField();
            /**Returns  the name of this field 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /** Gets all of the integers stored in this field  @return  Array of integers in this field 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<int> GetIntegers
            (
            );
            /** Sets all of the integers stored in this field 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetIntegers
            (
                const std::vector<int> & integers /** New Array of integers in this field */
            );
            /** Gets all of the doubles in this field  @return  Array of doubles in this field 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetDoubles
            (
            );
            /** Sets all of the doubles in this field 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDoubles
            (
                const std::vector<double> & doubles /** New Array of doubles in this field */
            );
            /** Gets all of the strings in this field  @return  Array of strings in this field 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetStrings
            (
            );
            /** Sets all of the strings in this field 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStrings
            (
                std::vector<NXString> & strings /** New Array of strings in this field   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets all of the objects in this field  @return  Array of objects in this field 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::TaggedObject *> GetObjects
            (
            );
            /** Sets all of the objects in this field 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetObjects
            (
                const std::vector<NXOpen::TaggedObject *> & objects /** New Array of strings in this field */
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