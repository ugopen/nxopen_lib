#ifndef NXOpen_CAE_DURABILITYEVENTCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_DURABILITYEVENTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurabilityEventCollection.ja
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
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class DurabilityEventCollection;
    }
    namespace CAE
    {
        class DurabilityMetaSolution;
    }
    namespace CAE
    {
        class DurabilityEvent;
    }
    namespace CAE
    {
        class DurabilityRandomEvent;
    }
    namespace CAE
    {
        class DurabilityRandomEventBuilder;
    }
    namespace CAE
    {
        class DurabilityStaticEvent;
    }
    namespace CAE
    {
        class DurabilityStaticEventBuilder;
    }
    namespace CAE
    {
        class DurabilityTransientEvent;
    }
    namespace CAE
    {
        class DurabilityTransientEventBuilder;
    }
    namespace CAE
    {
        class DurabilityEventCollectionImpl;
        /** Represents a collection of durability events.  <br> To obtain an instance of this class, refer to @link CAE::DurabilityMetaSolution  CAE::DurabilityMetaSolution @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurabilityEventCollection : public TaggedObjectCollection
        {
            private: DurabilityEventCollectionImpl * m_durabilityeventcollection_impl;
            private: NXOpen::CAE::DurabilityMetaSolution* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit DurabilityEventCollection(NXOpen::CAE::DurabilityMetaSolution *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~DurabilityEventCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::DurabilityEventCollection::iterator::copy,initializer)
            class iterator
            {
            public:
                /** Value type associated with iterator*/ 

                typedef CAE::DurabilityEvent * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::DurabilityEventCollection *context) : m_context(context), m_current(NULL_TAG)
                {
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
                NXOPENCPP_CAEEXPORT  value_type operator * ();
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
                NXOPENCPP_CAEEXPORT  void next();
                NXOpen::CAE::DurabilityEventCollection *m_context;
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
            /** Finds a durability event with a specified name.  @return  The durability event 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilityEvent * FindObject
            (
                const NXString & name /** name of the durability event  */
            );
            /** Finds a durability event with a specified name.  @return  The durability event 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            NXOpen::CAE::DurabilityEvent * FindObject
            (
                const char * name /** name of the durability event  */
            );
            /** Delete a durability event. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void DeleteEvent
            (
                NXOpen::CAE::DurabilityEvent * eventTag /** The durability event to be deleted */
            );
            /** Makes a clone of a durability event.  @return  Cloned event 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilityEvent * CloneEvent
            (
                NXOpen::CAE::DurabilityEvent * source /** Source event */
            );
            /** Creates the builder object of the durability static event.  @return   
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilityStaticEventBuilder * CreateStaticEventBuilder
            (
                NXOpen::CAE::DurabilityStaticEvent * eventTag /** eventtag */ 
            );
            /** Creates the builder object of the durability random event.  @return   
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilityRandomEventBuilder * CreateRandomEventBuilder
            (
                NXOpen::CAE::DurabilityRandomEvent * eventTag /** eventtag */ 
            );
            /** Creates the builder object of the durability transient event.  @return   
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilityTransientEventBuilder * CreateTransientEventBuilder
            (
                NXOpen::CAE::DurabilityTransientEvent * eventTag /** eventtag */ 
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
