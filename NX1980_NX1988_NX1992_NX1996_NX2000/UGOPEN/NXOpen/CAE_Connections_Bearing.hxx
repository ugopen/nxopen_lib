#ifndef NXOpen_CAE_CONNECTIONS_BEARING_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_BEARING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_Bearing.ja
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
#include <NXOpen/CAE_Connections_NodalTarget.hxx>
#include <NXOpen/CAE_Connections_Types.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/CAE_Connections_IConnection.hxx>
#include <NXOpen/CAE_Connections_ICsys.hxx>
#include <NXOpen/CAE_Connections_INodalTargetsContainer.hxx>
#include <NXOpen/CAE_Connections_INodalTargetsPairing.hxx>
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
            class Bearing;
        }
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace CAE
    {
        namespace Connections
        {
            class IConnection;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class ICsys;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class INodalTargetsContainer;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class INodalTargetsPairing;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class NodalTarget;
        }
    }
    class CoordinateSystem;
    class Direction;
    class Expression;
    class INXObject;
    namespace CAE
    {
        namespace Connections
        {
            class _BearingBuilder;
            class BearingImpl;
            /** Bearing connection. Use this interface to set/get properties and parameters of the Bearing connection.  
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  Bearing : public NXOpen::CAE::Connections::IConnection, public virtual NXOpen::CAE::Connections::INodalTargetsContainer, public virtual NXOpen::CAE::Connections::INodalTargetsPairing, public virtual NXOpen::CAE::Connections::ICsys
            {
                private: BearingImpl * m_bearing_impl;
                private: friend class  _BearingBuilder;
                protected: Bearing();
                public: ~Bearing();
                /** Set the target type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetTargetType
                (
                    int index /** index */ ,
                    NXOpen::CAE::Connections::NodalTargetType type /** type */ 
                );
                /** Get target 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::NodalTarget * GetTarget
                (
                    int index /** index */ 
                );
                /**Returns  the pairing method of targets 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::NodalPairingMethod PairingMethod
                (
                );
                /**Sets  the pairing method of targets 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetPairingMethod
                (
                    NXOpen::CAE::Connections::NodalPairingMethod method /** method */ 
                );
                /**Returns  the pairing search orientation 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Direction * SearchOrientation
                (
                );
                /**Sets  the pairing search orientation 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetSearchOrientation
                (
                    NXOpen::Direction * orientation /** orientation */ 
                );
                /**Returns  the search cone angle 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * SearchConeAngle
                (
                );
                /**Returns  the search range 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * SearchRange
                (
                );
                /**Returns  the csys type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::CsysType CsysType
                (
                );
                /**Sets  the csys type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetCsysType
                (
                    NXOpen::CAE::Connections::CsysType csysType /** csystype */ 
                );
                /**Returns  the csys 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CoordinateSystem * Csys
                (
                );
                /**Sets  the csys 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetCsys
                (
                    NXOpen::CoordinateSystem * csys /** csys */ 
                );
                /** Gets supported csys types of connection.  @return  Supported CSys Types 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::CAE::Connections::CsysType> GetSupportedCsysTypes
                (
                );
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