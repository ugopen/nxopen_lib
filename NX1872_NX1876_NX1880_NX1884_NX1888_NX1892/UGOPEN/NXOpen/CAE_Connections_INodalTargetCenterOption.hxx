#ifndef NXOpen_CAE_CONNECTIONS_INODALTARGETCENTEROPTION_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_INODALTARGETCENTEROPTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_INodalTargetCenterOption.ja
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
#include <NXOpen/INXObject.hxx>
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
        namespace Connections
        {
            class INodalTargetCenterOption;
        }
    }
    class INXObject;
    namespace CAE
    {
        namespace Connections
        {
            /**  @brief  This class represents an Interface to the Nodal Target Center Option.  

              
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  INodalTargetCenterOption : public virtual NXOpen::INXObject
            {
                public: virtual ~INodalTargetCenterOption() {}
                /**Returns  the flag indicating to use Legs's Center of Gravity 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual bool UseLegsCog
                (
                ) = 0;
                /**Sets  the flag indicating to use Legs's Center of Gravity 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetUseLegsCog
                (
                    bool useLegsCog /** uselegscog */ 
                ) = 0;
            };
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