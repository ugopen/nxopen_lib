#ifndef NXOpen_ASSEMBLIES_ARRANGEMENTCOLLECTION_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_ARRANGEMENTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ArrangementCollection.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Assemblies
    {
        class ArrangementCollection;
    }
    namespace Assemblies
    {
        class ComponentAssembly;
    }
    namespace Assemblies
    {
        class Arrangement;
    }
    namespace Assemblies
    {
        class ArrangementCollectionImpl;
        /** a collection of arrangements  <br> To obtain an instance of this class, refer to @link Assemblies::ComponentAssembly Assemblies::ComponentAssembly@endlink  <br> */
        class NXOPENCPPEXPORT  ArrangementCollection : public TaggedObjectCollection
        {
            private: ArrangementCollectionImpl * m_arrangementcollection_impl;
            private: NXOpen::Assemblies::ComponentAssembly* m_owner;
            /** Constructor */
            public: explicit ArrangementCollection(NXOpen::Assemblies::ComponentAssembly *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ArrangementCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Assemblies::Arrangement * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Assemblies::ArrangementCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Assemblies::ArrangementCollection *m_context;
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
            /** Creates an arrangement, based on an existing arrangement. Note that any @link ComponentAssembly ComponentAssembly@endlink  
                    that contains components will have at least one arrangement. See @link Assemblies::ComponentAssembly::ActiveArrangement Assemblies::ComponentAssembly::ActiveArrangement@endlink .
                  @return  the new arrangement  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: NXOpen::Assemblies::Arrangement * Create
            (
                NXOpen::Assemblies::Arrangement * templateArrangement /** The original arranegment. The new arrangement will be copied from this. */,
                const NXString & name /** The name of the new arrangement  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Finds the @link  Arrangement   Arrangement @endlink  with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.

                An exception will be thrown if no object can be found with the given journal identifier.  @return  Arrangement found, or null if no such arrangement exists. <br> License requirements : None */
            public: NXOpen::Assemblies::Arrangement * FindObject
            (
                const NXString & journalIdentifier /** Name of the arrangement to be found */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
