#ifndef NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONSWEEPBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONSWEEPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_SubdivisionSweepBuilder.ja
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
#include <NXOpen/Features_Subdivision_SubdivisionSweepBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
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
            class SubdivisionSweepBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace Subdivision
        {
            class CageSectionDataList;
        }
    }
    namespace Features
    {
        namespace Subdivision
        {
            class _SubdivisionSweepBuilderBuilder;
            class SubdivisionSweepBuilderImpl;
            /** Represents a @link NXOpen::Features::Subdivision::SubdivisionSweepBuilder NXOpen::Features::Subdivision::SubdivisionSweepBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSweepBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSweepBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            CanSew </td> <td> 
             
            1 </td> </tr> 

            </table>  

             <br>  Created in NX10.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SubdivisionSweepBuilder : public NXOpen::Builder
            {
                private: SubdivisionSweepBuilderImpl * m_subdivisionsweepbuilder_impl;
                private: friend class  _SubdivisionSweepBuilderBuilder;
                protected: SubdivisionSweepBuilder();
                public: ~SubdivisionSweepBuilder();
                /**Returns  the section objects. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::CageSectionDataList * Sections
                (
                );
                /**Returns  the guide objects. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::CageSectionDataList * Guides
                (
                );
                /**Returns  the value indicating if open edges of the swept mesh can be sewn with selected input open edges.
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanSew
                (
                );
                /**Sets  the value indicating if open edges of the swept mesh can be sewn with selected input open edges.
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetCanSew
                (
                    bool canSew /** cansew */ 
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
