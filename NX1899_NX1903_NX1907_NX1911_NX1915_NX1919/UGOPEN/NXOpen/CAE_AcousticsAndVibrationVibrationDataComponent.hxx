#ifndef NXOpen_CAE_ACOUSTICSANDVIBRATIONVIBRATIONDATACOMPONENT_HXX_INCLUDED
#define NXOpen_CAE_ACOUSTICSANDVIBRATIONVIBRATIONDATACOMPONENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AcousticsAndVibrationVibrationDataComponent.ja
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
#include <NXOpen/CAE_IPostScenarioDataSource.hxx>
#include <NXOpen/NXObject.hxx>
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
        class AcousticsAndVibrationVibrationDataComponent;
    }
    namespace CAE
    {
        class IPostScenarioDataSource;
    }
    class NXObject;
    namespace CAE
    {
        class _AcousticsAndVibrationVibrationDataComponentBuilder;
        class AcousticsAndVibrationVibrationDataComponentImpl;
        /** Represents a @link NXOpen::CAE::AcousticsAndVibrationVibrationDataComponent NXOpen::CAE::AcousticsAndVibrationVibrationDataComponent@endlink . 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AcousticsAndVibrationVibrationDataComponent : public NXOpen::NXObject, public virtual NXOpen::CAE::IPostScenarioDataSource
        {
            private: AcousticsAndVibrationVibrationDataComponentImpl * m_acousticsandvibrationvibrationdatacomponent_impl;
            private: friend class  _AcousticsAndVibrationVibrationDataComponentBuilder;
            protected: AcousticsAndVibrationVibrationDataComponent();
            public: ~AcousticsAndVibrationVibrationDataComponent();
            /** Create selection recipes based on the nodes existing in the file that match the component selections 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void CreateSelectionRecipes
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