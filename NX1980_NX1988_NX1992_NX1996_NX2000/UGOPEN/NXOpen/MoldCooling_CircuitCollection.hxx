#ifndef NXOpen_MOLDCOOLING_CIRCUITCOLLECTION_HXX_INCLUDED
#define NXOpen_MOLDCOOLING_CIRCUITCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MoldCooling_CircuitCollection.ja
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
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_moldcooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MoldCooling
    {
        class CircuitCollection;
    }
    namespace MoldCooling
    {
        class Manager;
    }
    namespace MoldCooling
    {
        class Circuit;
    }
    class Part;
    namespace MoldCooling
    {
        class CircuitCollectionImpl;
        /**  @brief  Represents collection @link MoldCooling::Circuit MoldCooling::Circuit@endlink .  

          <br> To obtain an instance of this class, refer to @link NXOpen::MoldCooling::Manager  NXOpen::MoldCooling::Manager @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_MOLDCOOLINGEXPORT  CircuitCollection : public NXOpen::TaggedObjectCollection
        {
            private: CircuitCollectionImpl * m_circuitcollection_impl;
            private: NXOpen::MoldCooling::Manager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CircuitCollection(NXOpen::MoldCooling::Manager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CircuitCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::MoldCooling::CircuitCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::MoldCooling::Circuit *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::MoldCooling::CircuitCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOPENCPP_MOLDCOOLINGEXPORT  value_type operator * () const;
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
                NXOPENCPP_MOLDCOOLINGEXPORT  void next();
                NXOpen::MoldCooling::CircuitCollection *m_context;
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
            /** Finds a cooling circuit with the specified name 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_mold_cool_basic (" NX Mold Cooling Application") */
            public: NXOpen::MoldCooling::Circuit * FindObject
            (
                NXOpen::Part * part /** part */ ,
                const NXString & name /** Name of the circuit being looked for. */
            );
            /** Finds a cooling circuit with the specified name 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_mold_cool_basic (" NX Mold Cooling Application") */
            NXOpen::MoldCooling::Circuit * FindObject
            (
                NXOpen::Part * part /** part */ ,
                const char * name /** Name of the circuit being looked for. */
            );
            /** Returns the list of cooling circuits 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_mold_cool_basic (" NX Mold Cooling Application") */
            public: void GetCircuits
            (
                NXOpen::Part * part /** part */ ,
                std::vector<NXOpen::MoldCooling::Circuit *> & circuits /** circuits */ 
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