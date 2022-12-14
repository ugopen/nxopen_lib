#ifndef NXOpen_SAFETY_MODELSYSTEM_HXX_INCLUDED
#define NXOpen_SAFETY_MODELSYSTEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Safety_ModelSystem.ja
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
#include <NXOpen/Safety_Arrangement.hxx>
#include <NXOpen/libsafetyopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Safety
    {
        class ModelSystem;
    }
    class NXObject;
    namespace Safety
    {
        class Arrangement;
    }
    namespace Safety
    {
        class _ModelSystemBuilder;
        class ModelSystemImpl;
        /**  Represents a Safety System.  <br> To create or edit an instance of this class, use @link NXOpen::Safety::ModelSystemBuilder  NXOpen::Safety::ModelSystemBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class SAFETYOPENCPPEXPORT  ModelSystem : public NXOpen::NXObject
        {
            private: ModelSystemImpl * m_modelsystem_impl;
            private: friend class  _ModelSystemBuilder;
            protected: ModelSystem();
            public: ~ModelSystem();
            /** Select arrangement for initial positioning 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetUserArrangement
            (
                NXOpen::Safety::Arrangement * arrangement /** Arrangement to activate. */
            );
            /** Select design arrangement 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDesignArrangement
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
