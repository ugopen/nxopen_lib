#ifndef NXOpen_CAE_LAMINATEMATORIENTATION_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEMATORIENTATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateMatOrientation.ja
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
        class LaminateMatOrientation;
    }
    class NXObject;
    namespace CAE
    {
        class _LaminateMatOrientationBuilder;
        class LaminateMatOrientationImpl;
        /** Laminate Material Orientation  <br> To create or edit an instance of this class, use @link NXOpen::CAE::LaminateMatOrientationBuilder  NXOpen::CAE::LaminateMatOrientationBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LaminateMatOrientation : public NXOpen::NXObject
        {
            private: LaminateMatOrientationImpl * m_laminatematorientation_impl;
            private: friend class  _LaminateMatOrientationBuilder;
            protected: LaminateMatOrientation();
            public: ~LaminateMatOrientation();
            /**Returns  the name of the material orientation 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name of the material orientation 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetName
            (
                const NXString & name /** the material orientation name */
            );
            /**Sets  the name of the material orientation 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            void SetName
            (
                const char * name /** the material orientation name */
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
