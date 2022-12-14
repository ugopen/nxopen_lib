#ifndef NXOpen_TOOLING_MOLDFILLINGBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_MOLDFILLINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_MoldFillingBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_CloneObject.hxx>
#include <NXOpen/Tooling_SpreadsheetData.hxx>
#include <NXOpen/Tooling_StandardPartData.hxx>
#include <NXOpen/ugmath.hxx>
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
        class MoldFillingBuilder;
    }
    namespace Assemblies
    {
        class Component;
    }
    namespace Assemblies
    {
        class SelectComponent;
    }
    namespace Assemblies
    {
        class SelectComponentList;
    }
    class Builder;
    class Point;
    class SelectNXObject;
    namespace Tooling
    {
        class CloneObject;
    }
    namespace Tooling
    {
        class SpreadsheetData;
    }
    namespace Tooling
    {
        class StandardPartData;
    }
    namespace Tooling
    {
        class _MoldFillingBuilderBuilder;
        class MoldFillingBuilderImpl;
        /**  @brief  Builder used to add a gate/runner standard part from fill library, it returns NULL. 

          <br> To create a new instance of this class, use @link NXOpen::Tooling::MoldwizardManager::CreateMoldFillingBuilder  NXOpen::Tooling::MoldwizardManager::CreateMoldFillingBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Constraint </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        InstallOptions </term> <description> 
         
        AddInstance </description> </item> 

        <item><term> 
         
        IsBalanced </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        MoveAllGates </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        MoveOptions </term> <description> 
         
        Move </description> </item> 

        <item><term> 
         
        Rename </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  MoldFillingBuilder : public NXOpen::Builder
        {
            /**  @brief  The modification options of the selected fill component.  

             */
            public: enum MoveOption
            {
                MoveOptionMove/** Modifying current component */,
                MoveOptionCopyInstance/** Copying instance and Modifying */,
                MoveOptionCopyPart/** Copying new part and Modifying */
            };

            /**  @brief  The installation type of the fill component. 

              */
            public: enum InstallOption
            {
                InstallOptionAddInstance/** Instance */,
                InstallOptionNewComponent/** New part */
            };

            private: MoldFillingBuilderImpl * m_moldfillingbuilder_impl;
            private: friend class  _MoldFillingBuilderBuilder;
            protected: MoldFillingBuilder();
            public: ~MoldFillingBuilder();
            /**Returns   @brief  the fill component to be edit.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponent * FillComponent
            (
            );
            /**  @brief  Deletes selected fill component.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void DeleteFill
            (
            );
            /**Returns   @brief  the modification option.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::MoldFillingBuilder::MoveOption MoveOptions
            (
            );
            /**Sets   @brief  the modification option.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetMoveOptions
            (
                NXOpen::Tooling::MoldFillingBuilder::MoveOption movecopy /** movecopy */ 
            );
            /**Returns   @brief  the position object(point or runner body) used to place a gate component.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * PositionObject
            (
            );
            /**Returns   @brief  the gates added by selecting a runner body.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * AddedGatesByRunner
            (
            );
            /**Returns   @brief  the point used to place a runner component.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * PositionPoint
            (
            );
            /**Sets   @brief  the point used to place a runner component.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetPositionPoint
            (
                NXOpen::Point * positionPoint /** positionpoint */ 
            );
            /**Returns   @brief  a value that indicates whether to move all gates or not when moving the active gate.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool MoveAllGates
            (
            );
            /**Sets   @brief  a value that indicates whether to move all gates or not when moving the active gate.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetMoveAllGates
            (
                bool moveAllGates /** moveallgates */ 
            );
            /**Returns   @brief  the installation option when adding multiple gates one time.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::MoldFillingBuilder::InstallOption InstallOptions
            (
            );
            /**Sets   @brief  the installation option when adding multiple gates one time.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetInstallOptions
            (
                NXOpen::Tooling::MoldFillingBuilder::InstallOption installOptions /** installoptions */ 
            );
            /**Returns   @brief  a value that indicates whether the rename dialog should be activated when adding a fill component.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool Rename
            (
            );
            /**Sets   @brief  a value that indicates whether the rename dialog should be activated when adding a fill component.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetRename
            (
                bool rename /** rename */ 
            );
            /**Returns   @brief  a value that indicates whether placing gates as product layout.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsBalanced
            (
            );
            /**Sets   @brief  a value that indicates whether placing gates as product layout.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetBalanced
            (
                bool isBalanced /** isbalanced */ 
            );
            /**Returns   @brief  a value that indicates whether adding a constraint when placing a fill component.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool Constraint
            (
            );
            /**Sets   @brief  a value that indicates whether adding a constraint when placing a fill component.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetConstraint
            (
                bool constraint /** constraint */ 
            );
            /**  @brief  Sets manipulator position.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetManipulatorPosition
            (
                const NXOpen::Matrix3x3 & matrix /** Matrix of the specified coordinates */,
                const NXOpen::Point3d & position /** Origin point of the specified coordinates */
            );
            /**  @brief  Saves the position of fill component to be edit.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SaveEditingFillComponentPosition
            (
                const NXOpen::Matrix3x3 & matrix /** Transform matrix of the editing component */,
                const NXOpen::Point3d & position /** Transform origin point of the editing component */
            );
            /**  @brief  Sets spreadsheet data.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetParameterTreeData
            (
                NXOpen::Tooling::SpreadsheetData * sheetData /** Spreadsheet data */
            );
            /**  @brief  Sets standard part client data.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetFillClientData
            (
                NXOpen::Tooling::StandardPartData * clientData /** Standard part client data */
            );
            /**  @brief  Edits standard part dimensions.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void EditComponentDimensions
            (
                NXOpen::Assemblies::Component * addedPartOcc /** The component to be edit */
            );
            /**  @brief  Adds gate or runner component.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void AddFillingComponents
            (
            );
            /**  @brief  Sets the specified component as the active component.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetActiveFillComponent
            (
                NXOpen::Assemblies::Component * activePartOcc /** The component to be set as the active component*/
            );
            /**  @brief  Gets spreadsheet data from specified fill component.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void GetDataFromSelectedFillComponent
            (
                NXOpen::Tooling::SpreadsheetData * sheetData /** Spreadsheet data */
            );
            /**  @brief  Removes added fill components.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RemoveAddedComponents
            (
            );
            /**  @brief  Places the gate as product layout.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void GateLayoutAction
            (
            );
            /**  @brief  Creates clone object.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void CreateCloneObject
            (
            );
            /**  @brief  Preview selected fill component.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void PreviewSelectedFillComponent
            (
            );
            /**  @brief  Gets fill standard part library data.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void AskFillLibraryData
            (
                bool isFromMemberView /** True if user drags an fill item from reuse library */,
                const NXString & libName /** Name of the fill library */,
                const NXString & libPath /** Path of the fill library */
            );
            /**  @brief  Gets fill standard part library data.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            void AskFillLibraryData
            (
                bool isFromMemberView /** True if user drags an fill item from reuse library */,
                const char * libName /** Name of the fill library */,
                const char * libPath /** Path of the fill library */
            );
            /**  @brief  Gets selected part data, and assign it to standard part client data.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetClientDataWithSelectedItem
            (
                const NXString & catalogName /** Catalog name of the fill component */,
                const NXString & descriptiveName /** Descriptive name of the fill component */
            );
            /**  @brief  Gets selected part data, and assign it to standard part client data.  

             
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            void SetClientDataWithSelectedItem
            (
                const char * catalogName /** Catalog name of the fill component */,
                const char * descriptiveName /** Descriptive name of the fill component */
            );
            /** Gets clone client data.  @return  A @link NXOpen::Tooling::CloneObject NXOpen::Tooling::CloneObject@endlink  instance 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Tooling::CloneObject * GetCloneObject
            (
            );
            /** Sets clone client data. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCloneObject
            (
                NXOpen::Tooling::CloneObject * cloneObject /** A @link NXOpen::Tooling::CloneObject NXOpen::Tooling::CloneObject@endlink  instance */
            );
            /** Sets parent part as work part according to the value defined in sheet. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetParentAsWorkPart
            (
                NXOpen::Tooling::SpreadsheetData * sheetData /** Spreadsheet data */
            );
            /** Gets the last selected fill component. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Assemblies::Component * GetLastFillComponent
            (
            );
            /** Sets the last selected fill component. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetLastFillComponent
            (
                NXOpen::Assemblies::Component * lastFillComponent /** lastfillcomponent */ 
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
