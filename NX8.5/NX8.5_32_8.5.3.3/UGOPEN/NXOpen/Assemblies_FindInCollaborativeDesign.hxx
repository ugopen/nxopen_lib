#ifndef NXOpen_ASSEMBLIES_FINDINCOLLABORATIVEDESIGN_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_FINDINCOLLABORATIVEDESIGN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_FindInCollaborativeDesign.ja
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
#include <NXOpen/Assemblies_FindInCollaborativeDesign.hxx>
#include <NXOpen/Assemblies_Partition.hxx>
#include <NXOpen/Assemblies_SearchResultElement.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_assemblies_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Assemblies
    {
        class FindInCollaborativeDesign;
    }
    namespace Assemblies
    {
        class Partition;
    }
    namespace Assemblies
    {
        class SearchResultElement;
    }
    class NXObject;
    namespace Assemblies
    {
        class _FindInCollaborativeDesignBuilder;
        class FindInCollaborativeDesignImpl;
        /**
                FindInCollaborativeDesign is a searcher for performing simple searches in the context of a subset.
             <br> To get an instance of this object use @link Assemblies::SubsetBuilder Assemblies::SubsetBuilder@endlink   <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  FindInCollaborativeDesign : public NXObject
        {
            /** The type of object for which the search is performed.
                    */
            public: enum ObjectType
            {
                ObjectTypePartition/** Search for partitions */,
                ObjectTypeDesignElement/** Search for Design Elements */
            };

            /** The attribute against which the search text is matched.
                    */
            public: enum SearchType
            {
                SearchTypeItemQuery/** Match text with item name or id */
            };

            private: FindInCollaborativeDesignImpl * m_findincollaborativedesign_impl;
            private: friend class  _FindInCollaborativeDesignBuilder;
            protected: FindInCollaborativeDesign();
            public: ~FindInCollaborativeDesign();
            /** Generate the search results according to the search text.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void PerformFind
            (
                NXOpen::Assemblies::FindInCollaborativeDesign::ObjectType objectType /** objecttype */ ,
                NXOpen::Assemblies::FindInCollaborativeDesign::SearchType searchType /** searchtype */ ,
                const NXString & searchText /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Generate the search results according to the search text.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            void PerformFind
            (
                NXOpen::Assemblies::FindInCollaborativeDesign::ObjectType objectType /** objecttype */ ,
                NXOpen::Assemblies::FindInCollaborativeDesign::SearchType searchType /** searchtype */ ,
                const char * searchText /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Generate the search results according to the search text, searching only
                        within the partition.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void PerformFind
            (
                NXOpen::Assemblies::Partition * partition /** partition */ ,
                NXOpen::Assemblies::FindInCollaborativeDesign::ObjectType objectType /** objecttype */ ,
                NXOpen::Assemblies::FindInCollaborativeDesign::SearchType searchType /** searchtype */ ,
                const NXString & searchText /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Generate the search results according to the search text, searching only
                        within the partition.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            void PerformFind
            (
                NXOpen::Assemblies::Partition * partition /** partition */ ,
                NXOpen::Assemblies::FindInCollaborativeDesign::ObjectType objectType /** objecttype */ ,
                NXOpen::Assemblies::FindInCollaborativeDesign::SearchType searchType /** searchtype */ ,
                const char * searchText /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Retrieve the @link Partition Partition@endlink s found in the last search.
                     @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: std::vector<NXOpen::Assemblies::Partition *> GetPartitions
            (
            );
            /** Retrieve the @link SearchResultElement SearchResultElement@endlink s found in the last search.
                     @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: std::vector<NXOpen::Assemblies::SearchResultElement *> GetSearchResultElements
            (
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
