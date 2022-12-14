#ifndef NXOpen_CAE_BEAMSECTION_HXX_INCLUDED
#define NXOpen_CAE_BEAMSECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_BeamSection.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class BeamSection;
    }
    namespace CAE
    {
        class PropertyTable;
    }
    class NXObject;
    namespace CAE
    {
        class _BeamSectionBuilder;
        class BeamSectionImpl;
        /** Represents a Beam Cross Section  <br> This is an abstract class.  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  BeamSection : public NXOpen::NXObject
        {
            /** Represents the direction */
            public: enum DirectionOption
            {
                DirectionOptionHorizontal/** Indicates the horizontal direction of beam section */,
                DirectionOptionVertical/** Indicates the vertical direction of beam section */
            };

             /** Represents the properties of the beam section. */
            public:
            struct Properties
            {
                public: /** Area of section                                                 */double Area;
                public: /** Principal angle                                                 */double PrincipalAngle;
                public: /** Moment of Inertia about y-axis                                  */double MomentInertiaYY;
                public: /** Moment of Inertia about z-axis                                  */double MomentInertiaZZ;
                public: /** YZ-Product of Inertia                                           */double MomentInertiaYZ;
                public: /** Torsional coefficient                                           */double TorsionCoefficient;
                public: /** Warping coefficient                                             */double WarpingCoefficient;
                public: /** Offset measured from centroid to shear center in y-axis         */double YEccentricity;
                public: /** Offset measured from centroid to shear center in z-axis         */double ZEccentricity;
                public: /** Principal Moment of Inertia about y-axis                        */double PrincipalMomentInertiaYY;
                public: /** Principal Moment of Inertia about z-axis                        */double PrincipalMomentInertiaZZ;
                public: Properties() :
                    Area(),
                    PrincipalAngle(),
                    MomentInertiaYY(),
                    MomentInertiaZZ(),
                    MomentInertiaYZ(),
                    TorsionCoefficient(),
                    WarpingCoefficient(),
                    YEccentricity(),
                    ZEccentricity(),
                    PrincipalMomentInertiaYY(),
                    PrincipalMomentInertiaZZ()
                {
                }
                /** Constructor for the Properties struct. */ 
                public: Properties(double areaInitial /** Area of section                                                 */, 
                        double principalAngleInitial /** Principal angle                                                 */, 
                        double momentInertiaYYInitial /** Moment of Inertia about y-axis                                  */, 
                        double momentInertiaZZInitial /** Moment of Inertia about z-axis                                  */, 
                        double momentInertiaYZInitial /** YZ-Product of Inertia                                           */, 
                        double torsionCoefficientInitial /** Torsional coefficient                                           */, 
                        double warpingCoefficientInitial /** Warping coefficient                                             */, 
                        double yEccentricityInitial /** Offset measured from centroid to shear center in y-axis         */, 
                        double zEccentricityInitial /** Offset measured from centroid to shear center in z-axis         */, 
                        double principalMomentInertiaYYInitial /** Principal Moment of Inertia about y-axis                        */, 
                        double principalMomentInertiaZZInitial /** Principal Moment of Inertia about z-axis                        */) :
                    Area(areaInitial),
                    PrincipalAngle(principalAngleInitial),
                    MomentInertiaYY(momentInertiaYYInitial),
                    MomentInertiaZZ(momentInertiaZZInitial),
                    MomentInertiaYZ(momentInertiaYZInitial),
                    TorsionCoefficient(torsionCoefficientInitial),
                    WarpingCoefficient(warpingCoefficientInitial),
                    YEccentricity(yEccentricityInitial),
                    ZEccentricity(zEccentricityInitial),
                    PrincipalMomentInertiaYY(principalMomentInertiaYYInitial),
                    PrincipalMomentInertiaZZ(principalMomentInertiaZZInitial)
                {
                }
            };

            private: BeamSectionImpl * m_beamsection_impl;
            private: friend class  _BeamSectionBuilder;
            protected: BeamSection();
            public: ~BeamSection();
            /** Gets the section descriptor name.  @return  The descriptor name of section 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString GetDescriptorName
            (
            );
            /**Returns  the section property table of definition 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PropertyTable * PropertyTable
            (
            );
            /** Gets the stress recovery points 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void GetStressRecoveryPoints
            (
                std::vector<NXOpen::Point2d> & points /** The stress recovery points of section */
            );
            /**Returns  the section properties 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::BeamSection::Properties SectionProperties
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
