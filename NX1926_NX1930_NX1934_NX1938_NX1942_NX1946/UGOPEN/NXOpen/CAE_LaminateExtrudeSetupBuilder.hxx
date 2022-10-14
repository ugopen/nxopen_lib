#ifndef NXOpen_CAE_LAMINATEEXTRUDESETUPBUILDER_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEEXTRUDESETUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateExtrudeSetupBuilder.ja
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
#include <NXOpen/CAE_LaminateSelectEntitiesBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class LaminateExtrudeSetupBuilder;
    }
    class Builder;
    namespace CAE
    {
        class LaminatePly;
    }
    namespace CAE
    {
        class LaminateSelectEntitiesBuilder;
    }
    namespace CAE
    {
        class SelectCAEFaceList;
    }
    class Expression;
    namespace CAE
    {
        class _LaminateExtrudeSetupBuilderBuilder;
        class LaminateExtrudeSetupBuilderImpl;
        /** Represents a @link NXOpen::CAE::LaminateExtrudeSetup NXOpen::CAE::LaminateExtrudeSetup@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::LaminateGlobalLayupMgr::CreateLaminateExtrudeSetupBuilder  NXOpen::CAE::LaminateGlobalLayupMgr::CreateLaminateExtrudeSetupBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        CutFaceDrops </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FlipNormals </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        KeepInvalidElems </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        MinElemThickness </term> <description> 
         
        0.05 </description> </item> 

        <item><term> 
         
        NumSmoothIterations </term> <description> 
         
        2 </description> </item> 

        <item><term> 
         
        SinglePlyPerLayer </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        SmoothNormals </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        SmoothRatio </term> <description> 
         
        0.5 </description> </item> 

        </list> 

         <br>  Created in NX6.0.4.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LaminateExtrudeSetupBuilder : public NXOpen::Builder
        {
            /** Samcef element type. */
            public: enum SamcefElementTypeEnum
            {
                SamcefElementTypeEnumSolid/** Solid. */,
                SamcefElementTypeEnumSolidShell/** Solid Shell. */,
                SamcefElementTypeEnumSolidPly/** Solid Ply. */
            };

            private: LaminateExtrudeSetupBuilderImpl * m_laminateextrudesetupbuilder_impl;
            private: friend class  _LaminateExtrudeSetupBuilderBuilder;
            protected: LaminateExtrudeSetupBuilder();
            public: ~LaminateExtrudeSetupBuilder();
            /**Returns  the name of the laminate extrusion setup 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString ExtrudeName
            (
            );
            /**Sets  the name of the laminate extrusion setup 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetExtrudeName
            (
                const NXString & extrudeName /** extrudename */ 
            );
            /**Sets  the name of the laminate extrusion setup 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            void SetExtrudeName
            (
                const char * extrudeName /** extrudename */ 
            );
            /**Returns  the geometric face(s) and element faces on which to perform the extrusion 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateSelectEntitiesBuilder * Selection
            (
            );
            /**Returns  the option to group plies into single layer(s) of extruded elements 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool SinglePlyPerLayer
            (
            );
            /**Sets  the option to group plies into single layer(s) of extruded elements 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetSinglePlyPerLayer
            (
                bool singlePlyPerLayer /** singleplyperlayer */ 
            );
            /**Returns  the option to flip the element normals for the extrusion process 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: bool FlipNormals
            (
            );
            /**Sets  the option to flip the element normals for the extrusion process 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetFlipNormals
            (
                bool flipNormals /** flipnormals */ 
            );
            /**Returns  the option to (de)activate homogeneous ply meshes 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool HomogeneousPlies
            (
            );
            /**Sets  the option to (de)activate homogeneous ply meshes 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetHomogeneousPlies
            (
                bool homogeneousPlies /** homogeneousplies */ 
            );
            /**Returns  the option to use SAMCEF solid shells 
             <br>  @deprecated Deprecated in NX12.0.0.  Use method @link NXOpen::CAE::LaminateExtrudeSetupBuilder::SamcefElementType NXOpen::CAE::LaminateExtrudeSetupBuilder::SamcefElementType@endlink  <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  Use method NXOpen::CAE::LaminateExtrudeSetupBuilder::SamcefElementType") bool SamcefSolidShells
            (
            );
            /**Sets  the option to use SAMCEF solid shells 
             <br>  @deprecated Deprecated in NX12.0.0.  Use method @link NXOpen::CAE::LaminateExtrudeSetupBuilder::SetSamcefElementType NXOpen::CAE::LaminateExtrudeSetupBuilder::SetSamcefElementType@endlink  <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  Use method NXOpen::CAE::LaminateExtrudeSetupBuilder::SetSamcefElementType") void SetSamcefSolidShells
            (
                bool samcefSolidShells /** samcefsolidshells */ 
            );
            /**Returns  the samcef element type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateExtrudeSetupBuilder::SamcefElementTypeEnum SamcefElementType
            (
            );
            /**Sets  the samcef element type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetSamcefElementType
            (
                NXOpen::CAE::LaminateExtrudeSetupBuilder::SamcefElementTypeEnum samcefElementType /** samcefelementtype */ 
            );
            /**Returns  the option to smooth the shell normals used for extrusion 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool SmoothNormals
            (
            );
            /**Sets  the option to smooth the shell normals used for extrusion 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetSmoothNormals
            (
                bool smoothNormals /** smoothnormals */ 
            );
            /**Returns  the neighbor normal weigth ratio for normal smoothing 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double SmoothRatio
            (
            );
            /**Sets  the neighbor normal weigth ratio for normal smoothing 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetSmoothRatio
            (
                double smoothRatio /** smoothratio */ 
            );
            /**Returns  the number of iterations for normal smoothing 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int NumSmoothIterations
            (
            );
            /**Sets  the number of iterations for normal smoothing 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetNumSmoothIterations
            (
                int numSmoothIterations /** numsmoothiterations */ 
            );
            /**Returns  the option to keep invalid extruded elements 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool KeepInvalidElems
            (
            );
            /**Sets  the option to keep invalid extruded elements 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetKeepInvalidElems
            (
                bool keepInvalidElems /** keepinvalidelems */ 
            );
            /**Returns  the option use cutting faces 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool Cuts
            (
            );
            /**Sets  the option use cutting faces 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetCuts
            (
                bool cuts /** cuts */ 
            );
            /**Returns  the cutting face(s) selection 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectCAEFaceList * CutFaceSelect
            (
            );
            /**Returns  the relative minimum thickness for a corner node ply element. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double MinElemThickness
            (
            );
            /**Sets  the relative minimum thickness for a corner node ply element. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetMinElemThickness
            (
                double minElemThickness /** minelemthickness */ 
            );
            /**Returns  the tolerance to snap nodes to the cutting face borders. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SnapToCutFaceTolerance
            (
            );
            /**Returns  the option to consider cut ply elements as drop-offs 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool CutFaceDrops
            (
            );
            /**Sets  the option to consider cut ply elements as drop-offs 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetCutFaceDrops
            (
                bool cutFaceDrops /** cutfacedrops */ 
            );
            /**Returns  the option to (de)activate reference plane location 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReferencePlaneLocation
            (
            );
            /**Sets  the option to (de)activate reference plane location 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetReferencePlaneLocation
            (
                bool referencePlaneLocation /** referenceplanelocation */ 
            );
            /**Returns  the option to (de)activate the sandwich inflatoin
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool SandwichInflation
            (
            );
            /**Sets  the option to (de)activate the sandwich inflatoin
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetSandwichInflation
            (
                bool sandwichInflation /** sandwichinflation */ 
            );
            /**Returns  the top-skin-mesh options for the sandwich inflation
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: int SandwichTopSkinMeshOption
            (
            );
            /**Sets  the top-skin-mesh options for the sandwich inflation
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetSandwichTopSkinMeshOption
            (
                int sandwichTopSkinMeshOption /** sandwichtopskinmeshoption */ 
            );
            /** Add a core ply to the list of selected cores, used for ply-based Laminate 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: bool AddSandwichCorePly
            (
                NXOpen::CAE::LaminatePly * ply /** ply */ 
            );
            /** Clear the selection of the sandwich core ply 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void ClearSandwichCorePly
            (
                bool clear /** clear */ 
            );
            /**Returns  the number of core element layers for the sandwich inflation
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: int SandwichNumCoreElementLayers
            (
            );
            /**Sets  the number of core element layers for the sandwich inflation
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetSandwichNumCoreElementLayers
            (
                int sandwichNumCoreElementLayers /** sandwichnumcoreelementlayers */ 
            );
            /**Returns  the bottom-skin-mesh options for the sandwich inflation
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: int SandwichBottomSkinMeshOption
            (
            );
            /**Sets  the bottom-skin-mesh options for the sandwich inflation
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetSandwichBottomSkinMeshOption
            (
                int sandwichBottomSkinMeshOption /** sandwichbottomskinmeshoption */ 
            );
        };
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