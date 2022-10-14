#ifndef NXOpen_CAM_ELEMENTINTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_ELEMENTINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ElementIntBuilder.ja
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
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ElementIntBuilder;
    }
    namespace CAM
    {
        class _ElementIntBuilderBuilder;
        class ElementIntBuilderImpl;
        /** Represents a builder for an Element int value in of a CAM.CAMObject 
         <br>  Created in NX10.0.1.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ElementIntBuilder : public NXOpen::TaggedObject
        {
            private: ElementIntBuilderImpl * m_elementintbuilder_impl;
            private: friend class  _ElementIntBuilderBuilder;
            protected: ElementIntBuilder();
            public: ~ElementIntBuilder();
            /**Returns  the current value 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: int Value
            (
            );
            /**Sets  the current value 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetValue
            (
                int newValue /** the new value */
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