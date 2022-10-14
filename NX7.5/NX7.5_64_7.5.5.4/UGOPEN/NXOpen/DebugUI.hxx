#ifndef NXOpen_DEBUGUI_HXX_INCLUDED
#define NXOpen_DEBUGUI_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DebugUI.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopendebuguicpp_exports.hxx>
namespace NXOpen
{
    class DebugUI;
    class BlockStylerDebugSession;
    class _DebugUIBuilder;
    class DebugUIImpl;
    /** Represents a class that is used for NX testing that depends on the UI.  This class should not
    be made available to customers */
    class NXOPENDEBUGUICPPEXPORT  DebugUI : public TaggedObject
    {
        private: DebugUIImpl * m_debugui_impl;
        private: static DebugUI *theDebugUI;
        public: static DebugUI *GetDebugUI();
        private: friend class  _DebugUIBuilder;
        protected: DebugUI();
        public: ~DebugUI();
        /**This can only run certain macros.  This method is not for general use.  
            Use of it with out consultation is on a use at your own risk.  <br> License requirements : None */
        public: void ExecuteMacro
        (
            const NXString & fileName /** Name of file   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );


        /** Returns the @link BlockStylerDebugSession BlockStylerDebugSession@endlink  object belonging to this debug session */
        public: NXOpen::BlockStylerDebugSession *BlockStylerDebug();
    };
}
#undef EXPORTLIBRARY
#endif