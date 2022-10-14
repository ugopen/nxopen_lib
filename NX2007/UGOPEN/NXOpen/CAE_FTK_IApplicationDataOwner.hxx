#ifndef NXOpen_CAE_FTK_IAPPLICATIONDATAOWNER_HXX_INCLUDED
#define NXOpen_CAE_FTK_IAPPLICATIONDATAOWNER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FTK_IApplicationDataOwner.ja
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
        namespace FTK
        {
            class IApplicationDataOwner;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class IApplicationData;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            /** Represents the interface for  application specific data owner
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  IApplicationDataOwner
            {
                virtual void EnsureVtableExists() {}
                public: virtual ~IApplicationDataOwner() {}
                /** Gets the application specific data associated with the record 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::FTK::IApplicationData * GetApplicationData
                (
                ) = 0;
                /** Sets the application specific data to the record 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void SetApplicationData
                (
                    NXOpen::CAE::FTK::IApplicationData * applicationData /** applicationdata */ 
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