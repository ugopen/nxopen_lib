#ifndef NXOpen_ANNOTATIONS_ARBITRARYTARGETDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ARBITRARYTARGETDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ArbitraryTargetData.ja
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
#include <NXOpen/Annotations_DatumTargetData.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class ArbitraryTargetData;
    }
    namespace Annotations
    {
        class DatumTargetData;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        class ArbitraryTargetDataImpl;
        /** Represents arbitrary datum target data 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  ArbitraryTargetData : public Annotations::DatumTargetData
        {
            private: ArbitraryTargetDataImpl * m_arbitrarytargetdata_impl;
            /// \cond NX_NO_DOC 
            public: explicit ArbitraryTargetData(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~ArbitraryTargetData();
            /**Returns  the upper text.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString UpperText
            (
            );
            /**Sets  the upper text.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetUpperText
            (
                const NXString & upperText /** New upper text */
            );
            /**Sets  the upper text.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            void SetUpperText
            (
                const char * upperText /** New upper text */
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
