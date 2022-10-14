#ifndef NXOpen_UISTYLER_DIALOG_HXX_INCLUDED
#define NXOpen_UISTYLER_DIALOG_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_Dialog.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/SelectionHandle.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/UIStyler_StylerItem.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>
namespace NXOpen
{
    namespace UIStyler
    {
        class Dialog;
    }
    class SelectionHandle;
    namespace UIStyler
    {
        class BitMap;
    }
    namespace UIStyler
    {
        class ButtonLayout;
    }
    namespace UIStyler
    {
        class CollapsibleGroup;
    }
    namespace UIStyler
    {
        class ColorTool;
    }
    namespace UIStyler
    {
        class DialogItem;
    }
    namespace UIStyler
    {
        class GroupBox;
    }
    namespace UIStyler
    {
        class IntegerItem;
    }
    namespace UIStyler
    {
        class IntegerScale;
    }
    namespace UIStyler
    {
        class LabelItem;
    }
    namespace UIStyler
    {
        class MultiSelectList;
    }
    namespace UIStyler
    {
        class MultiTextBox;
    }
    namespace UIStyler
    {
        class OptionMenu;
    }
    namespace UIStyler
    {
        class OptionToggle;
    }
    namespace UIStyler
    {
        class PropertyPage;
    }
    namespace UIStyler
    {
        class PushButton;
    }
    namespace UIStyler
    {
        class RadioBox;
    }
    namespace UIStyler
    {
        class RealItem;
    }
    namespace UIStyler
    {
        class RealScale;
    }
    namespace UIStyler
    {
        class RowColumn;
    }
    namespace UIStyler
    {
        class ScrolledWindow;
    }
    namespace UIStyler
    {
        class SelectionBox;
    }
    namespace UIStyler
    {
        class Separator;
    }
    namespace UIStyler
    {
        class SingleSelectList;
    }
    namespace UIStyler
    {
        class StringItem;
    }
    namespace UIStyler
    {
        class StylerItem;
    }
    namespace UIStyler
    {
        class TabControl;
    }
    namespace UIStyler
    {
        class Toggle;
    }
    namespace UIStyler
    {
        class ToolPalette;
    }
    namespace UIStyler
    {
        class WideString;
    }
    namespace UIStyler
    {
        /** Represents dialog response */
        enum DialogResponse
        {
            DialogResponsePickResponse = 1/** User response was a selection of objects.*/,
            DialogResponseOk/** OK button was selected. */,
            DialogResponseCancel/** Cancel button was selected. */,
            DialogResponseBack/** Back button was selected. */,
            DialogResponseApply/** Apply button was selected. */,
            DialogResponseHelp/** Help button was selected. */,
            DialogResponseObjectSelected/** Object was selected. */,
            DialogResponseObjectSelectedByName/** Object was selected by name. */,
            DialogResponseCbTerminate/** Callback routine has terminated. */
        };

        /** Represents indexes */
        enum DialogIndex
        {
            DialogIndexNoSubIndex = -1/** All sub items are selected.*/
        };

    }
    namespace UIStyler
    {
        /** Represents a DialogItem for UI Styler. */
        class NXOPENUICPPEXPORT Dialog : public TransientObject
        {
            /** Represents dialog item type */
            public: enum ItemType
            {
                ItemTypePushButton/** push button */ ,
                ItemTypeDialogItem/** dialog item */ ,
                ItemTypeRadioBox/** radio box */ ,
                ItemTypeRealItem/** real item */ ,
                ItemTypeRealScale/** real scale */ ,
                ItemTypeBitmap/** bitmap */ ,
                ItemTypeRowColumn/** row column */ ,
                ItemTypeButtonLayout/** button layout */ ,
                ItemTypeScrolledWindow/** scrolled window */ ,
                ItemTypeColorTool/** color tool */ ,
                ItemTypeSelectionBox/** selection box */ ,
                ItemTypeSeparator/** separator */ ,
                ItemTypeSingleSelectList/** single select list */ ,
                ItemTypeStringItem/** string item */ ,
                ItemTypeGroupBox/** group box */ ,
                ItemTypeIntegerItem/** integer item */ ,
                ItemTypeIntegerScale/** integer scale */ ,
                ItemTypeMultiSelectList/** multi select list */ ,
                ItemTypeLabelItem/** label item */ ,
                ItemTypeMultiTextBox/** multi text box */ ,
                ItemTypeTabControl/** tab control */ ,
                ItemTypeOptionMenu/** option menu */ ,
                ItemTypeToggle/** toggle */ ,
                ItemTypeOptionToggle/** option toggle */ ,
                ItemTypeToolPalette/** tool palette */ ,
                ItemTypeWideString/** wide string */ ,
                ItemTypePropertyPage/** property page */ ,
                ItemTypeCollapsibleGroup/** collapsible group */ 
            };

            public: explicit Dialog(void *ptr);
            /** Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET or Java, this 
                method is automatically called when the object is deleted by the 
                garbage collector.  <br> License requirements : None */
            public: virtual ~Dialog();
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::DialogItem * GetDialogIndex
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::PushButton * GetPushButton
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::BitMap * GetBitmap
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::ButtonLayout * GetButtonLayout
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::ColorTool * GetColorTool
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::GroupBox * GetGroupBox
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::IntegerItem * GetIntegerItem
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::IntegerScale * GetIntegerScale
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::MultiSelectList * GetMultiSelectList
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::MultiTextBox * GetMultiTextBox
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::OptionMenu * GetOptionMenu
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::OptionToggle * GetOptionToggle
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::PropertyPage * GetPropertyPage
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::RadioBox * GetRadioBox
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::RealItem * GetRealItem
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::RealScale * GetRealScale
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::RowColumn * GetRowColumn
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::ScrolledWindow * GetScrolledWindow
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::SelectionBox * GetSelectionBox
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::Separator * GetSeparator
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::SingleSelectList * GetSingleSelectList
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::StringItem * GetStringItem
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::TabControl * GetTabControl
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::Toggle * GetToggle
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::ToolPalette * GetToolPalette
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::LabelItem * GetLabelItem
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::CollapsibleGroup * GetCollapsibleGroup
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::WideString * GetWideString
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the dialog item with specified item identifier  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::StylerItem * GetStylerItem
            (
                const NXString & itemIdentifier /** Dialog name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::UIStyler::Dialog::ItemType type /** type */ 
            );
            /** Gets the dialog item for a selection handle  @return   <br> License requirements : None */
            public: NXOpen::UIStyler::StylerItem * GetDialogItemUsingSelectionHandle
            (
                NXOpen::SelectionHandle * select /**Selection handle */
            );
            /** Displays an NX (UIStyler generated) "bottom" dialog.  This dialog 
                    is displayed to NX. Show Method can only be called once for the 
                    dialog object.Once show method is called @link UIStyler::Dialog::GetStylerItem UIStyler::Dialog::GetStylerItem@endlink  
                    will create any item
                 @return   <br> License requirements : None */
            public: NXOpen::UIStyler::DialogResponse Show
            (
            );
            /** Registers the dialog with a menu item. <br> License requirements : None */
            public: void RegisterWithUiMenu
            (
                bool isTopDialog /** is top dialog */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif