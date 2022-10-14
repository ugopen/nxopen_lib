#ifndef NXOpen_ANNOTATIONS_SEARCHMODELVIEWCOLLECTION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SEARCHMODELVIEWCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SearchModelViewCollection.ja
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
#include <NXOpen/Annotations_SearchCriteriaDatumFeatureSymbolBuilder.hxx>
#include <NXOpen/Annotations_SearchCriteriaDatumTargetBuilder.hxx>
#include <NXOpen/Annotations_SearchCriteriaDimensionBuilder.hxx>
#include <NXOpen/Annotations_SearchCriteriaFeatureControlFrameBuilder.hxx>
#include <NXOpen/Annotations_SearchCriteriaPMINotesBuilder.hxx>
#include <NXOpen/Annotations_SearchCriteriaSurfaceFinishBuilder.hxx>
#include <NXOpen/Annotations_SearchModelViewBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class SearchModelViewCollection;
    }
    namespace Annotations
    {
        class PmiManager;
    }
    namespace Annotations
    {
        class SearchModelView;
    }
    namespace Annotations
    {
        class SearchCriteriaDatumFeatureSymbolBuilder;
    }
    namespace Annotations
    {
        class SearchCriteriaDatumTargetBuilder;
    }
    namespace Annotations
    {
        class SearchCriteriaDimensionBuilder;
    }
    namespace Annotations
    {
        class SearchCriteriaFeatureControlFrameBuilder;
    }
    namespace Annotations
    {
        class SearchCriteriaPMINotesBuilder;
    }
    namespace Annotations
    {
        class SearchCriteriaSurfaceFinishBuilder;
    }
    namespace Annotations
    {
        class SearchModelViewBuilder;
    }
    class ModelingView;
    class NXObject;
    namespace Annotations
    {
        class SearchModelViewCollectionImpl;
        /** Represents a collection of @link Annotations::SearchModelView Annotations::SearchModelView@endlink  objects.  <br> To obtain an instance of this class, refer to @link Annotations::PmiManager Annotations::PmiManager@endlink  <br> */
        class NXOPENCPPEXPORT  SearchModelViewCollection : public TaggedObjectCollection
        {
            private: SearchModelViewCollectionImpl * m_searchmodelviewcollection_impl;
            private: NXOpen::Annotations::PmiManager* m_owner;
            /** Constructor */
            public: explicit SearchModelViewCollection(NXOpen::Annotations::PmiManager *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~SearchModelViewCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Annotations::SearchModelView * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Annotations::SearchModelViewCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                iterator(const iterator &other): m_context(NULL), m_current(NULL_TAG)
                {
                    copy(other);
                }
                /** Copy constructor */
                iterator &operator =(const iterator &other)
                {
                    if (&other != this)
                        copy(other);
                    return *this;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are equal. */
                bool operator ==(const iterator &other) const
                {
                    return m_current == other.m_current && m_context == other.m_context;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are not equal. */
                bool operator !=(const iterator &other) const
                {
                    return !operator == (other);
                }
                /** Return the element currently pointed to by the iterator. */
                NXOPENCPPEXPORT  value_type operator * ();
                /** Points the iterator to next element. */
                iterator & operator ++()
                {
                    next();
                    return *this;
                }
                /** Points the iterator to next element. */
                iterator operator ++(int)
                {
                    iterator tmp(*this);
                    ++*this;
                    return tmp;
                }
            private:
                void copy(const iterator &other)
                {
                    m_context = other.m_context;
                    m_current = other.m_current;
                    for (int i = 0; i < sizeof(m_state)/sizeof(m_state[0]); i++)
                         m_state[i] = other.m_state[i];
                }
                NXOPENCPPEXPORT  void next();
                NXOpen::Annotations::SearchModelViewCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            /** Returns an iterator addressing the first element. */
            iterator begin();
            /** Returns an iterator addressing one past the last element. */
            iterator end()
            {
                return iterator(this);
            }
            /** Creates the Search PMI builder  @return   <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder * CreateSearchModelViewBuilder
            (
                NXOpen::ModelingView * searchModelView /** search model view*/
            );
            /** Creates a @link Annotations::SearchCriteriaDimensionBuilder Annotations::SearchCriteriaDimensionBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDimensionBuilder * CreateSearchCriteriaDimensionBuilder
            (
                NXOpen::NXObject * searchCriteria /** search criteria */
            );
            /** Creates a @link Annotations::SearchCriteriaFeatureControlFrameBuilder Annotations::SearchCriteriaFeatureControlFrameBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder * CreateSearchCriteriaFeatureControlFrameBuilder
            (
                NXOpen::NXObject * searchCriteria /** search criteria */
            );
            /** Creates a @link Annotations::SearchCriteriaDatumFeatureSymbolBuilder Annotations::SearchCriteriaDatumFeatureSymbolBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDatumFeatureSymbolBuilder * CreateSearchCriteriaDatumFeatureSymbolBuilder
            (
                NXOpen::NXObject * searchCriteria /** search criteria */
            );
            /** Creates a @link Annotations::SearchCriteriaDatumTargetBuilder Annotations::SearchCriteriaDatumTargetBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDatumTargetBuilder * CreateSearchCriteriaDatumTargetBuilder
            (
                NXOpen::NXObject * searchCriteria /** search criteria */
            );
            /** Creates a @link Annotations::SearchCriteriaSurfaceFinishBuilder Annotations::SearchCriteriaSurfaceFinishBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaSurfaceFinishBuilder * CreateSearchCriteriaSurfaceFinishBuilder
            (
                NXOpen::NXObject * searchCriteria /** search criteria */
            );
            /** Creates a @link Annotations::SearchCriteriaPMINotesBuilder Annotations::SearchCriteriaPMINotesBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaPMINotesBuilder * CreateSearchCriteriaPminotesBuilder
            (
                NXOpen::NXObject * searchCriteria /** search criteria */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif