#ifndef NXOpen_CAE_IMPORTEDSIMINTERFACECOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_IMPORTEDSIMINTERFACECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ImportedSimInterfaceCollection.ja
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
        class ImportedSimInterfaceCollection;
    }
    namespace CAE
    {
        class SimSimulation;
    }
    namespace CAE
    {
        class ImportedSimInterface;
    }
    namespace CAE
    {
        class SimulationInterface;
    }
    namespace CAE
    {
        class ImportedSimInterfaceCollectionImpl;
        /**  @brief  Provides methods for managing Imported Simulation interfaces @link NXOpen::CAE::ImportedSimInterface NXOpen::CAE::ImportedSimInterface@endlink  in a sim part  

           <br> To obtain an instance of this class, refer to @link NXOpen::CAE::SimSimulation  NXOpen::CAE::SimSimulation @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ImportedSimInterfaceCollection : public NXOpen::TaggedObjectCollection
        {
            /** These represent the options for expression conflict */
            public: enum ExpressionConflictOption
            {
                ExpressionConflictOptionKeepExisting/** Keep Existing */,
                ExpressionConflictOptionKeepImported/** Keep Imported */,
                ExpressionConflictOptionKeepBoth/** Keep Both     */
            };

            private: ImportedSimInterfaceCollectionImpl * m_importedsiminterfacecollection_impl;
            private: NXOpen::CAE::SimSimulation* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ImportedSimInterfaceCollection(NXOpen::CAE::SimSimulation *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ImportedSimInterfaceCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::ImportedSimInterfaceCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::ImportedSimInterface *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::ImportedSimInterfaceCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::ImportedSimInterfaceCollection *m_context;
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
            /** Creates a SimulationInterface
                      @return  Simulation Interface found 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ImportedSimInterface * CreateImportedSimulationInterface
            (
                NXOpen::CAE::SimulationInterface * simif /** Simulation Interface*/,
                NXOpen::CAE::ImportedSimInterfaceCollection::ExpressionConflictOption expconfop /** expression conflict option */
            );
            /** Finds the @link NXOpen::CAE::ImportedSimInterface NXOpen::CAE::ImportedSimInterface@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with the given journal identifier.  @return  Simulation Interface found 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ImportedSimInterface * FindObject
            (
                const NXString & journalIdentifier /** Identifier to be found */
            );
            /** Finds the @link NXOpen::CAE::ImportedSimInterface NXOpen::CAE::ImportedSimInterface@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with the given journal identifier.  @return  Simulation Interface found 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::ImportedSimInterface * FindObject
            (
                const char * journalIdentifier /** Identifier to be found */
            );
            /** Delete imported simulation interface 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteSimInterface
            (
                NXOpen::CAE::ImportedSimInterface * importedSimIF /** Simulation Interface*/
            );
            /** Load source simulation 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void LoadSourceSim
            (
                NXOpen::CAE::ImportedSimInterface * importedSimIF /** Simulation Interface*/
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