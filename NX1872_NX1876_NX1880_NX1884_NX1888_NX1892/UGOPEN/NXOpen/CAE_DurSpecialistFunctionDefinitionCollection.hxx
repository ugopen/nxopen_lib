#ifndef NXOpen_CAE_DURSPECIALISTFUNCTIONDEFINITIONCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTFUNCTIONDEFINITIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistFunctionDefinitionCollection.ja
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
#include <NXOpen/CAE_DurSpecialistFunctionDefinition.hxx>
#include <NXOpen/CAE_DurSpecialistFunctionDefinitionBuilder.hxx>
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
        class DurSpecialistFunctionDefinitionCollection;
    }
    namespace CAE
    {
        class DurSpecialistSolution;
    }
    namespace CAE
    {
        class DurSpecialistFunctionDefinition;
    }
    namespace CAE
    {
        class DurSpecialistFunctionDefinitionBuilder;
    }
    namespace CAE
    {
        class DurSpecialistLocalDefinition;
    }
    namespace CAE
    {
        class DurSpecialistFunctionDefinitionCollectionImpl;
        /** Represents a collection of DurSpecialist FunctionDefinition.  <br> Use @link CAE::DurSpecialistSolution::FunctionDefinitions CAE::DurSpecialistSolution::FunctionDefinitions@endlink  to get the instance of this class.  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistFunctionDefinitionCollection : public NXOpen::TaggedObjectCollection
        {
            private: DurSpecialistFunctionDefinitionCollectionImpl * m_durspecialistfunctiondefinitioncollection_impl;
            private: NXOpen::CAE::DurSpecialistSolution* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit DurSpecialistFunctionDefinitionCollection(NXOpen::CAE::DurSpecialistSolution *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~DurSpecialistFunctionDefinitionCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::DurSpecialistFunctionDefinitionCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::DurSpecialistFunctionDefinition *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::DurSpecialistFunctionDefinitionCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::DurSpecialistFunctionDefinitionCollection *m_context;
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
            /** Finds the @link NXOpen::CAE::DurSpecialistFunctionDefinition NXOpen::CAE::DurSpecialistFunctionDefinition@endlink  object with the given name.  @return  @link NXOpen::CAE::DurSpecialistFunctionDefinition NXOpen::CAE::DurSpecialistFunctionDefinition@endlink  object with this name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: NXOpen::CAE::DurSpecialistFunctionDefinition * FindObject
            (
                const NXString & name /** Name of the FunctionDefinition  */
            );
            /** Finds the @link NXOpen::CAE::DurSpecialistFunctionDefinition NXOpen::CAE::DurSpecialistFunctionDefinition@endlink  object with the given name.  @return  @link NXOpen::CAE::DurSpecialistFunctionDefinition NXOpen::CAE::DurSpecialistFunctionDefinition@endlink  object with this name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            NXOpen::CAE::DurSpecialistFunctionDefinition * FindObject
            (
                const char * name /** Name of the FunctionDefinition  */
            );
            /** Creates a @link NXOpen::CAE::DurSpecialistFunctionDefinitionBuilder NXOpen::CAE::DurSpecialistFunctionDefinitionBuilder@endlink   @return  Builder object
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: NXOpen::CAE::DurSpecialistFunctionDefinitionBuilder * CreateFunctionDefinitionBuilderFromSolution
            (
                NXOpen::CAE::DurSpecialistFunctionDefinition * functionDefinition /** @link NXOpen::CAE::DurSpecialistFunctionDefinition NXOpen::CAE::DurSpecialistFunctionDefinition@endlink  to be edited */
            );
            /** Creates a @link NXOpen::CAE::DurSpecialistFunctionDefinitionBuilder NXOpen::CAE::DurSpecialistFunctionDefinitionBuilder@endlink   @return  Builder object 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: NXOpen::CAE::DurSpecialistFunctionDefinitionBuilder * CreateFunctionDefinitionBuilderFromLocalDefinition
            (
                NXOpen::CAE::DurSpecialistLocalDefinition * localDefTag /** @link NXOpen::CAE::DurSpecialistLocalDefinition NXOpen::CAE::DurSpecialistLocalDefinition@endlink  owning the @link NXOpen::CAE::DurSpecialistFunctionDefinition NXOpen::CAE::DurSpecialistFunctionDefinition@endlink  */,
                NXOpen::CAE::DurSpecialistFunctionDefinition * functionDefinition /** @link NXOpen::CAE::DurSpecialistFunctionDefinition NXOpen::CAE::DurSpecialistFunctionDefinition@endlink  to be edited */
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
