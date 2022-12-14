#ifndef NXOpen_TOOLING_TRIMMOLDCOMPONENTSBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_TRIMMOLDCOMPONENTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_TrimMoldComponentsBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class TrimMoldComponentsBuilder;
    }
    class Builder;
    class NXObject;
    class ScCollector;
    class SelectBody;
    class SelectBodyList;
    namespace Tooling
    {
        class _TrimMoldComponentsBuilderBuilder;
        class TrimMoldComponentsBuilderImpl;
        /** Represents a builder to be used to create Mold Wizard trim mold components.  <br> To create a new instance of this class, use @link NXOpen::Tooling::TrimMoldComponentsCollection::CreateTrimMoldComponentsBuilder  NXOpen::Tooling::TrimMoldComponentsCollection::CreateTrimMoldComponentsBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        ActionType </term> <description> 
         
        Trim </description> </item> 

        <item><term> 
         
        TargetSelectScope </term> <description> 
         
        Product </description> </item> 

        <item><term> 
         
        TrimPart </term> <description> 
         
        Notrimpart </description> </item> 

        <item><term> 
         
        TrimSurface </term> <description> 
         
        SelectFaces </description> </item> 

        </list> 

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  TrimMoldComponentsBuilder : public NXOpen::Builder
        {
            /** the processing type of Trim Mold Components. */
            public: enum TrimMethod
            {
                TrimMethodTrim/** Trim */,
                TrimMethodUntrim/** Untrim */
            };

            /** the trim part options where a part chosen to work around */
            public: enum TrimPartName
            {
                TrimPartNameNotrimpart/** No Trim Part */
            };

            /** trim surface types */
            public: enum TrimSurfaceName
            {
                TrimSurfaceNameSelectFaces/** Select faces */,
                TrimSurfaceNameSelectSheetBody/** Select sheet body */
            };

            /** the target bodies selection scope */
            public: enum TargetScope
            {
                TargetScopeProduct/** Select target bodies in product node part  */,
                TargetScopeAny/** Select target bodies in any part of the entire assembly */
            };

            private: TrimMoldComponentsBuilderImpl * m_trimmoldcomponentsbuilder_impl;
            private: friend class  _TrimMoldComponentsBuilderBuilder;
            protected: TrimMoldComponentsBuilder();
            public: ~TrimMoldComponentsBuilder();
            /**Returns  the action type defines the current trim method used to processing a mold components. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::TrimMoldComponentsBuilder::TrimMethod ActionType
            (
            );
            /**Sets  the action type defines the current trim method used to processing a mold components. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetActionType
            (
                NXOpen::Tooling::TrimMoldComponentsBuilder::TrimMethod actionType /** actiontype */ 
            );
            /**Returns  the target bodies which collects the bodies to be trimmed or untrimmed. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * TargetBodies
            (
            );
            /**Returns  the trim part where trim surface features are found. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::TrimMoldComponentsBuilder::TrimPartName TrimPart
            (
            );
            /**Sets  the trim part where trim surface features are found. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetTrimPart
            (
                NXOpen::Tooling::TrimMoldComponentsBuilder::TrimPartName trimPart /** trimpart */ 
            );
            /**Returns  the trim surface used to trim the target bodies. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::TrimMoldComponentsBuilder::TrimSurfaceName TrimSurface
            (
            );
            /**Sets  the trim surface used to trim the target bodies. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetTrimSurface
            (
                NXOpen::Tooling::TrimMoldComponentsBuilder::TrimSurfaceName trimSurface /** trimsurface */ 
            );
            /**Returns  the tool sheet body used to trim the target bodies. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * ToolSheetBody
            (
            );
            /**Returns  the tool face used to trim the target bodies. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * ToolFace
            (
            );
            /**Returns  the indication to reverse the trim direction. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool TrimDirection
            (
            );
            /**Sets  the indication to reverse the trim direction. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetTrimDirection
            (
                bool trimDirection /** trimdirection */ 
            );
            /**Returns  the selection scope for target body selection. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::TrimMoldComponentsBuilder::TargetScope TargetSelectScope
            (
            );
            /**Sets  the selection scope for target body selection. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetTargetSelectScope
            (
                NXOpen::Tooling::TrimMoldComponentsBuilder::TargetScope targetSelectScope /** targetselectscope */ 
            );
            /** Set details of the trim data. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetTrimDataDetails
            (
                int surfaceType /** the surface type. */,
                int trimDirection /** the trim direction. */,
                const std::vector<NXOpen::NXObject *> & targets /** array of target ejector pins. */,
                const std::vector<NXOpen::NXObject *> & tools /** array of tool objects. */
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
