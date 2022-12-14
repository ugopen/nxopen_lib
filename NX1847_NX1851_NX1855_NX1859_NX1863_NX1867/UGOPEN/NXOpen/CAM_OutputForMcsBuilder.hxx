#ifndef NXOpen_CAM_OUTPUTFORMCSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_OUTPUTFORMCSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_OutputForMcsBuilder.ja
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
#include <NXOpen/CAM_MoveBuilder.hxx>
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
        class OutputForMcsBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class _OutputForMcsBuilderBuilder;
        class OutputForMcsBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents output for mcs builder  <br> To create a new instance of this class, use @link NXOpen::CAM::MoveCollection::CreateOutputForMcsBuilder  NXOpen::CAM::MoveCollection::CreateOutputForMcsBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  OutputForMcsBuilder : public NXOpen::CAM::MoveBuilder
        {
            /** the MCS types*/
            public: enum Types
            {
                TypesCurrentOperation/** current operation */,
                TypesPreviousOperation/** previous operation */,
                TypesMainMcs/** main mcs */
            };

            private: OutputForMcsBuilderImpl * m_outputformcsbuilder_impl;
            private: friend class  _OutputForMcsBuilderBuilder;
            protected: OutputForMcsBuilder();
            public: ~OutputForMcsBuilder();
            /**Returns  the MCS 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::OutputForMcsBuilder::Types Mcs
            (
            );
            /**Sets  the MCS 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMcs
            (
                NXOpen::CAM::OutputForMcsBuilder::Types mcs /** mcs */ 
            );
        };

        /// \endcond 
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
