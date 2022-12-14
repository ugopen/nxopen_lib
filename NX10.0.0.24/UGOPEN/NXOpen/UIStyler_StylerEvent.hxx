#ifndef NXOpen_UISTYLER_STYLEREVENT_HXX_INCLUDED
#define NXOpen_UISTYLER_STYLEREVENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_StylerEvent.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/UIStyler_StylerItem.hxx>
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
    namespace UIStyler
    {
        class StylerEvent;
    }
    namespace UIStyler
    {
        class StylerItem;
    }
    namespace UIStyler
    {
    }
    namespace UIStyler
    {
        class StylerEventImpl;
        /** Represents a StylerEvent 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENUICPPEXPORT  StylerEvent : public NXOpen::TransientObject
        {
            /** Describes callback reason */
            public: enum Reason
            {
                ReasonNoReason = -1/** No reason */,
                ReasonActivateReason/** Activate reason */,
                ReasonValueChangedReason/** Value changed reason */,
                ReasonDragReason/** Drag reason */,
                ReasonDoubleClickReason/** Double click reason */,
                ReasonOkReason/** Ok reason */,
                ReasonApplyReason/** Apply reason */,
                ReasonBackReason/** BAck reason */,
                ReasonCancelReason/** Cancel reason */,
                ReasonConstructReason/** Construct reason */,
                ReasonDestructReason/** Destruct reason */,
                ReasonFileopReason/** File operation reason */,
                ReasonSwitchReason/** Switch reason */,
                ReasonFileOperationReason/** File operation reason */,
                ReasonExitFileOperationReason/** Exit file operation reason */
            };

            /** Describes indicator value */
            public: enum Indicator
            {
                IndicatorNoValue = -1/** No value */,
                IndicatorStringValue/** String value */,
                IndicatorStringPointerValue/** String pointer value */,
                IndicatorIntegerValue/** Integer value */,
                IndicatorIntegerPointerValue/** Integer pointer value */,
                IndicatorRealValue/** Real value */,
                IndicatorRealPointerValue/** Real pointer value */,
                IndicatorSelectionValue/** Selection value */,
                IndicatorOptionToggleValue/** Option toggle value */
            };

            /** Describes event index */
            public: enum Miscellaneous
            {
                MiscellaneousNoSubIndex = -1/** No sub index */,
                MiscellaneousOkIndex/** Ok index */,
                MiscellaneousApplyIndex/** Apply index */,
                MiscellaneousBackIndex/** Back index */,
                MiscellaneousCancelIndex/** Cancel index */
            };

            private: StylerEventImpl * m_stylerevent_impl;
            /// \cond NX_NO_DOC 
            public: explicit StylerEvent(void *ptr);
            /// \endcond 
            /** Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET or Java, this 
                method is automatically called when the object is deleted by the 
                garbage collector. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~StylerEvent();
            /** Gets the dialog item @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::UIStyler::StylerItem * GetStylerItem
            (
            );
            /**Gets the reason for the event @return  Reason 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::UIStyler::StylerEvent::Reason GetReason
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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
