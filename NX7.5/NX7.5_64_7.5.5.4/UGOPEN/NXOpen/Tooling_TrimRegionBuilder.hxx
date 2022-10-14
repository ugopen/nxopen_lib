#ifndef NXOpen_TOOLING_TRIMREGIONBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_TRIMREGIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_TrimRegionBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_TrimRegionBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class TrimRegionBuilder;
    }
    class Builder;
    class NXObject;
    class RegionPointList;
    class SelectBody;
    class SelectNXObjectList;
    namespace Tooling
    {
        class _TrimRegionBuilderBuilder;
        class TrimRegionBuilderImpl;
        /** Mold Wizard trim region management builder, trims a body to a boundary of edges, curves or bodies.
                Optionally creates output trimmed sheet body as a patch surface.  <br> To create a new instance of this class, use @link Tooling::TrimRegionCollection::CreateTrimRegionBuilder Tooling::TrimRegionCollection::CreateTrimRegionBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AsPatchSurface </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        BoundaryType </td> <td> 
         
        BodyCurve </td> </tr> 

        <tr><td> 
         
        RegionType </td> <td> 
         
        Keep </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  TrimRegionBuilder : public Builder
        {
            /** represents the boundary type option, body/curve type or traverse type. */
            public: enum BoundaryOption
            {
                BoundaryOptionBodyCurve/** select body/edge/curve as boundary object */,
                BoundaryOptionTraverse/** use traverse loop to select boundary object */
            };

            /** represents the option to keep or discard the selected region. */
            public: enum RegionOption
            {
                RegionOptionKeep/** selected region will be kept. */,
                RegionOptionDiscard/** selected region will be discarded. */
            };

            private: TrimRegionBuilderImpl * m_trimregionbuilder_impl;
            private: friend class  _TrimRegionBuilderBuilder;
            protected: TrimRegionBuilder();
            public: ~TrimRegionBuilder();
            /**Returns  the selection of target to create trim region, body type only.  <br> License requirements : None */
            public: NXOpen::SelectBody * TargetBody
            (
            );
            /**Returns  the value of boundary type option, which specifies to use body or edge/curve as boundary object.  <br> License requirements : None */
            public: NXOpen::Tooling::TrimRegionBuilder::BoundaryOption BoundaryType
            (
            );
            /**Sets  the value of boundary type option, which specifies to use body or edge/curve as boundary object.  <br> License requirements : None */
            public: void SetBoundaryType
            (
                NXOpen::Tooling::TrimRegionBuilder::BoundaryOption boundaryType /** boundarytype */ 
            );
            /**Returns  the selection of boundary body to extract region faces, which are used for create intersection curves with target.  <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * BoundaryBody
            (
            );
            /**Returns  the selection of region point, which will be kept or discarded as the result of trim region.  <br> License requirements : None */
            public: NXOpen::RegionPointList * RegionPoint
            (
            );
            /**Returns  the value of the option, which specifies to keep or discard the selected region.  <br> License requirements : None */
            public: NXOpen::Tooling::TrimRegionBuilder::RegionOption RegionType
            (
            );
            /**Sets  the value of the option, which specifies to keep or discard the selected region.  <br> License requirements : None */
            public: void SetRegionType
            (
                NXOpen::Tooling::TrimRegionBuilder::RegionOption regionType /** regiontype */ 
            );
            /**Returns  the value of option, which specifies whether to set the result region as patch surface or not.  <br> License requirements : None */
            public: bool AsPatchSurface
            (
            );
            /**Sets  the value of option, which specifies whether to set the result region as patch surface or not.  <br> License requirements : None */
            public: void SetAsPatchSurface
            (
                bool asPatchSurface /** aspatchsurface */ 
            );
            /** Returns the value of surface patch color.  <br> License requirements : None */
            public: void GetColorValue
            (
                double* redValue /** red value between 0 and 1 */,
                double* greenValue /** green value between 0 and 1 */,
                double* blueValue /** blue value between 0 and 1 */
            );
            /** Sets the value of surface patch color.  <br> License requirements : None */
            public: void SetColorValue
            (
                double redValue /** red value between 0 and 1 */,
                double greenValue /** green value between 0 and 1 */,
                double blueValue /** blue value between 0 and 1 */
            );
            /** Sets the edges from traverse loop to builder data.  <br> License requirements : None */
            public: void SetTraverseEdges
            (
                const std::vector<NXOpen::NXObject *> & traverseEdges /** the selected edges */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif