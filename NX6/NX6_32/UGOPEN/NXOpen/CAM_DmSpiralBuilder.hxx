#ifndef NXOpen_CAM_DMSPIRALBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DMSPIRALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DmSpiralBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class DmSpiralBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class StepoverBuilder;
    }
    class Point;
    namespace CAM
    {
        class _DmSpiralBuilderBuilder;
        /** Represents a Spiral Drive Method Builder  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT DmSpiralBuilder : public TaggedObject
        {
            /** Available types for Spiral drive method stepover in SurfaceContour.
                        This enum type is obsolete.
                    */
            public: enum DmSpiralStepoverTypes
            {
                DmSpiralStepoverTypesConstant/** Constant */,
                DmSpiralStepoverTypesToolDiameter/** Tool diameter percentage */
            };

            private: friend class  _DmSpiralBuilderBuilder;
            protected: DmSpiralBuilder();
            /**Returns  the Spiral Drive Method Stepover type.
                        This property is obsolete.
                     <br> License requirements : None */
            public: NXOpen::CAM::DmSpiralBuilder::DmSpiralStepoverTypes DmSpiralStepoverMenu
            (
            );
            /**Sets  the Spiral Drive Method Stepover type.
                        This property is obsolete.
                     <br> License requirements : None */
            public: void SetDmSpiralStepoverMenu
            (
                NXOpen::CAM::DmSpiralBuilder::DmSpiralStepoverTypes dmSpiralStepoverTypeValue /** the Spiral Stepover type value */
            );
            /**Returns  the Stepover Distance.
                        This property is obsolete.
                     <br> License requirements : None */
            public: double SpiralStepoverDistance
            (
            );
            /**Sets  the Stepover Distance.
                        This property is obsolete.
                     <br> License requirements : None */
            public: void SetSpiralStepoverDistance
            (
                double stepoverDist /** the Stepover Distance */
            );
            /**Returns  the Stepover Percent.
                        This property is obsolete.
                     <br> License requirements : None */
            public: double SpiralStepoverPercent
            (
            );
            /**Sets  the Stepover Percent.
                        This property is obsolete.
                     <br> License requirements : None */
            public: void SetSpiralStepoverPercent
            (
                double stepoverPercent /** the Stepover Percent */
            );
            /**Returns  the Spiral Stepover builder  <br> License requirements : None */
            public: NXOpen::CAM::StepoverBuilder * SpiralStepoverBuilder
            (
            );
            /**Returns  the Spiral Radius  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * SpiralRadiusBuilder
            (
            );
            /**Returns  the Pattern Center Point  <br> License requirements : None */
            public: NXOpen::Point * PatternCenterPoint
            (
            );
            /**Sets  the Pattern Center Point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPatternCenterPoint
            (
                NXOpen::Point * centerPoint /** centerpoint */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif