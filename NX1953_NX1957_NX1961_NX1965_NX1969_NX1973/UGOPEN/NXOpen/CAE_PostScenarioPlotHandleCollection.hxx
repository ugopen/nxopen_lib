#ifndef NXOpen_CAE_POSTSCENARIOPLOTHANDLECOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_POSTSCENARIOPLOTHANDLECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostScenarioPlotHandleCollection.ja
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
        class PostScenarioPlotHandleCollection;
    }
    namespace CAE
    {
        class PostScenario;
    }
    namespace CAE
    {
        class PostScenarioPlotHandle;
    }
    namespace CAE
    {
        class PostScenarioPlotHandleCollectionImpl;
        /** The collection of Plots the scenario is attached to. 

                
                    Access is provided via @link NXOpen::CAE::PostScenarioPlotHandle NXOpen::CAE::PostScenarioPlotHandle@endlink  instances.

                    The Plots are determined by the selected @link CAE::PostScenarioBuilder::Visualization CAE::PostScenarioBuilder::Visualization @endlink and @link CAE::PostScenarioBuilder::SetVisualization CAE::PostScenarioBuilder::SetVisualization @endlink .

                    If multiple scenarios are overlaid, the resulting visualization can change.
                  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::PostScenario  NXOpen::CAE::PostScenario @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostScenarioPlotHandleCollection : public NXOpen::TaggedObjectCollection
        {
            private: PostScenarioPlotHandleCollectionImpl * m_postscenarioplothandlecollection_impl;
            private: NXOpen::CAE::PostScenario* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit PostScenarioPlotHandleCollection(NXOpen::CAE::PostScenario *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PostScenarioPlotHandleCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::PostScenarioPlotHandleCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::PostScenarioPlotHandle *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::PostScenarioPlotHandleCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::PostScenarioPlotHandleCollection *m_context;
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
            /** Finds a @link CAE::PostScenarioPlotHandle CAE::PostScenarioPlotHandle@endlink  instance. In general, this method 
                        should not be used in handwritten code and it exists to support record and playback of journals.
                        
                        For handwritten code, consider using the alternative Find methods of this class.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PostScenarioPlotHandle * FindObject
            (
                const NXString & plotName /** plotname */ 
            );
            /** Finds a @link CAE::PostScenarioPlotHandle CAE::PostScenarioPlotHandle@endlink  instance. In general, this method 
                        should not be used in handwritten code and it exists to support record and playback of journals.
                        
                        For handwritten code, consider using the alternative Find methods of this class.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAE::PostScenarioPlotHandle * FindObject
            (
                const char * plotName /** plotname */ 
            );
            /** Finds a @link CAE::PostScenarioPlotHandle CAE::PostScenarioPlotHandle@endlink  based on the viewport index. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PostScenarioPlotHandle * FindObjectByViewport
            (
                int viewportIndex /** viewportindex */ 
            );
            /** Finds a @link CAE::PostScenarioPlotHandle CAE::PostScenarioPlotHandle@endlink  based on the descriptive name of the plot. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PostScenarioPlotHandle * FindObjectByDescriptiveName
            (
                const NXString & visualizationDefinitionName /** visualizationdefinitionname */ 
            );
            /** Finds a @link CAE::PostScenarioPlotHandle CAE::PostScenarioPlotHandle@endlink  based on the descriptive name of the plot. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAE::PostScenarioPlotHandle * FindObjectByDescriptiveName
            (
                const char * visualizationDefinitionName /** visualizationdefinitionname */ 
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
