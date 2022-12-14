#ifndef NXOpen_GATEWAY_DESIGNSPACEEXPLORERAUTOTESTPRINT_HXX_INCLUDED
#define NXOpen_GATEWAY_DESIGNSPACEEXPLORERAUTOTESTPRINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Gateway_DesignSpaceExplorerAutotestPrint.ja
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
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Gateway
    {
        class DesignSpaceExplorerAutotestPrint;
    }
    class DebugSession;
    namespace Gateway
    {
        class DesignSpaceExplorerAutotestPrintImpl;

        /// \cond NX_NO_DOC 
        /** Represents a class that is used for NX Design Space Explorer Autotest testing. This class should not be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENDEBUGSESSIONCPPEXPORT  DesignSpaceExplorerAutotestPrint
        {
            private: DesignSpaceExplorerAutotestPrintImpl * m_designspaceexplorerautotestprint_impl;
            private: NXOpen::DebugSession* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit DesignSpaceExplorerAutotestPrint(NXOpen::DebugSession *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~DesignSpaceExplorerAutotestPrint();

            /// \cond NX_NO_DOC 
            /** JA Print Design Space Explorer data
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void PrintDesignSpaceExplorerData
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Registers the design space explorer validation custom compare functions 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void RegisterCustomCompareFunctions
            (
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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
