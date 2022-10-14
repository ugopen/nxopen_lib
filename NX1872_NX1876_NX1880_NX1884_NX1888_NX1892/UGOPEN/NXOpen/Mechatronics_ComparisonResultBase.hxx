#ifndef NXOpen_MECHATRONICS_COMPARISONRESULTBASE_HXX_INCLUDED
#define NXOpen_MECHATRONICS_COMPARISONRESULTBASE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_ComparisonResultBase.ja
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
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class ComparisonResultBase;
    }
    namespace Mechatronics
    {
    }
    namespace Mechatronics
    {
        class ComparisonResultBaseImpl;
        /** Represents base object of comparison result 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  ComparisonResultBase : public NXOpen::TransientObject
        {
            private: ComparisonResultBaseImpl * m_comparisonresultbase_impl;
            /// \cond NX_NO_DOC 
            public: explicit ComparisonResultBase(void *ptr);
            /// \endcond 
            /** Frees the object from memory. After this method is called, it is illegal to use the object. In .NET, this method is automatically called when the object is deleted by the garbage collector. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~ComparisonResultBase();
            /**Returns  the flag marked if the object will be ingored when applying it to logical model 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool Ignored
            (
            );
            /**Sets  the flag marked if the object will be ingored when applying it to logical model 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetIgnored
            (
                bool isIgnored /** Mark if the object will be ingored when applying it to logical model */
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