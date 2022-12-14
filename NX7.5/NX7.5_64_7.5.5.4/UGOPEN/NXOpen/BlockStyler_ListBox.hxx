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
        /** Represents a ListBox block */
        class NXOPENUICPPEXPORT  ListBox : public BlockStyler::UIBlock
        {
            public: /** Add callback  <br> License requirements : None */
            typedef NXOpen::Callback1<int, NXOpen::BlockStyler::ListBox *> AddCallback;
            public: /** Delete callback.  Return a non-zero value in order to veto the deletion.  <br> License requirements : None */
            typedef NXOpen::Callback1<int, NXOpen::BlockStyler::ListBox *> DeleteCallback;
            private: ListBoxImpl * m_listbox_impl;
            private: friend class  _ListBoxBuilder;
            protected: ListBox();
            public: ~ListBox();
            /** Sets the Add handler.  This handler is called when the Add button is pressed.
                The handler is responsible for adding an item to the list.  Nothing will be added to the list unless the handler
                adds it.  <br> License requirements : None */
            public: void SetAddHandler
            (
                const NXOpen::BlockStyler::ListBox::AddCallback&  cb /** cb */ 
            );
            /** Sets the Delete handler.  If you set this handler, the handler will be
                called when the Delete button is pressed.  The handler does not need to implement code
                to delete the item.  The list will delete the selected items if and only if the handler returns 0.  <br> License requirements : None */
            public: void SetDeleteHandler
            (
                const NXOpen::BlockStyler::ListBox::DeleteCallback&  cb /** cb */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
