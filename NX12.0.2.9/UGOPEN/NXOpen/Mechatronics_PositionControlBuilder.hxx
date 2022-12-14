#ifndef NXOpen_MECHATRONICS_POSITIONCONTROLBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_POSITIONCONTROLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_PositionControlBuilder.ja
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
#include <NXOpen/Mechatronics_PhysicsConstraintBuilder.hxx>
#include <NXOpen/Mechatronics_PhysicsConstraintBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class PositionControlBuilder;
    }
    class Expression;
    namespace Mechatronics
    {
        class PhysicsConstraintBuilder;
    }
    namespace Mechatronics
    {
        class SelectPhysicsJoint;
    }
    class NXObject;
    class SelectNXObject;
    namespace Mechatronics
    {
        class _PositionControlBuilderBuilder;
        class PositionControlBuilderImpl;
        /** Represents a @link NXOpen::Mechatronics::PositionControlBuilder NXOpen::Mechatronics::PositionControlBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Mechatronics::PositionControlCollection::CreatePositionControlBuilder  NXOpen::Mechatronics::PositionControlCollection::CreatePositionControlBuilder @endlink  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  PositionControlBuilder : public NXOpen::Mechatronics::PhysicsConstraintBuilder
        {
            /** the axis types. */
            public: enum Axis
            {
                AxisAngular/** angular */,
                AxisLinear/** linear */,
                AxisMixed/** Mix angular and linear */
            };

            /** the angular path options. */
            public: enum AngularPathOptions
            {
                AngularPathOptionsFollowShortestPath/** follow shortest path */,
                AngularPathOptionsRotateClockwise/** rotate clockwise */,
                AngularPathOptionsRotateCounterclockwise/** rotate counter-clockwise */,
                AngularPathOptionsTrackMultipleTurns/** track multiple turns */
            };

            private: PositionControlBuilderImpl * m_positioncontrolbuilder_impl;
            private: friend class  _PositionControlBuilderBuilder;
            protected: PositionControlBuilder();
            public: ~PositionControlBuilder();
            /**Returns  the joint select. This can be a @link NXOpen::Mechatronics::HingeJoint NXOpen::Mechatronics::HingeJoint@endlink , @link NXOpen::Mechatronics::SlidingJoint NXOpen::Mechatronics::SlidingJoint@endlink 
                    , @link NXOpen::Mechatronics::CylindricalJoint NXOpen::Mechatronics::CylindricalJoint@endlink  and @link NXOpen::Mechatronics::TransportSurface NXOpen::Mechatronics::TransportSurface@endlink . 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::SelectPhysicsJoint * AxisJoint
            (
            );
            /** Sets the joint. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetAxisJoint
            (
                NXOpen::NXObject * axisJoint /** axis joint */ 
            );
            /**Returns  the axis type. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::PositionControlBuilder::Axis AxisType
            (
            );
            /**Sets  the axis type. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetAxisType
            (
                NXOpen::Mechatronics::PositionControlBuilder::Axis axisType /** axistype */ 
            );
            /**Returns  the angular path. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::PositionControlBuilder::AngularPathOptions AngularPath
            (
            );
            /**Sets  the angular path. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetAngularPath
            (
                NXOpen::Mechatronics::PositionControlBuilder::AngularPathOptions angularPath /** angularpath */ 
            );
            /**Returns  the destination. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Destination
            (
            );
            /**Returns  the speed. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Speed
            (
            );
            /**Returns  the use acceleration flag, which is used to control if the position control includes acceleration data. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseAcceleration
            (
            );
            /**Sets  the use acceleration flag, which is used to control if the position control includes acceleration data. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetUseAcceleration
            (
                bool useAcceleration /** useacceleration */ 
            );
            /**Returns  the max acceleration, which is used to set the maximum acceleration for position control. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaxAcceleration
            (
            );
            /**Returns  the max deceleration, which is used to set the maximum deceleration for position control. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaxDeceleration
            (
            );
            /**Returns  the limit jerk flag, which is used to control if the position control includes jerk data. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool LimitJerk
            (
            );
            /**Sets  the limit jerk flag, which is used to control if the position control includes jerk data. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetLimitJerk
            (
                bool limitJerk /** limitjerk */ 
            );
            /**Returns  the max jerk, which is used to set the maximum jerk for position control. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaxJerk
            (
            );
            /**Returns  whether or not to enable the limit force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool EnableLimitForce
            (
            );
            /**Sets  whether or not to enable the limit force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetEnableLimitForce
            (
                bool enable /** enable */ 
            );
            /**Returns  the max force that speed control can apply. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ForwardForce
            (
            );
            /**Returns  the min force that speed control can apply. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ReverseForce
            (
            );
            /**Returns  the direction type, which works only when the position control is used to
                        drive @link NXOpen::Mechatronics::TransportSurface NXOpen::Mechatronics::TransportSurface@endlink  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::SpeedPositionControlDirectiontype DirectionType
            (
            );
            /**Sets  the direction type, which works only when the position control is used to
                        drive @link NXOpen::Mechatronics::TransportSurface NXOpen::Mechatronics::TransportSurface@endlink  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetDirectionType
            (
                NXOpen::Mechatronics::SpeedPositionControlDirectiontype directionType /** directiontype */ 
            );
            /**Returns  the signal select. This can be a @link NXOpen::Mechatronics::Signal NXOpen::Mechatronics::Signal@endlink 
                        or @link NXOpen::Mechatronics::AdapterSignal NXOpen::Mechatronics::AdapterSignal@endlink .
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::SelectNXObject * Signal
            (
            );
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
