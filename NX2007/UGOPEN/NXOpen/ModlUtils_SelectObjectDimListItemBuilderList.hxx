#ifndef NXOpen_MODLUTILS_SELECTOBJECTDIMLISTITEMBUILDERLIST_HXX_INCLUDED
#define NXOpen_MODLUTILS_SELECTOBJECTDIMLISTITEMBUILDERLIST_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ModlUtils_SelectObjectDimListItemBuilderList.ja
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
#include <NXOpen/libnxopencpp_modlutils_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace ModlUtils
    {
        class SelectObjectDimListItemBuilderList;
    }
    namespace ModlUtils
    {
        class SelectObjectDimListItemBuilder;
    }
    namespace ModlUtils
    {
        class _SelectObjectDimListItemBuilderListBuilder;
        class SelectObjectDimListItemBuilderListImpl;
        /** Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_MODLUTILSEXPORT  SelectObjectDimListItemBuilderList : public NXOpen::TaggedObject
        {
            private: SelectObjectDimListItemBuilderListImpl * m_selectobjectdimlistitembuilderlist_impl;
            private: friend class  _SelectObjectDimListItemBuilderListBuilder;
            protected: SelectObjectDimListItemBuilderList();
            public: ~SelectObjectDimListItemBuilderList();

            /// \cond NX_NO_DOC 
            /** Appends a set of objects to the list
                
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void Append
            (
                const std::vector<NXOpen::ModlUtils::SelectObjectDimListItemBuilder *> & objects /** items to append */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Appends an object to the list
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Append
            (
                NXOpen::ModlUtils::SelectObjectDimListItemBuilder * object /** item to append */
            );

            /// \endcond 
            /**Returns  the length of the list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int Length
            (
            );
            /** Deletes the item at the index specified.  The size of the list does
                *   not change, but the item at this index is set to NULL.
                
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void ClearIndex
            (
                int deleteIdx /** index of item to be deleted */
            );

            /// \cond NX_NO_DOC 
            /** Finds the index where the input object appears.  If it does not appear,
                *   -1 is returned.
                 @return  index of input object, -1 if not on list 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: int FindIndex
            (
                NXOpen::ModlUtils::SelectObjectDimListItemBuilder * obj /** Object to find index for */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the object at the input index.  May be NULL.
                 @return  object found at input index 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ModlUtils::SelectObjectDimListItemBuilder * FindItem
            (
                int index /** index of object to return */
            );

            /// \endcond 
            /** Erases the object from the list, but does not delete the object.
                    The list is shifted so that there isn't a null where the object used to be. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Erase
            (
                int index /** index of item to be removed from the list */
            );
            /** Erases the object at the given position from the list.
                    The list is shifted so that there isn't a null where the object used to be. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Erase
            (
                int index /** index of item to be removed from the list */,
                NXOpen::ObjectList::DeleteOption deleteOption /** whether to delete the object */
            );

            /// \cond NX_NO_DOC 
            /** Erases the object from the list, but does not delete the object.
                    The list is shifted so that there isn't a null where the object used to exist. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Erase
            (
                NXOpen::ModlUtils::SelectObjectDimListItemBuilder * obj /** object to be removed from the list */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Erases the object from the list.
                    The list is shifted so that there isn't a null where the object used to exist. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Erase
            (
                NXOpen::ModlUtils::SelectObjectDimListItemBuilder * obj /** object to be removed from the list */,
                NXOpen::ObjectList::DeleteOption deleteOption /** whether to delete the object */
            );

            /// \endcond 
            /** Clears the entire list without deleting the objects.  The caller is responsible for 
                    accounting for these objects.  If they are not used or deleted by the time the part is 
                    closed (in other words, leaked) an error will occur 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Clear
            (
            );
            /** Clears the entire list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Clear
            (
                NXOpen::ObjectList::DeleteOption deleteOption /** whether to delete the objects when removing them */
            );

            /// \cond NX_NO_DOC 
            /** Gets the contents of the entire list  @return  The list contents 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::ModlUtils::SelectObjectDimListItemBuilder *> GetContents
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Sets the contents of the entire list. This overwrites the previous contents of this list, 
                    but does not delete any objects that were originally on the list.
                 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetContents
            (
                const std::vector<NXOpen::ModlUtils::SelectObjectDimListItemBuilder *> & objects /** The list contents */
            );

            /// \endcond 
            /** Exchanges the position of two objects inside the list.
                    The first object is placed where the second used to be,
                    and second object where the first used to be. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Swap
            (
                int index1 /** location of the first item */,
                int index2 /** location of the second item */
            );

            /// \cond NX_NO_DOC 
            /** Exchanges the position of two objects inside the list.
                    The first object is placed where the second used to be,
                    and second object where the first used to be. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Swap
            (
                NXOpen::ModlUtils::SelectObjectDimListItemBuilder * object1 /** first item */,
                NXOpen::ModlUtils::SelectObjectDimListItemBuilder * object2 /** second item */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Inserts an object at the specified location 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Insert
            (
                int location /** location at which to insert the object */,
                NXOpen::ModlUtils::SelectObjectDimListItemBuilder * object /** object to be inserted */
            );

            /// \endcond 
            /** Move object at the specified location to the top of the list.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void MoveToTop
            (
                int index /** location of the item */
            );
            /** Move object at the specified location to the bottom of the list.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void MoveToBottom
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
