#ifndef NXOpen_CAE_RESPONSESIMULATION_STRAINGAGECOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_STRAINGAGECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_StrainGageCollection.ja
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
#include <NXOpen/CAE_ResponseSimulation_StrainGage.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        namespace ResponseSimulation
        {
            class StrainGageCollection;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class Manager;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class StrainGage;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class StrainGageBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class StrainGageCollectionImpl;
            /** Represents a collection of response analysis strain gage  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::ResponseSimulation::Manager  NXOpen::CAE::ResponseSimulation::Manager @endlink  <br> 
             <br>  Created in NX6.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  StrainGageCollection : public NXOpen::TaggedObjectCollection
            {
                private: StrainGageCollectionImpl * m_straingagecollection_impl;
                private: NXOpen::CAE::ResponseSimulation::Manager* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit StrainGageCollection(NXOpen::CAE::ResponseSimulation::Manager *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~StrainGageCollection();
                /** Iterator for accessing the contents of the collection. */
                //lint -sem(NXOpen::CAE::ResponseSimulation::StrainGageCollection::iterator::copy,initializer)
                class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::ResponseSimulation::StrainGage *>
                {
                public:
                    /** Default constructor */
                    iterator() : m_context(NULL), m_current(NULL_TAG)
                    {
                        // coverity[uninit_member]
                    } //lint !e1401 m_state is not initialized
                    /// \cond NX_NO_DOC
                    explicit iterator(NXOpen::CAE::ResponseSimulation::StrainGageCollection *context) : m_context(context), m_current(NULL_TAG)
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
                    NXOpen::CAE::ResponseSimulation::StrainGageCollection *m_context;
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
                /** Creates a strain gage buider  @return   
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrainGageBuilder * CreateStrainGageBuilder
                (
                    NXOpen::CAE::ResponseSimulation::StrainGage * strainGage /** strain gage */ 
                );
                /** Finds an strain gage with specified gage name  @return   
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrainGage * FindObject
                (
                    const NXString & name /** name */ 
                );
                /** Finds an strain gage with specified gage name  @return   
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                NXOpen::CAE::ResponseSimulation::StrainGage * FindObject
                (
                    const char * name /** name */ 
                );
            }; //lint !e1712 default constructor not defined for class  

        }
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