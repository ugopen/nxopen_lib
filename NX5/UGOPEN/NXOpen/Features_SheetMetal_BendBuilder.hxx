#ifndef NXOpen_FEATURES_SHEETMETAL_BENDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_BENDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_BendBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_SheetMetal_BendOptions.hxx>
#include <NXOpen/SheetmetalFeatureProperty.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class BendBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BendOptions;
        }
    }
    namespace Features
    {
        class SketchFeature;
    }
    class Section;
    namespace Features
    {
        namespace SheetMetal
        {
            class _BendBuilderBuilder;
            /** Represents a Bend feature builder.  <br> To create a new instance of this class, use @link Features::SheetMetal::SheetmetalManager::CreateBendFeatureBuilder Features::SheetMetal::SheetmetalManager::CreateBendFeatureBuilder@endlink  <br> */
            class NXOPENCPPEXPORT BendBuilder : public Features::FeatureBuilder
            {
                /** This enum represents the Bend Direction for Bend. */
                public: enum BendDirectionOptions
                {
                    BendDirectionOptionsSectionNormalSide/** Bend is created on the side of the section normal. */,
                    BendDirectionOptionsSectionReverseNormalSide/** Bend is created on the side opposite to that of the section normal */
                };

                /** This enum represents the Fixed Side for Bend. */
                public: enum FixedSideOptions
                {
                    FixedSideOptionsSectionSideLeft/** Side pointed to by the inverse of the tangent cross normal vector */,
                    FixedSideOptionsSectionSideRight/** Side pointed to by the tangent cross normal vector */
                };

                /** This enum represents the Bend Location (Material Side) for Bend. */
                public: enum BendLocationOptions
                {
                    BendLocationOptionsOuterMoldLine/** outer mold line */ ,
                    BendLocationOptionsCenterLine/** center line */ ,
                    BendLocationOptionsInnerMoldLine/** inner mold line */ ,
                    BendLocationOptionsMaterialInside/** material inside */ ,
                    BendLocationOptionsMaterialOutside/** material outside */ 
                };

                private: friend class  _BendBuilderBuilder;
                protected: BendBuilder();
                /**Returns  the Section  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Section * Section
                (
                );
                /**Sets  the Section  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetSection
                (
                    NXOpen::Section * section /** section */ 
                );
                /**Returns  the Bend Options  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::BendOptions * BendOptions
                (
                );
                /**Returns  the Bend Location (Material Side)  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::BendBuilder::BendLocationOptions BendLocation
                (
                );
                /**Sets  the Bend Location (Material Side)  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetBendLocation
                (
                    NXOpen::Features::SheetMetal::BendBuilder::BendLocationOptions bend_location /** bend location */ 
                );
                /**Returns  the Extend Option  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: bool ExtendProfile
                (
                );
                /**Sets  the Extend Option  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetExtendProfile
                (
                    bool extend_option /** extend option */ 
                );
                /** the Bend Angle  @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Expression * GetBendAngle
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetBendAngle
                (
                    const NXString & bend_angle /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the Bend Direction <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::BendBuilder::BendDirectionOptions Direction
                (
                );
                /**Sets  the Bend Direction <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetDirection
                (
                    NXOpen::Features::SheetMetal::BendBuilder::BendDirectionOptions direction /** direction */ 
                );
                /**Returns  the Fixed Side  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::BendBuilder::FixedSideOptions FixedSide
                (
                );
                /**Sets  the Fixed Side  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetFixedSide
                (
                    NXOpen::Features::SheetMetal::BendBuilder::FixedSideOptions fixed_side /** fixed side */ 
                );
                /**Returns  the Sketch  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SketchFeature * Sketch
                (
                );
                /**Sets  the Sketch  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetSketch
                (
                    NXOpen::Features::SketchFeature * sketch /** sketch */ 
                );
                /** Verify whether the builder data is valid for creating bend or not.
                             <br> 
                                 If the Builder data is valid, returned value should be 0

                             <br> 
                         @return  Data Validity Flag. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: int ValidateBuilderData
                (
                );
                /** the application context of Bend  @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::ApplicationContext GetApplicationContext
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetApplicationContext
                (
                    NXOpen::Features::SheetMetal::ApplicationContext app_context /** app context */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
