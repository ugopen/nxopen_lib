#ifndef NXOpen_ANNOTATIONS_SEARCHMODELVIEWBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SEARCHMODELVIEWBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SearchModelViewBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
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
        class SearchModelViewBuilder;
    }
    class Builder;
    class NXObject;
    class TaggedObjectList;
    namespace Annotations
    {
        class _SearchModelViewBuilderBuilder;
        class SearchModelViewBuilderImpl;
        /**
            Represents a @link NXOpen::Annotations::SearchModelViewBuilder NXOpen::Annotations::SearchModelViewBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::Annotations::SearchModelViewCollection::CreateSearchModelViewBuilder  NXOpen::Annotations::SearchModelViewCollection::CreateSearchModelViewBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        PmiType </td> <td> 
         
        Dimension </td> </tr> 

        </table>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  SearchModelViewBuilder : public NXOpen::Builder
        {
            /** the search criteria pmitype */
            public: enum PmiTypes
            {
                PmiTypesDimension/** dimension type */,
                PmiTypesFeatureControlFrame/** feature control frame type */,
                PmiTypesDatumFeatureSymbol/** datum feature symbol type */,
                PmiTypesDatumTarget/** datum target type */,
                PmiTypesSurfaceFinish/** surface finish type */,
                PmiTypesNote/** note type */
            };

            /** Represents the value comparision options*/
            public: enum ValueComparisionOptions
            {
                ValueComparisionOptionsLess/** less */ ,
                ValueComparisionOptionsLessEqual/** less equal */ ,
                ValueComparisionOptionsEqual/** equal */ ,
                ValueComparisionOptionsMoreEqual/** more equal */ ,
                ValueComparisionOptionsMore/** more */ 
            };

            /** Represents the text comparision options*/
            public: enum TextComparisionOptions
            {
                TextComparisionOptionsEquals/** Equals*/,
                TextComparisionOptionsContains/** Contains */
            };

            /** seaerch scope type */
            public: enum SearchScopeOptions
            {
                SearchScopeOptionsWorkPart/** work part only */,
                SearchScopeOptionsWorkPartAndComponents/** work part and components */
            };

            private: SearchModelViewBuilderImpl * m_searchmodelviewbuilder_impl;
            private: friend class  _SearchModelViewBuilderBuilder;
            protected: SearchModelViewBuilder();
            public: ~SearchModelViewBuilder();
            /**Returns  the pmi type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::PmiTypes PmiType
            (
            );
            /**Sets  the pmi type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetPmiType
            (
                NXOpen::Annotations::SearchModelViewBuilder::PmiTypes pmiType /** pmitype */ 
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void ExecuteSearch
            (
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SaveAsModelView
            (
            );
            /**Returns  the search scope 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::SearchScopeOptions SearchScope
            (
            );
            /**Sets  the search scope 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSearchScope
            (
                NXOpen::Annotations::SearchModelViewBuilder::SearchScopeOptions searchScope /** searchscope */ 
            );
            /**Returns  the name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString ModelViewName
            (
            );
            /**Sets  the name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetModelViewName
            (
                const NXString & modelViewName /** modelviewname */ 
            );
            /**Sets  the name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetModelViewName
            (
                const char * modelViewName /** modelviewname */ 
            );
            /**Returns  the criteria list 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObjectList * CriteriaList
            (
            );
            /** All results  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::NXObject *> GetResults
            (
            );
            /** Create search criteria object in search model view builder @return  criteria object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * CreateCriteriaObject
            (
                NXOpen::Annotations::SearchModelViewBuilder::PmiTypes searchType /** search type */
            );
            /** Delete search criteria object in search model view builder
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void DeleteCriteriaObject
            (
                NXOpen::NXObject * criteriaObject /** criteria Object */
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