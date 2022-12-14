#ifndef NXOpen_CAE_CONNECTIONS_COMMONTYPES_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_COMMONTYPES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_CommonTypes.ja
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
            /** Connection type */
            enum ConnectionType
            {
                ConnectionTypeSpotWeld/** SpotWeld */,
                ConnectionTypeAdhesive/** Adhesive */,
                ConnectionTypeBolt/** Bolt */,
                ConnectionTypeSpring/** Spring */,
                ConnectionTypeRigid/** Rigid */,
                ConnectionTypeBushing/** Bushing */,
                ConnectionTypeDamper/** Damper */,
                ConnectionTypeKinematic/** Kinematic */,
                ConnectionTypeSeamWeld/** Seam Weld */,
                ConnectionTypeSealing/** Sealing */,
                ConnectionTypeRivet/** Rivet */,
                ConnectionTypeLumpedMass/** Lumped Mass */,
                ConnectionTypeClinch/** Clinch */,
                ConnectionTypeCrimp/** Crimp */,
                ConnectionTypeBar/** Bar */,
                ConnectionTypeBearing/** Bearing */
            };

            /** Element type */
            enum ElementType
            {
                ElementTypeNone/** None */,
                ElementTypeEHex8/** Hex8 */,
                ElementTypeEHex8Spider/** Hex8 + Spider */,
                ElementTypeE1d/** 1D */,
                ElementTypeE1DSpider/** 1D + Spider */,
                ElementTypeESpider/** Spider */,
                ElementTypeEBushing/** Bushing Elm */,
                ElementTypeESpring/** Spring Elm */,
                ElementTypeEDamper/** Damper Elm */,
                ElementTypeERigid/** Rigid Elm */,
                ElementTypeEKinematic/** Kinematic Elm */,
                ElementTypeERigidConnector/** Rigid Connector */,
                ElementTypeERigidRigidConnector/** Rigid Connector - Rigid Connector */,
                ElementTypeEInterpolationSpider/** Interpolation + Spider */,
                ElementTypeEMassRigidSpider/** Concentrated Mass + Rigid Spider */,
                ElementTypeEMassInterpolationSpider/** Concentrated Mass + Interpolation Spider */,
                ElementTypeEScalarSpringRigidSpider/** Scalar Spring + Rigid Spider */,
                ElementTypeEScalarSpringRigidInterpolationSpider/** Scalar Spring + Rigid Spider + Interpolation Spider */,
                ElementTypeEJoint/** Joint Elm */,
                ElementTypeEJointInterpolation/** Joint Interpolation */,
                ElementTypeEBeamRigidSpider/** Beam + Rigid Spider */,
                ElementTypeEBar/** Bar + Rigid Spider */,
                ElementTypeEBarInterpolationSpider/** Bar + Interpolation Spider */,
                ElementTypeECbear2Fou3InterpolationSpider/** CBEAR2 + FOU3 + Interpolation Spider */,
                ElementTypeECbear2RigidSpider/** CBear2 + Rbe2 */,
                ElementTypeECbush2RigidSpider/** CBush2 + Rbe2 */,
                ElementTypeEBeamSpider/** Beam Spider */,
                ElementTypeECbush2Fou3InterpolationSpider/** CBUSH2 + FOU3 + Interpolation Spider */,
                ElementTypeEConstrainedJointMPCSpider/** Constrained Joint + MPC Spider */,
                ElementTypeEMassFou3InterpolationSpider/** Concentrated Mass + FOU3 + Interpolation Spider */,
                ElementTypeEFou3InterpolationSpider/** FOU3 + Interpolation Spider */,
                ElementTypeEBeam/** Beam */,
                ElementTypeECWeld/** CWeld */
            };

            /** composer Connection type */
            enum ComposerConnectionType
            {
                ComposerConnectionTypeBolt/** Bolt */,
                ComposerConnectionTypeSpring/** Spring */,
                ComposerConnectionTypeLatch/** Latch */,
                ComposerConnectionTypeBushing/** Bushing */,
                ComposerConnectionTypeBumpStop/** BumpStop */,
                ComposerConnectionTypeKinematic/** Kinematic */,
                ComposerConnectionTypeWeatherStrip/** WeatherStrip */,
                ComposerConnectionTypeSeamWeld/** SeamWeld */,
                ComposerConnectionTypeAdhesive/** Adhesive */,
                ComposerConnectionTypeSpotWeld/** SpotWeld */,
                ComposerConnectionTypeBar/** Bar */
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

#endif
