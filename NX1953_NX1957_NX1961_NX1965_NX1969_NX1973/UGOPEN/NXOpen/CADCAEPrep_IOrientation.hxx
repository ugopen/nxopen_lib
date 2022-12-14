#ifndef NXOpen_CADCAEPREP_IORIENTATION_HXX_INCLUDED
#define NXOpen_CADCAEPREP_IORIENTATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CADCAEPrep_IOrientation.ja
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
#include <NXOpen/NXObject.hxx>
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
        class IOrientation;
    }
    class NXObject;
    namespace CADCAEPrep
    {
        class _IOrientationBuilder;
        class IOrientationImpl;
        /** The object containing the information about the IOrientation.  <br> No instance of this base class, use specific children class getters in <ja>CADCAEPrep.IdealizedBeam</ja>  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CADCAEPREPEXPORT  IOrientation : public NXOpen::NXObject
        {
            private: IOrientationImpl * m_iorientation_impl;
            private: friend class  _IOrientationBuilder;
            protected: IOrientation();
            public: ~IOrientation();
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
