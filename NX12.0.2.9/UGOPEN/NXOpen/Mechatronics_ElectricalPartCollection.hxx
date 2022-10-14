#ifndef NXOpen_MECHATRONICS_ELECTRICALPARTCOLLECTION_HXX_INCLUDED
#define NXOpen_MECHATRONICS_ELECTRICALPARTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_ElectricalPartCollection.ja
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
#include <NXOpen/Mechatronics_ElectricalPart.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class ElectricalPartCollection;
    }
    namespace Mechatronics
    {
        class MechatronicsManager;
    }
    namespace Mechatronics
    {
        class ElectricalPart;
    }
    namespace Mechatronics
    {
        class ElectricalPartBuilder;
    }
    namespace Mechatronics
    {
        class ElectricalPartCollectionImpl;
        /** Represents a @link NXOpen::Mechatronics::ElectricalPartCollection NXOpen::Mechatronics::ElectricalPartCollection@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::Mechatronics::MechatronicsManager  NXOpen::Mechatronics::MechatronicsManager @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  ElectricalPartCollection : public NXOpen::TaggedObjectCollection
        {
            private: ElectricalPartCollectionImpl * m_electricalpartcollection_impl;
            private: NXOpen::Mechatronics::MechatronicsManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ElectricalPartCollection(NXOpen::Mechatronics::MechatronicsManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ElectricalPartCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Mechatronics::ElectricalPartCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Mechatronics::ElectricalPart *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Mechatronics::ElectricalPartCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOPENCPP_MECHATRONICSEXPORT  value_type operator * ();
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
                NXOPENCPP_MECHATRONICSEXPORT  void next();
                NXOpen::Mechatronics::ElectricalPartCollection *m_context;
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
            /** Create builder for ElectricalPart class  @return @link  NXOpen::Mechatronics::ElectricalPart   NXOpen::Mechatronics::ElectricalPart @endlink  object 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::ElectricalPartBuilder * CreateElectricalPartBuilder
            (
                NXOpen::Mechatronics::ElectricalPart * object /** @link NXOpen::Mechatronics::ElectricalPart NXOpen::Mechatronics::ElectricalPart@endlink  to be edited, if NULL then create a new one */
            );
            /** Finds the @link NXOpen::Mechatronics::ElectricalPart NXOpen::Mechatronics::ElectricalPart@endlink  object with the given name.  @return  @link NXOpen::Mechatronics::ElectricalPart NXOpen::Mechatronics::ElectricalPart@endlink  object with this name. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::ElectricalPart * FindObject
            (
                const NXString & name /** Name of the object, actually it shall be handle. */
            );
            /** Finds the @link NXOpen::Mechatronics::ElectricalPart NXOpen::Mechatronics::ElectricalPart@endlink  object with the given name.  @return  @link NXOpen::Mechatronics::ElectricalPart NXOpen::Mechatronics::ElectricalPart@endlink  object with this name. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            NXOpen::Mechatronics::ElectricalPart * FindObject
            (
                const char * name /** Name of the object, actually it shall be handle. */
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