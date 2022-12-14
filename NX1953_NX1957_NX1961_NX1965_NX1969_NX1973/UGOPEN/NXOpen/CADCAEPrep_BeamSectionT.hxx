#ifndef NXOpen_CADCAEPREP_BEAMSECTIONT_HXX_INCLUDED
#define NXOpen_CADCAEPREP_BEAMSECTIONT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CADCAEPrep_BeamSectionT.ja
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
        class BeamSectionT;
    }
    namespace CADCAEPrep
    {
        class IBeamSection;
    }
    namespace CADCAEPrep
    {
        class _BeamSectionTBuilder;
        class BeamSectionTImpl;
        /** T sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CADCAEPREPEXPORT  BeamSectionT : public NXOpen::CADCAEPrep::IBeamSection
        {
            private: BeamSectionTImpl * m_beamsectiont_impl;
            private: friend class  _BeamSectionTBuilder;
            protected: BeamSectionT();
            public: ~BeamSectionT();
            /**Returns  the width 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double W
            (
            );
            /**Returns  the height 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double H
            (
            );
            /**Returns  the flange thickness 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double Tf
            (
            );
            /**Returns  the web thickness 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double Tw
            (
            );
            /** Edit the section parameters 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void Edit
            (
                double width /** width */ ,
                double height /** height */ ,
                double flangeThickness /** flangethickness */ ,
                double webThickness /** webthickness */ 
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
