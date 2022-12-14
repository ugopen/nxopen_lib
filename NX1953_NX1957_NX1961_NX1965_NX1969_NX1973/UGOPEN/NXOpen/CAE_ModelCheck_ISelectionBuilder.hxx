#ifndef NXOpen_CAE_MODELCHECK_ISELECTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MODELCHECK_ISELECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelCheck_ISelectionBuilder.ja
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
#include <NXOpen/CAE_ModelCheckDataTypes.hxx>
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
        namespace ModelCheck
        {
            class ISelectionBuilder;
        }
    }
    namespace CAE
    {
        namespace ModelCheck
        {
            /**  @brief  Represents the model check selection builder  

               <br> This is an interface, and cannot be instantiated.  <br> 
             <br>  Created in NX11.0.1.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ISelectionBuilder
            {
                virtual void EnsureVtableExists() {}
                public: virtual ~ISelectionBuilder() {}
                /**Returns  the check scope setting 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::ModelCheck::CheckScope CheckScopeOption
                (
                ) = 0;
                /**Sets  the check scope setting 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: virtual void SetCheckScopeOption
                (
                    NXOpen::CAE::ModelCheck::CheckScope scope /** scope */ 
                ) = 0;
            }; //lint !e1712 default constructor not defined for class  

        }
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
