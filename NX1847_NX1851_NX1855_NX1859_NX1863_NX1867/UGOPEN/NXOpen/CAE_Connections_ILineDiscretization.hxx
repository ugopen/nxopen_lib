#ifndef NXOpen_CAE_CONNECTIONS_ILINEDISCRETIZATION_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_ILINEDISCRETIZATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_ILineDiscretization.ja
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
#include <NXOpen/CAE_Connections_Types.hxx>
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
            class ILineDiscretization;
        }
    }
    class Expression;
    class INXObject;
    namespace CAE
    {
        namespace Connections
        {
            /**  @brief  This class represents an Interface to the Diameter parameters.  

              
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ILineDiscretization : public virtual NXOpen::INXObject
            {
                public: virtual ~ILineDiscretization() {}
                /**Returns  the usage of original nodes of connection 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual bool UseOriginalNodesOfConnection
                (
                ) = 0;
                /**Sets  the usage of original nodes of connection 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetUseOriginalNodesOfConnection
                (
                    bool use /** use */ 
                ) = 0;
                /**Returns  the usage of max length step 
                 <br>  @deprecated Deprecated in NX1847.0.0.  This functionality is no longer supported. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX1847.0.0.  This functionality is no longer supported.") virtual bool UseMaxLengthStep
                (
                ) = 0;
                /**Sets  the usage of max length step 
                 <br>  @deprecated Deprecated in NX1847.0.0.  This functionality is no longer supported. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NX_DEPRECATED("Deprecated in NX1847.0.0.  This functionality is no longer supported.") virtual void SetUseMaxLengthStep
                (
                    bool use /** use */ 
                ) = 0;
                /**Returns  the line Discretization distance from start 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * DistanceFromStart
                (
                ) = 0;
                /**Returns  the line Discretization distance to end 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * DistanceToEnd
                (
                ) = 0;
                /**Returns  the line Discretization length step 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * LengthStep
                (
                ) = 0;
                /**Returns  the line Discretization max length step 
                 <br>  @deprecated Deprecated in NX1847.0.0.  This functionality is no longer supported. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX1847.0.0.  This functionality is no longer supported.") virtual NXOpen::Expression * MaxLengthStep
                (
                ) = 0;
                /**Returns  the number of connections 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual int NumberOfDiscretizationPoints
                (
                ) = 0;
                /**Sets  the number of connections 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetNumberOfDiscretizationPoints
                (
                    int num /** num */ 
                ) = 0;
                /**Returns  the discretization method 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::DiscretizationMethod DiscretizationMethod
                (
                ) = 0;
                /**Sets  the discretization method 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetDiscretizationMethod
                (
                    NXOpen::CAE::Connections::DiscretizationMethod method /** method */ 
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
