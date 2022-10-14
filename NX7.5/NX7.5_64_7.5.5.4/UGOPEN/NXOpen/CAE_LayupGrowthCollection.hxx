#ifndef NXOpen_CAE_LAYUPGROWTHCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_LAYUPGROWTHCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LayupGrowthCollection.ja
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
    namespace CAE
    {
        class LayupGrowthCollection;
    }
    namespace CAE
    {
        class LaminateGlobalLayupMgr;
    }
    namespace CAE
    {
        class LayupGrowth;
    }
    namespace CAE
    {
        class LayupGrowthCollectionImpl;
        /** Represents a collection of layup growth rules  <br> To obtain an instance of this class, refer to @link CAE::LaminateGlobalLayupMgr CAE::LaminateGlobalLayupMgr@endlink  <br> 
         @deprecated Deprecated in NX7.5.0 <br> 
        */
        class NXOPENCPPEXPORT  NX_DEPRECATED("Deprecated in NX7.5.0")  LayupGrowthCollection : public TaggedObjectCollection
        {
            private: LayupGrowthCollectionImpl * m_layupgrowthcollection_impl;
            private: NXOpen::CAE::LaminateGlobalLayupMgr* m_owner;
            /** Constructor */
            public: explicit LayupGrowthCollection(NXOpen::CAE::LaminateGlobalLayupMgr *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~LayupGrowthCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef CAE::LayupGrowth * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::CAE::LayupGrowthCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::LayupGrowthCollection *m_context;
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
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif