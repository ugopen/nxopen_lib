#ifndef NXOpen_MOTION_BODYCONTACTRECURDYN_HXX_INCLUDED
#define NXOpen_MOTION_BODYCONTACTRECURDYN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_BodyContactRecurdyn.ja
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
#include <NXOpen/Motion_BodyContactRecurdyn.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class BodyContactRecurdyn;
    }
    class NXObject;
    namespace Motion
    {
        class _BodyContactRecurdynBuilder;
        /** Represents a @link Motion::BodyContactRecurdyn Motion::BodyContactRecurdyn@endlink  */
        class NXOPENCPPEXPORT BodyContactRecurdyn : public NXObject
        {
            /** the enum for forec model of 3D contact */
            public: enum ForceModel
            {
                ForceModelImpact/** impact */ ,
                ForceModelPoisson/** poisson */ 
            };

            /** the enum for friction option of 3D contact */
            public: enum CoulombFriction
            {
                CoulombFrictionOff/** off */ ,
                CoulombFrictionOn/** on */ 
            };

            /** the enum for contact type option of 3D contact */
            public: enum ContactType
            {
                ContactTypePatch/** patch */ ,
                ContactTypeSurface/** surface */ ,
                ContactTypeSolid/** solid */ 
            };

            /** the enum for surface type option of 3D contact */
            public: enum SurfaceType
            {
                SurfaceTypeFaceted/** faceted */ ,
                SurfaceTypeFitted/** fitted */ 
            };

            private: friend class  _BodyContactRecurdynBuilder;
            protected: BodyContactRecurdyn();
            /**Returns  the stiffness  <br> License requirements : None */
            public: double Stiffness
            (
            );
            /**Sets  the stiffness  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStiffness
            (
                double stiffness /** stiffness */ 
            );
            /**Returns  the force model type <br> License requirements : None */
            public: NXOpen::Motion::BodyContactRecurdyn::ForceModel ForceModelType
            (
            );
            /**Sets  the force model type <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetForceModelType
            (
                NXOpen::Motion::BodyContactRecurdyn::ForceModel forceModel /** force model */ 
            );
            /**Returns  the force exponent  <br> License requirements : None */
            public: double ForceExponent
            (
            );
            /**Sets  the force exponent  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetForceExponent
            (
                double forceExponent /** force exponent */ 
            );
            /**Returns  the material damping  <br> License requirements : None */
            public: double MaterialDamping
            (
            );
            /**Sets  the material damping  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMaterialDamping
            (
                double materialDamping /** material damping */ 
            );
            /**Returns  the penetration depth  <br> License requirements : None */
            public: double PenetrationDepth
            (
            );
            /**Sets  the penetration depth  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetPenetrationDepth
            (
                double penetrationDepth /** penetration depth */ 
            );
            /**Returns  the Buffer Radius Factor  <br> License requirements : None */
            public: double BufferRadiusFactor
            (
            );
            /**Sets  the Buffer Radius Factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetBufferRadiusFactor
            (
                double bufferRadiusFactor /** buffer radius factor */ 
            );
            /**Returns  the Maximun Step Size Factor  <br> License requirements : None */
            public: double MaximumStepSizeFactor
            (
            );
            /**Sets  the Maximun Step Size Factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMaximumStepSizeFactor
            (
                double maximumStepSizeFactor /** maximum step size factor */ 
            );
            /**Returns  the Plane Maximum Penetration of the first geometry <br> License requirements : None */
            public: double FirstGeometryMaximumPenetration
            (
            );
            /**Sets  the Plane Maximum Penetration of the first geometry <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstGeometryMaximumPenetration
            (
                double firstGeometryMaximumPenetration /** first geometry maximum penetration */ 
            );
            /**Returns  the Plane Tolerance Factor of the first geometry <br> License requirements : None */
            public: double FirstGeometryPlaneToleranceFactor
            (
            );
            /**Sets  the Plane Tolerance Factor of the first geometry <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstGeometryPlaneToleranceFactor
            (
                double firstGeometryPlaneToleranceFactor /** first geometry plane tolerance factor */ 
            );
            /**Returns  the Plane Maximum Penetration of the second geometry <br> License requirements : None */
            public: double SecondGeometryMaximumPenetration
            (
            );
            /**Sets  the Plane Maximum Penetration of the second geometry <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondGeometryMaximumPenetration
            (
                double secondGeometryMaximumPenetration /** second geometry maximum penetration */ 
            );
            /**Returns  the Plane Tolerance Factor of the second geometry <br> License requirements : None */
            public: double SecondGeometryPlaneToleranceFactor
            (
            );
            /**Sets  the Plane Tolerance Factor of the second geometry <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondGeometryPlaneToleranceFactor
            (
                double secondGeometryPlaneToleranceFactor /** second geometry plane tolerance factor */ 
            );
            /**Returns  the coulomb friction option <br> License requirements : None */
            public: NXOpen::Motion::BodyContactRecurdyn::CoulombFriction CoulombFrictionOption
            (
            );
            /**Sets  the coulomb friction option <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetCoulombFrictionOption
            (
                NXOpen::Motion::BodyContactRecurdyn::CoulombFriction coulombFriction /** coulomb friction */ 
            );
            /**Returns  the coulomb coefficient  <br> License requirements : None */
            public: double StaticCoefficient
            (
            );
            /**Sets  the coulomb coefficient  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStaticCoefficient
            (
                double staticCoefficient /** static coefficient */ 
            );
            /**Returns  the stiction velocity  <br> License requirements : None */
            public: double StictionVelocity
            (
            );
            /**Sets  the stiction velocity  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStictionVelocity
            (
                double stictionVelocity /** stiction velocity */ 
            );
            /**Returns  the dynamic coefficient  <br> License requirements : None */
            public: double DynamicCoefficient
            (
            );
            /**Sets  the dynamic coefficient  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDynamicCoefficient
            (
                double dynamicCoefficient /** dynamic coefficient */ 
            );
            /**Returns  the friction velocity  <br> License requirements : None */
            public: double FrictionVelocity
            (
            );
            /**Sets  the friction velocity  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFrictionVelocity
            (
                double frictionVelocity /** friction velocity */ 
            );
            /**Returns  the contact type option <br> License requirements : None */
            public: NXOpen::Motion::BodyContactRecurdyn::ContactType ContactTypeOption
            (
            );
            /**Sets  the contact type option <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetContactTypeOption
            (
                NXOpen::Motion::BodyContactRecurdyn::ContactType contactType /** contact type */ 
            );
            /**Returns  the surface type option <br> License requirements : None */
            public: NXOpen::Motion::BodyContactRecurdyn::SurfaceType SurfaceTypeOption
            (
            );
            /**Sets  the surface type option <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSurfaceTypeOption
            (
                NXOpen::Motion::BodyContactRecurdyn::SurfaceType surfaceType /** surface type */ 
            );
            /**Returns  the rebound Damping Factor Flag <br> License requirements : None */
            public: bool ReboundDampingFactorFlag
            (
            );
            /**Sets  the rebound Damping Factor Flag <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetReboundDampingFactorFlag
            (
                bool reboundDampingFactorFlag /** rebound damping factor flag */ 
            );
            /**Returns  the rebound Damping Factor <br> License requirements : None */
            public: double ReboundDampingFactor
            (
            );
            /**Sets  the rebound Damping Factor <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetReboundDampingFactor
            (
                double reboundDampingFactor /** rebound damping factor */ 
            );
            /**Returns  the global Max. Penetration <br> License requirements : None */
            public: double GlobalMaxPenetration
            (
            );
            /**Sets  the global Max. Penetration <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetGlobalMaxPenetration
            (
                double globalMaxPenetration /** global max penetration */ 
            );
            /**Returns  the auto global maximum penetration flag <br> License requirements : None */
            public: int AutoGlobalMaxPenetrationFlag
            (
            );
            /**Sets  the auto global maximum penetration flag <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetAutoGlobalMaxPenetrationFlag
            (
                int autoGlobalMaxPenetrationFlag /** auto global max penetration flag */ 
            );
            /**Returns  the local Max. Penetration  <br> License requirements : None */
            public: double LocalMaxPenetration
            (
            );
            /**Sets  the local Max. Penetration  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetLocalMaxPenetration
            (
                double localMaxPenetration /** local max penetration */ 
            );
            /**Returns  the auto local maximum penetration flag <br> License requirements : None */
            public: int AutoLocalMaxPenetrationFlag
            (
            );
            /**Sets  the auto local maximum penetration flag <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetAutoLocalMaxPenetrationFlag
            (
                int autoLocalMaxPenetrationFlag /** auto local max penetration flag */ 
            );
            /**Returns  the max Facet Size Factor Flag <br> License requirements : None */
            public: bool FirstGeometryMaxFacetSizeFactorFlag
            (
            );
            /**Sets  the max Facet Size Factor Flag <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstGeometryMaxFacetSizeFactorFlag
            (
                bool maxFacetSizeFactorFlag /** max facet size factor flag */ 
            );
            /**Returns  the max Facet Size Factor  <br> License requirements : None */
            public: double FirstGeometryMaxFacetSizeFactor
            (
            );
            /**Sets  the max Facet Size Factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstGeometryMaxFacetSizeFactor
            (
                double maxFacetSizeFactor /** max facet size factor */ 
            );
            /**Returns  the bounding Buffer Length  <br> License requirements : None */
            public: double FirstGeometryBoundingBufferLength
            (
            );
            /**Sets  the bounding Buffer Length  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstGeometryBoundingBufferLength
            (
                double boundingBufferLength /** bounding buffer length */ 
            );
            /**Returns  the max Facet Size Factor Flag <br> License requirements : None */
            public: bool SecondGeometryMaxFacetSizeFactorFlag
            (
            );
            /**Sets  the max Facet Size Factor Flag <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondGeometryMaxFacetSizeFactorFlag
            (
                bool maxFacetSizeFactorFlag /** max facet size factor flag */ 
            );
            /**Returns  the max Facet Size Factor  <br> License requirements : None */
            public: double SecondGeometryMaxFacetSizeFactor
            (
            );
            /**Sets  the max Facet Size Factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondGeometryMaxFacetSizeFactor
            (
                double maxFacetSizeFactor /** max facet size factor */ 
            );
            /**Returns  the bounding Buffer Length  <br> License requirements : None */
            public: double SecondGeometryBoundingBufferLength
            (
            );
            /**Sets  the bounding Buffer Length  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondGeometryBoundingBufferLength
            (
                double boundingBufferLength /** bounding buffer length */ 
            );
            /**Returns  the Plane Tolerance Factor of the first geometry for solid contact <br> License requirements : None */
            public: double FirstGeometryPlaneToleranceFactorSolidContact
            (
            );
            /**Sets  the Plane Tolerance Factor of the first geometry for solid contact <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstGeometryPlaneToleranceFactorSolidContact
            (
                double firstGeometryPlaneToleranceFactorSolidContact /** first geometry plane tolerance factor solid contact */ 
            );
            /**Returns  the Plane Tolerance Factor of the second geometry for solid contact <br> License requirements : None */
            public: double SecondGeometryPlaneToleranceFactorSolidContact
            (
            );
            /**Sets  the Plane Tolerance Factor of the second geometry for solid contact <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondGeometryPlaneToleranceFactorSolidContact
            (
                double secondGeometryPlaneToleranceFactorSolidContact /** second geometry plane tolerance factor solid contact */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
