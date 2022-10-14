#ifndef NXOpen_CAE_OPTIMIZATION_TBSRESTRICTAREACOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_OPTIMIZATION_TBSRESTRICTAREACOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Optimization_TBSRestrictAreaCollection.ja
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
        namespace Optimization
        {
            class TBSRestrictAreaCollection;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            class TBSOptimizationSolution;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            class TBSRestrictArea;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            class TBSRestrictAreaCollectionImpl;
            /** Represents a collection of @link CAE::Optimization::TBSRestrictArea CAE::Optimization::TBSRestrictArea@endlink   <br> To obtain an instance of this class, refer to @link CAE::Optimization::TBSOptimizationSolution  CAE::Optimization::TBSOptimizationSolution @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TBSRestrictAreaCollection : public TaggedObjectCollection
            {
                private: TBSRestrictAreaCollectionImpl * m_tbsrestrictareacollection_impl;
                private: NXOpen::CAE::Optimization::TBSOptimizationSolution* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit TBSRestrictAreaCollection(NXOpen::CAE::Optimization::TBSOptimizationSolution *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~TBSRestrictAreaCollection();
                /** Iterator for accessing the contents of the collection. */
                //lint -sem(NXOpen::CAE::Optimization::TBSRestrictAreaCollection::iterator::copy,initializer)
                class iterator
                {
                public:
                    /** Value type associated with iterator*/ 

                    typedef CAE::Optimization::TBSRestrictArea * value_type;
                    /** Default constructor */
                    iterator() : m_context(NULL), m_current(NULL_TAG)
                    {
                    } //lint !e1401 m_state is not initialized
                    /// \cond NX_NO_DOC
                    explicit iterator(NXOpen::CAE::Optimization::TBSRestrictAreaCollection *context) : m_context(context), m_current(NULL_TAG)
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
                    NXOpen::CAE::Optimization::TBSRestrictAreaCollection *m_context;
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
                /** Finds a restrict area with the specified name within an optimization solution  @return  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: NXOpen::CAE::Optimization::TBSRestrictArea * FindObject
                (
                    const NXString & name /** name */ 
                );
                /** Finds a restrict area with the specified name within an optimization solution  @return  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                NXOpen::CAE::Optimization::TBSRestrictArea * FindObject
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