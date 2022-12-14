#ifndef NXOpen_TOOLDESIGNER_SELECTWELDSBUILDER_HXX_INCLUDED
#define NXOpen_TOOLDESIGNER_SELECTWELDSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ToolDesigner_SelectWeldsBuilder.ja
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
#include <NXOpen/Assemblies_SubsetBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/PDM_ModelElementRevision.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/ToolDesigner_SelectWeldsBuilder.hxx>
#include <NXOpen/libtooldesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace ToolDesigner
    {
        class SelectWeldsBuilder;
    }
    namespace Assemblies
    {
        class SubsetBuilder;
    }
    class Builder;
    namespace PDM
    {
        class ModelElementRevision;
    }
    class SelectTaggedObject;
    namespace ToolDesigner
    {
        class _SelectWeldsBuilderBuilder;
        class SelectWeldsBuilderImpl;
        /** SelectWeldsBuilder   <br> To create a new instance of this class, use @link NXOpen::ToolDesigner::ToolDesignerManager::CreateSelectWeldsBuilder  NXOpen::ToolDesigner::ToolDesignerManager::CreateSelectWeldsBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ActivateVolFilterToggle </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX10.0.0.  <br>  
        */
        class TOOLDESIGNEROPENCPPEXPORT  SelectWeldsBuilder : public NXOpen::Builder
        {
            private: SelectWeldsBuilderImpl * m_selectweldsbuilder_impl;
            private: friend class  _SelectWeldsBuilderBuilder;
            protected: SelectWeldsBuilder();
            public: ~SelectWeldsBuilder();
            /**Returns  the volume box selection 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObject * VolumeBoxSelection
            (
            );
            /**Returns  the activate vol filter toggle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool ActivateVolFilterToggle
            (
            );
            /**Sets  the activate vol filter toggle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetActivateVolFilterToggle
            (
                bool activateVolFilterToggle /** activatevolfiltertoggle */ 
            );
            /** Do Weld Assignment 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void AssignWeld
            (
                NXOpen::PDM::ModelElementRevision * weldPoint /** weldpoint */ 
            );
            /** Do Weld Unassignment 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void UnassignWeld
            (
                NXOpen::PDM::ModelElementRevision * weldPoint /** weldpoint */ 
            );
            /** GetCurrentSubsetBuilder  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SubsetBuilder * GetCurrentSubsetBuilder
            (
            );
            /** Fetch Weld Points In Scope 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void FetchWeldPointsInScope
            (
                std::vector<NXOpen::PDM::ModelElementRevision *> & weldPoints /** weldpoints */ 
            );
            /** Set Top Vertex for volume search 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTopVertex
            (
                double xValue /** xvalue */ ,
                double yValue /** yvalue */ ,
                double zValue /** zvalue */ 
            );
            /** Set Bottom Vertex for volume search 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBottomVertex
            (
                double xValue /** xvalue */ ,
                double yValue /** yvalue */ ,
                double zValue /** zvalue */ 
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
