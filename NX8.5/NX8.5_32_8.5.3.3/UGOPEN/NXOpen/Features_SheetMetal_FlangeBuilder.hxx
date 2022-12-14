#ifndef NXOpen_FEATURES_SHEETMETAL_FLANGEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_FLANGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_FlangeBuilder.ja
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
#include <NXOpen/Features_SheetMetal_SheetmetalBaseBuilder.hxx>
#include <NXOpen/Features_SheetMetal_BendOptions.hxx>
#include <NXOpen/ugmath.hxx>
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
            class FlangeBuilder;
        }
    }
    class Edge;
    class Expression;
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
            class SheetmetalBaseBuilder;
        }
    }
    class Plane;
    class Sketch;
    namespace Features
    {
        namespace SheetMetal
        {
            class _FlangeBuilderBuilder;
            class FlangeBuilderImpl;
            /** Represents a Flange feature builder.  <br> To create a new instance of this class, use @link Features::SheetMetal::SheetmetalManager::CreateFlangeFeatureBuilder  Features::SheetMetal::SheetmetalManager::CreateFlangeFeatureBuilder @endlink  <br> 
             <br>  Created in NX4.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  FlangeBuilder : public Features::SheetMetal::SheetmetalBaseBuilder
            {
                /** This enum represents the inset type for the material of the flange. */
                public: enum InsetTypeOptions
                {
                    InsetTypeOptionsMaterialInside/** The flange is flush with the thickness face on the inside */,
                    InsetTypeOptionsMaterialOutside/** The flange is flush with the thickness face on the outside */,
                    InsetTypeOptionsBendOutside/** The bend and flange are outside the thickness face */
                };

                /** This enum indicates the two ways that the flange length can be measured. */
                public: enum LengthTypeOptions
                {
                    LengthTypeOptionsInsideDimension/** The flange length is dimensioned to the Inner Mold line. */,
                    LengthTypeOptionsOutsideDimension/** The flange length is dimensioned to the Outer Mold Line. */,
                    LengthTypeOptionsWebDimension/** The flange length is dimensioned to the Bend Tangent Line. */
                };

                /** This enum represents the offset type for the flange. */
                public: enum OffsetTypeOptions
                {
                    OffsetTypeOptionsInside/** The flange is offset to the inside of the face */,
                    OffsetTypeOptionsOutside/** The flange is offset to the outside of the face */
                };

                /** This enum represents the width type for the flange. */
                public: enum WidthTypeOptions
                {
                    WidthTypeOptionsFullEdge/** The flange spans the entire edge. */,
                    WidthTypeOptionsCenterOfEdge/** The flange is centered on the edge. */,
                    WidthTypeOptionsAtEdgeEnd/** The flange starts from the specified end of the edge. */,
                    WidthTypeOptionsFromEdgeEnd/** The flange starts at a specified distance from an end of the edge. */,
                    WidthTypeOptionsFromBothEnds/** The flange starts and ends at specified distances from the ends of the edge. */,
                    WidthTypeOptionsCustom/** The flange sketch has been edited after creation and may or may not conform to any of the above. */
                };

                /** This enum represents the match face option for the flange. */
                public: enum MatchFaceOptions
                {
                    MatchFaceOptionsNone/** The flange is placed on the selected edge */,
                    MatchFaceOptionsUntilSelected/** The flange face is extended until the selected plane */
                };

                private: FlangeBuilderImpl * m_flangebuilder_impl;
                private: friend class  _FlangeBuilderBuilder;
                protected: FlangeBuilder();
                public: ~FlangeBuilder();
                /**Returns  the edge on which the flange is created.
                             <br> 
                                The edge should be linear and it should not be a thickness edge.
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Edge * Edge
                (
                );
                /**Sets  the edge on which the flange is created.
                             <br> 
                                The edge should be linear and it should not be a thickness edge.
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetEdge
                (
                    NXOpen::Edge * edge /** The flange is created on this edge. */
                );
                /**Returns  the bend options object. 
                             <br> 
                            The bend options object stores additional parameters for the bend, such as bend radius, bend 
                            relief width and depth, corner relief type etc.
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Features::SheetMetal::BendOptions * BendOptions
                (
                );
                /**Returns  the offset type for the flange.  
                             <br> 
                                Describes the value of the offset in @link Offset Offset @endlink and @link SetOffset SetOffset @endlink .
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Features::SheetMetal::FlangeBuilder::OffsetTypeOptions OffsetType
                (
                );
                /**Sets  the offset type for the flange.  
                             <br> 
                                Describes the value of the offset in @link Offset Offset @endlink and @link SetOffset SetOffset @endlink .
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetOffsetType
                (
                    NXOpen::Features::SheetMetal::FlangeBuilder::OffsetTypeOptions offsetType /** The flange can be offset inside or outside. */
                );
                /**Returns  the offset value for the flange. 
                             <br> 
                                The direction of the offset is determined by the value off @link OffsetType OffsetType@endlink . 
                             <br> 
                         
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Expression * Offset
                (
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetOffset
                (
                    const NXString & offset /** The flange offset value   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                void SetOffset
                (
                    const char * offset /** The flange offset value   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the length of the flange.
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Expression * Length
                (
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetLength
                (
                    const NXString & length /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                void SetLength
                (
                    const char * length /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  a enum indicating the length type.        
                        For Features created in NX8 and above:
                        The way length is measured for the flange. It can either be measure from the inside edge or the outside edge.
                             <br> 
                                Flange length can be specified starting from the selected edge or from the corresponding edge on the other face 
                                (other linear edge on the other side of the thickness face). If the length is specified from the
                                selected edge use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension@endlink  or
                                if the flange length is specifed from the other edge use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension@endlink .
                             <br> 
                        
                        For Features created in NX8 and above:        
                        Flange length can be measure from the Inner Mold Line, Outer Mold Line or Bend Tangent Line.
                             <br> 
                                Inner Mold Line: Intersection of inner tab face and inner flange web face
                                Outer Mold Line: Intersection of outer tab face and outer flange web face
                                Bend  Tangent Line: common edge between flange web face and bend face.
                                
                                Flange length can be specified starting from the inner mold line or outer mold line or bend tangent line. If the length is specified from the
                                inner mold line use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension@endlink  or
                                if the flange length is specifed from the outer mold line use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension@endlink or
                                if the flange length is specifed from the bend tangent line use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsWebDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsWebDimension@endlink .
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptions LengthType
                (
                );
                /**Sets  a enum indicating the length type.        
                        For Features created in NX8 and above:
                        The way length is measured for the flange. It can either be measure from the inside edge or the outside edge.
                             <br> 
                                Flange length can be specified starting from the selected edge or from the corresponding edge on the other face 
                                (other linear edge on the other side of the thickness face). If the length is specified from the
                                selected edge use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension@endlink  or
                                if the flange length is specifed from the other edge use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension@endlink .
                             <br> 
                        
                        For Features created in NX8 and above:        
                        Flange length can be measure from the Inner Mold Line, Outer Mold Line or Bend Tangent Line.
                             <br> 
                                Inner Mold Line: Intersection of inner tab face and inner flange web face
                                Outer Mold Line: Intersection of outer tab face and outer flange web face
                                Bend  Tangent Line: common edge between flange web face and bend face.
                                
                                Flange length can be specified starting from the inner mold line or outer mold line or bend tangent line. If the length is specified from the
                                inner mold line use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension@endlink  or
                                if the flange length is specifed from the outer mold line use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension@endlink or
                                if the flange length is specifed from the bend tangent line use value @link Features::SheetMetal::FlangeBuilder::LengthTypeOptionsWebDimension Features::SheetMetal::FlangeBuilder::LengthTypeOptionsWebDimension@endlink .
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetLengthType
                (
                    NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptions lengthType /** length type */ 
                );
                /**Returns  the inset type (inside, outside, bendoutside) for the flange.

                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Features::SheetMetal::FlangeBuilder::InsetTypeOptions InsetType
                (
                );
                /**Sets  the inset type (inside, outside, bendoutside) for the flange.

                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetInsetType
                (
                    NXOpen::Features::SheetMetal::FlangeBuilder::InsetTypeOptions insetType /** inset type */ 
                );
                /**Returns  the width type for flange.
                             <br> 
                                Use one of the values from @link Features::SheetMetal::FlangeBuilder::WidthTypeOptions Features::SheetMetal::FlangeBuilder::WidthTypeOptions@endlink . Depending on which of the 
                                values from the enum is used, none, either or both of the distance values from 
                                @link FirstDistance FirstDistance@endlink   and @link SecondDistance SecondDistance@endlink 
                                may be used. Here is a description of the distances:
                                
                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFullEdge Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFullEdge@endlink , then both the @link FirstDistance FirstDistance@endlink 
                                and @link SecondDistance SecondDistance@endlink  values are unused.
                                
                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCenterOfEdge Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCenterOfEdge@endlink , then both the @link FirstDistance FirstDistance@endlink 
                                and @link SecondDistance SecondDistance@endlink  represent exactly half the width of the flange.

                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd@endlink , then @link FirstDistance FirstDistance@endlink 
                                represents the width of the flange, starting from the end of the edge specified by the @link Vertex Vertex@endlink  and 
                                the @link SecondDistance SecondDistance@endlink  is not used.
                               
                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd@endlink , then @link FirstDistance FirstDistance@endlink 
                                represents the distance of the start point of the flange from the end of the edge specified by @link Vertex Vertex@endlink  
                                and @link SecondDistance SecondDistance@endlink  represents the width of the flange.
                               
                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds@endlink , then @link FirstDistance FirstDistance@endlink 
                                represents the distance of the start point of the flange from the from the end of the edge specified by @link Vertex Vertex@endlink   
                                and @link SecondDistance SecondDistance@endlink  represents the distance of the end point of the flange from end of the edge opposite to the end 
                                specified by @link Vertex Vertex@endlink .
                                
                                The value @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCustom Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCustom@endlink , cannot be set by the user. It is set internally if the
                                sketch for the flange has been edited after creation. In this case, the expressions @link FirstDistance FirstDistance@endlink 
                                and @link SecondDistance SecondDistance@endlink  may or may not retain their original meaning when the flange was first created, 
                                so the user should not rely on these any more to mean anything specific.
                                
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptions WidthType
                (
                );
                /**Sets  the width type for flange.
                             <br> 
                                Use one of the values from @link Features::SheetMetal::FlangeBuilder::WidthTypeOptions Features::SheetMetal::FlangeBuilder::WidthTypeOptions@endlink . Depending on which of the 
                                values from the enum is used, none, either or both of the distance values from 
                                @link FirstDistance FirstDistance@endlink   and @link SecondDistance SecondDistance@endlink 
                                may be used. Here is a description of the distances:
                                
                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFullEdge Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFullEdge@endlink , then both the @link FirstDistance FirstDistance@endlink 
                                and @link SecondDistance SecondDistance@endlink  values are unused.
                                
                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCenterOfEdge Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCenterOfEdge@endlink , then both the @link FirstDistance FirstDistance@endlink 
                                and @link SecondDistance SecondDistance@endlink  represent exactly half the width of the flange.

                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd@endlink , then @link FirstDistance FirstDistance@endlink 
                                represents the width of the flange, starting from the end of the edge specified by the @link Vertex Vertex@endlink  and 
                                the @link SecondDistance SecondDistance@endlink  is not used.
                               
                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd@endlink , then @link FirstDistance FirstDistance@endlink 
                                represents the distance of the start point of the flange from the end of the edge specified by @link Vertex Vertex@endlink  
                                and @link SecondDistance SecondDistance@endlink  represents the width of the flange.
                               
                                If the value is @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds@endlink , then @link FirstDistance FirstDistance@endlink 
                                represents the distance of the start point of the flange from the from the end of the edge specified by @link Vertex Vertex@endlink   
                                and @link SecondDistance SecondDistance@endlink  represents the distance of the end point of the flange from end of the edge opposite to the end 
                                specified by @link Vertex Vertex@endlink .
                                
                                The value @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCustom Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCustom@endlink , cannot be set by the user. It is set internally if the
                                sketch for the flange has been edited after creation. In this case, the expressions @link FirstDistance FirstDistance@endlink 
                                and @link SecondDistance SecondDistance@endlink  may or may not retain their original meaning when the flange was first created, 
                                so the user should not rely on these any more to mean anything specific.
                                
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetWidthType
                (
                    NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptions widthType /** width type */ 
                );
                /**Returns  a distance based on @link WidthType WidthType@endlink .
                             <br> 
                                See @link WidthType WidthType @endlink and @link SetWidthType SetWidthType @endlink  for a detailed desctiption of what this distance stands for.
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Expression * FirstDistance
                (
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetFirstDistance
                (
                    const NXString & firstDistance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                void SetFirstDistance
                (
                    const char * firstDistance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  a distance based on @link WidthType WidthType@endlink .
                             <br> 
                                See @link WidthType WidthType @endlink and @link SetWidthType SetWidthType @endlink  for a detailed desctiption of what this distance stands for.
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Expression * SecondDistance
                (
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSecondDistance
                (
                    const NXString & secondDistance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                void SetSecondDistance
                (
                    const char * secondDistance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the vertex on the flange edge, needed to dimension the flange width.
                             <br> 
                                The vertex needs to be specified ONLY if @link WidthType WidthType@endlink  is
                                set to one of @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd@endlink ,  
                                @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd@endlink . In case of 
                                @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds@endlink , the start vertex of the edge
                                is assumed to be the start point for @link FirstDistance FirstDistance@endlink .
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Point3d Vertex
                (
                );
                /**Sets  the vertex on the flange edge, needed to dimension the flange width.
                             <br> 
                                The vertex needs to be specified ONLY if @link WidthType WidthType@endlink  is
                                set to one of @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd@endlink ,  
                                @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd@endlink . In case of 
                                @link Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds@endlink , the start vertex of the edge
                                is assumed to be the start point for @link FirstDistance FirstDistance@endlink .
                             <br> 
                        
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetVertex
                (
                    const NXOpen::Point3d & vertex /** A vertex on the flange edge. */
                );
                /**Returns  the bend angle for flange. It should be set in degrees (??????). 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Expression * BendAngle
                (
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetBendAngle
                (
                    const NXString & bendAngle /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                void SetBendAngle
                (
                    const char * bendAngle /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Verify that the builder data is valid for creating a flange.
                             <br> 
                                 If the builder data is valid, return value is zero.
                             <br> 
                         @return  A value of zero is returned if the data in the builder is valid. 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: int ValidateBuilderData
                (
                );
                /** Get the flange sketch   @return  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Sketch * GetSketch
                (
                );
                /** Edit the sketch base on a new edge you need to call SetEdge to set a new edge
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void EditSketch
                (
                );
                /** Delete the flange sketch 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: void DeleteSketch
                (
                );
                /**Returns  the Match Plane. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Plane * MatchPlane
                (
                );
                /**Sets  the Match Plane. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetMatchPlane
                (
                    NXOpen::Plane * matchPlane /** matchplane */ 
                );
                /**Returns  the match face selection type.
                             <br> 
                                None for Regular Flange.
                                Until Selected for Match To Face type Flange .
                             <br> 
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::FlangeBuilder::MatchFaceOptions MatchFaceOption
                (
                );
                /**Sets  the match face selection type.
                             <br> 
                                None for Regular Flange.
                                Until Selected for Match To Face type Flange .
                             <br> 
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetMatchFaceOption
                (
                    NXOpen::Features::SheetMetal::FlangeBuilder::MatchFaceOptions matchFaceOption /** matchfaceoption */ 
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
