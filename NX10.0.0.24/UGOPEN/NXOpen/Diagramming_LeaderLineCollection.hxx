#ifndef NXOpen_DIAGRAMMING_LEADERLINECOLLECTION_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_LEADERLINECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_LeaderLineCollection.ja
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
#include <NXOpen/Diagramming_LeaderLine.hxx>
#include <NXOpen/Diagramming_LeaderLineBuilder.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_diagramming_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Diagramming
    {
        class LeaderLineCollection;
    }
    namespace Diagramming
    {
        class DiagrammingManager;
    }
    namespace Diagramming
    {
        class LeaderLine;
    }
    namespace Diagramming
    {
        class LeaderLineBuilder;
    }
    namespace Diagramming
    {
        class LeaderLineCollectionImpl;

        /// \cond NX_NO_DOC 
        /** Represents a collection of leader line.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  LeaderLineCollection : public NXOpen::TaggedObjectCollection
        {
            private: LeaderLineCollectionImpl * m_leaderlinecollection_impl;
            private: NXOpen::Diagramming::DiagrammingManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit LeaderLineCollection(NXOpen::Diagramming::DiagrammingManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~LeaderLineCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Diagramming::LeaderLineCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Diagramming::LeaderLine *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Diagramming::LeaderLineCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOPENCPP_DIAGRAMMINGEXPORT  value_type operator * ();
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
                NXOPENCPP_DIAGRAMMINGEXPORT  void next();
                NXOpen::Diagramming::LeaderLineCollection *m_context;
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
            /** Creates a @link NXOpen::Diagramming::LeaderLineBuilder NXOpen::Diagramming::LeaderLineBuilder@endlink .  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::LeaderLineBuilder * CreateLeaderLineBuilder
            (
                NXOpen::Diagramming::LeaderLine * leaderLine /** @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  to be edited, if NULL then create a new one */
            );
            /** Finds the @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name.  @return  @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  with this name. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::LeaderLine * FindObject
            (
                const NXString & journalIdentifier /** Identifier to be found */
            );
            /** Finds the @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name.  @return  @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  with this name. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Diagramming::LeaderLine * FindObject
            (
                const char * journalIdentifier /** Identifier to be found */
            );
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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