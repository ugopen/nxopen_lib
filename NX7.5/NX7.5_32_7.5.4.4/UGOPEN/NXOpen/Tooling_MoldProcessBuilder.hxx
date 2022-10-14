#ifndef NXOpen_TOOLING_MOLDPROCESSBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_MOLDPROCESSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_MoldProcessBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/Tooling_MoldProcessBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class MoldProcessBuilder;
    }
    class Builder;
    class SelectPoint;
    namespace Tooling
    {
        class _MoldProcessBuilderBuilder;
        class MoldProcessBuilderImpl;
        /** Represents a Tooling::MoldProcessBuilder builder  <br> To create a new instance of this class, use @link Tooling::MoldProcessCollection::CreateMoldProcessBuilder Tooling::MoldProcessCollection::CreateMoldProcessBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Rename </td> <td> 
         
        0 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  MoldProcessBuilder : public Builder
        {
            private: MoldProcessBuilderImpl * m_moldprocessbuilder_impl;
            private: friend class  _MoldProcessBuilderBuilder;
            protected: MoldProcessBuilder();
            public: ~MoldProcessBuilder();
            /**Returns  the component selected to be edited. The edition will start Standard Part Management dialog  <br> License requirements : None */
            public: NXOpen::SelectPoint * CompSelect
            (
            );
            /**Returns  the rename toggle let users choose whether to run Part Name Management dialog  <br> License requirements : None */
            public: bool Rename
            (
            );
            /**Sets  the rename toggle let users choose whether to run Part Name Management dialog  <br> License requirements : None */
            public: void SetRename
            (
                bool rename /** rename */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif