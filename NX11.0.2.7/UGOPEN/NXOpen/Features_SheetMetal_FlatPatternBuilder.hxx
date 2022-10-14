#ifndef NXOpen_FEATURES_SHEETMETAL_FLATPATTERNBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_FLATPATTERNBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_FlatPatternBuilder.ja
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
#include <NXOpen/Features_SheetMetal_CornerTreatmentBuilder.hxx>
#include <NXOpen/Features_SheetMetal_FlatPatternBuilder.hxx>
#include <NXOpen/Features_SheetMetal_SheetmetalBaseBuilder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObject.hxx>
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
            class FlatPatternBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class CornerTreatmentBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class SheetmetalBaseBuilder;
        }
    }
    class Section;
    class SelectEdge;
    class SelectFace;
    namespace Features
    {
        namespace SheetMetal
        {
            class _FlatPatternBuilderBuilder;
            class FlatPatternBuilderImpl;
            /** Represents a Flat Pattern feature builder.  <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::SheetmetalManager::CreateFlatPatternBuilder  NXOpen::Features::SheetMetal::SheetmetalManager::CreateFlatPatternBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            InnerCornerTreatment.TreatmentType </td> <td> 
             
            None </td> </tr> 

            <tr><td> 
             
            InnerCornerTreatment.UseGlobal </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            InnerCornerTreatment.Value.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            </table>  

             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  FlatPatternBuilder : public NXOpen::Features::SheetMetal::SheetmetalBaseBuilder
            {
                private: FlatPatternBuilderImpl * m_flatpatternbuilder_impl;
                private: friend class  _FlatPatternBuilderBuilder;
                protected: FlatPatternBuilder();
                public: ~FlatPatternBuilder();
                /**Returns  the upward face selection 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectFace * UpwardFace
                (
                );
                /**Returns  the x axis edge selection. This edge selection is necessary when a face from a formed 
                            **  solid body is picked as Upward face. If a face from a flat solid is selected,
                            **  this value will be ignored. 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectEdge * XAxisEdge
                (
                );
                /**Returns  the flag which decides if the flattened solid will be transformed to Absolute CSYS. This flag will only be 
                            **  used if the Upward face belongs to a formed sheet metal body. If a face from a flat solid is selected,
                            **  this value will be ignored.
                            
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: bool TransformToAbsoluteCsys
                (
                );
                /**Sets  the flag which decides if the flattened solid will be transformed to Absolute CSYS. This flag will only be 
                            **  used if the Upward face belongs to a formed sheet metal body. If a face from a flat solid is selected,
                            **  this value will be ignored.
                            
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetTransformToAbsoluteCsys
                (
                    bool transformFlag /** True = Transform to ABS, False = Do not transform to ABS. */
                );
                /**Returns  the end of the edge where the tangent will define the x axis for flat as solid. This value will only
                            **  be used when a face from a formed solid body is picked as Upward face. If a face from a flat solid is selected,
                            **  this value will be ignored.
                            
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point3d ReferenceVertex
                (
                );
                /**Sets  the end of the edge where the tangent will define the x axis for flat as solid. This value will only
                            **  be used when a face from a formed solid body is picked as Upward face. If a face from a flat solid is selected,
                            **  this value will be ignored.
                            
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetReferenceVertex
                (
                    const NXOpen::Point3d & vertex /** One of the end points of the reference edge. */
                );
                /**Returns  the added geometry selection 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * AddedGeometry
                (
                );
                /**Returns  the outer corner treatment corner object 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::CornerTreatmentBuilder * OuterCornerTreatment
                (
                );
                /**Returns  the inner corner treatment corner object 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::CornerTreatmentBuilder * InnerCornerTreatment
                (
                );
                /**Returns  the show interior feature curves toggle value 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowInteriorFeatureCurves
                (
                );
                /**Sets  the show interior feature curves toggle value 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetShowInteriorFeatureCurves
                (
                    bool showInteriorFeatureCurves /** showinteriorfeaturecurves */ 
                );
                /**Returns  the flat pattern view name string 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString FlatPatternViewName
                (
                );
                /** Set the flag to generate inner and outer mold lines for flat pattern features created before NX11.
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void GenerateMoldLines
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