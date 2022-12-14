#ifndef NXOpen_ANNOTATIONS_CIRCULARCENTERLINEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_CIRCULARCENTERLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CircularCenterlineBuilder.ja
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
#include <NXOpen/Annotations_CircleCenterlineBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class CircularCenterlineBuilder;
    }
    namespace Annotations
    {
        class CircleCenterlineBuilder;
    }
    namespace Annotations
    {
        class _CircularCenterlineBuilderBuilder;
        /** Represents a CircularCenterlineBuilder Builder  <br> To create a new instance of this class, use @link Annotations::CenterlineCollection::CreateCircularCenterlineBuilder Annotations::CenterlineCollection::CreateCircularCenterlineBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        FullCircle </td> <td> 
         
        true </td> </tr> 

        <tr><td> 
         
        Type </td> <td> 
         
        Through3Points </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT CircularCenterlineBuilder : public Annotations::CircleCenterlineBuilder
        {
            private: friend class  _CircularCenterlineBuilderBuilder;
            protected: CircularCenterlineBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
