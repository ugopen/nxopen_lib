#ifndef NXOpen_MECHATRONICS_INVERSEKINEMATICSBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_INVERSEKINEMATICSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_InverseKinematicsBuilder.ja
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
#include <NXOpen/Mechatronics_EulerConvention.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/ugmath.hxx>
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
        class InverseKinematicsBuilder;
    }
    class Builder;
    class CoordinateSystem;
    namespace Mechatronics
    {
        class FrameBuilderList;
    }
    namespace Mechatronics
    {
        class SelectRigidBody;
    }
    namespace Mechatronics
    {
        class Tracer;
    }
    class Point;
    namespace Mechatronics
    {
        class _InverseKinematicsBuilderBuilder;
        class InverseKinematicsBuilderImpl;
        /** Represents a @link NXOpen::Mechatronics::InverseKinematics NXOpen::Mechatronics::InverseKinematics@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Mechatronics::InverseKinematicsCollection::CreateInverseKinematicsBuilder  NXOpen::Mechatronics::InverseKinematicsCollection::CreateInverseKinematicsBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  InverseKinematicsBuilder : public NXOpen::Builder
        {
            /** the inverse kinematics types. */
            public: enum Types
            {
                TypesOnline/** dynamically operate the motors in simulation.*/,
                TypesOffline/** assign motors value before simulation. */
            };

            /** Specifies the result of the inverse kinematics solver. */
            public: enum SolverResult
            {
                SolverResultSuccess/** Successfully solved. */,
                SolverResultApproximate/** The target is not reachable, closest solution is returned. */,
                SolverResultLimits/** The target is not reachable due to limits, closest solution is returned. */,
                SolverResultReachError/** A reach error occurs. */,
                SolverResultTimeout/** A timeout error occurs due to collision avoidance. */,
                SolverResultCollidingTarget/** The target pose is colliding. */,
                SolverResultCollidingStart/** The start pose is colliding. */,
                SolverResultLimitError/** Cannot move toward the target due to limits. */,
                SolverResultTargetEqualsStart/** It is not possible to go closer to the target due to the kinematics. */,
                SolverResultUnknown/** An unknown error occurs in the inverse kinematics solver. */
            };

            private: InverseKinematicsBuilderImpl * m_inversekinematicsbuilder_impl;
            private: friend class  _InverseKinematicsBuilderBuilder;
            protected: InverseKinematicsBuilder();
            public: ~InverseKinematicsBuilder();
            /**Returns  the type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::InverseKinematicsBuilder::Types Type
            (
            );
            /**Sets  the type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetType
            (
                NXOpen::Mechatronics::InverseKinematicsBuilder::Types type /** type */ 
            );
            /**Returns  the rigid body. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::SelectRigidBody * RigidBody
            (
            );
            /**Returns  the start point. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * StartPoint
            (
            );
            /**Sets  the start point. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetStartPoint
            (
                NXOpen::Point * startPoint /** startpoint */ 
            );
            /** Sets the start orientation. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetStartOrientation
            (
                const NXOpen::Matrix3x3 & startOrit /** The start orientation matrix. */
            );
            /** Gets the start orientation.  @return  The start orientation matrix. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Matrix3x3 GetStartOrientation
            (
            );
            /**Returns  the list containing the defined frames. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::FrameBuilderList * FrameList
            (
            );
            /**Returns  the name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the option of avoiding collision. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool AvoidCollision
            (
            );
            /**Sets  the option of avoiding collision. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetAvoidCollision
            (
                bool avoidCollision /** avoidcollision */ 
            );
            /**Returns  the option of generating tracer object. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool GenerateTracer
            (
            );
            /**Sets  the option of generating tracer object. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetGenerateTracer
            (
                bool bTracer /** btracer */ 
            );
            /** Returns the solver result.  @return  The result of the inverse kinematics solver 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::InverseKinematicsBuilder::SolverResult GetResult
            (
            );
            /** Returns the pose that encounters error. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::CoordinateSystem * GetErrorPose
            (
            );
            /**Returns  the Euler angle convention. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::Convention EulerAngleConvention
            (
            );
            /**Sets  the Euler angle convention. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetEulerAngleConvention
            (
                NXOpen::Mechatronics::Convention type /** type */ 
            );
            /** Set reference tracer object. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetTracer
            (
                NXOpen::Mechatronics::Tracer * tracer /** tracer */ 
            );
            /** Get the flag of auto execute IK solve. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool GetIsAutosolve
            (
            );
            /** Set the flag of auto execute IK solve. If this flag is true, the system will solve the kinematics objects
                    then update the controllers and operations accordingly when create or update IK object
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetIsAutosolve
            (
                bool autoSolve /** autosolve */ 
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
