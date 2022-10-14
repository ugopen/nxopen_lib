#ifndef NXOpen_CAE_CAEDOFSETCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_CAEDOFSETCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CaeDOFSetCollection.ja
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
        class CaeDOFSetCollection;
    }
    namespace CAE
    {
        class SimSimulation;
    }
    namespace CAE
    {
        class CaeDOFSet;
    }
    namespace CAE
    {
        class FENode;
    }
    class TaggedObject;
    namespace CAE
    {
        class CaeDOFSetCollectionImpl;
        /**  @brief  Provides methods for managing DOFSet @link CAE::CaeDOFSet CAE::CaeDOFSet@endlink  

           <br> To obtain an instance of this class, refer to @link CAE::SimSimulation  CAE::SimSimulation @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CaeDOFSetCollection : public TaggedObjectCollection
        {
            private: CaeDOFSetCollectionImpl * m_caedofsetcollection_impl;
            private: NXOpen::CAE::SimSimulation* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CaeDOFSetCollection(NXOpen::CAE::SimSimulation *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CaeDOFSetCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::CaeDOFSetCollection::iterator::copy,initializer)
            class iterator
            {
            public:
                /** Value type associated with iterator*/ 

                typedef CAE::CaeDOFSet * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                { // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::CaeDOFSetCollection *context) : m_context(context), m_current(NULL_TAG)
                { // coverity[uninit_member]
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
                NXOpen::CAE::CaeDOFSetCollection *m_context;
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
            /** Create a DOFSet
                    A true for a dof logical entry would mean that the dof is included for that corresponding node.
                    A false would mean that the dof is not included for that node.  @return  The created DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::CaeDOFSet * CreateDofset
            (
                const NXString & dofsetName /**  Name of a DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::CAE::FENode *> & nodes /** Array of nodes in the DOFSet @link CAE::FENode CAE::FENode@endlink  */,
                const std::vector<bool> & dof1 /** Array of DOF1 values  */,
                const std::vector<bool> & dof2 /** Array of DOF2 values  */,
                const std::vector<bool> & dof3 /** Array of DOF3 values  */,
                const std::vector<bool> & dof4 /** Array of DOF4 values  */,
                const std::vector<bool> & dof5 /** Array of DOF5 values  */,
                const std::vector<bool> & dof6 /** Array of DOF6 values  */
            );
            /** Create a DOFSet
                    A true for a dof logical entry would mean that the dof is included for that corresponding node.
                    A false would mean that the dof is not included for that node.  @return  The created DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::CaeDOFSet * CreateDofset
            (
                const char * dofsetName /**  Name of a DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::CAE::FENode *> & nodes /** Array of nodes in the DOFSet @link CAE::FENode CAE::FENode@endlink  */,
                const std::vector<bool> & dof1 /** Array of DOF1 values  */,
                const std::vector<bool> & dof2 /** Array of DOF2 values  */,
                const std::vector<bool> & dof3 /** Array of DOF3 values  */,
                const std::vector<bool> & dof4 /** Array of DOF4 values  */,
                const std::vector<bool> & dof5 /** Array of DOF5 values  */,
                const std::vector<bool> & dof6 /** Array of DOF6 values  */
            );
            /** Create a Union of DOFSets @return  The created union DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::CaeDOFSet * CreateUnionDofset
            (
                const NXString & dofsetName /**  Name of the unioned DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::CAE::CaeDOFSet *> & objects /** DOFSets that need to be unioned */
            );
            /** Create a Union of DOFSets @return  The created union DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::CaeDOFSet * CreateUnionDofset
            (
                const char * dofsetName /**  Name of the unioned DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::CAE::CaeDOFSet *> & objects /** DOFSets that need to be unioned */
            );
            /** Create an Intersection of DOFSets @return  The created intersection DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::CaeDOFSet * CreateIntersectionDofset
            (
                const NXString & dofsetName /**  Name of the intersection DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::CAE::CaeDOFSet *> & objects /** DOFSets that need to be intersected */
            );
            /** Create an Intersection of DOFSets @return  The created intersection DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::CaeDOFSet * CreateIntersectionDofset
            (
                const char * dofsetName /**  Name of the intersection DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::CAE::CaeDOFSet *> & objects /** DOFSets that need to be intersected */
            );
            /** Create a XOR of DOFSets @return  The created XOR DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::CaeDOFSet * CreateExclusiveOrDofset
            (
                const NXString & dofsetName /**  Name of the XOR DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::CAE::CaeDOFSet *> & objects /** DOFSets that need to be XORed */
            );
            /** Create a XOR of DOFSets @return  The created XOR DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::CaeDOFSet * CreateExclusiveOrDofset
            (
                const char * dofsetName /**  Name of the XOR DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::CAE::CaeDOFSet *> & objects /** DOFSets that need to be XORed */
            );
            /** Copy a DOFSet  @return  The copied DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::CaeDOFSet * CopyDofset
            (
                const NXString & dofsetName /**  Name of the copied DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAE::CaeDOFSet * sourceDofset /** The source DOFSet object */
            );
            /** Copy a DOFSet  @return  The copied DOFSet object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::CaeDOFSet * CopyDofset
            (
                const char * dofsetName /**  Name of the copied DOFSet   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAE::CaeDOFSet * sourceDofset /** The source DOFSet object */
            );
            /** Finds the @link  CAE::CaeDOFSet   CAE::CaeDOFSet @endlink  with the given identifier as recorded in a journal. 
                        An object may not return the same value as its JournalIdentifier in different versions of 
                        the software. However newer versions of the software should find the same object when 
                        FindObject is passed older versions of its journal identifier. In general, this method 
                        should not be used in handwritten code and exists to support record and playback of journals.

                        An exception will be thrown if no object can be found with the given journal identifier.  @return  The found DOFSet 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::CaeDOFSet * FindObject
            (
                const NXString & journalIdentifier /** Identifier of the DOFSet you want */
            );
            /** Finds the @link  CAE::CaeDOFSet   CAE::CaeDOFSet @endlink  with the given identifier as recorded in a journal. 
                        An object may not return the same value as its JournalIdentifier in different versions of 
                        the software. However newer versions of the software should find the same object when 
                        FindObject is passed older versions of its journal identifier. In general, this method 
                        should not be used in handwritten code and exists to support record and playback of journals.

                        An exception will be thrown if no object can be found with the given journal identifier.  @return  The found DOFSet 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            NXOpen::CAE::CaeDOFSet * FindObject
            (
                const char * journalIdentifier /** Identifier of the DOFSet you want */
            );
            /** Query DOFSets list
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void QueryDofsetList
            (
                std::vector<NXOpen::TaggedObject *> & objects /** objects */ 
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