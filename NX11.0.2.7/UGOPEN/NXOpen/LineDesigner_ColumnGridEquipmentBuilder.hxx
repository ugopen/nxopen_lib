#ifndef NXOpen_LINEDESIGNER_COLUMNGRIDEQUIPMENTBUILDER_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_COLUMNGRIDEQUIPMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_ColumnGridEquipmentBuilder.ja
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
#include <NXOpen/KFObject.hxx>
#include <NXOpen/LineDesigner_ColumnGridEquipmentBuilder.hxx>
#include <NXOpen/LineDesigner_PickRectanglePointsBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class ColumnGridEquipmentBuilder;
    }
    class Builder;
    class Expression;
    class KFObject;
    namespace LineDesigner
    {
        class PickRectanglePointsBuilder;
    }
    class NXObjectList;
    class Section;
    namespace LineDesigner
    {
        class _ColumnGridEquipmentBuilderBuilder;
        class ColumnGridEquipmentBuilderImpl;
        /**
            Represents a LineDesigner.ColumnGridEquipment builder

             <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateColumnGridEquipmentBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateColumnGridEquipmentBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        BubbleDiameter </td> <td> 
         
        1200 </td> </tr> 

        <tr><td> 
         
        BubbleExtension </td> <td> 
         
        750 </td> </tr> 

        <tr><td> 
         
        BubbleExtensionOffset </td> <td> 
         
        400 </td> </tr> 

        <tr><td> 
         
        BubbleLeader </td> <td> 
         
        750 </td> </tr> 

        <tr><td> 
         
        ColumnBaseDepth.Value </td> <td> 
         
        800 (millimeters part), 32 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnBaseDiameter.Value </td> <td> 
         
        800 (millimeters part), 32 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnBaseHeight.Value </td> <td> 
         
        900 (millimeters part), 35 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnBaseLowerDiameter.Value </td> <td> 
         
        900 (millimeters part), 32 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnBaseTypeEnum </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        ColumnBaseUpperDiameter.Value </td> <td> 
         
        800 (millimeters part), 32 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnBaseWidth.Value </td> <td> 
         
        800 (millimeters part), 35 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnDepth.Value </td> <td> 
         
        600 (millimeters part), 25 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnDiameter.Value </td> <td> 
         
        800 (millimeters part), 25 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnDisplayIDs </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        ColumnElevation.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnHeight.Value </td> <td> 
         
        3000 (millimeters part), 120 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnRotate90Degrees </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ColumnSpacingDouble </td> <td> 
         
        15000 </td> </tr> 

        <tr><td> 
         
        ColumnThickness.Value </td> <td> 
         
        30 (millimeters part), 2 (inches part) </td> </tr> 

        <tr><td> 
         
        ColumnTypeEnum </td> <td> 
         
        IBeam </td> </tr> 

        <tr><td> 
         
        ColumnWideNumber </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        ColumnWidth.Value </td> <td> 
         
        600 (millimeters part), 12 (inches part) </td> </tr> 

        <tr><td> 
         
        CreateBottomBubblesToggle </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CreateLeftBubblesToggle </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CreateRightBubblesToggle </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CreateTopBubblesToggle </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        DefineGlobalSizeToggle </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        DisplayGridToggle </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        RowDeepNumber </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        RowSpacingDouble </td> <td> 
         
        15000 </td> </tr> 

        <tr><td> 
         
        SelectGridArea.AllowRotation </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        UseSpacingToggle </td> <td> 
         
        1 </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  ColumnGridEquipmentBuilder : public NXOpen::Builder
        {
            /** This enum is providing possible column types    */
            public: enum ColumnType
            {
                ColumnTypeIBeam/** ibeam */ ,
                ColumnTypeTBeam/** tbeam */ ,
                ColumnTypeRectangle/** rectangle */ ,
                ColumnTypeCircle/** circle */ ,
                ColumnTypeUserDefine/** user define */ 
            };

            /** This enum is providing possible column base types   */
            public: enum ColumnBaseType
            {
                ColumnBaseTypeNone/** none */ ,
                ColumnBaseTypeRectangle/** rectangle */ ,
                ColumnBaseTypeCircle/** circle */ ,
                ColumnBaseTypeCone/** cone */ ,
                ColumnBaseTypeUserDefine/** user define */ 
            };

            private: ColumnGridEquipmentBuilderImpl * m_columngridequipmentbuilder_impl;
            private: friend class  _ColumnGridEquipmentBuilderBuilder;
            protected: ColumnGridEquipmentBuilder();
            public: ~ColumnGridEquipmentBuilder();
            /**Returns  the define global size toggle of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool DefineGlobalSizeToggle
            (
            );
            /**Sets  the define global size toggle of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetDefineGlobalSizeToggle
            (
                bool defineGlobalSizeToggle /** defineglobalsizetoggle */ 
            );
            /**Returns  the selected grid area of column grid
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::LineDesigner::PickRectanglePointsBuilder * SelectGridArea
            (
            );
            /**Sets  the selected grid area of column grid
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetSelectGridArea
            (
                NXOpen::LineDesigner::PickRectanglePointsBuilder * selectGridArea /** selectgridarea */ 
            );
            /**Returns  the display grid status of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool DisplayGridToggle
            (
            );
            /**Sets  the display grid status of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetDisplayGridToggle
            (
                bool displayGridToggle /** displaygridtoggle */ 
            );
            /**Returns  the status for using column row spacing of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool UseSpacingToggle
            (
            );
            /**Sets  the status for using column row spacing of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetUseSpacingToggle
            (
                bool useSpacingToggle /** usespacingtoggle */ 
            );
            /**Returns  the spacing between columns 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: double ColumnSpacingDouble
            (
            );
            /**Sets  the spacing between columns 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetColumnSpacingDouble
            (
                double columnSpacingDouble /** columnspacingdouble */ 
            );
            /**Returns  the value of row spacing between columns
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: double RowSpacingDouble
            (
            );
            /**Sets  the value of row spacing between columns
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetRowSpacingDouble
            (
                double rowSpacingDouble /** rowspacingdouble */ 
            );
            /**Returns  the number of column of columns in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: int ColumnWideNumber
            (
            );
            /**Sets  the number of column of columns in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetColumnWideNumber
            (
                int columnWideNumber /** columnwidenumber */ 
            );
            /**Returns  the number of rows of columns in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: int RowDeepNumber
            (
            );
            /**Sets  the number of rows of columns in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetRowDeepNumber
            (
                int rowDeepNumber /** rowdeepnumber */ 
            );
            /**Returns  the column type of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::LineDesigner::ColumnGridEquipmentBuilder::ColumnType ColumnTypeEnum
            (
            );
            /**Sets  the column type of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetColumnTypeEnum
            (
                NXOpen::LineDesigner::ColumnGridEquipmentBuilder::ColumnType columnTypeEnum /** columntypeenum */ 
            );
            /**Returns  the column cross section of columns of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Section * ColumnCrossSection
            (
            );
            /**Returns  the column height of columns of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnHeight
            (
            );
            /**Returns  the column depth of column grid  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnDepth
            (
            );
            /**Returns the column diameter of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnDiameter
            (
            );
            /**Returns  the column width of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnWidth
            (
            );
            /**Returns  the column elevation of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnElevation
            (
            );
            /**Returns  the column thickness of coulmn grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnThickness
            (
            );
            /**Returns  the status of 90 degree column rotation for column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool ColumnRotate90Degrees
            (
            );
            /**Sets  the status of 90 degree column rotation for column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetColumnRotate90Degrees
            (
                bool columnRotate90Degrees /** columnrotate90degrees */ 
            );
            /**Returns  the status of column display ids in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool ColumnDisplayIDs
            (
            );
            /**Sets  the status of column display ids in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetColumnDisplayIDs
            (
                bool columnDisplayIDs /** columndisplayids */ 
            );

            /// \cond NX_NO_DOC 
            /** TODO: fill in a description for this 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void ModifyColumnsButton
            (
            );

            /// \endcond 
            /**Returns  the column base type of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::LineDesigner::ColumnGridEquipmentBuilder::ColumnBaseType ColumnBaseTypeEnum
            (
            );
            /**Sets  the column base type of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetColumnBaseTypeEnum
            (
                NXOpen::LineDesigner::ColumnGridEquipmentBuilder::ColumnBaseType columnBaseTypeEnum /** columnbasetypeenum */ 
            );
            /**Returns  the column base cross section of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Section * ColumnBaseCrossSection
            (
            );
            /**Returns  the column base height of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnBaseHeight
            (
            );
            /**Returns  the column base depth of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnBaseDepth
            (
            );
            /**Returns  the column base diameter of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnBaseDiameter
            (
            );
            /**Returns  the column base upper diameter of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnBaseUpperDiameter
            (
            );
            /**Returns the column base lower diameter of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnBaseLowerDiameter
            (
            );
            /**Returns  the column base width of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * ColumnBaseWidth
            (
            );

            /// \cond NX_NO_DOC 
            /**Returns  the column data list 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::NXObjectList * ColumnDataList
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the row data list 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::NXObjectList * RowDataList
            (
            );

            /// \endcond 
            /**Returns  the bubbles unallowed characters in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXString BubblesUnallowedChars
            (
            );
            /**Sets  the bubbles unallowed characters in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetBubblesUnallowedChars
            (
                const NXString & bubblesUnallowedChars /** bubblesunallowedchars */ 
            );
            /**Sets  the bubbles unallowed characters in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            void SetBubblesUnallowedChars
            (
                const char * bubblesUnallowedChars /** bubblesunallowedchars */ 
            );
            /**Returns  the status to create top bubbles in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool CreateTopBubblesToggle
            (
            );
            /**Sets  the status to create top bubbles in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetCreateTopBubblesToggle
            (
                bool createTopBubblesToggle /** createtopbubblestoggle */ 
            );
            /**Returns  the status to create right bubbles of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool CreateRightBubblesToggle
            (
            );
            /**Sets  the status to create right bubbles of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetCreateRightBubblesToggle
            (
                bool createRightBubblesToggle /** createrightbubblestoggle */ 
            );
            /**Returns  the status to create bottom bubbles of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool CreateBottomBubblesToggle
            (
            );
            /**Sets  the status to create bottom bubbles of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetCreateBottomBubblesToggle
            (
                bool createBottomBubblesToggle /** createbottombubblestoggle */ 
            );
            /**Returns  the status to create left bubbles of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool CreateLeftBubblesToggle
            (
            );
            /**Sets  the status to create left bubbles of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetCreateLeftBubblesToggle
            (
                bool createLeftBubblesToggle /** createleftbubblestoggle */ 
            );
            /**Returns  the bubble extension offset value of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: double BubbleExtensionOffset
            (
            );
            /**Sets  the bubble extension offset value of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetBubbleExtensionOffset
            (
                double bubbleExtensionOffset /** bubbleextensionoffset */ 
            );
            /**Returns  the value of bubble extension of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: double BubbleExtension
            (
            );
            /**Sets  the value of bubble extension of column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetBubbleExtension
            (
                double bubbleExtension /** bubbleextension */ 
            );

            /// \cond NX_NO_DOC 
            /**Returns  the bubble leader 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: double BubbleLeader
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the bubble leader 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetBubbleLeader
            (
                double bubbleLeader /** bubbleleader */ 
            );

            /// \endcond 
            /**Returns  the value of bubble diameter in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: double BubbleDiameter
            (
            );
            /**Sets  the value of bubble diameter in column grid 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetBubbleDiameter
            (
                double bubbleDiameter /** bubblediameter */ 
            );

            /// \cond NX_NO_DOC 
            /**Returns  the kf object 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::KFObject * KfObject
            (
            );

            /// \endcond 
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
