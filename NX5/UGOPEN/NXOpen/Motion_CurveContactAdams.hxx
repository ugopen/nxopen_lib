#ifndef NXOpen_MOTION_CURVECONTACTADAMS_HXX_INCLUDED
#define NXOpen_MOTION_CURVECONTACTADAMS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_CurveContactAdams.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Motion_CurveContactAdams.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class CurveContactAdams;
    }
    class NXObject;
    namespace Motion
    {
        class _CurveContactAdamsBuilder;
        /** Represents a @link Motion::CurveContactAdams Motion::CurveContactAdams@endlink  */
        class NXOPENCPPEXPORT CurveContactAdams : public NXObject
        {
            private: friend class  _CurveContactAdamsBuilder;
            protected: CurveContactAdams();
            /**Returns  the stiffness  <br> License requirements : None */
            public: double Stiffness
            (
            );
            /**Sets  the stiffness  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStiffness
            (
                double stiffness /** stiffness */ 
            );
            /**Returns  the force exponent  <br> License requirements : None */
            public: double ForceExponent
            (
            );
            /**Sets  the force exponent  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetForceExponent
            (
                double force_exponent /** force exponent */ 
            );
            /**Returns  the material damping  <br> License requirements : None */
            public: double MaterialDamping
            (
            );
            /**Sets  the material damping  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMaterialDamping
            (
                double material_damping /** material damping */ 
            );
            /**Returns  the penetration depth  <br> License requirements : None */
            public: double PenetrationDepth
            (
            );
            /**Sets  the penetration depth  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetPenetrationDepth
            (
                double penetration_depth /** penetration depth */ 
            );
            /**Returns  the static coefficient  <br> License requirements : None */
            public: double StaticCoefficient
            (
            );
            /**Sets  the static coefficient  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStaticCoefficient
            (
                double static_coefficient /** static coefficient */ 
            );
            /**Returns  the slip velocity  <br> License requirements : None */
            public: double SlipVelocity
            (
            );
            /**Sets  the slip velocity  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSlipVelocity
            (
                double slip_velocity /** slip velocity */ 
            );
            /**Returns  the dynamic coefficient  <br> License requirements : None */
            public: double DynamicCoefficient
            (
            );
            /**Sets  the dynamic coefficient  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDynamicCoefficient
            (
                double dynamic_coefficient /** dynamic coefficient */ 
            );
            /**Returns  the transition velocity  <br> License requirements : None */
            public: double TransitionVelocity
            (
            );
            /**Sets  the transition velocity  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetTransitionVelocity
            (
                double transition_velocity /** transition velocity */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif