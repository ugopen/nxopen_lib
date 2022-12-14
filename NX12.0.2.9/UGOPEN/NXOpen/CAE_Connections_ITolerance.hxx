#ifndef NXOpen_CAE_CONNECTIONS_ITOLERANCE_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_ITOLERANCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_ITolerance.ja
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
#include <NXOpen/Expression.hxx>
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
            class ITolerance;
        }
    }
    class Expression;
    class INXObject;
    namespace CAE
    {
        namespace Connections
        {
            /**  @brief  This class represents an Interface to the Tolerance parameters.  

              
             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ITolerance : public virtual NXOpen::INXObject
            {
                public: virtual ~ITolerance() {}
                /**Returns  the maximum distance from definition point to center of support element 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * MaxDistCGToElemCG
                (
                ) = 0;
                /**Returns  the maximum normal distance from definition point to center of element 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * MaxNormalDistCGToFlanges
                (
                ) = 0;
                /**Returns  the maximum angle of normals with the projection surface 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * MaxAngleBetweenNormals
                (
                ) = 0;
                /**Returns  the projection tolerance 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * ProjectTolerance
                (
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
