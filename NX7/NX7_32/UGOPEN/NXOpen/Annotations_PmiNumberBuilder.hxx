#ifndef NXOpen_ANNOTATIONS_PMINUMBERBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMINUMBERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiNumberBuilder.ja
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
#include <NXOpen/Annotations_PmiNumberBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiNumberBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class _PmiNumberBuilderBuilder;
        /** Represents a @link Annotations::PmiNumber Annotations::PmiNumber@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreatePmiNumberBuilder Annotations::PmiAttributeCollection::CreatePmiNumberBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        NumberValue </td> <td> 
         
        0 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT PmiNumberBuilder : public Annotations::PmiAttributeBuilder
        {
            private: friend class  _PmiNumberBuilderBuilder;
            protected: PmiNumberBuilder();
            /**Returns  the str title  <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the str title  <br> License requirements : None */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Returns  the num value  <br> License requirements : None */
            public: double NumberValue
            (
            );
            /**Sets  the num value  <br> License requirements : None */
            public: void SetNumberValue
            (
                double numberValue /** numbervalue */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
