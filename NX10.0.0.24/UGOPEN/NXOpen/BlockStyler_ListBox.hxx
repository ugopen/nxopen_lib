#ifndef NXOpen_BLOCKSTYLER_LISTBOX_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_LISTBOX_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_ListBox.ja
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
#include <NXOpen/BlockStyler_ListBox.hxx>
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
        class ListBox;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    namespace BlockStyler
    {
        class _ListBoxBuilder;
        class ListBoxImpl;
        /** Represents a ListBox block 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENUICPPEXPORT  ListBox : public NXOpen::BlockStyler::UIBlock
        {
            public: /** Add callback 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<int, NXOpen::BlockStyler::ListBox *> AddCallback;
            public: /** Delete callback.  Return a non-zero value in order to veto the deletion. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<int, NXOpen::BlockStyler::ListBox *> DeleteCallback;
            private: ListBoxImpl * m_listbox_impl;
            private: friend class  _ListBoxBuilder;
            protected: ListBox();
            public: ~ListBox();
            /** Sets the Add handler.  This handler is called when the Add button is pressed.
                The handler is responsible for adding an item to the list.  Nothing will be added to the list unless the handler
                adds it. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAddHandler
            (
                const NXOpen::BlockStyler::ListBox::AddCallback&  cb /** cb */ 
            );
            /** Sets the Delete handler.  If you set this handler, the handler will be
                called when the Delete button is pressed.  The handler does not need to implement code
                to delete the item.  The list will delete the selected items if and only if the handler returns 0. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDeleteHandler
            (
                const NXOpen::BlockStyler::ListBox::DeleteCallback&  cb /** cb */ 
            );
            /**Returns  the AllowDeselectForSingleSelect. Allows deselection of item using Ctrl+MB1 when single select is true.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool AllowDeselectForSingleSelect
            (
            );
            /**Sets  the AllowDeselectForSingleSelect. Allows deselection of item using Ctrl+MB1 when single select is true.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAllowDeselectForSingleSelect
            (
                bool allow /** allow */ 
            );
            /**Returns  the Height
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int Height
            (
            );
            /**Sets  the Height
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetHeight
            (
                int height /** height */ 
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
                bool sensitive /** sensitive */ 
            );
            /**Returns  the IsDeleteButtonSensitive
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsDeleteButtonSensitive
            (
            );
            /**Sets  the IsDeleteButtonSensitive
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDeleteButtonSensitive
            (
                bool sesitive /** sesitive */ 
            );
            /** Gets the ListItems @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetListItems
            (
            );
            /** Sets the ListItems
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetListItems
            (
                std::vector<NXString> & items /** items */ 
            );
            /**Returns  the Localize. If true, translates the Label string into the language of the current locale.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool Localize
            (
            );
            /**Sets  the Localize. If true, translates the Label string into the language of the current locale.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLocalize
            (
                bool localize /** localize */ 
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
                int maxHeight /** max height */ 
            );
            /**Returns  the MaximumStringLength
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int MaximumStringLength
            (
            );
            /**Sets  the MaximumStringLength
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMaximumStringLength
            (
                int maxLength /** max length */ 
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
                int minHeight /** min height */ 
            );
            /**Returns  the ResizeHeightWithDialog
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ResizeHeightWithDialog
            (
            );
            /**Sets  the ResizeHeightWithDialog
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetResizeHeightWithDialog
            (
                bool resize /** resize */ 
            );
            /** Gets SelectedItems @return  selected items
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<int> GetSelectedItems
            (
            );
            /** Sets SelectedItems
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectedItems
            (
                const std::vector<int> & selectedItems /** selected items*/
            );
            /**Returns  the ShowAddButton. If true, Add button is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowAddButton
            (
            );
            /**Sets  the ShowAddButton. If true, Add button is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowAddButton
            (
                bool show /** show */ 
            );
            /**Returns  the ShowDeleteButton. If true, Delete button is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowDeleteButton
            (
            );
            /**Sets  the ShowDeleteButton. If true, Delete button is shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowDeleteButton
            (
                bool show /** show */ 
            );
            /**Returns  the ShowMoveUpDownButtons. If true, MoveUp and MoveDown buttons are shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowMoveUpDownButtons
            (
            );
            /**Sets  the ShowMoveUpDownButtons. If true, MoveUp and MoveDown buttons are shown.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetShowMoveUpDownButtons
            (
                bool show /** show */ 
            );
            /**Returns  the SingleSelect. If true, only single item can be selected.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool SingleSelect
            (
            );
            /**Sets  the SingleSelect. If true, only single item can be selected.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSingleSelect
            (
                bool sinleSelect /** sinle select */ 
            );
            /**Returns  the SelectedItemIndex. Valid only if SingleSelect is true. Otherwise -1 is returned.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int SelectedItemIndex
            (
            );
            /**Sets  the SelectedItemIndex. Valid only if SingleSelect is true. Otherwise -1 is returned.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectedItemIndex
            (
                int index /** index */ 
            );
            /**Returns  the SelectedItemString. Valid only if SingleSelect is true. Otherwise empty string is returned.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString SelectedItemString
            (
            );
            /**Sets  the SelectedItemString. Valid only if SingleSelect is true. Otherwise empty string is returned.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectedItemString
            (
                const NXString & string /** string */ 
            );
            /**Sets  the SelectedItemString. Valid only if SingleSelect is true. Otherwise empty string is returned.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetSelectedItemString
            (
                const char * string /** string */ 
            );
            /** Gets the SelectedItemStrings @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetSelectedItemStrings
            (
            );
            /** Sets the SelectedItemStrings. Selects the list items based on input array of strings.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectedItemStrings
            (
                std::vector<NXString> & strings /** strings */ 
            );
            /** Gets the SelectedItemBooleans. This method returns an integer array of boolen values populated with 0 and 1 @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<int> GetSelectedItemBooleans
            (
            );
            /** Sets the SelectedItemStrings. Selects the list items based on input boolean array. Item is deselcted if value is 0 and selected otherwise.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectedItemBooleans
            (
                const std::vector<int> & items /** items */ 
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
