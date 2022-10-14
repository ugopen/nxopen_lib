#ifndef NXOpen_DRAWINGS_SECTIONINVIEWBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_SECTIONINVIEWBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_SectionInViewBuilder.ja
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
#include <NXOpen/Drawings_HiddenObjectsBuilder.hxx>
#include <NXOpen/Drawings_SectionInViewBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class SectionInViewBuilder;
    }
    class Builder;
    namespace Drawings
    {
        class HiddenObjectsBuilder;
    }
    namespace Drawings
    {
        class SelectDraftingViewList;
    }
    namespace Drawings
    {
        class _SectionInViewBuilderBuilder;
        class SectionInViewBuilderImpl;
        /** This builder allows the user to select a view in which component or
                solid body objects can be designated as section, non-sectioned, or neither  <br> To create a new instance of this class, use @link Drawings::DraftingViewCollection::CreateSectionInViewBuilder  Drawings::DraftingViewCollection::CreateSectionInViewBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        EditType </td> <td> 
         
        MakeNonSectioned </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  SectionInViewBuilder : public Builder
        {
            /** Edit Section type */
            public: enum EditSxtype
            {
                EditSxtypeMakeNonSectioned/** make non sectioned */ ,
                EditSxtypeMakeSectioned/** make sectioned */ ,
                EditSxtypeRemoveViewSpecific/** remove view specific */ 
            };

            private: SectionInViewBuilderImpl * m_sectioninviewbuilder_impl;
            private: friend class  _SectionInViewBuilderBuilder;
            protected: SectionInViewBuilder();
            public: ~SectionInViewBuilder();
            /**Returns  the views 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SelectDraftingViewList * Views
            (
            );
            /**Returns  the objects 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::HiddenObjectsBuilder * EditObjects
            (
            );
            /**Returns  the type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SectionInViewBuilder::EditSxtype EditType
            (
            );
            /**Sets  the type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetEditType
            (
                NXOpen::Drawings::SectionInViewBuilder::EditSxtype editType /** edittype */ 
            );
        };
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