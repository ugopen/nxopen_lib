#ifndef NXOpen_MENDIXREPORTING_CHECKERDATASTATUS_HXX_INCLUDED
#define NXOpen_MENDIXREPORTING_CHECKERDATASTATUS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MendixReporting_CheckerDataStatus.ja
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
#include <NXOpen/libnxopencpp_mendixreporting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MendixReporting
    {
        class CheckerDataStatus;
    }
    class Session;
    namespace MendixReporting
    {
        class CheckerDataStatusImpl;

        /// \cond NX_NO_DOC 
        /** Represents a class that keeps the checker data status  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_MENDIXREPORTINGEXPORT  CheckerDataStatus
        {
            private: CheckerDataStatusImpl * m_checkerdatastatus_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CheckerDataStatus(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CheckerDataStatus();

            /// \cond NX_NO_DOC 
            /** Returns the response json string of all the available status for the checker data  @return  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetAvailableCheckerStatus
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
