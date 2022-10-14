#ifndef NXOpen_UISTYLER_ATTACHMENT_HXX_INCLUDED
#define NXOpen_UISTYLER_ATTACHMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_Attachment.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>
namespace NXOpen
{
    namespace UIStyler
    {
        class Attachment;
    }
    namespace UIStyler
    {
    }
    namespace UIStyler
    {
        /** Represents an Attachment for UI Styler */
        class NXOPENUICPPEXPORT Attachment : public TransientObject
        {
            /** Represents alignment option for Styler Item */
            public: enum AttachType
            {
                AttachTypeDialog/** Dialog type */,
                AttachTypeDefault/** Default type  */,
                AttachTypeNone/** None type */,
                AttachTypeNoChange/** No change type */,
                AttachTypeItem/** Item type */
            };

            public: explicit Attachment(void *ptr);
            /** Free resources associated with the instance. 
                 After this method is called, it is illegal to use the object.  
                 In .NET or Java, this method is automatically called when 
                 the object is deleted by the garbage collector.  <br> License requirements : None */
            public: virtual ~Attachment();
            /** Sets whether the dialog item is at the center <br> License requirements : None */
            public: void SetCenter
            (
                bool is_center /** center*/
            );
            /** Sets the attach type top <br> License requirements : None */
            public: void SetAttachTypeTop
            (
                NXOpen::UIStyler::Attachment::AttachType attach_type_top /** attach_type_top */
            );
            /** Sets the attach type left <br> License requirements : None */
            public: void SetAttachTypeLeft
            (
                NXOpen::UIStyler::Attachment::AttachType attach_type_left /** attach type left */ 
            );
            /** Sets the attach type right <br> License requirements : None */
            public: void SetAttachTypeRight
            (
                NXOpen::UIStyler::Attachment::AttachType attach_type_right /** attach type right */ 
            );
            /** Sets the top offset <br> License requirements : None */
            public: void SetTopOffset
            (
                int offset_top /** offset top */ 
            );
            /** Sets the left offset <br> License requirements : None */
            public: void SetLeftOffset
            (
                int offset_left /** offset left */ 
            );
            /** Sets the right offset <br> License requirements : None */
            public: void SetRightOffset
            (
                int offset_right /** offset right */ 
            );
            /** Sets the top dialog item <br> License requirements : None */
            public: void SetTopDialogItem
            (
                const NXString & top_item_identifire /** Top item identifier   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the left dialog item <br> License requirements : None */
            public: void SetLeftDialogItem
            (
                const NXString & left_item_identifire /** Left item identifier   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the right dialog item <br> License requirements : None */
            public: void SetRightDialogItem
            (
                const NXString & right_item_identifire /** Right item identifier   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif