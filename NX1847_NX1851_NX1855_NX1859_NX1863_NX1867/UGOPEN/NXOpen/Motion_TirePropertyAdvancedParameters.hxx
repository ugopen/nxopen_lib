#ifndef NXOpen_MOTION_TIREPROPERTYADVANCEDPARAMETERS_HXX_INCLUDED
#define NXOpen_MOTION_TIREPROPERTYADVANCEDPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_TirePropertyAdvancedParameters.ja
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
        class TirePropertyAdvancedParameters;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Motion
    {
        class MotionFunction;
    }
    namespace Motion
    {
        class SelectFieldData;
    }
    namespace Motion
    {
        class _TirePropertyAdvancedParametersBuilder;
        class TirePropertyAdvancedParametersImpl;
        /** Represents a TirePropertyAdvancedParameters builder 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  TirePropertyAdvancedParameters : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** the rolling radius type.
                        When 'None' is selected a 0.0 value is exported for the Rolling Radius parameter.
                        'Bias' is used for a bias-ply tire and 'Belted' is for a belted radial tire.
                    */
            public: enum RollingType
            {
                RollingTypeNone/** none */ ,
                RollingTypeBias/** bias */ ,
                RollingTypeBelted/** belted */ 
            };

            /** The block type can be Function when a spline curve is used or
                    Profile when a profile is used.
                    */
            public: enum FrictType
            {
                FrictTypeFunction/** function */ ,
                FrictTypeProfile/** profile */ 
            };

            /** The block type can be Function when a spline curve is used or
                    Profile when a profile is used.
                    */
            public: enum ContactType
            {
                ContactTypeFunction/** function */ ,
                ContactTypeProfile/** profile */ 
            };

            /** the type of surface interaction calculations used.
                         <br> 
                        If type Simple is selected, the longitudinal friction coefficient is a function of the rolling slip only.
                        If type Hard is selected, the longitudinal friction coefficient is a function of the rolling slip,
                        section width, and the surface hardness.
                        If type Soil is selected, the longitudinal friction coefficient is a function of the rolling slip,
                        section width, section height, and the cone index.
                        If FrictCurve (Rolling Slip Friction Curve) is selected, a curve is used to describe the longitudinal friction coefficient
                        as a function of rolling slip (using the friction coefficient parameter from Standard Tire Property).
                        If VelFrictCurve (Rolling Slip Velocity Friction Curve) is selected, a curve is used to describe the longitudinal 
                        friction coefficient as a function of tirepatch rolling slip velocity (using the friction coefficient parameter from the TirePropertyBasicParameters)
                        If FrictSurface or VelFrictSurface are selected, spline surface from data table files are used instead of curves. 
                        In this case an additional contact area curve can be selected.
                        If Soil is selected, the rolling resistance is calculated as part of the longitudinal friction coefficient formula;
                        in all other case, the nominal rolling resistance coefficient (Rolling Resistence variable) is used. <br> */
            public: enum SurfType
            {
                SurfTypeSimple/** simple */ ,
                SurfTypeHard/** hard */ ,
                SurfTypeSoil/** soil */ ,
                SurfTypeVelFrictCurve/** vel frict curve */ ,
                SurfTypeFrictCurve/** frict curve */ ,
                SurfTypeVelFrictSurface/** vel frict surface */ ,
                SurfTypeFrictSurface/** frict surface */ 
            };

            private: TirePropertyAdvancedParametersImpl * m_tirepropertyadvancedparameters_impl;
            private: friend class  _TirePropertyAdvancedParametersBuilder;
            protected: TirePropertyAdvancedParameters();
            public: ~TirePropertyAdvancedParameters();
            /**Returns  the transitional damping deflection.
                         <br> 
                        When non-zero, this value is used to attenuate the normal damping force for small tire deflections.
                        If a value of zero is entered, the nominal damping rate is used.
                        The normal damping rate is found by the formula:
                            CD (1 - e-3d/d0)
                        where:
                        CD is the nominal damping rate (from damping coeff or curve damping), 
                        d is the tire normal deflection,
                        and d0 is the transitional normal damping deflection. <br> 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * TransDampingDeflection
            (
            );
            /**Returns  the distributed contact 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool DistributedContact
            (
            );
            /**Sets  the distributed contact 
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
            /**Returns  the rolling radius of the tire.
                        This value is found by dividing the distance traveled during one rotation by 2 PI.
                        If a value of zero is entered, the deflected radius found in the tire normal force calculation
                        will be used to calculate the tirepatch slip and tire force application point.
                        If a positive value is entered, this value will be used to calculate the tirepatch slip 
                        and tire force application point.
                        If a negative value is entered, this value will be used to calculate the tirepatch slip,
                        but the tire force application point will be at the deflected radius
                        (this formulation simulates a tire with steel non-deformable belt).
                        
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * RollingRadiusValue
            (
            );
            /**Returns  the rolling radius type.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::TirePropertyAdvancedParameters::RollingType RollingRadiusType
            (
            );
            /**Sets  the rolling radius type.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetRollingRadiusType
            (
                NXOpen::Motion::TirePropertyAdvancedParameters::RollingType type /** type */ 
            );
            /**Returns  the surface type.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::TirePropertyAdvancedParameters::SurfType SurfaceType
            (
            );
            /**Sets  the surface type.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSurfaceType
            (
                NXOpen::Motion::TirePropertyAdvancedParameters::SurfType type /** type */ 
            );
            /**Returns  the cone index.
                        This is an index value of the Surface type.
                        For Soil Surface type, this value is the cone index. 
                        For Hard Surface type, this is the rubber hardness. Units are force per length squared.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * ConeIndex
            (
            );
            /**Returns  the section height.
                        This is used by the Soil surface model and is related to unloaded diameter and rim diameter.
                        The section height is also used as the carcass diameter to calculate the lateral offset of the
                        tire patch due to carcass roll. This is used in calculating the roll moment due to lateral offset
                        of the tire patch.        
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * SectionHeight
            (
            );
            /**Returns  the section width.
                        This is used by the Hard and Soil surface models.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * SectionWidth
            (
            );
            /**Returns  the friction function.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::MotionFunction * FrictionFunction
            (
            );
            /**Sets  the friction function.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFrictionFunction
            (
                NXOpen::Motion::MotionFunction * func /** func */ 
            );
            /**Returns  the contact area function.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::MotionFunction * ContactAreaFunction
            (
            );
            /**Sets  the contact area function.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetContactAreaFunction
            (
                NXOpen::Motion::MotionFunction * func /** func */ 
            );
            /**Returns  the friction surface file 
             <br>  @deprecated Deprecated in NX12.0.1.  FrictionSurfaceProfile <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  FrictionSurfaceProfile") NXString FrictionSurfaceFile
            (
            );
            /**Sets  the friction surface file 
             <br>  @deprecated Deprecated in NX12.0.1.  FrictionSurfaceProfile <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  FrictionSurfaceProfile") void SetFrictionSurfaceFile
            (
                const NXString & fileName /** filename */ 
            );
            /**Sets  the friction surface file 
             <br>  @deprecated Deprecated in NX12.0.1.  FrictionSurfaceProfile <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetFrictionSurfaceFile
            (
                const char * fileName /** filename */ 
            );
            /**Returns  the friction surface profile 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::SelectFieldData * FrictionSurfaceProfile
            (
            );
            /**Returns  the aligning moment arm.
                        This parameter is only used in the @link Motion::TirePropertyBasic Motion::TirePropertyBasic@endlink . 
                        It is produced about the tire vertical axis using this coefficient and the lateral force acting at the tire/road interface.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * AligningMomentArm
            (
            );
            /**Returns  the relaxation length.
                        This value, combined with the fore/aft velocity, determines the time constant 
                        of a first-order equation, which is used to attenuate response of the lateral 
                        force and aligning torque. A value of zero results in no lag. If a variable 
                        relaxation length is desired the user can place a user defined equation in the
                        file relaxln.f. This file can be found in the user defined subroutines directory.
                        If a user defined relaxation length is used, then the value in the form-fill should
                        be an approximation of the nominal value. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * RelaxationLength
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
            /**Returns  the friction type.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::TirePropertyAdvancedParameters::FrictType FrictionType
            (
            );
            /**Sets  the friction type.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFrictionType
            (
                NXOpen::Motion::TirePropertyAdvancedParameters::FrictType type /** type */ 
            );
            /**Returns  the friction Profile.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::SelectFieldData * FrictionProfile
            (
            );
            /**Returns  the contact area type.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::TirePropertyAdvancedParameters::ContactType ContactAreaType
            (
            );
            /**Sets  the contact area type.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetContactAreaType
            (
                NXOpen::Motion::TirePropertyAdvancedParameters::ContactType type /** type */ 
            );
            /**Returns  the Contact Area Profile.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::SelectFieldData * ContactAreaProfile
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
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