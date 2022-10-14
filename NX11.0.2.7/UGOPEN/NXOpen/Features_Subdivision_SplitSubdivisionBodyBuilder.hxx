#ifndef NXOpen_FEATURES_SUBDIVISION_SPLITSUBDIVISIONBODYBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_SPLITSUBDIVISIONBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_SplitSubdivisionBodyBuilder.ja
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
#include <NXOpen/Features_Subdivision_SplitSubdivisionBodyBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace Subdivision
        {
            class SplitSubdivisionBodyBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace Subdivision
        {
            class SelectSubdivisionBodyList;
        }
    }
    namespace Features
    {
        namespace Subdivision
        {
            class _SplitSubdivisionBodyBuilderBuilder;
            class SplitSubdivisionBodyBuilderImpl;
            /** Represents a @link Features::Subdivision::SplitSubdivisionBodyBuilder Features::Subdivision::SplitSubdivisionBodyBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSplitSubdivisionBodyBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSplitSubdivisionBodyBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            InputBodyOption </td> <td> 
             
            Delete </td> </tr> 

            </table>  

             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SplitSubdivisionBodyBuilder : public NXOpen::Builder
            {
                /** Options indicating actions to be taken on input @link Features::Subdivision::SubdivisionBody Features::Subdivision::SubdivisionBody@endlink  features */
                public: enum InputBodyOptions
                {
                    InputBodyOptionsKeep/** Keep the feature as they are */,
                    InputBodyOptionsHide/** Hide the features */,
                    InputBodyOptionsDelete/** Delete the features */
                };

                private: SplitSubdivisionBodyBuilderImpl * m_splitsubdivisionbodybuilder_impl;
                private: friend class  _SplitSubdivisionBodyBuilderBuilder;
                protected: SplitSubdivisionBodyBuilder();
                public: ~SplitSubdivisionBodyBuilder();
                /**Returns  the @link Features::Subdivision::SubdivisionBody Features::Subdivision::SubdivisionBody@endlink  features to split 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::SelectSubdivisionBodyList * SubdivisionBodiesToSplit
                (
                );
                /**Returns  the input body option 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::SplitSubdivisionBodyBuilder::InputBodyOptions InputBodyOption
                (
                );
                /**Sets  the input body option 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetInputBodyOption
                (
                    NXOpen::Features::Subdivision::SplitSubdivisionBodyBuilder::InputBodyOptions inputBody /** inputbody */ 
                );
            };
        }
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