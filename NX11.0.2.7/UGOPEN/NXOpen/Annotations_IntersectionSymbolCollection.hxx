#ifndef NXOpen_ANNOTATIONS_INTERSECTIONSYMBOLCOLLECTION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_INTERSECTIONSYMBOLCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_IntersectionSymbolCollection.ja
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
#include <iterator>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Annotations_IntersectionSymbolBuilder.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class IntersectionSymbolCollection;
    }
    namespace Annotations
    {
        class AnnotationManager;
    }
    namespace Annotations
    {
        class IntersectionSymbol;
    }
    namespace Annotations
    {
        class IntersectionSymbolBuilder;
    }
    namespace Annotations
    {
        class IntersectionSymbolCollectionImpl;
        /** Represents a collection of @link NXOpen::Annotations::IntersectionSymbol NXOpen::Annotations::IntersectionSymbol@endlink  objects  <br> To obtain an instance of this class, refer to @link NXOpen::Annotations::AnnotationManager  NXOpen::Annotations::AnnotationManager @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  IntersectionSymbolCollection : public NXOpen::TaggedObjectCollection
        {
            private: IntersectionSymbolCollectionImpl * m_intersectionsymbolcollection_impl;
            private: NXOpen::Annotations::AnnotationManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit IntersectionSymbolCollection(NXOpen::Annotations::AnnotationManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~IntersectionSymbolCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Annotations::IntersectionSymbolCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Annotations::IntersectionSymbol *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Annotations::IntersectionSymbolCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                }//lint !e1401 m_state is not initialized
                /// \endcond
                /** Copy constructor */
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
                NXOPENCPP_ANNOTATIONSEXPORT  value_type operator * ();
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
                NXOPENCPP_ANNOTATIONSEXPORT  void next();
                NXOpen::Annotations::IntersectionSymbolCollection *m_context;
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
            /** Creates the IntersectionSymbolBuilder  @return  IntersectionSymbolBuilder object 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Annotations::IntersectionSymbolBuilder * CreateIntersectionSymbolBuilder
            (
                NXOpen::Annotations::IntersectionSymbol * intersectionPt /** @link NXOpen::Annotations::IntersectionSymbol NXOpen::Annotations::IntersectionSymbol@endlink  to be edited, if NULL then create a new one */
            );
            /** Finds the intersection symbol with the given name.  An exception will be 
                    thrown if no object can be found with given name  @return  Intersecton Symbol with this identifier 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::IntersectionSymbol * FindObject
            (
                const NXString & journalIdentifier /** Identifier of the intersection symbol to be found */
            );
            /** Finds the intersection symbol with the given name.  An exception will be 
                    thrown if no object can be found with given name  @return  Intersecton Symbol with this identifier 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Annotations::IntersectionSymbol * FindObject
            (
                const char * journalIdentifier /** Identifier of the intersection symbol to be found */
            );
        }; //lint !e1712 default constructor not defined for class  

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