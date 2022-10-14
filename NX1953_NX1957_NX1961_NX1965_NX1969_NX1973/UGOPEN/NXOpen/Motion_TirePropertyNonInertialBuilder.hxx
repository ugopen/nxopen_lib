#ifndef NXOpen_MOTION_TIREPROPERTYNONINERTIALBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_TIREPROPERTYNONINERTIALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_TirePropertyNonInertialBuilder.ja
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
#include <NXOpen/Motion_ExpressionFunctionBuilder.hxx>
#include <NXOpen/Motion_TirePropertyBuilder.hxx>
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
        class TirePropertyNonInertialBuilder;
    }
    class Expression;
    namespace Motion
    {
        class ExpressionFunctionBuilder;
    }
    namespace Motion
    {
        class TirePropertyBuilder;
    }
    namespace Motion
    {
        class _TirePropertyNonInertialBuilderBuilder;
        class TirePropertyNonInertialBuilderImpl;
        /** Represents a builder for a Non-inertial Tire Property  <br> To create a new instance of this class, use @link NXOpen::Motion::TirePropertyNonInertialCollection::CreateTirePropertyNonInertialBuilder  NXOpen::Motion::TirePropertyNonInertialCollection::CreateTirePropertyNonInertialBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AligningMomentArm.Value </term> <description> 
         
        0.0 (millimeters part), 0.0 (inches part) </description> </item> 

        <item><term> 
         
        CorneringStiffness.Value </term> <description> 
         
        1000000.0 (millimeters part), 224808.944 (inches part) </description> </item> 

        <item><term> 
         
        DistributedContact </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FrictionCoefficient.Value </term> <description> 
         
        1.0 (millimeters part), 1.0 (inches part) </description> </item> 

        <item><term> 
         
        NumDivisions.Value </term> <description> 
         
        1 (millimeters part), 1 (inches part) </description> </item> 

        <item><term> 
         
        Radius.Value </term> <description> 
         
        300.0 (millimeters part), 11.811 (inches part) </description> </item> 

        <item><term> 
         
        RollingResistance.Value </term> <description> 
         
        0.0 (millimeters part), 0.0 (inches part) </description> </item> 

        <item><term> 
         
        StaticHold </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        VerticalDamping.Value </term> <description> 
         
        0.0 (millimeters part), 0.0 (inches part) </description> </item> 

        <item><term> 
         
        VerticalStiffness.DataType </term> <description> 
         
        Expression </description> </item> 

        </list> 

         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  TirePropertyNonInertialBuilder : public NXOpen::Motion::TirePropertyBuilder
        {
            private: TirePropertyNonInertialBuilderImpl * m_tirepropertynoninertialbuilder_impl;
            private: friend class  _TirePropertyNonInertialBuilderBuilder;
            protected: TirePropertyNonInertialBuilder();
            public: ~TirePropertyNonInertialBuilder();
            /**Returns  the radius.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * Radius
            (
            );
            /**Returns  the friction coefficient between the tire and road.
                        Should be greater than or equal to zero. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * FrictionCoefficient
            (
            );
            /**Returns  the vertical stiffness.
                        It is specified as an @link ExpressionFunctionBuilder  ExpressionFunctionBuilder @endlink , depening on the type a constant (expression) or a function will be used.
                        It is the tire stiffness normal to the road profile. 
                        Vertical stiffness defines tire normal force as a linear (if a constant is selected) or a non-linear (if a function is selected) function of vertical deflection.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::ExpressionFunctionBuilder * VerticalStiffness
            (
            );
            /**Returns  the vertical damping.
                        It is used in the normal force calculation. 
                        A vertical damping coefficient defines the normal force due to vertical deflection velocity. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * VerticalDamping
            (
            );
            /**Returns  the distributed contact.
                        If true, the Number of Divisions will be exported with a value required to be higher than 1 , otherwise a value of 0 will be exported to the solver. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool DistributedContact
            (
            );
            /**Sets  the distributed contact.
                        If true, the Number of Divisions will be exported with a value required to be higher than 1 , otherwise a value of 0 will be exported to the solver. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDistributedContact
            (
                bool inValue /** invalue */ 
            );
            /**Returns  the number of divisions.
                        When the distributed contact normal force model is to be used, 
                        this variable should be set to the number of vertical "slices" into which the tire is divided.
                        If a simple "point-contact" normal force model is desired, this variable should be set to zero.
                        The distributed contact model should be used when the road profile contains abrupt changes. 
                        NumDivisions should be set high enough so that each "slice" is smaller than the smallest road profile feature. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * NumDivisions
            (
            );
            /**Returns  the rolling resistance coefficient of the tire.
                        It is used to calculate a force as a function of the normal force.
                        This adds to the longitudinal force acting as the tire/road interface. 
                        This represents parasitic longitudinal force due to carcass deformation losses, bearing friction, etc., as a fraction of normal force. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * RollingResistance
            (
            );
            /**Returns  the aligning moment arm.
                        It is produced about the tire vertical axis using this coefficient and the lateral force acting at the tire/road interface.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * AligningMomentArm
            (
            );
            /**Returns  the cornering stiffness constant
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * CorneringStiffness
            (
            );
            /**Returns  the static hold.
                        it controls whether or not the tire should generate holding forces during static or quasistatic analysis.
                        When this parameter is true, the tire will generate the following fictitious forces during static analysis,
                        or during the static phase of STATIC/DYNAMIC analysis (see the System Data and Static elements documentation for more details).
                        First, a torque is applied to the chassis to introduce stiffness for vehicle yaw motion.
                        Finally, forces are applied in the fore-aft and lateral chassis directions in order to prevent equilibrium problems.
                        Disabling these forces may cause the static analysis to fail. If the vehicle is on a flat road,
                        then the fictitious forces will yield a physically meaningful static vehicle position. These forces attempt to keep the tire spin angle, 
                        chassis lateral/longitudinal postion at their initial values. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool StaticHold
            (
            );
            /**Sets  the static hold.
                        it controls whether or not the tire should generate holding forces during static or quasistatic analysis.
                        When this parameter is true, the tire will generate the following fictitious forces during static analysis,
                        or during the static phase of STATIC/DYNAMIC analysis (see the System Data and Static elements documentation for more details).
                        First, a torque is applied to the chassis to introduce stiffness for vehicle yaw motion.
                        Finally, forces are applied in the fore-aft and lateral chassis directions in order to prevent equilibrium problems.
                        Disabling these forces may cause the static analysis to fail. If the vehicle is on a flat road,
                        then the fictitious forces will yield a physically meaningful static vehicle position. These forces attempt to keep the tire spin angle, 
                        chassis lateral/longitudinal postion at their initial values. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStaticHold
            (
                bool inValue /** invalue */ 
            );
            /**Returns  the unique name of the tire property.
                        This must be set after this builder is attached to its owner.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXString Name
            (
            );
            /**Sets  the unique name of the tire property.
                        This must be set after this builder is attached to its owner.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the unique name of the tire property.
                        This must be set after this builder is attached to its owner.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetName
            (
                const char * name /** name */ 
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