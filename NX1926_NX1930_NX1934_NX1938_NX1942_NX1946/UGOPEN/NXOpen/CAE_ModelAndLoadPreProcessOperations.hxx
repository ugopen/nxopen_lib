#ifndef NXOpen_CAE_MODELANDLOADPREPROCESSOPERATIONS_HXX_INCLUDED
#define NXOpen_CAE_MODELANDLOADPREPROCESSOPERATIONS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelAndLoadPreProcessOperations.ja
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
#include <NXOpen/CAE_ModelAndLoadPreProcessOperation.hxx>
#include <NXOpen/CAE_ModelAndLoadPreProcessOperationBuilder.hxx>
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
        class ModelAndLoadPreProcessOperations;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcess;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcessOperation;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcessOperationBuilder;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcessOperationsImpl;
        /** Represents a collection of MLPP events.  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::ModelAndLoadPreProcess  NXOpen::CAE::ModelAndLoadPreProcess @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ModelAndLoadPreProcessOperations : public NXOpen::TaggedObjectCollection
        {
            private: ModelAndLoadPreProcessOperationsImpl * m_modelandloadpreprocessoperations_impl;
            private: NXOpen::CAE::ModelAndLoadPreProcess* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ModelAndLoadPreProcessOperations(NXOpen::CAE::ModelAndLoadPreProcess *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ModelAndLoadPreProcessOperations();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::ModelAndLoadPreProcessOperations::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::ModelAndLoadPreProcessOperation *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::ModelAndLoadPreProcessOperations *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::ModelAndLoadPreProcessOperations *m_context;
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
            /** Finds a block with a specified name.  @return  The mlpp operation 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ModelAndLoadPreProcessOperation * FindObject
            (
                const NXString & name /** name of the block  */
            );
            /** Finds a block with a specified name.  @return  The mlpp operation 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::ModelAndLoadPreProcessOperation * FindObject
            (
                const char * name /** name of the block  */
            );
            /** Delete a durability event. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteOperation
            (
                NXOpen::CAE::ModelAndLoadPreProcessOperation * blockTag /** The mlpp operation to be deleted */
            );
            /** Creates the builder object of the MLPP Block.  @return   
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ModelAndLoadPreProcessOperationBuilder * CreateBuilder
            (
                const NXString & operationTypeString /** operationtypestring */ 
            );
            /** Creates the builder object of the MLPP Block.  @return   
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::ModelAndLoadPreProcessOperationBuilder * CreateBuilder
            (
                const char * operationTypeString /** operationtypestring */ 
            );
            /** Creates the builder object of the MLPP Block.  @return   
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ModelAndLoadPreProcessOperationBuilder * EditBuilder
            (
                NXOpen::CAE::ModelAndLoadPreProcessOperation * baseOp /** baseop */ 
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