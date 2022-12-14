#ifndef NXOpen_FEATURES_SHEETMETAL_DIMPLEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_DIMPLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_DimpleBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class DimpleBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
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
            class _DimpleBuilderBuilder;
            /** Represents a Dimple feature builder.  <br> To create a new instance of this class, use @link Features::SheetMetal::SheetmetalManager::CreateDimpleFeatureBuilder Features::SheetMetal::SheetmetalManager::CreateDimpleFeatureBuilder@endlink  <br> */
            class NXOPENCPPEXPORT DimpleBuilder : public Features::FeatureBuilder
            {
                /** This enum represents the depth direction for the dimple. */
                public: enum DepthTypeOptions
                {
                    DepthTypeOptionsSectionNormalSide/** Dimple punched on the side of the section normal. */,
                    DepthTypeOptionsSectionReverseNormalSide/** Dimple punched on the side opposite to that of the section normal */
                };

                /** This enum represents the side of the section that the dimple punches material. The "left" option
                            represents the side to the left of a person who is walking along the section in the direction of its curves
                            when the section normal is pointing up. The "right" option represents the person's right hand side.
                            This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
                            along the section can also be represented by the vector resulting from the cross product of the curve tangent
                            (of the section curve at that point) and the section normal. The "left" side is the opposite. */
                public: enum SectionSideOptions
                {
                    SectionSideOptionsLeft/** Side pointed to by the inverse of the tangent cross normal vector */,
                    SectionSideOptionsRight/** Side pointed to by the tangent cross normal vector */
                };

                /** the Dimension options for dimple. This specifies whether the dimple's depth must be measured from the plane to which the section
                            is attached or from the */
                public: enum DimensionTypeOptions
                {
                    DimensionTypeOptionsOffset/** the actual depth will be depth plus the thickness of sheet. */,
                    DimensionTypeOptionsFull/** the actual extent distance will be the value specified as depth. */
                };

                /** the side walls material option. This specifies whether the dimple's outerwalls or the innerwalls coincide with the section outline */
                public: enum SidewallTypeOptions
                {
                    SidewallTypeOptionsOutside/** the innerface of the dimple side walls coincides with the section outline. */,
                    SidewallTypeOptionsInside/** the outerface of the dimple side walls coincides with the section outline. */
                };

                private: friend class  _DimpleBuilderBuilder;
                protected: DimpleBuilder();
                /**Returns  the Section used by the Dimple. Section can be Open/Closed.
                             <br> 
                                The section is protruded on the reference face at finite distance of extent and in the direction of
                                extent side. The actual extent distance will be determined by the active dimension option i.e. Offset
                                Dimension or Full Dimension. In case of Offset Dimension the actual extent distance will be offset
                                dimension distance plus the thickness of sheet. In case of Full Dimension the actual extent distance
                                will be the Full dimension distance.
                                In case of open section, the end segments are extended to the nearest flat face edges. If the end
                                segments are already crossing the flat face edges, those segments will be trimmed to the edges.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Section * Section
                (
                );
                /**Sets  the Section used by the Dimple. Section can be Open/Closed.
                             <br> 
                                The section is protruded on the reference face at finite distance of extent and in the direction of
                                extent side. The actual extent distance will be determined by the active dimension option i.e. Offset
                                Dimension or Full Dimension. In case of Offset Dimension the actual extent distance will be offset
                                dimension distance plus the thickness of sheet. In case of Full Dimension the actual extent distance
                                will be the Full dimension distance.
                                In case of open section, the end segments are extended to the nearest flat face edges. If the end
                                segments are already crossing the flat face edges, those segments will be trimmed to the edges.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetSection
                (
                    NXOpen::Section * section /** section */ 
                );
                /**Returns  the section Side for the Dimple section.
                             <br> 
                                This is used to specify which side of the section should remain stationary during the Dimple operation.
                                Dimple's section is a set of connected curves. The material exists on both sides of the section curves.
                                section Side specifies - the material on which side of the curve must be punched.The other side shall
                                be bent to the specified angle with respect to this fixed side. This is how you calculate Left/Right.
                                Get the Section Normal (N)Get the Tangent of the section.(T) Result =  CrossProduct(N, T). The resultant
                                vector is called RIGHT. This vector shall be in the direction of one if the two sides of the material.If
                                you want the material on the side of Result to be punched, then you have to pass the value of
                                @link Features::SheetMetal::DimpleBuilder::SectionSideOptionsRight Features::SheetMetal::DimpleBuilder::SectionSideOptionsRight@endlink  If you want the
                                other side to be punched, then you have to send @link Features::SheetMetal::DimpleBuilder::SectionSideOptionsLeft Features::SheetMetal::DimpleBuilder::SectionSideOptionsLeft@endlink .
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::DimpleBuilder::SectionSideOptions SectionSide
                (
                );
                /**Sets  the section Side for the Dimple section.
                             <br> 
                                This is used to specify which side of the section should remain stationary during the Dimple operation.
                                Dimple's section is a set of connected curves. The material exists on both sides of the section curves.
                                section Side specifies - the material on which side of the curve must be punched.The other side shall
                                be bent to the specified angle with respect to this fixed side. This is how you calculate Left/Right.
                                Get the Section Normal (N)Get the Tangent of the section.(T) Result =  CrossProduct(N, T). The resultant
                                vector is called RIGHT. This vector shall be in the direction of one if the two sides of the material.If
                                you want the material on the side of Result to be punched, then you have to pass the value of
                                @link Features::SheetMetal::DimpleBuilder::SectionSideOptionsRight Features::SheetMetal::DimpleBuilder::SectionSideOptionsRight@endlink  If you want the
                                other side to be punched, then you have to send @link Features::SheetMetal::DimpleBuilder::SectionSideOptionsLeft Features::SheetMetal::DimpleBuilder::SectionSideOptionsLeft@endlink .
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetSectionSide
                (
                    NXOpen::Features::SheetMetal::DimpleBuilder::SectionSideOptions sectionSide /** section side */ 
                );
                /** Depth of the Dimple @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * GetDepth
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetDepth
                (
                    const NXString & extent /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the Direction in which the Dimple is punched.
                             <br> 
                                This is used to specify the direction in which the punching should happen. If Punching must happen in the
                                direction of the Section Normal (specified using the @link Features::SheetMetal::DimpleBuilder::Section Features::SheetMetal::DimpleBuilder::Section @endlink and @link Features::SheetMetal::DimpleBuilder::SetSection Features::SheetMetal::DimpleBuilder::SetSection @endlink ) then
                                pass the value of @link Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionNormalSide Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionNormalSide@endlink 
                                If punching must happen in the opposite direction to that of Section Normal, set the value to be
                                @link Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionReverseNormalSide Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionReverseNormalSide@endlink 
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::DimpleBuilder::DepthTypeOptions DepthType
                (
                );
                /**Sets  the Direction in which the Dimple is punched.
                             <br> 
                                This is used to specify the direction in which the punching should happen. If Punching must happen in the
                                direction of the Section Normal (specified using the @link Features::SheetMetal::DimpleBuilder::Section Features::SheetMetal::DimpleBuilder::Section @endlink and @link Features::SheetMetal::DimpleBuilder::SetSection Features::SheetMetal::DimpleBuilder::SetSection @endlink ) then
                                pass the value of @link Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionNormalSide Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionNormalSide@endlink 
                                If punching must happen in the opposite direction to that of Section Normal, set the value to be
                                @link Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionReverseNormalSide Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionReverseNormalSide@endlink 
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetDepthType
                (
                    NXOpen::Features::SheetMetal::DimpleBuilder::DepthTypeOptions depthType /** depth type */ 
                );
                /** Taper Angle of the Dimple.
                             <br> 
                                In case of a tapered dimple, the taper angle is applied on the side faces of the above-protruded section.
                                The affects of taper angle will always increases the cavity volume of the dimple.
                             <br> 
                         @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * GetTaperAngle
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetTaperAngle
                (
                    const NXString & taperAngle /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the Rounding type of the Sharp edges of bottom face and top face.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: bool IncludeRounding
                (
                );
                /**Sets  the Rounding type of the Sharp edges of bottom face and top face.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetIncludeRounding
                (
                    bool includeRounding /** include rounding */ 
                );
                /** Radius value of the sharp edges on the top face @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * GetPunchRadius
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetPunchRadius
                (
                    const NXString & punchRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Radius value of the sharp edges of the bottom face @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * GetDieRadius
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetDieRadius
                (
                    const NXString & dieRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the Rounding Option for section Corners which contain Non Fillet Radii
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: bool FilletSectionCorners
                (
                );
                /**Sets  the Rounding Option for section Corners which contain Non Fillet Radii
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetFilletSectionCorners
                (
                    bool filletSectionCorners /** fillet section corners */ 
                );
                /** Fillet Radius to be applied for rounding the Sharp section Corners
                         @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * GetFilletRadius
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetFilletRadius
                (
                    const NXString & filletRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the Offset Dimension
                             <br> 
                                The actual extent distance of the Dimple will be determined by the active dimension option.
                                In case of @link Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsOffset Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsOffset@endlink  the actual extent distance will be offset dimension distance plus the thickness of sheet.
                                In case of @link Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsFull Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsFull@endlink  the actual extent distance will be the Full dimension distance.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::DimpleBuilder::DimensionTypeOptions DimensionType
                (
                );
                /**Sets  the Offset Dimension
                             <br> 
                                The actual extent distance of the Dimple will be determined by the active dimension option.
                                In case of @link Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsOffset Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsOffset@endlink  the actual extent distance will be offset dimension distance plus the thickness of sheet.
                                In case of @link Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsFull Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsFull@endlink  the actual extent distance will be the Full dimension distance.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetDimensionType
                (
                    NXOpen::Features::SheetMetal::DimpleBuilder::DimensionTypeOptions dimensionType /** dimension type */ 
                );
                /**Returns  the side where the material must be added to the dimple. Done with Respect to the section
                             <br> 
                                If @link Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsInside Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsInside@endlink  is specified, the material of the dimple sidewalls will be added to the interior of the section.
                                If @link Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsOutside Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsOutside@endlink  is specified,the material will be added from the lifted section such that the volume of the dimple cavity is increased.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::DimpleBuilder::SidewallTypeOptions SidewallType
                (
                );
                /**Sets  the side where the material must be added to the dimple. Done with Respect to the section
                             <br> 
                                If @link Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsInside Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsInside@endlink  is specified, the material of the dimple sidewalls will be added to the interior of the section.
                                If @link Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsOutside Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsOutside@endlink  is specified,the material will be added from the lifted section such that the volume of the dimple cavity is increased.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetSidewallType
                (
                    NXOpen::Features::SheetMetal::DimpleBuilder::SidewallTypeOptions sidewallType /** sidewall type */ 
                );
                /**Returns  the Slave Sketch used by the Dimple, If one exists.
                             <br> 
                                If the Sketch is created internally as part of the Dimple command in the UI, then it shall be consumed by the Dimple and shall not show up as a seperate feature in the Part Navigator.
                                If such a behaviour is deired, then specify the Sketch here.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SketchFeature * Sketch
                (
                );
                /**Sets  the Slave Sketch used by the Dimple, If one exists.
                             <br> 
                                If the Sketch is created internally as part of the Dimple command in the UI, then it shall be consumed by the Dimple and shall not show up as a seperate feature in the Part Navigator.
                                If such a behaviour is deired, then specify the Sketch here.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetSketch
                (
                    NXOpen::Features::SketchFeature * sketch /** sketch */ 
                );
                /** Verify whether the builder data is valid for creating a dimple or not.
                             <br> 
                                 If the Builder data is valid, returned value shall be 0

                             <br> 
                         @return  Data Validity Flag. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int ValidateBuilderData
                (
                );
                /**Returns  
                         the minimum tool clearance expression.
                           
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * MinimumToolClearance
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
