#ifndef NXOpen_CAM_DMUSEREXITCIBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DMUSEREXITCIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DmUserExitCiBuilder.ja
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
        class DmUserExitCiBuilder;
    }
    namespace CAM
    {
        class _DmUserExitCiBuilderBuilder;
        class DmUserExitCiBuilderImpl;
        /** Represents a exit name ci Builder 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  DmUserExitCiBuilder : public NXOpen::TaggedObject
        {
            private: DmUserExitCiBuilderImpl * m_dmuserexitcibuilder_impl;
            private: friend class  _DmUserExitCiBuilderBuilder;
            protected: DmUserExitCiBuilder();
            public: ~DmUserExitCiBuilder();
            /**Returns  the Project Type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DmUserExitCi
            (
            );
            /**Sets  the Project Type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDmUserExitCi
            (
                const NXString & dmUserExitCiValue /** the project type value */
            );
            /**Sets  the Project Type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetDmUserExitCi
            (
                const char * dmUserExitCiValue /** the project type value */
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