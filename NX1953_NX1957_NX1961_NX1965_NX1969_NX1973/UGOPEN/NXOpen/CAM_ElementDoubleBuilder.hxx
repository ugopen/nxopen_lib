#ifndef NXOpen_CAM_ELEMENTDOUBLEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_ELEMENTDOUBLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ElementDoubleBuilder.ja
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
        class ElementDoubleBuilder;
    }
    namespace CAM
    {
        class _ElementDoubleBuilderBuilder;
        class ElementDoubleBuilderImpl;
        /** Represents a builder for an Element double value in of a CAM.CAMObject 
         <br>  Created in NX9.0.3.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ElementDoubleBuilder : public NXOpen::TaggedObject
        {
            private: ElementDoubleBuilderImpl * m_elementdoublebuilder_impl;
            private: friend class  _ElementDoubleBuilderBuilder;
            protected: ElementDoubleBuilder();
            public: ~ElementDoubleBuilder();
            /**Returns  the current value 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: double Value
            (
            );
            /**Sets  the current value 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetValue
            (
                double newValue /** the new value */
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
