#ifndef NXOpen_CAE_MODELUPDATESOLUTIONCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_MODELUPDATESOLUTIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelUpdateSolutionCollection.ja
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
        class ModelUpdateSolutionCollection;
    }
    namespace CAE
    {
        class CorrelManager;
    }
    namespace CAE
    {
        class ModelUpdateSolution;
    }
    namespace CAE
    {
        class ModelUpdateSensitivityViewerBuilder;
    }
    namespace CAE
    {
        class ModelUpdateSolutionBuilder;
    }
    namespace CAE
    {
        class ModelUpdateSolutionCollectionImpl;
        /** Represents a collection of model update meta solution  <br> To obtain an instance of this class, refer to @link CAE::CorrelManager  CAE::CorrelManager @endlink  <br> */
        class NXOPENCPP_CAEEXPORT  ModelUpdateSolutionCollection : public TaggedObjectCollection
        {
            private: ModelUpdateSolutionCollectionImpl * m_modelupdatesolutioncollection_impl;
            private: NXOpen::CAE::CorrelManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ModelUpdateSolutionCollection(NXOpen::CAE::CorrelManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ModelUpdateSolutionCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::ModelUpdateSolutionCollection::iterator::copy,initializer)
            class iterator
            {
            public:
                /** Value type associated with iterator*/ 

                typedef CAE::ModelUpdateSolution * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::ModelUpdateSolutionCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::ModelUpdateSolutionCollection *m_context;
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
            /** Creates the builder object of model update meta solution  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ModelUpdateSolutionBuilder * CreateSolutionBuilder
            (
                NXOpen::CAE::ModelUpdateSolution * solution /** Model update solution being edit*/
            );
            /** Finds a model update meta solution with specified solution name  @return  Model Update meta solution found 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ModelUpdateSolution * FindObject
            (
                const NXString & solutionName /** Solution to be found  */
            );
            /** Finds a model update meta solution with specified solution name  @return  Model Update meta solution found 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAE::ModelUpdateSolution * FindObject
            (
                const char * solutionName /** Solution to be found  */
            );
            /**Returns  the active solution 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ModelUpdateSolution * ActiveSolution
            (
            );
            /**Sets  the active solution 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetActiveSolution
            (
                NXOpen::CAE::ModelUpdateSolution * activeSolution /** active solution */ 
            );
            /** Creates the builder object of model update sensitivity viewer  @return   
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NXOpen::CAE::ModelUpdateSensitivityViewerBuilder * CreateSensitivityViewerBuilder
            (
                NXOpen::CAE::ModelUpdateSolution * solution /** Model Update setup */
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
