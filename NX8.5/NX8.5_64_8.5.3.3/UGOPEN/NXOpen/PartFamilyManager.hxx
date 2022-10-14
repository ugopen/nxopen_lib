#ifndef NXOpen_PARTFAMILYMANAGER_HXX_INCLUDED
#define NXOpen_PARTFAMILYMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PartFamilyManager.ja
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
#include <NXOpen/PartFamilyMemberValues.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class PartFamilyManager;
    class Part;
    class PartFamilyMemberValues;
    class PartFamilyManagerImpl;
    /** This class represents part family  <br> Use @link Part::GetPartFamilyManager Part::GetPartFamilyManager@endlink  to get the instance of this class.  <br> 
     <br>  Created in NX6.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  PartFamilyManager : public TransientObject
    {
        private: PartFamilyManagerImpl * m_partfamilymanager_impl;
        /// \cond NX_NO_DOC 
        public: explicit PartFamilyManager(void *ptr);
        /// \endcond 
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~PartFamilyManager();
        /** Get the number of family members in the family  @return  the number of members in the family 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: int GetMemberCount
        (
        );
        /** Create member part in the family  @return  the new member part 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Part * CreateMember
        (
            int memberIndex /** the index of member for which part needs to be created*/
        );
        /** Add member in the family  @return  the index of created member 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: int AddMember
        (
            NXOpen::PartFamilyMemberValues * memberData /** the member values*/
        );
        /** Edit member in the family 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void EditMember
        (
            int memberIndex /** the index of member that needs to be edited */,
            NXOpen::PartFamilyMemberValues * newMemberData /** the new member data*/
        );
        /** Delete member in the family 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void DeleteMember
        (
            int memberIndex /** the index of member that needs to be deleted */
        );
        /** Ask index of member name in the family  @return  index of the member name 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: int AskIndexOfMemberName
        (
            const NXString & memberName /** the member name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Ask index of member name in the family  @return  index of the member name 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        int AskIndexOfMemberName
        (
            const char * memberName /** the member name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Print the part family table 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintFamilyTable
        (
        );
        /** Get the existing member or create a new one if it does not exist  @return  established member name 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString EstablishMember
        (
            int memberIndex /** index of member */
        );
    }; //lint !e1712 default constructor not defined for class  

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