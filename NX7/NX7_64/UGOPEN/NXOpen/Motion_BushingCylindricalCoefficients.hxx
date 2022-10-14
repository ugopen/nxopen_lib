#ifndef NXOpen_MOTION_BUSHINGCYLINDRICALCOEFFICIENTS_HXX_INCLUDED
#define NXOpen_MOTION_BUSHINGCYLINDRICALCOEFFICIENTS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_BushingCylindricalCoefficients.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/Motion_BushingCylindricalCoefficients.hxx>
#include <NXOpen/Motion_BushingCylindricalCoefficientsComponent.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class BushingCylindricalCoefficients;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Motion
    {
        class BushingCylindricalCoefficientsComponent;
    }
    namespace Motion
    {
        class _BushingCylindricalCoefficientsBuilder;
        /**
            Represents a Motion BushingCylindricalCoefficients
            */
        class NXOPENCPPEXPORT BushingCylindricalCoefficients : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _BushingCylindricalCoefficientsBuilder;
            protected: BushingCylindricalCoefficients();
            /**Returns  the stiffness coefficients, it is used in @link BushingBuilder::BushingTypesCylindrical BushingBuilder::BushingTypesCylindrical@endlink  case  <br> License requirements : None */
            public: NXOpen::Motion::BushingCylindricalCoefficientsComponent * StiffnessCoefficients
            (
            );
            /**Returns  the damping coefficients, it is used in @link BushingBuilder::BushingTypesCylindrical BushingBuilder::BushingTypesCylindrical@endlink  case  <br> License requirements : None */
            public: NXOpen::Motion::BushingCylindricalCoefficientsComponent * DampingCoefficients
            (
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif