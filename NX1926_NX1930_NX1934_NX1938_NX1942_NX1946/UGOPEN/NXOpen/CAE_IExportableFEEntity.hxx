#ifndef NXOpen_CAE_IEXPORTABLEFEENTITY_HXX_INCLUDED
#define NXOpen_CAE_IEXPORTABLEFEENTITY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_IExportableFEEntity.ja
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
        class IExportableFEEntity;
    }
    namespace CAE
    {
        /** Represents an EXPORTABLE_FE_ENTITY. 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  IExportableFEEntity
        {
            virtual void EnsureVtableExists() {}
            public: virtual ~IExportableFEEntity() {}
            /** Returns the solver card syntax strings for this entity.  @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: virtual std::vector<NXString> GetSolverCardSyntax
            (
            ) = 0;
        }; //lint !e1712 default constructor not defined for class  

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