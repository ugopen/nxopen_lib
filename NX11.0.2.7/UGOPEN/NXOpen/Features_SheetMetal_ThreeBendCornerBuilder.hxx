#ifndef NXOpen_FEATURES_SHEETMETAL_THREEBENDCORNERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_THREEBENDCORNERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_ThreeBendCornerBuilder.ja
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
            class ThreeBendCornerBuilder;
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
            class _ThreeBendCornerBuilderBuilder;
            class ThreeBendCornerBuilderImpl;
            /** The Three Bend Corner feature class. Users can identify multiple input face pairs for each three bend 
                    corner feature. Each pair is made up of one face each from adjacent bends. The bends must both have the 
                    same radius and sweep angle, and they must also be connected via another adjoining bend.
                 <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::SheetmetalManager::CreateThreeBendCornerFeatureBuilder  NXOpen::Features::SheetMetal::SheetmetalManager::CreateThreeBendCornerFeatureBuilder @endlink  <br> 
             <br>  Created in NX4.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ThreeBendCornerBuilder : public NXOpen::Features::FeatureBuilder
            {
                /** This enum represents the corner treatment type. */
                public: enum TreatmentTypeOptions
                {
                    TreatmentTypeOptionsOpen/** open */ ,
                    TreatmentTypeOptionsClosed/** closed */ ,
                    TreatmentTypeOptionsCircularCutout/** circular cutout */ ,
                    TreatmentTypeOptionsUCutout/** ucutout */ ,
                    TreatmentTypeOptionsVCutout/** vcutout */ 
                };

                /**This enum represents Origin type*/
                public: enum OriginTypes
                {
                    OriginTypesBendCenter/** The relief origin will be at the intersection of first bend's centerline and bisector of corner angle. */,
                    OriginTypesCornerPoint/** The relief origin will be at the corner point.*/
                };

                private: ThreeBendCornerBuilderImpl * m_threebendcornerbuilder_impl;
                private: friend class  _ThreeBendCornerBuilderBuilder;
                protected: ThreeBendCornerBuilder();
                public: ~ThreeBendCornerBuilder();
                /** Input a bend face pair for the three bend corner feature. This method can be called multiple  
                           times for a feature, with each bend face pair representing a unique corner.
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void AddFacePair
                (
                    NXOpen::Face * firstFace /**  A bend face from a bend */,
                    NXOpen::Face * secondFace /**  A bend face from an adjacent bend */
                );
                /** Removes a face pair (that represents a unique corner) from the list of face pairs already added.
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void RemoveFacePair
                (
                    NXOpen::Face * firstFace /** A face from an already selected face pair */,
                    NXOpen::Face * secondFace /** The other face from the face pair */
                );
                /**Returns  the number of face pairs already identified for the three bend corner feature.
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int NumberOfFacePairs
                (
                );
                /** Gets the bend face pair at the given index. The index can vary between zero and one less than the 
                            value returned by @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::NumberOfFacePairs NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::NumberOfFacePairs@endlink .
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void GetFacePair
                (
                    int index /** Index of the desired face pair */,
                    NXOpen::Face ** firstFace /** First face of the face pair */,
                    NXOpen::Face ** secondFace /** Second face of the face pair */
                );
                /**Returns  the corner treatment type.
                             <br> 
                                The @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentType NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentType @endlink and @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::SetTreatmentType NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::SetTreatmentType @endlink ) specifies how the 
                                corner should be treated. Valid options are in @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptions NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptions@endlink . 
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptions TreatmentType
                (
                );
                /**Sets  the corner treatment type.
                             <br> 
                                The @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentType NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentType @endlink and @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::SetTreatmentType NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::SetTreatmentType @endlink ) specifies how the 
                                corner should be treated. Valid options are in @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptions NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptions@endlink . 
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetTreatmentType
                (
                    NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptions treatmentType /** The type of treatment specified for the corner*/
                );
                /**Returns  the diameter used for circular, u and v cutout corner treatments. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Diameter
                (
                );
                /** The diameter used for the circular cutout corner treatment. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout@endlink  or 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .            .
                        
                 <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Expression::SetRightHandSide NXOpen::Expression::SetRightHandSide@endlink  on the @link NXOpen::Expression NXOpen::Expression@endlink  object returned from @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::Diameter NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::Diameter@endlink  instead. <br>  

                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::Expression::SetRightHandSide on the NXOpen::Expression object returned from NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::Diameter instead.") void SetDiameter
                (
                    const NXString & diameter /** The diameter for the circular cutout corner treatment */
                );
                /** The diameter used for the circular cutout corner treatment. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout@endlink  or 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .            .
                        
                 <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Expression::SetRightHandSide NXOpen::Expression::SetRightHandSide@endlink  on the @link NXOpen::Expression NXOpen::Expression@endlink  object returned from @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::Diameter NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::Diameter@endlink  instead. <br>  

                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                void SetDiameter
                (
                    const char * diameter /** The diameter for the circular cutout corner treatment */
                );
                /**Returns  the relief origin used for circular, u and v cutout corner treatments. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .
                        
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::OriginTypes OriginType
                (
                );
                /**Sets  the relief origin used for circular, u and v cutout corner treatments. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .
                        
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetOriginType
                (
                    NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::OriginTypes originType /** The relief origin type*/
                );
                /**Returns  the offset used for circular, u and v cutout corner treatments. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .
                        
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * Offset
                (
                );
                /** Verify that the builder data is valid for creation of a three bend corner.
                             <br> 
                                 If the data in the builder is valid, the return value is 0
                             <br> 
                         @return  Returns 0 if the data in the builder is valid 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int ValidateBuilderData
                (
                );
                /**Returns  the angle 1 used for the v cutout treatment. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .
                        
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * VCutoutAngle1
                (
                );
                /**Returns  the angle 2 used for the v cutout treatment. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .
                        
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * VCutoutAngle2
                (
                );
                /**Returns  the miter root radius used for three bend corner miter treatment. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsClosed NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsClosed@endlink .
                        
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * MiterRootRadius
                (
                );
                /**Returns  the blend miter radius used for three bend corner miter treatment. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsClosed NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsClosed@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout@endlink  or 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .  
                        
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * BlendMiterRadius
                (
                );
                /**Returns  the flange clearance used for three bend corner miter treatment. This only applies when the treatment type is set to 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsOpen NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsOpen@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsClosed NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsClosed@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout@endlink  or 
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout@endlink  or
                            @link NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout@endlink .  
                        
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * FlangeClearance
                (
                );
                /**Returns  whether the corner will be closed using miter.
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: bool MiterCorner
                (
                );
                /**Sets  whether the corner will be closed using miter.
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetMiterCorner
                (
                    bool miterCorner /** mitercorner */ 
                );
                /**Returns  the option for smooth transition from miter to cutout edges.
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: bool BlendMiter
                (
                );
                /**Sets  the option for smooth transition from miter to cutout edges.
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBlendMiter
                (
                    bool blendMiter /** blendmiter */ 
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