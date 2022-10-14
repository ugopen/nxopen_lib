#ifndef NXOpen_CAE_ACOUSTICSANDVIBRATIONPOTENTIALFLOWSOLUTIONCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_ACOUSTICSANDVIBRATIONPOTENTIALFLOWSOLUTIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AcousticsAndVibrationPotentialFlowSolutionCollection.ja
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
#include <NXOpen/CAE_AcousticsAndVibrationPotentialFlowSolution.hxx>
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
        class AcousticsAndVibrationPotentialFlowSolutionCollection;
    }
    namespace CAE
    {
        class AcousticsAndVibrationManager;
    }
    namespace CAE
    {
        class AcousticsAndVibrationPotentialFlowSolution;
    }
    namespace CAE
    {
        class AcousticsAndVibrationPotentialFlowSolutionBuilder;
    }
    namespace CAE
    {
        class AcousticsAndVibrationPotentialFlowSolutionCollectionImpl;
        /** Represents a collection of CAE_AcousticsAndVibration PotentialFlowSolutions.  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::AcousticsAndVibrationManager  NXOpen::CAE::AcousticsAndVibrationManager @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AcousticsAndVibrationPotentialFlowSolutionCollection : public NXOpen::TaggedObjectCollection
        {
            private: AcousticsAndVibrationPotentialFlowSolutionCollectionImpl * m_acousticsandvibrationpotentialflowsolutioncollection_impl;
            private: NXOpen::CAE::AcousticsAndVibrationManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit AcousticsAndVibrationPotentialFlowSolutionCollection(NXOpen::CAE::AcousticsAndVibrationManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~AcousticsAndVibrationPotentialFlowSolutionCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolutionCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolution *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolutionCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolutionCollection *m_context;
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
            /** Finds a Potential Flow solution with a specified name.  @return  The solution 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolution * FindObject
            (
                const NXString & name /** name of the solution  */
            );
            /** Finds a Potential Flow solution with a specified name.  @return  The solution 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolution * FindObject
            (
                const char * name /** name of the solution  */
            );
            /** Creates a Potential Flow solution. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolution * Create
            (
            );
            /** Delete a Potential Flow solution. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Delete
            (
                NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolution * solution /** solution */ 
            );
            /** Clone a Potential Flow solution. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolution * CloneSolution
            (
                NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolution * solution /** solution */ 
            );
            /** Creates the builder for a Potential Flow solution. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolutionBuilder * CreateBuilder
            (
                NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolution * solution /** solution */ 
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