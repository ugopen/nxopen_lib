#ifndef NXOpen_ANNOTATIONS_FRAMEBARCOLLECTION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_FRAMEBARCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_FrameBarCollection.ja
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
#include <NXOpen/Annotations_AddTicBuilder.hxx>
#include <NXOpen/Annotations_FrameBarBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
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
        class FrameBarCollection;
    }
    namespace Annotations
    {
        class AnnotationManager;
    }
    namespace Annotations
    {
        class FrameBar;
    }
    namespace Annotations
    {
        class AddTicBuilder;
    }
    namespace Annotations
    {
        class FrameBarBuilder;
    }
    namespace Annotations
    {
        class FrameBarCollectionImpl;
        /** Represents a collection of @link Annotations::FrameBar Annotations::FrameBar@endlink  objects  <br> To obtain an instance of this class, refer to @link Annotations::AnnotationManager  Annotations::AnnotationManager @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  FrameBarCollection : public TaggedObjectCollection
        {
            private: FrameBarCollectionImpl * m_framebarcollection_impl;
            private: NXOpen::Annotations::AnnotationManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit FrameBarCollection(NXOpen::Annotations::AnnotationManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~FrameBarCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Annotations::FrameBarCollection::iterator::copy,initializer)
            class iterator
            {
            public:
                /** Value type associated with iterator*/ 

                typedef Annotations::FrameBar * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                { // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Annotations::FrameBarCollection *context) : m_context(context), m_current(NULL_TAG)
                { // coverity[uninit_member]
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
                NXOpen::Annotations::FrameBarCollection *m_context;
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
            /** If NULL create a new Frame bar, otherwise edit existing Frame bar Annotatation @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_ship_drafting ("Ship Drafting") */
            public: NXOpen::Annotations::FrameBarBuilder * CreateFrameBarBuilder
            (
                NXOpen::Annotations::FrameBar * framebar /** frame bar*/
            );
            /** Creates a @link Annotations::AddTicBuilder Annotations::AddTicBuilder@endlink   @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_ship_drafting ("Ship Drafting") */
            public: NXOpen::Annotations::AddTicBuilder * CreateAddTicBuilder
            (
                NXOpen::Annotations::FrameBar * framebar /** frame bar*/
            );
            /** Finds the frame bar with the given name.  An exception will be 
                    thrown if no object can be found with given name  @return  frame bar with this identifier 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::FrameBar * FindObject
            (
                const NXString & journalIdentifier /** Identifier of the frame bar to be found */
            );
            /** Finds the frame bar with the given name.  An exception will be 
                    thrown if no object can be found with given name  @return  frame bar with this identifier 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Annotations::FrameBar * FindObject
            (
                const char * journalIdentifier /** Identifier of the frame bar to be found */
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
