#ifndef NXOpen_MOTION_JOINTDEFINE_HXX_INCLUDED
#define NXOpen_MOTION_JOINTDEFINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_JointDefine.ja
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
        class JointDefine;
    }
    namespace CAE
    {
        class Function;
    }
    class CoordinateSystem;
    class Direction;
    class Expression;
    namespace Motion
    {
        class Link;
    }
    namespace Motion
    {
        class SelectFieldData;
    }
    class NXMatrix;
    class Point;
    namespace Motion
    {
        class _JointDefineBuilder;
        class JointDefineImpl;
        /** Represents a joint define object 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  JointDefine : public NXOpen::TaggedObject
        {
            /** Joint define type */
            public: enum Type
            {
                TypeRevolute/** This joint type is a single axis rotation.
                                                                        This joint removes 5 degrees of freedom.
                                                                        The origins of csys_1 and csys_2 are
                                                                        identical and the z axes of csys_1 and
                                                                        csys_2 are collinear and codirected. */,
                TypeSlider/** This joint type is a single translation.
                                                                        This joint removes 5 degrees of freedom.
                                                                        The orientations of csys_1 and csys_2 are
                                                                        identical and the z axes are collinear and
                                                                        codirected. */,
                TypeCylindrical/** This joint type is a single rotation and
                                                                        a single translation.  This joint removes
                                                                        4 degrees of freedom.  The z axes of csys_1
                                                                        and csys_2 are collinear and codirected  */,
                TypeScrew/** This joint type is used to couple the 
                                                                        rotation and translation of a cylindrical
                                                                        joint to remove one degree of freedom.  
                                                                        It should be created on the same pair
                                                                        of links as the cylindrical joint.  If 
                                                                        the screw joint needs to be driven, it
                                                                        may be coupled with a revolution joint and 
                                                                        a slider joint instead. */,
                TypeUniversal/** This joint type allows two rotations.  It
                                                                            removes 4 degrees of freedom.  The origins
                                                                            of csys_1 and csys_2 are identical.  The
                                                                            rotations about the x axis of csys_2 are
                                                                            equal and opposite to the rotations about
                                                                            the x axis of csys_1. */,
                TypeSpherical/** This joint type allows three rotations.
                                                                        It removes 3 degrees of freedom.  The
                                                                        origins of csys_1 and csys_2 are
                                                                        identical */,
                TypePlanar/** This joint type allows a single rotation
                                                                        and two translations.  It removes three
                                                                        degrees of freedom.  The z axes of csys_1
                                                                        and csys_2 are parallel and codirected.
                                                                        The origins of csys_1 and csys_2 are in
                                                                        a common xy-plane. */,
                TypeFixed/** This Joint fixes a link or weld two links, 
                                                                        It removes 6 degrees of freedom */,
                TypeConstantvelocity/** This joint type allows 2 rotational degrees of freedom,
                                                                            rotation about both z axes of the joint markers,
                                                                            Rotation about the second marker's z-axis is equal 
                                                                            and opposite to the first marker's rotation. 
                                                                            A constant velocity joint is similar to a universal joint, 
                                                                            but the exit angle of a constant velocity joint is equal to 
                                                                            the entry angle.The origins of csys_1 and csys_2
                                                                            are identical. */,
                TypeAtpoint/** This joint type allows 3 DOF: Markers are 
                                                                            always coincident, and only rotational motion 
                                                                            is allowed. */,
                TypeInline/** This joint type indicates a four degrees of freedom (3R + 1T DOF) 
                                                                            primitive that allows one translational and three rotational
                                                                            motions of one part with respect to another.One part so that
                                                                            it can only move along a straight line defined on a second part.
                                                                            The location of the inline joint on the first part must remain 
                                                                            on the z-axis of the second part. */,
                TypeInplane/** One part so that it can only move in a plane of a second part.
                                                                           The origin of the inplane joint on the first part must remain 
                                                                           in the xy-plane of the second part. Indicates a five degrees of freedom 
                                                                           (3R + 2T DOF) primitive that allows both translational and rotational
                                                                           motion of one part with respect to another.For an inplane primitive, 
                                                                           Adams/Solver imposes one translational constraint, which confines the
                                                                           translational motion of the I marker to the xy-plane of the J marker. */,
                TypeOrientation/** The coordinate system of one part so that it cannot rotate with respect 
                                                                            to a second part. The axes of the coordinate systems must maintain the
                                                                            same orientation. The location of the origins of the coordinate systems
                                                                            does not matter. Indicates a three degrees of freedom (3T DOF) primitive 
                                                                            that allows only translational motion of one part with respect to another .
                                                                            For an orientation primitive, Solver imposes three rotational constraints to 
                                                                            keep the orientation of the I marker identical to the orientation of the J marker. */,
                TypeParallel/** This joint type indicates a four degrees of freedom(1R + 3T DOF) primitive that allows 
                                                                            both translational and rotational motion of one part with respect to another .
                                                                            For a parallel axes primitive, Solver imposes two rotational constraints so
                                                                            that the z-axis of the I marker stays parallel to the z-axis of the J marker. 
                                                                            This primitive permits relative rotation about the common z-axis of I and J 
                                                                            and permits all relative displacements. */,
                TypePerpendicular/** This joint type indicates a five degrees of freedom (2R +3T DOF) primitive that allows both 
                                                                            translational and rotational motion of one part with respect to Another.
                                                                            For a perpendicular primitive, Solver imposes a single rotational constraint 
                                                                            on the I and the J markers so that their z-axes remain perpendicular. This 
                                                                            allows relative rotations about either z-axis, but does not allow any relative 
                                                                            rotation in the direction perpendicular to both z-axes. */
            };

            /** Defines the orientation type of joint */
            public: enum OrientationType
            {
                OrientationTypeVector/** Vector orientation type */,
                OrientationTypeCsys/** CSYS orientation type*/
            };

            /** Defines the method type of screw joints */
            public: enum ScrewJointMethodType
            {
                ScrewJointMethodTypeRatio/** Ratio method */,
                ScrewJointMethodTypeDisplacementcurve/** Displacement curve method */
            };

            /** Defines the ratio type for screw joints */
            public: enum ScrewJointRatioType
            {
                ScrewJointRatioTypeExpression/** Expression type */,
                ScrewJointRatioTypeSpline/** Spline type */,
                ScrewJointRatioTypeProfile/** Profile type */
            };

            /** Defines the displacement curve type for screw joints */
            public: enum ScrewJointDisplCurveType
            {
                ScrewJointDisplCurveTypeSpline/** Spline type */,
                ScrewJointDisplCurveTypeProfile/** Profile type */
            };

            /** Defines the axis type for universal joints */
            public: enum UniversalJointAxisType
            {
                UniversalJointAxisTypeRotational/** Rotational Axis Type */,
                UniversalJointAxisTypeCrossPin/** Cross Pin Axis Type */
            };

            private: JointDefineImpl * m_jointdefine_impl;
            private: friend class  _JointDefineBuilder;
            protected: JointDefine();
            public: ~JointDefine();
            /**Returns  the joint type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::JointDefine::Type JointType
            (
            );
            /**Sets  the joint type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetJointType
            (
                NXOpen::Motion::JointDefine::Type jointType /** joint type */ 
            );
            /**Returns  the display scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: double DisplayScale
            (
            );
            /**Sets  the display scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDisplayScale
            (
                double displayScale /** display scale */ 
            );
            /**Returns   the joint name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXString Name
            (
            );
            /**Sets   the joint name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & jointName /** joint name */ 
            );
            /**Sets   the joint name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetName
            (
                const char * jointName /** joint name */ 
            );
            /**Returns  the option of snap links 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool SnapLinks
            (
            );
            /**Sets  the option of snap links 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSnapLinks
            (
                bool snapLinks /** snap links */ 
            );
            /**Returns  the first link object 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::Link * FirstLink
            (
            );
            /**Sets  the first link object 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstLink
            (
                NXOpen::Motion::Link * firstLink /** firstlink */ 
            );
            /**Returns  the origin of first link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Point * FirstOrigin
            (
            );
            /**Sets  the origin of first link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstOrigin
            (
                NXOpen::Point * firstOrigin /** firstorigin */ 
            );
            /**Returns  the first orientation type of joint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::JointDefine::OrientationType FirstOrientationType
            (
            );
            /**Sets  the first orientation type of joint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstOrientationType
            (
                NXOpen::Motion::JointDefine::OrientationType orientationType /** orientationtype */ 
            );
            /**Returns  the direction of first link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Direction * FirstVector
            (
            );
            /**Sets  the direction of first link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstVector
            (
                NXOpen::Direction * firstVector /** firstvector */ 
            );
            /**Returns  the matrix of first link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::NXMatrix * FirstMatrix
            (
            );
            /**Sets  the matrix of first link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstMatrix
            (
                NXOpen::NXMatrix * firstMatrix /** firstmatrix */ 
            );
            /**Returns  the CSYS of first link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::CoordinateSystem * FirstCsys
            (
            );
            /**Sets  the CSYS of first link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstCsys
            (
                NXOpen::CoordinateSystem * firstCsys /** firstcsys */ 
            );
            /**Returns  the second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::Link * SecondLink
            (
            );
            /**Sets  the second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondLink
            (
                NXOpen::Motion::Link * secondLink /** secondlink */ 
            );
            /**Returns  the origin of second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Point * SecondOrigin
            (
            );
            /**Sets  the origin of second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondOrigin
            (
                NXOpen::Point * secondOrigin /** secondorigin */ 
            );
            /**Returns  the second orientation type of joint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::JointDefine::OrientationType SecondOrientationType
            (
            );
            /**Sets  the second orientation type of joint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondOrientationType
            (
                NXOpen::Motion::JointDefine::OrientationType orientationType /** orientationtype */ 
            );
            /**Returns  the direction of second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Direction * SecondVector
            (
            );
            /**Sets  the direction of second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondVector
            (
                NXOpen::Direction * secondVector /** secondvector */ 
            );
            /**Returns  the matrix of second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::NXMatrix * SecondMatrix
            (
            );
            /**Sets  the matrix of second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondMatrix
            (
                NXOpen::NXMatrix * secondMatrix /** secondmatrix */ 
            );
            /**Returns  the csys of second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::CoordinateSystem * SecondCsys
            (
            );
            /**Sets  the csys of second link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondCsys
            (
                NXOpen::CoordinateSystem * secondCsys /** secondcsys */ 
            );
            /**Returns  the option of defining limits for joint 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link Motion::JointDefine::UpperLimitDefined Motion::JointDefine::UpperLimitDefined@endlink  and @link Motion::JointDefine::LowerLimitDefined Motion::JointDefine::LowerLimitDefined@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use Motion::JointDefine::UpperLimitDefined and Motion::JointDefine::LowerLimitDefined instead.") bool LimitsDefined
            (
            );
            /**Sets  the option of defining limits for joint 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link Motion::JointDefine::SetUpperLimitDefined Motion::JointDefine::SetUpperLimitDefined@endlink  and @link Motion::JointDefine::SetLowerLimitDefined Motion::JointDefine::SetLowerLimitDefined@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use Motion::JointDefine::SetUpperLimitDefined and Motion::JointDefine::SetLowerLimitDefined instead.") void SetLimitsDefined
            (
                bool limitsDefined /** limits defined */ 
            );
            /**Returns  the option of defining upper limit for joint 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool UpperLimitDefined
            (
            );
            /**Sets  the option of defining upper limit for joint 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetUpperLimitDefined
            (
                bool limitDefined /** limit defined */ 
            );
            /**Returns  the option of defining lower limit for joint 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool LowerLimitDefined
            (
            );
            /**Sets  the option of defining lower limit for joint 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetLowerLimitDefined
            (
                bool limitDefined /** limit defined */ 
            );
            /**Returns  the method type of a screw joint 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::JointDefine::ScrewJointMethodType MethodType
            (
            );
            /**Sets  the method type of a screw joint 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMethodType
            (
                NXOpen::Motion::JointDefine::ScrewJointMethodType methodType /** methodtype */ 
            );
            /**Returns  the ratio type of a screw joint 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::JointDefine::ScrewJointRatioType RatioType
            (
            );
            /**Sets  the ratio type of a screw joint 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRatioType
            (
                NXOpen::Motion::JointDefine::ScrewJointRatioType ratioType /** ratiotype */ 
            );
            /**Returns  the displacemnet curve type of a screw joint 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::JointDefine::ScrewJointDisplCurveType DisplCurveType
            (
            );
            /**Sets  the displacemnet curve type of a screw joint 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDisplCurveType
            (
                NXOpen::Motion::JointDefine::ScrewJointDisplCurveType displCurveType /** displcurvetype */ 
            );
            /**Returns  the screw ratio expression.  Used only when joint subtype is 
                @link  Motion::JointDefine::TypeScrew   Motion::JointDefine::TypeScrew @endlink .
                For Simcenter Solver, method type must be @link  Motion::JointDefine::ScrewJointMethodTypeRatio   Motion::JointDefine::ScrewJointMethodTypeRatio @endlink   which is the pitch of a screw's thread,
                and ratio type must be @link  Motion::JointDefine::ScrewJointRatioTypeExpression   Motion::JointDefine::ScrewJointRatioTypeExpression @endlink  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ScrewRatioExpression
            (
            );
            /**Returns  the spline function tag. Only valid for LMS solver if method type is @link Motion::JointDefine::ScrewJointMethodTypeRatio Motion::JointDefine::ScrewJointMethodTypeRatio@endlink ,
                and ratio type is @link Motion::JointDefine::ScrewJointRatioTypeSpline Motion::JointDefine::ScrewJointRatioTypeSpline@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Function * ScrewSplineFunction
            (
            );
            /**Sets  the spline function tag. Only valid for LMS solver if method type is @link Motion::JointDefine::ScrewJointMethodTypeRatio Motion::JointDefine::ScrewJointMethodTypeRatio@endlink ,
                and ratio type is @link Motion::JointDefine::ScrewJointRatioTypeSpline Motion::JointDefine::ScrewJointRatioTypeSpline@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetScrewSplineFunction
            (
                NXOpen::CAE::Function * splineFunction /** splinefunction */ 
            );
            /**Returns  the displacement curve function tag. Only valid for Simcenter Solver if method type is 
                @link Motion::JointDefine::ScrewJointMethodTypeDisplacementcurve Motion::JointDefine::ScrewJointMethodTypeDisplacementcurve@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Function * ScrewDisplCurveFunction
            (
            );
            /**Sets  the displacement curve function tag. Only valid for Simcenter Solver if method type is 
                @link Motion::JointDefine::ScrewJointMethodTypeDisplacementcurve Motion::JointDefine::ScrewJointMethodTypeDisplacementcurve@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetScrewDisplCurveFunction
            (
                NXOpen::CAE::Function * displCurveFunction /** displcurvefunction */ 
            );
            /**Returns  the upper limit expression.  Only used when limits option is TRUE 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * UpperLimitExpression
            (
            );
            /**Returns  the lower limit expression.  Only used when limits option is TRUE 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * LowerLimitExpression
            (
            );
            /**Returns  the upper limit angular expression.  Only used when limits option is TRUE 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * UpperLimitAngleExpression
            (
            );
            /**Returns  the lower limit angular expression.  Only used when limits option is TRUE 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * LowerLimitAngleExpression
            (
            );
            /**Returns  the options of excluded x constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool ExcludeXConstraint
            (
            );
            /**Sets  the options of excluded x constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetExcludeXConstraint
            (
                bool excludeXConstraint /** excludexconstraint */ 
            );
            /**Returns  the options of excluded y constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool ExcludeYConstraint
            (
            );
            /**Sets  the options of excluded y constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetExcludeYConstraint
            (
                bool excludeYConstraint /** excludeyconstraint */ 
            );
            /**Returns  the options of excluded z constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool ExcludeZConstraint
            (
            );
            /**Sets  the options of excluded z constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetExcludeZConstraint
            (
                bool excludeZConstraint /** excludezconstraint */ 
            );
            /**Returns  the options of excluded rx constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool ExcludeRxConstraint
            (
            );
            /**Sets  the options of excluded rx constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetExcludeRxConstraint
            (
                bool excludeRxConstraint /** excluderxconstraint */ 
            );
            /**Returns  the option of excluded ry constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool ExcludeRyConstraint
            (
            );
            /**Sets  the option of excluded ry constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetExcludeRyConstraint
            (
                bool excludeRyConstraint /** excluderyconstraint */ 
            );
            /**Returns  the options of excluded rz constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool ExcludeRzConstraint
            (
            );
            /**Sets  the options of excluded rz constraint. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeFixed   Motion::JointDefine::TypeFixed @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetExcludeRzConstraint
            (
                bool excludeRzConstraint /** excluderzconstraint */ 
            );
            /**Returns  the options of allowing rotation. Used only when joint subtype is 
                @link  Motion::JointDefine::TypePlanar   Motion::JointDefine::TypePlanar @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool RotationAllowed
            (
            );
            /**Sets  the options of allowing rotation. Used only when joint subtype is 
                @link  Motion::JointDefine::TypePlanar   Motion::JointDefine::TypePlanar @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetRotationAllowed
            (
                bool rotationAllowed /** rotationallowed */ 
            );
            /**Returns  the options of allowing rotation. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeConstantvelocity   Motion::JointDefine::TypeConstantvelocity @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool TranslationAllowed
            (
            );
            /**Sets  the options of allowing rotation. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeConstantvelocity   Motion::JointDefine::TypeConstantvelocity @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetTranslationAllowed
            (
                bool translationAllowed /** translationallowed */ 
            );
            /**Returns  the axis type. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeUniversal   Motion::JointDefine::TypeUniversal @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::JointDefine::UniversalJointAxisType AxisType
            (
            );
            /**Sets  the axis type. Used only when joint subtype is 
                @link  Motion::JointDefine::TypeUniversal   Motion::JointDefine::TypeUniversal @endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetAxisType
            (
                NXOpen::Motion::JointDefine::UniversalJointAxisType axisType /** axistype */ 
            );
            /**Returns  the ratio Profile.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::SelectFieldData * ScrewRatioProfile
            (
            );
            /**Returns  the displacement curve Profile.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::SelectFieldData * ScrewDisplCurveProfile
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