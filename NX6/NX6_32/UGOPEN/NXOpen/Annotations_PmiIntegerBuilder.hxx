#ifndef NXOpen_ANNOTATIONS_PMIINTEGERBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIINTEGERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiIntegerBuilder.ja
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
#include <NXOpen/Annotations_PmiIntegerBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiIntegerBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class _PmiIntegerBuilderBuilder;
        /** Represents a @link Annotations::PmiInteger Annotations::PmiInteger@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreatePmiIntegerBuilder Annotations::PmiAttributeCollection::CreatePmiIntegerBuilder@endlink  <br> 
        Default values:
        IntegerValue: 0
        */
        class NXOPENCPPEXPORT PmiIntegerBuilder : public Annotations::PmiAttributeBuilder
        {
            private: friend class  _PmiIntegerBuilderBuilder;
            protected: PmiIntegerBuilder();
            /**Returns  the str title  <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the str title  <br> License requirements : None */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Returns  the int value  <br> License requirements : None */
            public: int IntegerValue
            (
            );
            /**Sets  the int value  <br> License requirements : None */
            public: void SetIntegerValue
            (
                int integerValue /** integervalue */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif