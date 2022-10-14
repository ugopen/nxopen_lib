#ifndef NXOpen_CAE_CONNECTIONS_INONLINEARCYLINDRICALDAMPING_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_INONLINEARCYLINDRICALDAMPING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_INonlinearCylindricalDamping.ja
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
            class INonlinearCylindricalDamping;
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
            /**  @brief  This class represents an Interface to the Nonlinear Cylindrical Damping.  

              
             <br>  Created in NX1980.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  INonlinearCylindricalDamping : public virtual NXOpen::INXObject
            {
                public: virtual ~INonlinearCylindricalDamping() {}
                /**Returns  the Z nonlinear cylindrical damping 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * ZNonlinearCylindricalDamping
                (
                ) = 0;
                /**Sets  the Z nonlinear cylindrical damping 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetZNonlinearCylindricalDamping
                (
                    NXOpen::Fields::ScalarFieldWrapper * bridge /** bridge */ 
                ) = 0;
                /**Returns  the R nonlinear cylindrical damping 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * RNonlinearCylindricalDamping
                (
                ) = 0;
                /**Sets  the R nonlinear cylindrical damping 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetRNonlinearCylindricalDamping
                (
                    NXOpen::Fields::ScalarFieldWrapper * bridge /** bridge */ 
                ) = 0;
                /**Returns  the RZ nonlinear cylindrical damping 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * RzNonlinearCylindricalDamping
                (
                ) = 0;
                /**Sets  the RZ nonlinear cylindrical damping 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetRzNonlinearCylindricalDamping
                (
                    NXOpen::Fields::ScalarFieldWrapper * bridge /** bridge */ 
                ) = 0;
                /**Returns  the RR nonlinear cylindrical damping 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Fields::ScalarFieldWrapper * RrNonlinearCylindricalDamping
                (
                ) = 0;
                /**Sets  the RR nonlinear cylindrical damping 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetRrNonlinearCylindricalDamping
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