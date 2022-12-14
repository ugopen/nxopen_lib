#ifndef NXOpen_CAM_INSPECTIONREFERENCEFEATUREMODEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONREFERENCEFEATUREMODEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionReferenceFeatureModeBuilder.ja
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
#include <NXOpen/CAM_InspectionMethodBuilder.hxx>
#include <NXOpen/CAM_InheritableBuilder.hxx>
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
        class InspectionReferenceFeatureModeBuilder;
    }
    namespace CAM
    {
        class InheritableBuilder;
    }
    namespace CAM
    {
        class _InspectionReferenceFeatureModeBuilderBuilder;
        class InspectionReferenceFeatureModeBuilderImpl;
        /** Represents a builder for an inheritable reference feature mode enum value 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionReferenceFeatureModeBuilder : public NXOpen::CAM::InheritableBuilder
        {
            private: InspectionReferenceFeatureModeBuilderImpl * m_inspectionreferencefeaturemodebuilder_impl;
            private: friend class  _InspectionReferenceFeatureModeBuilderBuilder;
            protected: InspectionReferenceFeatureModeBuilder();
            public: ~InspectionReferenceFeatureModeBuilder();
            /**Returns  the current reference feature mode 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionMethodBuilder::ReferenceFeatureModeTypes Value
            (
            );
            /**Sets  the current reference feature mode 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetValue
            (
                NXOpen::CAM::InspectionMethodBuilder::ReferenceFeatureModeTypes itemValue /** the new reference feature mode */
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
