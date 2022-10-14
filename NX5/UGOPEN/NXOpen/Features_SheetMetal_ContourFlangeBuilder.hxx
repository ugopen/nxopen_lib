#ifndef NXOpen_FEATURES_SHEETMETAL_CONTOURFLANGEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_CONTOURFLANGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_ContourFlangeBuilder.ja
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
#include <NXOpen/Features_SheetMetal_MiterOptions.hxx>
#include <NXOpen/SheetmetalFeatureProperty.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class ContourFlangeBuilder;
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
        namespace SheetMetal
        {
            class MiterOptions;
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
            class _ContourFlangeBuilderBuilder;
            /** Represents a Contour Flange feature builder.  <br> To create a new instance of this class, use @link Features::SheetMetal::SheetmetalManager::CreateContourFlangeFeatureBuilder Features::SheetMetal::SheetmetalManager::CreateContourFlangeFeatureBuilder@endlink  <br> */
            class NXOPENCPPEXPORT ContourFlangeBuilder : public Features::FeatureBuilder
            {
                /** This enum represents the side of the section in which material is created. The "left" option
                            represents the side to the left of a person who is walking along the section in the direction of its curves
                            when the section normal is pointing up. The "right" option represents the person's right hand side.
                            This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
                            along the section can also be represented by the vector resulting from the cross product of the curve tangent
                            (of the section curve at that point) and the section normal. The "left" side is the opposite. */
                public: enum SectionSideOptions
                {
                    SectionSideOptionsLeft/** left */ ,
                    SectionSideOptionsRight/** right */ 
                };

                /** This enum represents the side in which the contour flange will be swept.*/
                public: enum SweepSideOptions
                {
                    SweepSideOptionsSectionNormalSide/** section normal side */ ,
                    SweepSideOptionsSectionReverseNormalSide/** section reverse normal side */ 
                };

                /** This enum represents the sweep type of the contour flange */
                public: enum SweepTypeOptions
                {
                    SweepTypeOptionsFinite/** finite */ ,
                    SweepTypeOptionsSymmetric/** symmetric */ ,
                    SweepTypeOptionsToEnd/** to end */ ,
                    SweepTypeOptionsChain/** chain */ 
                };

                private: friend class  _ContourFlangeBuilderBuilder;
                protected: ContourFlangeBuilder();
                /**Returns  the section of contour flange  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Section * Section
                (
                );
                /**Sets  the section of contour flange  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetSection
                (
                    NXOpen::Section * section /** section */ 
                );
                /** THE thickness of contour flange  @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Expression * GetThickness
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetThickness
                (
                    const NXString & thickness /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the thickness side of contour flange  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::ContourFlangeBuilder::SectionSideOptions ThicknessSide
                (
                );
                /**Sets  the thickness side of contour flange  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetThicknessSide
                (
                    NXOpen::Features::SheetMetal::ContourFlangeBuilder::SectionSideOptions section_side /** section side */ 
                );
                /** THE projection distance of contour flange  @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Expression * GetSweepDistance
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetSweepDistance
                (
                    const NXString & sweep_distance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the projection direction of contour flange  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::ContourFlangeBuilder::SweepSideOptions SweepSide
                (
                );
                /**Sets  the projection direction of contour flange  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetSweepSide
                (
                    NXOpen::Features::SheetMetal::ContourFlangeBuilder::SweepSideOptions sweep_side /** sweep side */ 
                );
                /**Returns  the projection side of contour flange <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::ContourFlangeBuilder::SweepTypeOptions SweepType
                (
                );
                /**Sets  the projection side of contour flange <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetSweepType
                (
                    NXOpen::Features::SheetMetal::ContourFlangeBuilder::SweepTypeOptions sweep_type /** sweep type */ 
                );
                /**Returns  the bend options  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::BendOptions * BendOptions
                (
                );
                /**Returns  the miter options  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::MiterOptions * MiterOptions
                (
                );
                /**Returns  the sketch  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SketchFeature * Sketch
                (
                );
                /**Sets  the sketch  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetSketch
                (
                    NXOpen::Features::SketchFeature * sketch /** sketch */
                );
                /** Verify whether the builder data is valid for creating a Contour Flange or not.
                             <br> 
                                 If the Builder data is valid, returned value shall be 0

                             <br> 
                         @return  Data Validity Flag. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: int ValidateBuilderData
                (
                );
                /**Returns  the section having chain edges.  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Section * EdgeChain
                (
                );
                /**Sets  the section having chain edges.  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetEdgeChain
                (
                    NXOpen::Section * edge_chain /** edge chain */ 
                );
                /**Returns  the contour flange type.  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: bool IsSecondary
                (
                );
                /**Sets  the contour flange type.  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetSecondary
                (
                    bool is_secondary /** is secondary */ 
                );
                /** the application context of Contour Flange  @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
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