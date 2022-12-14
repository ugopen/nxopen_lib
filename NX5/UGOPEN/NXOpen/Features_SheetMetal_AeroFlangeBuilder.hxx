#ifndef NXOpen_FEATURES_SHEETMETAL_AEROFLANGEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_AEROFLANGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_AeroFlangeBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class AeroFlangeBuilder;
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
    class Plane;
    class ScCollector;
    namespace Features
    {
        namespace SheetMetal
        {
            class _AeroFlangeBuilderBuilder;
            /** Represents a Aerospace Sheet Metal Flange Builder. 
                     <br> To create a new instance of this class, use @link Features::SheetMetal::AeroSheetmetalManager::CreateFlangeBuilder Features::SheetMetal::AeroSheetmetalManager::CreateFlangeBuilder@endlink  <br> */
            class NXOPENCPPEXPORT AeroFlangeBuilder : public Features::FeatureBuilder
            {
                /** This enum defines the length type options. 
                            */
                public: enum LengthType
                {
                    LengthTypeValue/** Value */,
                    LengthTypeInfer/** Infer from face */
                };

                /** This enum defines the ends of a bend edge 
                            */
                public: enum EndType
                {
                    EndTypeEnd1/** Start of section */,
                    EndTypeEnd2/** End of section */,
                    EndTypeClosed/** Periodic Bend Edge */
                };

                /** This enum defines the type of direction vector 
                            */
                public: enum DirType
                {
                    DirTypeBend/** Bend Direction Type */,
                    DirTypeDiscard/** Discard Direction Type */
                };

                /** This method defines the types of Flange Compensation 
                            */
                public: enum CompType
                {
                    CompTypeAutomatic/** Automatic */,
                    CompTypeAngle/** Angle */,
                    CompTypeDistance/** Distance */,
                    CompTypeNone/** None */
                };

                /** This enum defines the material types 
                            */
                public: enum MatType
                {
                    MatTypeMaterialInside/** Material Inside */,
                    MatTypeMaterialOutside/** Material Outside */,
                    MatTypeBendOutside/** Bend Outside */
                };

                /** This enum defines the flange length dimension types 
                            */
                public: enum DimType
                {
                    DimTypeInside/** Inside Dimension */,
                    DimTypeOutside/** Outside Dimension */
                };

                private: friend class  _AeroFlangeBuilderBuilder;
                protected: AeroFlangeBuilder();
                /**Sets  the base edge section object for the flange.
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetBaseEdges
                (
                    NXOpen::ScCollector * base_edges /** Base Edges */
                );
                /**Returns  the base edge section object for the flange.
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::ScCollector * BaseEdges
                (
                );
                /**Sets  the ref face smart collector object
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetRefFaces
                (
                    NXOpen::ScCollector * face_collector /** face collector */ 
                );
                /**Returns  the ref face smart collector object
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::ScCollector * RefFaces
                (
                );
                public: void SetAngle
                (
                    const NXString & angle_expression /** value of angle expression   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the angle expression. 
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Expression * Angle
                (
                );
                /** Set the type of length and the length expression. 
                                If there are no ref_face's then the only length type 
                                possible is "Value". If there are selected ref_face's 
                                and the length type is "Infer", then the length 
                                expression should be NULL.
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetLength
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::LengthType type /** length type input Value/Infer */,
                    const NXString & value_expression /** value of length expression   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Get the type of length and the length expression. 
                             @return  tag of length expression  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Expression * GetLength
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::LengthType* type /** length type Value/Infer */
                );
                /** Set flip direction.
                                This method is called if either the bend direction or the
                                material direction needs to be flipped. 
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetFlipDirection
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::DirType type /** direction type bend/discard */,
                    bool flip_flag /** flip_flag => false = do not flip, true = flip */
                );
                /** Get flip direction. 
                             @return  flip_flag => false = do not flip, true = flip  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: bool GetFlipDirection
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::DirType type /** direction type bend/discard */
                );
                /** Set end compensation.
                                This method sets the flange compensation for one end of a non-periodic
                                Base Edge section. The end_type input parameter denotes if the end is
                                the start of section(end1) or the end of section(end2). If the compensation
                                type( comp_type) is either Angle or Distance, an expression for the
                                value of compensation must be provided. This expression input can be NULL
                                for Automatic and None type of compensations.
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetEndCompensation
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::EndType end_type /** end1/end2 */,
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::CompType comp_type /** Automatic/Angle/Distance/None */,
                    const NXString & value_expression /** value of compensation expression   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Get end compensation.
                             @return  tag of compensation expression  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Expression * GetEndCompensation
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::EndType end_type /** end1/end2 */,
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::CompType* comp_type /** Automatic/Angle/Distance/None */
                );
                /** Set the end plane 
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetEndPlane
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::EndType end_type /** end1/end2 */,
                    NXOpen::Plane * end_plane /** smart plane entity */
                );
                /** Get the end plane 
                             @return  smart plane entity  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Plane * GetEndPlane
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::EndType end_type /** end1/end2 */
                );
                /** Set the flag that turns on/off the visibility of Contour Curve 
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetContourFlag
                (
                    bool show_contour /** false = Hide contour curve, true = Show contour curve */
                );
                /** Get the flag that turns on/off the visibility of Contour Curve 
                             @return  false = Hide contour curve, true = Show contour curve  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: bool GetContourFlag
                (
                );
                /** Set the material type of the flange 
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetMaterialType
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::MatType mat_type /** material inside/material outside/bend outside */
                );
                /** Get the material type of the flange 
                             @return  material inside/material outside/bend outside  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Features::SheetMetal::AeroFlangeBuilder::MatType GetMaterialType
                (
                );
                /** Set the length dimension type of the flange 
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetDimensionType
                (
                    NXOpen::Features::SheetMetal::AeroFlangeBuilder::DimType dim_type /** inside/outside */
                );
                /** Get the length dimension type of the flange 
                             @return  inside/outside  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Features::SheetMetal::AeroFlangeBuilder::DimType GetDimensionType
                (
                );
                /**Returns  the base edge section object for the flange.
                             <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BendOptions * BendOptions
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
