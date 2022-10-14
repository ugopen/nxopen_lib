#ifndef NXOpen_CAE_LAYOUTSTATECOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_LAYOUTSTATECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LayoutStateCollection.ja
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
#include <NXOpen/CAE_LayoutState.hxx>
#include <NXOpen/CAE_LayoutStateApplicator.hxx>
#include <NXOpen/CAE_LayoutStateBuilder.hxx>
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
        class LayoutStateCollection;
    }
    namespace CAE
    {
        class CaePart;
    }
    namespace CAE
    {
        class LayoutState;
    }
    namespace CAE
    {
        class LayoutStateApplicator;
    }
    namespace CAE
    {
        class LayoutStateBuilder;
    }
    namespace CAE
    {
        class LayoutStateCollectionImpl;
        /**  @brief  This class is a collection of @link NXOpen::CAE::LayoutState NXOpen::CAE::LayoutState@endlink .  

           <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaePart  NXOpen::CAE::CaePart @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LayoutStateCollection : public NXOpen::TaggedObjectCollection
        {
            private: LayoutStateCollectionImpl * m_layoutstatecollection_impl;
            private: NXOpen::CAE::CaePart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit LayoutStateCollection(NXOpen::CAE::CaePart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~LayoutStateCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::LayoutStateCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::LayoutState *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::LayoutStateCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::LayoutStateCollection *m_context;
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
            /** Finds a @link NXOpen::CAE::LayoutState NXOpen::CAE::LayoutState@endlink  with the specified name. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::LayoutState * Find
            (
                const NXString & name /** name of the layout state  */
            );
            /** Finds a @link NXOpen::CAE::LayoutState NXOpen::CAE::LayoutState@endlink  with the specified name. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::LayoutState * Find
            (
                const char * name /** name of the layout state  */
            );
            /** Creates a @link NXOpen::CAE::LayoutStateBuilder NXOpen::CAE::LayoutStateBuilder@endlink . This builder is used to create or edit Layout States. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::LayoutStateBuilder * CreateLayoutStateBuilder
            (
                NXOpen::CAE::LayoutState * layoutState /** layoutstate */ 
            );
            /** Deletes the specified @link NXOpen::CAE::LayoutState NXOpen::CAE::LayoutState@endlink  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteLayoutState
            (
                NXOpen::CAE::LayoutState * layoutState /** layoutstate */ 
            );
            /** Clones the specified @link NXOpen::CAE::LayoutState NXOpen::CAE::LayoutState@endlink   @return  resulting layout state  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::LayoutState * CloneLayoutState
            (
                NXOpen::CAE::LayoutState * fromLayoutState /** cloned layout state  */,
                const NXString & newName /** name of the new layout state  */
            );
            /** Clones the specified @link NXOpen::CAE::LayoutState NXOpen::CAE::LayoutState@endlink   @return  resulting layout state  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::LayoutState * CloneLayoutState
            (
                NXOpen::CAE::LayoutState * fromLayoutState /** cloned layout state  */,
                const char * newName /** name of the new layout state  */
            );
            /** Creates an empty @link NXOpen::CAE::LayoutState NXOpen::CAE::LayoutState@endlink   @return  resulting layout state  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::LayoutState * CreateEmptyLayoutState
            (
                const NXString & layoutStateName /** name of the new layout state  */
            );
            /** Creates an empty @link NXOpen::CAE::LayoutState NXOpen::CAE::LayoutState@endlink   @return  resulting layout state  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::LayoutState * CreateEmptyLayoutState
            (
                const char * layoutStateName /** name of the new layout state  */
            );
            /** Creates a @link NXOpen::CAE::LayoutStateApplicator NXOpen::CAE::LayoutStateApplicator@endlink . This builder is used to visualize layout states or exported layout states. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::LayoutStateApplicator * CreateLayoutStateApplicator
            (
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