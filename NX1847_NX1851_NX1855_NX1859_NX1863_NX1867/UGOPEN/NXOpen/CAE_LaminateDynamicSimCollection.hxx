#ifndef NXOpen_CAE_LAMINATEDYNAMICSIMCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEDYNAMICSIMCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateDynamicSimCollection.ja
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
        class LaminateDynamicSimCollection;
    }
    namespace CAE
    {
        class LaminateManager;
    }
    namespace CAE
    {
        class LaminateDynamicSim;
    }
    namespace CAE
    {
        class LaminateDampingFactorBuilder;
    }
    namespace CAE
    {
        class LaminateDynamicSimBuilder;
    }
    class TaggedObject;
    namespace CAE
    {
        class LaminateDynamicSimCollectionImpl;
        /** Represents a collection of laminate dynamic sims  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::LaminateManager  NXOpen::CAE::LaminateManager @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LaminateDynamicSimCollection : public NXOpen::TaggedObjectCollection
        {
            private: LaminateDynamicSimCollectionImpl * m_laminatedynamicsimcollection_impl;
            private: NXOpen::CAE::LaminateManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit LaminateDynamicSimCollection(NXOpen::CAE::LaminateManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~LaminateDynamicSimCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::LaminateDynamicSimCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::LaminateDynamicSim *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::LaminateDynamicSimCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::LaminateDynamicSimCollection *m_context;
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
            /** Finds a laminate dynamic sim with the specified name  @return  Laminate Dynamic Sim found 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateDynamicSim * FindObject
            (
                const NXString & name /** Laminate Dynamic Sim name to be found */
            );
            /** Finds a laminate dynamic sim with the specified name  @return  Laminate Dynamic Sim found 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            NXOpen::CAE::LaminateDynamicSim * FindObject
            (
                const char * name /** Laminate Dynamic Sim name to be found */
            );
            /**Returns  the active laminate dynamic sim 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateDynamicSim * Active
            (
            );
            /**Sets  the active laminate dynamic sim 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetActive
            (
                NXOpen::CAE::LaminateDynamicSim * dynamicSim /** Laminate dynamic sim to be set active */
            );
            /** Deletes the laminate dynamic sim 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void Delete
            (
                NXOpen::CAE::LaminateDynamicSim * dynamicSim /** Laminate dynamic sim to be deleted */
            );
            /** Clones the laminate dynamic sim 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void CloneDynamicSim
            (
                NXOpen::CAE::LaminateDynamicSim * dynamicSim /** Laminate dynamic sim to be cloned */
            );
            /** Creates a builder for the laminate dynamic sim.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateDynamicSimBuilder * CreateDynamicSimBuilder
            (
                NXOpen::CAE::LaminateDynamicSim * laminateDynamicSimTag /** The metasolution.*/
            );
            /** Creates a builder for the laminate damping factor.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateDampingFactorBuilder * CreateDampingFactorBuilder
            (
                NXOpen::TaggedObject * contextObjectTag /** The metasolution or the mode property.*/
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