#ifndef NXOpen_DISPLAY_CGFXMATTEXCOLLECTION_HXX_INCLUDED
#define NXOpen_DISPLAY_CGFXMATTEXCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_CgfxMattexCollection.ja
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
#include <NXOpen/Display_CgfxMattexBuilder.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_display_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Display
    {
        class CgfxMattexCollection;
    }
    class BasePart;
    namespace Display
    {
        class CgfxMattex;
    }
    namespace Display
    {
        class CgfxMattexBuilder;
    }
    class TaggedObject;
    namespace Display
    {
        class CgfxMattexCollectionImpl;
        /**
        Represents a collection @link NXOpen::Display::CgfxMattex NXOpen::Display::CgfxMattex@endlink  objects 
         <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
         <br>  @deprecated Deprecated in NX10.0.0.  No alternative provided for this class. <br>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NX_DEPRECATED("Deprecated in NX10.0.0.  No alternative provided for this class.") NXOPENCPP_DISPLAYEXPORT  CgfxMattexCollection : public NXOpen::TaggedObjectCollection
        {
            private: CgfxMattexCollectionImpl * m_cgfxmattexcollection_impl;
            private: NXOpen::BasePart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CgfxMattexCollection(NXOpen::BasePart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CgfxMattexCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Display::CgfxMattexCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Display::CgfxMattex *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Display::CgfxMattexCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                }//lint !e1401 m_state is not initialized
                /// \endcond
                /** Copy constructor */
                iterator(const iterator &other): m_context(nullptr), m_current(NULL_TAG)
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
                NXOPENCPP_DISPLAYEXPORT  value_type operator * () const;
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
                NXOPENCPP_DISPLAYEXPORT  void next();
                NXOpen::Display::CgfxMattexCollection *m_context;
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
            /** Creates a @link NXOpen::Display::CgfxMattexBuilder NXOpen::Display::CgfxMattexBuilder@endlink  
                     <br> This class is restricted to being called from a program running during an 
                    Interactive NX session.  If run from a non-interactive session it will 
                    return NULL. <br> 
                    
             <br>  @deprecated Deprecated in NX10.0.0.  No alternative provided for this class. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  No alternative provided for this class.") NXOpen::Display::CgfxMattexBuilder * CreateCgfxMattexBuilder
            (
                NXOpen::TaggedObject * cgfxmattex /** If cgfxmattex is not NULL, then this object will be edited*/
            );
            /** Finds the @link  NXOpen::Display::CgfxMattex   NXOpen::Display::CgfxMattex @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.

                    An exception will be thrown if no object can be found with the given journal identifier.  @return  CgfxMattex object found 
             <br>  @deprecated Deprecated in NX10.0.0.  No alternative provided for this class. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  No alternative provided for this class.") NXOpen::TaggedObject * Find
            (
                const NXString & journalIdentifier /** Identifier to be found */
            );
            /** Finds the @link  NXOpen::Display::CgfxMattex   NXOpen::Display::CgfxMattex @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.

                    An exception will be thrown if no object can be found with the given journal identifier.  @return  CgfxMattex object found 
             <br>  @deprecated Deprecated in NX10.0.0.  No alternative provided for this class. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::TaggedObject * Find
            (
                const char * journalIdentifier /** Identifier to be found */
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
