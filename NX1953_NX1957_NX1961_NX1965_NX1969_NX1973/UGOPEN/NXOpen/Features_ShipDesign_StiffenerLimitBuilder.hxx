#ifndef NXOpen_FEATURES_SHIPDESIGN_STIFFENERLIMITBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_STIFFENERLIMITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_StiffenerLimitBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace ShipDesign
        {
            class StiffenerLimitBuilder;
        }
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class SelectDisplayableObject;
    namespace Features
    {
        namespace ShipDesign
        {
            class _StiffenerLimitBuilderBuilder;
            class StiffenerLimitBuilderImpl;
            /** This class defines the path limit method used by a Stiffener or Edge Reinforcement feature. 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  StiffenerLimitBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                /** Path limiting method */
                public: enum LimitType
                {
                    LimitTypeValue/** Trim or extend by a fixed distance value. */,
                    LimitTypeSquareCut/** Stiffener will extend into limiting geometry. */,
                    LimitTypeNeatTrim/** It will automatically create an End Cut  that trim the stiffener to the selected geometry.*/,
                    LimitTypeBoundary/** boundary */ 
                };

                private: StiffenerLimitBuilderImpl * m_stiffenerlimitbuilder_impl;
                private: friend class  _StiffenerLimitBuilderBuilder;
                protected: StiffenerLimitBuilder();
                public: ~StiffenerLimitBuilder();
                /**Returns  the limit method 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerLimitBuilder::LimitType LimitMethod
                (
                );
                /**Sets  the limit method 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetLimitMethod
                (
                    NXOpen::Features::ShipDesign::StiffenerLimitBuilder::LimitType limitMethod /** limitmethod */ 
                );
                /**Returns  the fixed limiting value 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * LimitValue
                (
                );
                /**Returns  the limit clearance value 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * SquareCutClearance
                (
                );
                /**Returns  the limiting geometry 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectDisplayableObject * LimitGeometry
                (
                );
                /** Validate whether the inputs to the component are sufficient for 
                            commit to be called.  If the component is not in a state to commit
                            then an exception is thrown.  For example, if the component requires
                            you to set some property, this method will throw an exception if
                            you haven't set it.  This method throws a not yet implemented
                            NXException for some components.
                         @return  Was self validation successful 
                 <br>  Created in NX3.0.1.  <br>  
                 <br> License requirements : None */
                public: virtual bool Validate
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
