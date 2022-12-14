#ifndef NXOpen_CADCAEPREP_BEAMSECTIONTUBE_HXX_INCLUDED
#define NXOpen_CADCAEPREP_BEAMSECTIONTUBE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CADCAEPrep_BeamSectionTube.ja
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
#include <NXOpen/CADCAEPrep_IBeamSection.hxx>
#include <NXOpen/libnxopencpp_cadcaeprep_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CADCAEPrep
    {
        class BeamSectionTube;
    }
    namespace CADCAEPrep
    {
        class IBeamSection;
    }
    namespace CADCAEPrep
    {
        class _BeamSectionTubeBuilder;
        class BeamSectionTubeImpl;
        /** Tube sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CADCAEPREPEXPORT  BeamSectionTube : public NXOpen::CADCAEPrep::IBeamSection
        {
            private: BeamSectionTubeImpl * m_beamsectiontube_impl;
            private: friend class  _BeamSectionTubeBuilder;
            protected: BeamSectionTube();
            public: ~BeamSectionTube();
            /**Returns  the outside radius 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double Ro
            (
            );
            /**Returns  the inside radius 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double Ri
            (
            );
            /** Edit the section parameters 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void Edit
            (
                double radiusOutside /** radiusoutside */ ,
                double radiusInside /** radiusinside */ 
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
