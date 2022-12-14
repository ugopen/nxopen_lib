#ifndef NXOpen_CAM_WEDMARCOUTPUTTYPECIBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WEDMARCOUTPUTTYPECIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WedmArcOutputTypeCiBuilder.ja
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
        class WedmArcOutputTypeCiBuilder;
    }
    namespace CAM
    {
        class _WedmArcOutputTypeCiBuilderBuilder;
        class WedmArcOutputTypeCiBuilderImpl;
        /** Represents a WedmArcOutputTypeCiBuilder 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  WedmArcOutputTypeCiBuilder : public NXOpen::TaggedObject
        {
            /** Available types for output*/
            public: enum OutputTypes
            {
                OutputTypesLinearOnly/** linear only */,
                OutputTypesCirPerpToTaxis/** circular perpendicular to tool axis */,
                OutputTypesSynchronized/** synchronize for pair of moves */
            };

            private: WedmArcOutputTypeCiBuilderImpl * m_wedmarcoutputtypecibuilder_impl;
            private: friend class  _WedmArcOutputTypeCiBuilderBuilder;
            protected: WedmArcOutputTypeCiBuilder();
            public: ~WedmArcOutputTypeCiBuilder();
            /**Returns  the Motion Output Type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::WedmArcOutputTypeCiBuilder::OutputTypes OutputType
            (
            );
            /**Sets  the Motion Output Type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOutputType
            (
                NXOpen::CAM::WedmArcOutputTypeCiBuilder::OutputTypes outputType /** the motion output type */
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
