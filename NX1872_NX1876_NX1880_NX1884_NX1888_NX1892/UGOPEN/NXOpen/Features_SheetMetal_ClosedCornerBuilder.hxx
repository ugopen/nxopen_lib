#ifndef NXOpen_FEATURES_SHEETMETAL_CLOSEDCORNERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_CLOSEDCORNERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_ClosedCornerBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class ClosedCornerBuilder;
        }
    }
    class Expression;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class _ClosedCornerBuilderBuilder;
            class ClosedCornerBuilderImpl;
            /** Represents a Closed corner feature builder.  <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::SheetmetalManager::CreateClosedCornerFeatureBuilder  NXOpen::Features::SheetMetal::SheetmetalManager::CreateClosedCornerFeatureBuilder @endlink  <br> 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ClosedCornerBuilder : public NXOpen::Features::FeatureBuilder
            {
                /** This enum represents the feature types. */
                public: enum Types
                {
                    TypesCloseAndRelief/** close and relief */ ,
                    TypesRelief/** relief */ 
                };

                /**This enum represents Corner Closure type*/
                public: enum ClosureTypeOptions
                {
                    ClosureTypeOptionsClose/** close */ ,
                    ClosureTypeOptionsOverlap/** overlap */ 
                };

                /**This enum represents Corner treatment type*/
                public: enum TreatmentTypeOptions
                {
                    TreatmentTypeOptionsOpen/** Only Webs will be closed*/,
                    TreatmentTypeOptionsClosed/** Bend and Webs will be closed*/,
                    TreatmentTypeOptionsCircularCutout/** Circular shaped relief*/,
                    TreatmentTypeOptionsUCutout/** U shaped relief*/,
                    TreatmentTypeOptionsVCutout/** V shaped relief*/,
                    TreatmentTypeOptionsRectangularCutout/** Rectangular shaped relief*/
                };

                /**This enum represents Origin type*/
                public: enum OriginTypes
                {
                    OriginTypesBendCenter/** The relief origin will be at the intersection of first bend's centerline and bisector of corrner angle. */,
                    OriginTypesCornerPoint/** The relief origin will be at the corner point.*/
                };

                /**This enum represents cut method*/
                public: enum CutMethodTypes
                {
                    CutMethodTypesByTool/** The cut method will be by tool. */,
                    CutMethodTypesByPath/** The cut method will be by path.*/
                };

                private: ClosedCornerBuilderImpl * m_closedcornerbuilder_impl;
                private: friend class  _ClosedCornerBuilderBuilder;
                protected: ClosedCornerBuilder();
                public: ~ClosedCornerBuilder();
                /**Sets  the treatment type
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetTreatmentType
                (
                    NXOpen::Features::SheetMetal::ClosedCornerBuilder::TreatmentTypeOptions treatmentType /** The type of treatment specified for the corner*/
                );
                /**Returns  the treatment type
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ClosedCornerBuilder::TreatmentTypeOptions TreatmentType
                (
                );
                /**Sets  the closure type
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetClosureType
                (
                    NXOpen::Features::SheetMetal::ClosedCornerBuilder::ClosureTypeOptions closureType /** The type of closure specified for the corner*/
                );
                /**Returns  the closure type
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ClosedCornerBuilder::ClosureTypeOptions ClosureType
                (
                );
                /**Returns  the diameter.
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Diameter
                (
                );
                /**Returns  the gap.
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Gap
                (
                );
                /**Returns  the overlap.
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Overlap
                (
                );
                /** Add a face pair.
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void AddFacePair
                (
                    NXOpen::Face * firstFace /**  A bend face from a bend */,
                    NXOpen::Face * secondFace /**  A bend face from an adjacent bend */
                );
                /** Return the face pair. 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void GetFacePair
                (
                    int index /** Index of the desired face pair */,
                    NXOpen::Face ** firstFace /** First face of the face pair */,
                    NXOpen::Face ** secondFace /** Second face of the face pair */
                );
                /** Returns the number of face pairs already identified for the three bend corner feature.
                         @return  The number of face pairs currently identified 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int GetNumberOfFacePairs
                (
                );
                /** Validates the builder data. @return  Returns 0 if the data in the builder is valid 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int ValidateBuilderData
                (
                );
                /** Removes a face pair (that represents a unique corner) from the list of face pairs already added.
                        
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void RemoveFacePair
                (
                    NXOpen::Face * firstFace /** A face from an already selected face pair */,
                    NXOpen::Face * secondFace /** The other face from the face pair */
                );
                /**Returns  the feature type 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::ClosedCornerBuilder::Types Type
                (
                );
                /**Sets  the feature type 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetType
                (
                    NXOpen::Features::SheetMetal::ClosedCornerBuilder::Types type /** type */ 
                );
                /**Sets  the default origin will be at the corner point instead of the intersection of bend centerlines.
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetOrigin
                (
                    NXOpen::Features::SheetMetal::ClosedCornerBuilder::OriginTypes originType /** The default location of relief origin*/
                );
                /**Returns  the default origin will be at the corner point instead of the intersection of bend centerlines.
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ClosedCornerBuilder::OriginTypes Origin
                (
                );
                /**Returns  the value by which relief origin will be offset
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Offset
                (
                );
                /**Returns  the angle1 of V relief. This is the angle associated with the first bend selected.
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * VAngle1
                (
                );
                /**Returns  the angle2 of V relief. This is the angle associated to the second bend selected.
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * VAngle2
                (
                );
                /**Returns  the length of rectangular relief. The length is associated to the first bend selected.
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * RectangularLength
                (
                );
                /**Returns  the width of rectangular relief. The width is associated to the second bend selected. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * RectangularWidth
                (
                );
                /**Returns  the corner will be closed using the miter algorithm.
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: bool MiterCorner
                (
                );
                /**Sets  the corner will be closed using the miter algorithm.
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetMiterCorner
                (
                    bool miterCorner /** mitercorner */ 
                );
                /**Returns  the option for smooth transition from miter to cutout edges.
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: bool BlendMiter
                (
                );
                /**Sets  the option for smooth transition from miter to cutout edges.
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBlendMiter
                (
                    bool blendMiter /** blendmiter */ 
                );
                /**Returns  the cut method to be used for U/V cutout relief.
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::ClosedCornerBuilder::CutMethodTypes CutMethod
                (
                );
                /**Sets  the cut method to be used for U/V cutout relief.
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetCutMethod
                (
                    NXOpen::Features::SheetMetal::ClosedCornerBuilder::CutMethodTypes cutMethod /** The default location of relief origin*/
                );
                /**Returns  the length of U relief. 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Length
                (
                );
                /**Returns  the length of V relief associated with the first bend selected.
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Length1
                (
                );
                /**Returns  the length of V relief associated with the second bend selected.
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Length2
                (
                );
                /**Returns  the punch radius of tool associated with V relief.
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * PunchRadius
                (
                );
                /**Returns  the blend miter radius.
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * BlendMiterRadius
                (
                );
            };
        }
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
