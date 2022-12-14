#ifndef NXOpen_BLOCKSTYLER_SETLIST_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_SETLIST_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_SetList.ja
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
#include <NXOpen/BlockStyler_SetList.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace BlockStyler
    {
        class SetList;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    namespace BlockStyler
    {
        class _SetListBuilder;
        class SetListImpl;
        /** Represents a SetList block 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENUICPPEXPORT  SetList : public NXOpen::BlockStyler::UIBlock
        {
            /** During Insert, indicates whether component should be
                inserted before or after the insertion location */
            public: enum InsertionLocation
            {
                InsertionLocationBefore/** before */ ,
                InsertionLocationAfter/** after */ 
            };

            public: /** Add callback 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<int, NXOpen::BlockStyler::SetList *> AddCallback;
            public: /** Delete callback.  Return a non-zero value in order to veto the deletion. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback2<int, NXOpen::BlockStyler::SetList *, NXOpen::BlockStyler::UIBlock *> DeleteCallback;
            public: /** Reorder callback 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback4<int, NXOpen::BlockStyler::SetList *, NXOpen::BlockStyler::UIBlock *, int, int> ReorderCallback;
            private: SetListImpl * m_setlist_impl;
            private: friend class  _SetListBuilder;
            protected: SetList();
            public: ~SetList();
            /** Sets the seed using a dlx file.  The seed must be set during initialization.
                Setting the seed will also reset any Add and Delete handlers that has been registered,
                so SetSeed should be called prior to calling SetAddHandler or SetDeleteHandler. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSeed
            (
                const NXString & dlxFile /** The dlx file used to create the seed   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the seed using a dlx file.  The seed must be set during initialization.
                Setting the seed will also reset any Add and Delete handlers that has been registered,
                so SetSeed should be called prior to calling SetAddHandler or SetDeleteHandler. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            void SetSeed
            (
                const char * dlxFile /** The dlx file used to create the seed   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the AddNewSet handler.  If you set this handler, the handler will be
                called when the Add New Set button is pressed, and the handler will be responsible
                for adding an item to the list.  Nothing will be added to the list unless the handler
                adds it. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAddHandler
            (
                const NXOpen::BlockStyler::SetList::AddCallback&  cb /** cb */ 
            );
            /** Sets the Delete handler.  If you set this handler, the handler will be
                called when the Delete button is pressed.  The handler does not need to implement code
                to delete the item.  The list will delete the item if and only if the handler returns 0. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDeleteHandler
            (
                const NXOpen::BlockStyler::SetList::DeleteCallback&  cb /** cb */ 
            );
            /** Sets the Reorder observer.  If you set this observer, the observer will
                be called after an item is moved by pressing the Move Up and Down buttons.
                The observer does not need to implement the move up and down behavior and is called
                after the item has already been moved. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReorderObserver
            (
                const NXOpen::BlockStyler::SetList::ReorderCallback&  cb /** cb */ 
            );
            /** Adds an item to the end of the list  @return  The added item 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::BlockStyler::UIBlock * AddNewSet
            (
                bool copyPropertiesAndSelect /** Indicates whether to copy properties from the 
                                currently selected component and set focus to the new set */
            );
            /** Deletes an item from the list 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void Delete
            (
                NXOpen::BlockStyler::UIBlock * uicomp /** Item to delete */
            );
            /** Swaps the location of two items 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void Swap
            (
                NXOpen::BlockStyler::UIBlock * uicomp1 /** Item to swap */,
                NXOpen::BlockStyler::UIBlock * uicomp2 /** Item to swap */
            );
            /** Inserts an item before or after a specified item  @return  The inserted item 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::BlockStyler::UIBlock * InsertNewSet
            (
                NXOpen::BlockStyler::UIBlock * location /** Location to insert the new item */,
                NXOpen::BlockStyler::SetList::InsertionLocation insertBeforeOrAfter /** Indicates whether to insert the new item before or after the specified location */,
                bool copyPropertiesAndSelect /** Indicates whether to copy properties from the 
                                currently selected component and set focus to the new set */
            );
            /** Sets the text for the specified item.
                    If the list has a title column, the title column is not included in the item text. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetItemText
            (
                NXOpen::BlockStyler::UIBlock * item /** item */ ,
                std::vector<NXString> & strings /** The text.  The text may only contain characters in the locale character set */
            );
            /** Gets the text for the specified item.
                    If the list has a title column, the title column is not included in the item text.  @return  The text 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetItemText
            (
                NXOpen::BlockStyler::UIBlock * item /** item */ 
            );
            /** When an update event occurs on the list, this method finds the
                item in the list that was updated  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::BlockStyler::UIBlock * FindUpdated
            (
            );
            /** Gets the selected items  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::BlockStyler::UIBlock *> GetSelected
            (
            );
            /** Sets the selected items.  If the "Multiple Edit" property is false,
                no more than one item can be selected 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSelected
            (
                const std::vector<NXOpen::BlockStyler::UIBlock *> & items /** items */ 
            );
            /** Gets all the items in the list  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::BlockStyler::UIBlock *> GetItems
            (
            );
            /**Returns  the AddNewSetLabel. Specifies the label for AddNewSet button.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString AddNewSetLabel
            (
            );
            /**Sets  the AddNewSetLabel. Specifies the label for AddNewSet button.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAddNewSetLabel
            (
                const NXString & label /** label */ 
            );
            /**Sets  the AddNewSetLabel. Specifies the label for AddNewSet button.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetAddNewSetLabel
            (
                const char * label /** label */ 
            );
            /** Gets the ColumnLabels @return  Values to get from the property
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetColumnLabels
            (
            );
            /** Sets the ColumnLabels
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetColumnLabels
            (
                std::vector<NXString> & labels /** Values to set to the property*/
            );
            /** Gets the ColumnWidths @return  Values to get from the property
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<int> GetColumnWidths
            (
            );
            /** Sets the ColumnWidths
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetColumnWidths
            (
                const std::vector<int> & width /** Values to set to the property*/
            );
            /**Returns  the DefaultColumnWidth
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int DefaultColumnWidth
            (
            );
            /**Sets  the DefaultColumnWidth
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDefaultColumnWidth
            (
                int defaultWidth /** defaultwidth */ 
            );
            /**Returns  the IsAddButtonSensitive
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsAddButtonSensitive
            (
            );
            /**Sets  the IsAddButtonSensitive
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAddButtonSensitive
            (
                bool addButton /** addbutton */ 
            );
            /**Returns  the Layout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString LayoutAsString
            (
            );
            /**Sets  the Layout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLayoutAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the Layout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetLayoutAsString
            (
                const char * enumString /** enumstring */ 
            );
            /** Gets the Layout members @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetLayoutMembers
            (
            );
            /**Returns  the ListExpanded. If true, the list is expanded.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ListExpanded
            (
            );
            /**Sets  the ListExpanded. If true, the list is expanded.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetListExpanded
            (
                bool expanded /** expanded */ 
            );
            /**Returns  the ListHideGroup
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ListHideGroup
            (
            );
            /**Sets  the ListHideGroup
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetListHideGroup
            (
                bool listHideGroup /** listhidegroup */ 
            );
            /**Returns  the MaximumHeight
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int MaximumHeight
            (
            );
            /**Sets  the MaximumHeight
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMaximumHeight
            (
                int maxHeight /** maxheight */ 
            );
            /**Returns  the MinimumHeight
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int MinimumHeight
            (
            );
            /**Sets  the MinimumHeight
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMinimumHeight
            (
                int minHeight /** minheight */ 
            );
            /**Returns  the MultipleEdit
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool MultipleEdit
            (
            );
            /**Sets  the MultipleEdit
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMultipleEdit
            (
                bool multipleEdit /** multipleedit */ 
            );
            /**Returns  the NumberColumnString as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString NumberColumnString
            (
            );
            /**Sets  the NumberColumnString as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetNumberColumnString
            (
                const NXString & columnString /** columnstring */ 
            );
            /**Sets  the NumberColumnString as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetNumberColumnString
            (
                const char * columnString /** columnstring */ 
            );
            /**Returns  the NumberOfColumns
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int NumberOfColumns
            (
            );
            /**Sets  the NumberOfColumns
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetNumberOfColumns
            (
                int numColumns /** numcolumns */ 
            );
            /**Returns  the ResizeHeightWithDialog. If true, height of the block changes dynamically with dialog.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ResizeHeightWithDialog
            (
            );
            /**Sets  the ResizeHeightWithDialog. If true, height of the block changes dynamically with dialog.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetResizeHeightWithDialog
            (
                bool resize /** resize */ 
            );
            /**Returns  the SeedDlxFile as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString SeedDlxFile
            (
            );
            /**Sets  the SeedDlxFile as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSeedDlxFile
            (
                const NXString & dlxName /** dlxname */ 
            );
            /**Sets  the SeedDlxFile as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetSeedDlxFile
            (
                const char * dlxName /** dlxname */ 
            );
            /**Returns  the ShowAddNewSet. If true, "Add New Set" button is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowAddNewSet
            (
            );
            /**Sets  the ShowAddNewSet. If true, "Add New Set" button is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowAddNewSet
            (
                bool show /** show */ 
            );
            /**Returns  the ShowColumnHeadings
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowColumnHeadings
            (
            );
            /**Sets  the ShowColumnHeadings
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowColumnHeadings
            (
                bool show /** show */ 
            );
            /**Returns  the ShowRemove. If true, "Remove" button is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowRemove
            (
            );
            /**Sets  the ShowRemove. If true, "Remove" button is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowRemove
            (
                bool show /** show */ 
            );
            /**Returns  the ShowReorderControls
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowReorderControls
            (
            );
            /**Sets  the ShowReorderControls
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowReorderControls
            (
                bool show /** show */ 
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
