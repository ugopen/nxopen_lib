#ifndef NXOpen_CAE_CONNECTIONS_ISTIFFNESSDYNAMIC_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_ISTIFFNESSDYNAMIC_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_IStiffnessDynamic.ja
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
#include <NXOpen/Fields_ScalarFieldWrapper.hxx>
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
            class IStiffnessDynamic;
        }
    }
    namespace Fields
    {
        class ScalarFieldWrapper;
    }
    class INXObject;
    namespace CAE
    {
        namespace Connections
        {
            /**  @brief  This class represents an Interface to the Stiffness dynamic.  

              
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  IStiffnessDynamic : public virtual NXOpen::INXObject
            {
                public: virtual ~IStiffnessDynamic() {}
                /**Returns  the X stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * XStiffnessDynamic
                (
                ) = 0;
                /**Sets  the X stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetXStiffnessDynamic
                (
                    NXOpen::Fields::ScalarFieldWrapper * bridge /** bridge */ 
                ) = 0;
                /**Returns  the Y stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * YStiffnessDynamic
                (
                ) = 0;
                /**Sets  the Y stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetYStiffnessDynamic
                (
                    NXOpen::Fields::ScalarFieldWrapper * bridge /** bridge */ 
                ) = 0;
                /**Returns  the Z stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * ZStiffnessDynamic
                (
                ) = 0;
                /**Sets  the Z stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetZStiffnessDynamic
                (
                    NXOpen::Fields::ScalarFieldWrapper * bridge /** bridge */ 
                ) = 0;
                /**Returns  the RX stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * RxStiffnessDynamic
                (
                ) = 0;
                /**Sets  the RX stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetRxStiffnessDynamic
                (
                    NXOpen::Fields::ScalarFieldWrapper * bridge /** bridge */ 
                ) = 0;
                /**Returns  the RY stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * RyStiffnessDynamic
                (
                ) = 0;
                /**Sets  the RY stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetRyStiffnessDynamic
                (
                    NXOpen::Fields::ScalarFieldWrapper * bridge /** bridge */ 
                ) = 0;
                /**Returns  the RZ stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * RzStiffnessDynamic
                (
                ) = 0;
                /**Sets  the RZ stiffness dynamic 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetRzStiffnessDynamic
                (
                    NXOpen::Fields::ScalarFieldWrapper * bridge /** bridge */ 
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