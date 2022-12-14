#ifndef NXOpen_MOTION_JOINTFRICTIONADAMS_HXX_INCLUDED
#define NXOpen_MOTION_JOINTFRICTIONADAMS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_JointFrictionAdams.ja
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
#include <NXOpen/TaggedObject.hxx>
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
        class JointFrictionAdams;
    }
    class Expression;
    namespace Motion
    {
        class _JointFrictionAdamsBuilder;
        class JointFrictionAdamsImpl;
        /** Represents a adams joint friction object 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  JointFrictionAdams : public NXOpen::TaggedObject
        {
            /** Joint friction effect */
            public: enum FrictionEffect
            {
                FrictionEffectAll/** all */ ,
                FrictionEffectStiction/** stiction */ ,
                FrictionEffectSliding/** sliding */ 
            };

            /** Joint friction yoke type */
            public: enum FrictionYokeType
            {
                FrictionYokeTypeI/** i */ ,
                FrictionYokeTypeJ/** j */ 
            };

            /** Joint friction overlap_delta */
            public: enum FrictionOverlapDelta
            {
                FrictionOverlapDeltaConstant/** constant */ ,
                FrictionOverlapDeltaIncrease/** increase */ ,
                FrictionOverlapDeltaDecrease/** decrease */ 
            };

            private: JointFrictionAdamsImpl * m_jointfrictionadams_impl;
            private: friend class  _JointFrictionAdamsBuilder;
            protected: JointFrictionAdams();
            public: ~JointFrictionAdams();
            /**Returns  the mu static 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::MuStaticExpression Motion::JointFrictionAdams::MuStaticExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::MuStaticExpression to query or edit it.") double MuStatic
            (
            );
            /**Sets  the mu static 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::MuStaticExpression Motion::JointFrictionAdams::MuStaticExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::MuStaticExpression to query or edit it.") void SetMuStatic
            (
                double muStatic /** mu static */ 
            );
            /**Returns  the mu dynamic 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::MuDynamicExpression Motion::JointFrictionAdams::MuDynamicExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::MuDynamicExpression to query or edit it.") double MuDynamic
            (
            );
            /**Sets  the mu dynamic 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::MuDynamicExpression Motion::JointFrictionAdams::MuDynamicExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::MuDynamicExpression to query or edit it.") void SetMuDynamic
            (
                double muDynamic /** mu dynamic */ 
            );
            /**Returns  the stiction transition velocity 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::StictionTransitionVelocityExpression Motion::JointFrictionAdams::StictionTransitionVelocityExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::StictionTransitionVelocityExpression to query or edit it.") double StictionTransitionVelocity
            (
            );
            /**Sets  the stiction transition velocity 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::StictionTransitionVelocityExpression Motion::JointFrictionAdams::StictionTransitionVelocityExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::StictionTransitionVelocityExpression to query or edit it.") void SetStictionTransitionVelocity
            (
                double stictionTransitionVelocity /** stiction transition velocity */ 
            );
            /**Returns  the max stiction deformation 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::MaxStictionDeformationExpression Motion::JointFrictionAdams::MaxStictionDeformationExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::MaxStictionDeformationExpression to query or edit it.") double MaxStictionDeformation
            (
            );
            /**Sets  the max stiction deformation 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::MaxStictionDeformationExpression Motion::JointFrictionAdams::MaxStictionDeformationExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::MaxStictionDeformationExpression to query or edit it.") void SetMaxStictionDeformation
            (
                double maxStictionDeformation /** max stiction deformation */ 
            );
            /**Returns  the effect 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::JointFrictionAdams::FrictionEffect Effect
            (
            );
            /**Sets  the effect 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetEffect
            (
                NXOpen::Motion::JointFrictionAdams::FrictionEffect effect /** effect */ 
            );
            /**Returns  the preload 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool Preload
            (
            );
            /**Sets  the preload 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetPreload
            (
                bool preload /** preload */ 
            );
            /**Returns  the reaction force 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool ReactionForce
            (
            );
            /**Sets  the reaction force 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetReactionForce
            (
                bool reactionForce /** reaction force */ 
            );
            /**Returns  the bend moment 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool BendMoment
            (
            );
            /**Sets  the bend moment 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetBendMoment
            (
                bool bendMoment /** bend moment */ 
            );
            /**Returns  the torsional moment 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool TorsionalMoment
            (
            );
            /**Sets  the torsional moment 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetTorsionalMoment
            (
                bool torsionalMoment /** torsional moment */ 
            );
            /**Returns  the static equ 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool StaticEqu
            (
            );
            /**Sets  the static equ 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStaticEqu
            (
                bool staticEqu /** static equ */ 
            );
            /**Returns  the yoke type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::JointFrictionAdams::FrictionYokeType YokeType
            (
            );
            /**Sets  the yoke type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetYokeType
            (
                NXOpen::Motion::JointFrictionAdams::FrictionYokeType yokeType /** yoke type */ 
            );
            /**Returns  the ball radius 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::BallRadiusExpression Motion::JointFrictionAdams::BallRadiusExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::BallRadiusExpression to query or edit it.") double BallRadius
            (
            );
            /**Sets  the ball radius 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::BallRadiusExpression Motion::JointFrictionAdams::BallRadiusExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::BallRadiusExpression to query or edit it.") void SetBallRadius
            (
                double ballRadius /** ball radius */ 
            );
            /**Returns  the pin radius 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::PinRadiusExpression Motion::JointFrictionAdams::PinRadiusExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::PinRadiusExpression to query or edit it.") double PinRadius
            (
            );
            /**Sets  the pin radius 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::PinRadiusExpression Motion::JointFrictionAdams::PinRadiusExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::PinRadiusExpression to query or edit it.") void SetPinRadius
            (
                double pinRadius /** pin radius */ 
            );
            /**Returns  the bending arm 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::BendingArmExpression Motion::JointFrictionAdams::BendingArmExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::BendingArmExpression to query or edit it.") double BendingArm
            (
            );
            /**Sets  the bending arm 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::BendingArmExpression Motion::JointFrictionAdams::BendingArmExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::BendingArmExpression to query or edit it.") void SetBendingArm
            (
                double bendingArm /** bending arm */ 
            );
            /**Returns  the friction arm 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::FrictionArmExpression Motion::JointFrictionAdams::FrictionArmExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::FrictionArmExpression to query or edit it.") double FrictionArm
            (
            );
            /**Sets  the friction arm 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::FrictionArmExpression Motion::JointFrictionAdams::FrictionArmExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::FrictionArmExpression to query or edit it.") void SetFrictionArm
            (
                double frictionArm /** friction arm */ 
            );
            /**Returns  the reaction arm 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::ReactionArmExpression Motion::JointFrictionAdams::ReactionArmExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::ReactionArmExpression to query or edit it.") double ReactionArm
            (
            );
            /**Sets  the reaction arm 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::ReactionArmExpression Motion::JointFrictionAdams::ReactionArmExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::ReactionArmExpression to query or edit it.") void SetReactionArm
            (
                double reactionArm /** reaction arm */ 
            );
            /**Returns  the initial overlap 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::InitialOverlapExpression Motion::JointFrictionAdams::InitialOverlapExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::InitialOverlapExpression to query or edit it.") double InitialOverlap
            (
            );
            /**Sets  the initial overlap 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::InitialOverlapExpression Motion::JointFrictionAdams::InitialOverlapExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::InitialOverlapExpression to query or edit it.") void SetInitialOverlap
            (
                double initialOverlap /** initial overlap */ 
            );
            /**Returns  the force preload 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::ForcePreloadExpression Motion::JointFrictionAdams::ForcePreloadExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::ForcePreloadExpression to query or edit it.") double ForcePreload
            (
            );
            /**Sets  the force preload 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::ForcePreloadExpression Motion::JointFrictionAdams::ForcePreloadExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::ForcePreloadExpression to query or edit it.") void SetForcePreload
            (
                double forcePreload /** force preload */ 
            );
            /**Returns  the torque preload 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::TorquePreloadExpression Motion::JointFrictionAdams::TorquePreloadExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::TorquePreloadExpression to query or edit it.") double TorquePreload
            (
            );
            /**Sets  the torque preload 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link Motion::JointFrictionAdams::TorquePreloadExpression Motion::JointFrictionAdams::TorquePreloadExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using Motion::JointFrictionAdams::TorquePreloadExpression to query or edit it.") void SetTorquePreload
            (
                double torquePreload /** torque preload */ 
            );
            /**Returns  the overlap delta 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::JointFrictionAdams::FrictionOverlapDelta OverlapDelta
            (
            );
            /**Sets  the overlap delta 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetOverlapDelta
            (
                NXOpen::Motion::JointFrictionAdams::FrictionOverlapDelta overlapDelta /** overlap delta */ 
            );
            /**Returns  the mu static expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MuStaticExpression
            (
            );
            /**Returns  the mu dynamic expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MuDynamicExpression
            (
            );
            /**Returns  the stiction transition velocity expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StictionTransitionVelocityExpression
            (
            );
            /**Returns  the max stiction deformation expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaxStictionDeformationExpression
            (
            );
            /**Returns  the ball radius expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BallRadiusExpression
            (
            );
            /**Returns  the pin radius expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PinRadiusExpression
            (
            );
            /**Returns  the bending arm expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BendingArmExpression
            (
            );
            /**Returns  the friction arm expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * FrictionArmExpression
            (
            );
            /**Returns  the reaction arm expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ReactionArmExpression
            (
            );
            /**Returns  the initial overlap expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * InitialOverlapExpression
            (
            );
            /**Returns  the force preload expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ForcePreloadExpression
            (
            );
            /**Returns  the torque preload expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TorquePreloadExpression
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
