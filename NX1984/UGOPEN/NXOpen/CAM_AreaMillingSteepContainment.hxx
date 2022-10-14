#ifndef NXOpen_CAM_AREAMILLINGSTEEPCONTAINMENT_HXX_INCLUDED
#define NXOpen_CAM_AREAMILLINGSTEEPCONTAINMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_AreaMillingSteepContainment.ja
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
#include <NXOpen/CAM_AreaMillingContainment.hxx>
#include <NXOpen/CAM_AreaMillingContainment.hxx>
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
        class AreaMillingSteepContainment;
    }
    namespace CAM
    {
        class AreaMillingContainment;
    }
    namespace CAM
    {
        class StepoverBuilder;
    }
    namespace CAM
    {
        class _AreaMillingSteepContainmentBuilder;
        class AreaMillingSteepContainmentImpl;
        /** Represents a Steep Containment Builder 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  AreaMillingSteepContainment : public NXOpen::CAM::AreaMillingContainment
        {
            /** cut level types 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum CutLevelTypes
            {
                CutLevelTypesConstant/** Constant */,
                CutLevelTypesOptimized/** Optimized */
            };

            private: AreaMillingSteepContainmentImpl * m_areamillingsteepcontainment_impl;
            private: friend class  _AreaMillingSteepContainmentBuilder;
            protected: AreaMillingSteepContainment();
            public: ~AreaMillingSteepContainment();
            /**Returns  the Cut Direction 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::AreaMillingContainment::CutDirectionTypes AreaMillingCutDirection
            (
            );
            /**Sets  the Cut Direction 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAreaMillingCutDirection
            (
                NXOpen::CAM::AreaMillingContainment::CutDirectionTypes areaMillingCutDirection /** the Offset Mode value */
            );
            /**Returns  the cut level type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::AreaMillingSteepContainment::CutLevelTypes CutLevelType
            (
            );
            /**Sets  the cut level type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutLevelType
            (
                NXOpen::CAM::AreaMillingSteepContainment::CutLevelTypes newValue /** the cut level type */
            );
            /**Returns  the builder of area milling depth per cut 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::StepoverBuilder * DepthPerCut
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