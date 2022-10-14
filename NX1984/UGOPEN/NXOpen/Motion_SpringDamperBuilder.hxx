#ifndef NXOpen_MOTION_SPRINGDAMPERBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_SPRINGDAMPERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_SpringDamperBuilder.ja
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
#include <NXOpen/Motion_EntityPropTableBuilder.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class SpringDamperBuilder;
    }
    namespace Motion
    {
        class EntityPropTableBuilder;
    }
    namespace Motion
    {
        class _SpringDamperBuilderBuilder;
        class SpringDamperBuilderImpl;
        /** Represents a @link Motion::SpringDamper Motion::SpringDamper@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Motion::SpringDamperCollection::CreateSpringDamperBuilder  NXOpen::Motion::SpringDamperCollection::CreateSpringDamperBuilder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  SpringDamperBuilder : public NXOpen::Motion::EntityPropTableBuilder
        {
            /** Translational SpringDamper types */
            public: enum TranslationalType
            {
                TranslationalTypeMotionBody/** SpringDamper Translational Type MotionBody. Requires an action motion body. Can have a base motion body. */,
                TranslationalTypeSliderJoint/** SpringDamper Translational Type SliderJoint. Requires a Slider Joint as input. */,
                TranslationalTypeCylindricalJoint/** SpringDamper Translational Type CylindricalJoint. Requires a Cylindrical Joint as input. */
            };

            /** Rotational SpringDamper types */
            public: enum RotationalType
            {
                RotationalTypeRevoluteJoint/** SpringDamper Rotational Type RevoluteJoint. Requires a Revolute Joint as input. */,
                RotationalTypeCylindricalJoint/** SpringDamper Rotational Type CylindricalJoint. Requires a Cylindrical Joint as input. */,
                RotationalTypeScrewJoint/** SpringDamper Rotational Type ScrewJoint. Requires a Screw Joint as input. */,
                RotationalTypePlanarJoint/** SpringDamper Rotational Type PlanarJoint. Requires a Planar Joint as input. */
            };

            /** SpringDamper Parameter types */
            public: enum ParameterType
            {
                ParameterTypeExpression/** expression */ ,
                ParameterTypeFunction/** function */ ,
                ParameterTypeProfile2d/** profile2d */ ,
                ParameterTypeProfile3d/** profile3d */ ,
                ParameterTypeExpressionFunction/** expression function */ ,
                ParameterTypeExpressionProfile2d/** expression profile2d */ ,
                ParameterTypeExpressionProfile3d/** expression profile3d */ 
            };

            /** Application direction types */
            public: enum ApplicationDirectionType
            {
                ApplicationDirectionTypeBidirectional/** bidirectional */ ,
                ApplicationDirectionTypeTensionOnly/** tension only */ ,
                ApplicationDirectionTypeCompressionOnly/** compression only */ 
            };

            private: SpringDamperBuilderImpl * m_springdamperbuilder_impl;
            private: friend class  _SpringDamperBuilderBuilder;
            protected: SpringDamperBuilder();
            public: ~SpringDamperBuilder();
        };
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