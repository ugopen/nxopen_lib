#ifndef NXOpen_DISPLAY_DECALCOLLECTION_HXX_INCLUDED
#define NXOpen_DISPLAY_DECALCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_DecalCollection.ja
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
#include <NXOpen/Display_DecalBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class DecalCollection;
    }
    class BasePart;
    class Decal;
    namespace Display
    {
        class DecalBuilder;
    }
    class TaggedObject;
    namespace Display
    {
        class DecalCollectionImpl;
        /**
        Represents a collection decal material texture 
         <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
        class NXOPENCPPEXPORT  DecalCollection : public TaggedObjectCollection
        {
            private: DecalCollectionImpl * m_decalcollection_impl;
            private: NXOpen::BasePart* m_owner;
            /** Constructor */
            public: explicit DecalCollection(NXOpen::BasePart *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~DecalCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Decal * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Display::DecalCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Display::DecalCollection *m_context;
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
            /** Creates a @link Display::DecalBuilder Display::DecalBuilder@endlink  object if decal is NULL.  Otherwise, a Decal object will be edited  @return  return decal builder  <br> License requirements : None */
            public: NXOpen::Display::DecalBuilder * CreateDecalBuilder
            (
                NXOpen::TaggedObject * decal /** If decal is not NULL, then this object will be edited */
            );
            /** Creates a @link Display::DecalBuilder Display::DecalBuilder@endlink  object with image referenced object if decal is NULL.  Otherwise, a Decal object will be edited  @return  return decal builder  <br> License requirements : None */
            public: NXOpen::Display::DecalBuilder * CreateDecalBuilderFull
            (
                NXOpen::TaggedObject * decal /** If decal is not NULL, then this object will be edited */
            );
            /** Finds the @link  Decal   Decal @endlink  with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.

                An exception will be thrown if no object can be found with the given journal identifier.  @return  Decal found  <br> License requirements : None */
            public: NXOpen::Decal * FindDecalObject
            (
                const NXString & journalIdentifier /** Identifier to be found */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
