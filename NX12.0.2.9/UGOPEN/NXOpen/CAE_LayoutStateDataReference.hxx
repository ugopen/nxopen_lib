#ifndef NXOpen_CAE_LAYOUTSTATEDATAREFERENCE_HXX_INCLUDED
#define NXOpen_CAE_LAYOUTSTATEDATAREFERENCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LayoutStateDataReference.ja
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
        class LayoutStateDataReference;
    }
    namespace CAE
    {
        class _LayoutStateDataReferenceBuilder;
        class LayoutStateDataReferenceImpl;
        /**  @brief  This class represents a data reference of a layout state.  

           <br> This class can only be created internally  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LayoutStateDataReference : public NXOpen::TaggedObject
        {
            private: LayoutStateDataReferenceImpl * m_layoutstatedatareference_impl;
            private: friend class  _LayoutStateDataReferenceBuilder;
            protected: LayoutStateDataReference();
            public: ~LayoutStateDataReference();
            /** Overrides the content of the data reference with the specified string 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void OverrideContent
            (
                const NXString & referenceString /** referencestring */ 
            );
            /** Overrides the content of the data reference with the specified string 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void OverrideContent
            (
                const char * referenceString /** referencestring */ 
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
