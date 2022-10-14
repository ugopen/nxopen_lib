#ifndef NXOpen_CAE_CONNECTIONS_KINEMATIC_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_KINEMATIC_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_Kinematic.ja
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
#include <NXOpen/CAE_Connections_IDof.hxx>
#include <NXOpen/CAE_Connections_IDofCombination.hxx>
#include <NXOpen/CAE_Connections_IFriction.hxx>
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
            class Kinematic;
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
            class IDof;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IDofCombination;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IFriction;
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
            class _KinematicBuilder;
            class KinematicImpl;
            /** Kinematic connection. Use this interface to set/get properties and parameters of the Kinematic connection.  
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  Kinematic : public NXOpen::CAE::Connections::IConnection, public virtual NXOpen::CAE::Connections::ICsys, public virtual NXOpen::CAE::Connections::IDof, public virtual NXOpen::CAE::Connections::IDofCombination, public virtual NXOpen::CAE::Connections::IFriction, public virtual NXOpen::CAE::Connections::INodalTargetsContainer, public virtual NXOpen::CAE::Connections::INodalTargetsPairing
            {
                private: KinematicImpl * m_kinematic_impl;
                private: friend class  _KinematicBuilder;
                protected: Kinematic();
                public: ~Kinematic();
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
                /** Get the specified degrees of freedom  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::DofType GetDof
                (
                    NXOpen::CAE::Connections::Dof dof /** dof */ 
                );
                /** Set the specified degrees of freedom  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetDof
                (
                    NXOpen::CAE::Connections::Dof dof /** dof */ ,
                    NXOpen::CAE::Connections::DofType type /** type */ 
                );
                /**Returns  the degrees of freedom combination type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Connections::DofCombination DofCombination
                (
                );
                /**Sets  the degrees of freedom combination type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetDofCombination
                (
                    NXOpen::CAE::Connections::DofCombination type /** type */ 
                );
                /**Returns  the flag indicating whether to use friction parameters or not 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual bool UseFriction
                (
                );
                /**Sets  the flag indicating whether to use friction parameters or not 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: virtual void SetUseFriction
                (
                    bool useFriction /** usefriction */ 
                );
                /**Returns  the friction coefficient 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * FrictionCoefficient
                (
                );
                /**Returns  the tightening force 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * TighteningForce
                (
                );
                /**Returns  the radius characteristic length used by Revolute and Spherical Kinematic 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::Expression * CharacteristicLengthRadius
                (
                );
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