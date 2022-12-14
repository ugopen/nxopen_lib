#ifndef NXOpen_TOOLING_COOLINGPATTERNBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_COOLINGPATTERNBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_CoolingPatternBuilder.ja
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
#include <NXOpen/Section.hxx>
#include <NXOpen/Tooling_CoolingPatternBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class CoolingPatternBuilder;
    }
    class Builder;
    class Section;
    namespace Tooling
    {
        class _CoolingPatternBuilderBuilder;
        class CoolingPatternBuilderImpl;
        /**The builder class for Cooling pattern which assists you
               to create channels with selected curves. <br> To create a new instance of this class, use @link Tooling::CoolingPatternCollection::CreateCoolingPatternBuilder Tooling::CoolingPatternCollection::CreateCoolingPatternBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ChannelDiameter </td> <td> 
         
        10 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  CoolingPatternBuilder : public Builder
        {
            private: CoolingPatternBuilderImpl * m_coolingpatternbuilder_impl;
            private: friend class  _CoolingPatternBuilderBuilder;
            protected: CoolingPatternBuilder();
            public: ~CoolingPatternBuilder();
            /**Returns  the lines used to create the channel path.  <br> License requirements : None */
            public: NXOpen::Section * ChannelGuide
            (
            );
            /**Returns  the channel diameter  <br> License requirements : None */
            public: double ChannelDiameter
            (
            );
            /**Sets  the channel diameter  <br> License requirements : None */
            public: void SetChannelDiameter
            (
                double channelDiameter /** channeldiameter */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
