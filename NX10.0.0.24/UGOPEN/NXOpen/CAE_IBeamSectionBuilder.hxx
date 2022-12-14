#ifndef NXOpen_CAE_IBEAMSECTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_IBEAMSECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_IBeamSectionBuilder.ja
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
#include <NXOpen/CAE_IBeamSectionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class IBeamSectionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class PropertyTable;
    }
    namespace CAE
    {
        class _IBeamSectionBuilderBuilder;
        class IBeamSectionBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::IBeamSectionBuilder NXOpen::CAE::IBeamSectionBuilder@endlink 
             <br> This is an abstract class  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  IBeamSectionBuilder : public NXOpen::Builder
        {
            private: IBeamSectionBuilderImpl * m_ibeamsectionbuilder_impl;
            private: friend class  _IBeamSectionBuilderBuilder;
            protected: IBeamSectionBuilder();
            public: ~IBeamSectionBuilder();
            /**Returns  the section builder's @link NXOpen::CAE::PropertyTable NXOpen::CAE::PropertyTable@endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PropertyTable * PropertyTable
            (
            );
            /**Returns  the section name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString SectionName
            (
            );
            /**Sets  the section name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSectionName
            (
                const NXString & sectionName /** sectionname */ 
            );
            /**Sets  the section name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetSectionName
            (
                const char * sectionName /** sectionname */ 
            );
            /** Sets the user-defined stress recovery points. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetUserDefinedStressRecoveryPoints
            (
                const std::vector<NXOpen::Point2d> & points /** points */ 
            );
            /** Gets the user-defined stress recovery points. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void GetUserDefinedStressRecoveryPoints
            (
                std::vector<NXOpen::Point2d> & points /** points */ 
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
