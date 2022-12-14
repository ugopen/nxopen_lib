#ifndef NXOpen_MECHATRONICS_MATLABSIGNALCONNECTIONBUILDERLIST_HXX_INCLUDED
#define NXOpen_MECHATRONICS_MATLABSIGNALCONNECTIONBUILDERLIST_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_MATLABSignalConnectionBuilderList.ja
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
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class MATLABSignalConnectionBuilderList;
    }
    namespace Mechatronics
    {
        class MATLABSignalConnectionBuilder;
    }
    namespace Mechatronics
    {
        class _MATLABSignalConnectionBuilderListBuilder;
        class MATLABSignalConnectionBuilderListImpl;
        /** Represents a list of objects.
         <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
         <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

         <br>  Created in NX4.0.0.  <br>  
        */
        class NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") NXOPENCPP_MECHATRONICSEXPORT  MATLABSignalConnectionBuilderList : public NXOpen::TaggedObject
        {
            private: MATLABSignalConnectionBuilderListImpl * m_matlabsignalconnectionbuilderlist_impl;
            private: friend class  _MATLABSignalConnectionBuilderListBuilder;
            protected: MATLABSignalConnectionBuilderList();
            public: ~MATLABSignalConnectionBuilderList();
            /** Appends a set of objects to the list
                
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Append
            (
                const std::vector<NXOpen::Mechatronics::MATLABSignalConnectionBuilder *> & objects /** items to append */
            );
            /** Appends an object to the list
                
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Append
            (
                NXOpen::Mechatronics::MATLABSignalConnectionBuilder * object /** item to append */
            );
            /**Returns  the length of the list 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") int Length
            (
            );
            /** Deletes the item at the index specified.  The size of the list does
                *   not change, but the item at this index is set to NULL.
                
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void ClearIndex
            (
                int deleteIdx /** index of item to be deleted */
            );
            /** Finds the index where the input object appears.  If it does not appear,
                *   -1 is returned.
                 @return  index of input object, -1 if not on list 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") int FindIndex
            (
                NXOpen::Mechatronics::MATLABSignalConnectionBuilder * obj /** Object to find index for */
            );
            /** Returns the object at the input index.  May be NULL.
                 @return  object found at input index 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") NXOpen::Mechatronics::MATLABSignalConnectionBuilder * FindItem
            (
                int index /** index of object to return */
            );
            /** Erases the object from the list, but does not delete the object.
                    The list is shifted so that there isn't a null where the object used to be. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Erase
            (
                int index /** index of item to be removed from the list */
            );
            /** Erases the object at the given position from the list.
                    The list is shifted so that there isn't a null where the object used to be. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Erase
            (
                int index /** index of item to be removed from the list */,
                NXOpen::ObjectList::DeleteOption deleteOption /** whether to delete the object */
            );
            /** Erases the object from the list, but does not delete the object.
                    The list is shifted so that there isn't a null where the object used to exist. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Erase
            (
                NXOpen::Mechatronics::MATLABSignalConnectionBuilder * obj /** object to be removed from the list */
            );
            /** Erases the object from the list.
                    The list is shifted so that there isn't a null where the object used to exist. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Erase
            (
                NXOpen::Mechatronics::MATLABSignalConnectionBuilder * obj /** object to be removed from the list */,
                NXOpen::ObjectList::DeleteOption deleteOption /** whether to delete the object */
            );
            /** Clears the entire list without deleting the objects.  The caller is responsible for 
                    accounting for these objects.  If they are not used or deleted by the time the part is 
                    closed (in other words, leaked) an error will occur 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Clear
            (
            );
            /** Clears the entire list 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Clear
            (
                NXOpen::ObjectList::DeleteOption deleteOption /** whether to delete the objects when removing them */
            );
            /** Gets the contents of the entire list  @return  The list contents 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") std::vector<NXOpen::Mechatronics::MATLABSignalConnectionBuilder *> GetContents
            (
            );
            /** Sets the contents of the entire list. This overwrites the previous contents of this list, 
                    but does not delete any objects that were originally on the list.
                 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void SetContents
            (
                const std::vector<NXOpen::Mechatronics::MATLABSignalConnectionBuilder *> & objects /** The list contents */
            );
            /** Exchanges the position of two objects inside the list.
                    The first object is placed where the second used to be,
                    and second object where the first used to be. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Swap
            (
                int index1 /** location of the first item */,
                int index2 /** location of the second item */
            );
            /** Exchanges the position of two objects inside the list.
                    The first object is placed where the second used to be,
                    and second object where the first used to be. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Swap
            (
                NXOpen::Mechatronics::MATLABSignalConnectionBuilder * object1 /** first item */,
                NXOpen::Mechatronics::MATLABSignalConnectionBuilder * object2 /** second item */
            );
            /** Inserts an object at the specified location 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void Insert
            (
                int location /** location at which to insert the object */,
                NXOpen::Mechatronics::MATLABSignalConnectionBuilder * object /** object to be inserted */
            );
            /** Move object at the specified location to the top of the list.
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void MoveToTop
            (
                int index /** location of the item */
            );
            /** Move object at the specified location to the bottom of the list.
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") void MoveToBottom
            (
                int index /** location of the item */
            );
        };
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
