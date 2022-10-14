#ifndef NXOpen_CAE_AEROSTRUCTURES_LOADCASESETCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_AEROSTRUCTURES_LOADCASESETCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroStructures_LoadCaseSetCollection.ja
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
#include <NXOpen/CAE_AeroStructures_BaseSolution.hxx>
#include <NXOpen/CAE_AeroStructures_LoadCaseSet.hxx>
#include <NXOpen/CAE_AeroStructures_LoadCaseSetBuilder.hxx>
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
        namespace AeroStructures
        {
            class LoadCaseSetCollection;
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class BaseSolution;
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class LoadCaseSet;
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class LoadCaseSetBuilder;
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class LoadCaseSetCollectionImpl;
            /** Represents a collection of AeroStruct LoadCases  <br> Use @link CAE::AeroStructures::BaseSolution::LoadCaseSetCollection CAE::AeroStructures::BaseSolution::LoadCaseSetCollection@endlink  to get the instance of this class.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  LoadCaseSetCollection : public NXOpen::TaggedObjectCollection
            {
                private: LoadCaseSetCollectionImpl * m_loadcasesetcollection_impl;
                private: NXOpen::CAE::AeroStructures::BaseSolution* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit LoadCaseSetCollection(NXOpen::CAE::AeroStructures::BaseSolution *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~LoadCaseSetCollection();
                /** Iterator for accessing the contents of the collection. */
                //lint -sem(NXOpen::CAE::AeroStructures::LoadCaseSetCollection::iterator::copy,initializer)
                class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::AeroStructures::LoadCaseSet *>
                {
                public:
                    /** Default constructor */
                    iterator() : m_context(nullptr), m_current(NULL_TAG)
                    {
                        // coverity[uninit_member]
                    } //lint !e1401 m_state is not initialized
                    /// \cond NX_NO_DOC
                    explicit iterator(NXOpen::CAE::AeroStructures::LoadCaseSetCollection *context) : m_context(context), m_current(NULL_TAG)
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
                    NXOPENCPP_CAEEXPORT  value_type operator * () const;
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
                    NXOpen::CAE::AeroStructures::LoadCaseSetCollection *m_context;
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
                /** Finds the @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  object with the given name.  @return  @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  object with this name. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXOpen::CAE::AeroStructures::LoadCaseSet * FindObject
                (
                    const NXString & name /** LoadCaseSet Name  */
                );
                /** Finds the @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  object with the given name.  @return  @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  object with this name. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                NXOpen::CAE::AeroStructures::LoadCaseSet * FindObject
                (
                    const char * name /** LoadCaseSet Name  */
                );
                /** Creates a @link NXOpen::CAE::AeroStructures::LoadCaseSetBuilder NXOpen::CAE::AeroStructures::LoadCaseSetBuilder@endlink   @return  Builder object
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXOpen::CAE::AeroStructures::LoadCaseSetBuilder * CreateLoadCaseSetBuilder
                (
                    NXOpen::CAE::AeroStructures::LoadCaseSet * loadcaeset /** @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  to be edited */
                );
                /** Delete a AeroStruct loadcase set. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void DeleteLoadCaseSet
                (
                    NXOpen::CAE::AeroStructures::LoadCaseSet * loadcaseset /** @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  */
                );
                /** Create a AeroStruct loadcase set. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void CreateLoadCaseSet
                (
                    NXOpen::CAE::AeroStructures::LoadCaseSetBuilder * builder /** @link NXOpen::CAE::AeroStructures::LoadCaseSetBuilder NXOpen::CAE::AeroStructures::LoadCaseSetBuilder@endlink  */
                );
                /** Create a AeroStruct loadcase set. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void CloneLoadCaseSet
                (
                    NXOpen::CAE::AeroStructures::LoadCaseSet * loadcaseset /** @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  */
                );
                /** Import Load Case Set from file  @return  @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXOpen::CAE::AeroStructures::LoadCaseSet * ImportLoadCaseSetFromFile
                (
                    const NXString & fileName /** filename */ ,
                    NXString* errorMsg /** errormsg */ ,
                    std::vector<NXString> & warningMsg /** warningmsg */ 
                );
                /** Import Load Case Set from file  @return  @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                NXOpen::CAE::AeroStructures::LoadCaseSet * ImportLoadCaseSetFromFile
                (
                    const char * fileName /** filename */ ,
                    NXString* errorMsg /** errormsg */ ,
                    std::vector<NXString> & warningMsg /** warningmsg */ 
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