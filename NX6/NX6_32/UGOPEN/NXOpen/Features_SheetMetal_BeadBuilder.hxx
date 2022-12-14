#ifndef NXOpen_FEATURES_SHEETMETAL_BEADBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_BEADBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_BeadBuilder.ja
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
            class BeadBuilder;
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
            class _BeadBuilderBuilder;
            /** Represents a Bead feature builder.  <br> To create a new instance of this class, use @link Features::SheetMetal::SheetmetalManager::CreateBeadFeatureBuilder Features::SheetMetal::SheetmetalManager::CreateBeadFeatureBuilder@endlink  <br> */
            class NXOPENCPPEXPORT BeadBuilder : public Features::FeatureBuilder
            {
                /** This enum represents the cross section type options for the Bead.*/
                public: enum CrossSectionTypeOptions
                {
                    CrossSectionTypeOptionsCircular/** circular */ ,
                    CrossSectionTypeOptionsUshaped/** ushaped */ ,
                    CrossSectionTypeOptionsVshaped/** vshaped */ 
                };

                /** This enum represents the end type options for the Bead.*/
                public: enum EndTypeOptions
                {
                    EndTypeOptionsPunched/** punched */ ,
                    EndTypeOptionsLanced/** lanced */ ,
                    EndTypeOptionsFormed/** formed */ 
                };

                /** This enum represents the depth direction for the Bead. */
                public: enum HeightSideOptions
                {
                    HeightSideOptionsSectionNormalSide/** Material removed on the side of the section normal. */,
                    HeightSideOptionsSectionReverseNormalSide/** Material removed on the side opposite to that of the section normal */
                };

                private: friend class  _BeadBuilderBuilder;
                protected: BeadBuilder();
                /**Returns  the Section used by the bead. section should be open. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Section * Section
                (
                );
                /**Sets  the Section used by the bead. section should be open. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetSection
                (
                    NXOpen::Section * section /** section */ 
                );
                /**Returns  the height of the bead. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Height
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetHeight
                (
                    const NXString & beadHeight /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the width of the bead. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Width
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetWidth
                (
                    const NXString & beadWidth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the angle of the bead. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Angle
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetAngle
                (
                    const NXString & beadAngle /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the radius of the bead. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Radius
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetRadius
                (
                    const NXString & beadRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the Punched width of the bead. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * PunchedWidth
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetPunchedWidth
                (
                    const NXString & punchedWidth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the bead punch radius. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * PunchRadius
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetPunchRadius
                (
                    const NXString & punchRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the bead die radius. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * DieRadius
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetDieRadius
                (
                    const NXString & beadDieRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the Height side for the bead.
                             <br> 
                                This is used to specify the direction in which the Bead is created. If Bead creation must happen in the
                                direction of the Section Normal (specified using the @link Features::SheetMetal::BeadBuilder::Section Features::SheetMetal::BeadBuilder::Section @endlink and @link Features::SheetMetal::BeadBuilder::SetSection Features::SheetMetal::BeadBuilder::SetSection @endlink ) then
                                pass the value of @link Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionNormalSide Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionNormalSide@endlink 
                                If Bead creation must happen in the opposite direction to that of Section Normal, set the value to be
                                @link Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionReverseNormalSide Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionReverseNormalSide@endlink 
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BeadBuilder::HeightSideOptions HeightSide
                (
                );
                /**Sets  the Height side for the bead.
                             <br> 
                                This is used to specify the direction in which the Bead is created. If Bead creation must happen in the
                                direction of the Section Normal (specified using the @link Features::SheetMetal::BeadBuilder::Section Features::SheetMetal::BeadBuilder::Section @endlink and @link Features::SheetMetal::BeadBuilder::SetSection Features::SheetMetal::BeadBuilder::SetSection @endlink ) then
                                pass the value of @link Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionNormalSide Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionNormalSide@endlink 
                                If Bead creation must happen in the opposite direction to that of Section Normal, set the value to be
                                @link Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionReverseNormalSide Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionReverseNormalSide@endlink 
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetHeightSide
                (
                    NXOpen::Features::SheetMetal::BeadBuilder::HeightSideOptions heightSide /** height side */ 
                );
                /**Returns  the rounding type .
                             <br> 
                                Specify true to Round the Sharp edges.
                                Specify false to avoid rounding.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: bool IncludeRounding
                (
                );
                /**Sets  the rounding type .
                             <br> 
                                Specify true to Round the Sharp edges.
                                Specify false to avoid rounding.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetIncludeRounding
                (
                    bool rounding /** rounding */ 
                );
                /**Returns  the bead end type .
                             <br> 
                                Specify @link Features::SheetMetal::BeadBuilder::EndTypeOptionsFormed  Features::SheetMetal::BeadBuilder::EndTypeOptionsFormed @endlink  to have ends of bead feature be formed.
                                Specify @link Features::SheetMetal::BeadBuilder::EndTypeOptionsLanced  Features::SheetMetal::BeadBuilder::EndTypeOptionsLanced @endlink  to have ends of bead feature be Lanced.
                                Specify @link Features::SheetMetal::BeadBuilder::EndTypeOptionsPunched Features::SheetMetal::BeadBuilder::EndTypeOptionsPunched@endlink  to have ends of bead feature be Punched.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptions EndType
                (
                );
                /**Sets  the bead end type .
                             <br> 
                                Specify @link Features::SheetMetal::BeadBuilder::EndTypeOptionsFormed  Features::SheetMetal::BeadBuilder::EndTypeOptionsFormed @endlink  to have ends of bead feature be formed.
                                Specify @link Features::SheetMetal::BeadBuilder::EndTypeOptionsLanced  Features::SheetMetal::BeadBuilder::EndTypeOptionsLanced @endlink  to have ends of bead feature be Lanced.
                                Specify @link Features::SheetMetal::BeadBuilder::EndTypeOptionsPunched Features::SheetMetal::BeadBuilder::EndTypeOptionsPunched@endlink  to have ends of bead feature be Punched.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetEndType
                (
                    NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptions beadEndOptions /** bead end options */ 
                );
                /**Returns  the bead profile type .
                             <br> 
                                Specify @link Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsCircular Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsCircular@endlink  to have profile of half circle.
                                Specify @link Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsUshaped Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsUshaped@endlink  to have profile of U shape.
                                Specify @link Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsVshaped Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsVshaped@endlink  to have profile of V shape.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BeadBuilder::CrossSectionTypeOptions CrossSectionType
                (
                );
                /**Sets  the bead profile type .
                             <br> 
                                Specify @link Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsCircular Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsCircular@endlink  to have profile of half circle.
                                Specify @link Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsUshaped Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsUshaped@endlink  to have profile of U shape.
                                Specify @link Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsVshaped Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsVshaped@endlink  to have profile of V shape.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetCrossSectionType
                (
                    NXOpen::Features::SheetMetal::BeadBuilder::CrossSectionTypeOptions crossSectionOption /** cross section option */ 
                );
                /**Returns  the Slave Sketch used by the Bead, If one exists.
                             <br> 
                                If the Sketch is created internally as part of the Bead command in the UI, then it shall be consumed by the Bead and shall not show up as a seperate feature in the Part Navigator.
                                If such a behaviour is deired, then specify the Sketch here.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SketchFeature * Sketch
                (
                );
                /**Sets  the Slave Sketch used by the Bead, If one exists.
                             <br> 
                                If the Sketch is created internally as part of the Bead command in the UI, then it shall be consumed by the Bead and shall not show up as a seperate feature in the Part Navigator.
                                If such a behaviour is deired, then specify the Sketch here.
                             <br> 
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetSketch
                (
                    NXOpen::Features::SketchFeature * sketch /** sketch */ 
                );
                /** Verify whether the builder data is valid for creating a Bead or not.
                             <br> 
                                 If the Builder data is valid, returned value shall be 0

                             <br> 
                         @return  Data Validity Flag. <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int ValidateBuilderData
                (
                );
                /**Returns  
                         the Minimum tool clearance expression.           
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
