#ifndef NXOpen_TCINDRAWINGBOOKLET_HXX_INCLUDED
#define NXOpen_TCINDRAWINGBOOKLET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TCINDrawingBooklet.ja
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
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class TCINDrawingBooklet;
    class DebugSession;
    class TCINDrawingBookletImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for TCIN DrawingBooklet Autotest.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
     <br>  Created in NX8.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  TCINDrawingBooklet
    {
        private: TCINDrawingBookletImpl * m_tcindrawingbooklet_impl;
        private: NXOpen::DebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit TCINDrawingBooklet(NXOpen::DebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~TCINDrawingBooklet();
        /** Creates a new DrawingBooklet referencing a KF Part and Drawings 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void CreateNew
        (
            const NXString & itemId /** itemId for create */,
            const NXString & revisionId /** revisonId for create */,
            const NXString & itemType /** itemType for create */,
            const NXString & itemName /** item Name for create */,
            const NXString & folderPath /** where to put folderName in TC */,
            const NXString & folderName /** where to put in TC */,
            const NXString & kfPartSpec /** KF Part spec */,
            std::vector<NXString> & drawingPartSpecs /** drawings assoc w/ booklet */,
            NXString* drawingBookletItemId /** itemId of created booklet */,
            NXString* drawingBookletItemRevId /** itemRevId of created booklet */
        );
        /** Creates a new DrawingBooklet referencing a KF Part and Drawings 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void CreateNew
        (
            const char * itemId /** itemId for create */,
            const char * revisionId /** revisonId for create */,
            const char * itemType /** itemType for create */,
            const char * itemName /** item Name for create */,
            const char * folderPath /** where to put folderName in TC */,
            const char * folderName /** where to put in TC */,
            const char * kfPartSpec /** KF Part spec */,
            std::vector<NXString> & drawingPartSpecs /** drawings assoc w/ booklet */,
            NXString* drawingBookletItemId /** itemId of created booklet */,
            NXString* drawingBookletItemRevId /** itemRevId of created booklet */
        );
        /** Loads an Existing DrawingBooklet into NX 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void LoadFromDrawingPart
        (
            const NXString & drawingPartSpec /** load booklet assoc with drawing itemRev */,
            const NXString & revRuleName /** Revision Rule to be used */,
            NXString* drawingBookletItemId /** itemId of loaded booklet */,
            NXString* drawingBookletItemRevId /** itemRevId of loaded booklet */
        );
        /** Loads an Existing DrawingBooklet into NX 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void LoadFromDrawingPart
        (
            const char * drawingPartSpec /** load booklet assoc with drawing itemRev */,
            const char * revRuleName /** Revision Rule to be used */,
            NXString* drawingBookletItemId /** itemId of loaded booklet */,
            NXString* drawingBookletItemRevId /** itemRevId of loaded booklet */
        );
        /** Loads an Existing DrawingBooklet into NX 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void Load
        (
            const NXString & drawingBookletItemId /** itemId of booklet to load */,
            const NXString & drawingBookletItemRevId /** itemRevId of booklet to load */,
            const NXString & revRuleName /** Revision Rule to be used */
        );
        /** Loads an Existing DrawingBooklet into NX 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void Load
        (
            const char * drawingBookletItemId /** itemId of booklet to load */,
            const char * drawingBookletItemRevId /** itemRevId of booklet to load */,
            const char * revRuleName /** Revision Rule to be used */
        );
        /** Reloads an Existing DrawingBooklet into NX 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void Reload
        (
            const NXString & drawingBookletItemId /** itemId of booklet to reload */,
            const NXString & drawingBookletItemRevId /** itemRevId of booklet to reload */,
            const NXString & revRuleName /** Revision Rule to be used */
        );
        /** Reloads an Existing DrawingBooklet into NX 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void Reload
        (
            const char * drawingBookletItemId /** itemId of booklet to reload */,
            const char * drawingBookletItemRevId /** itemRevId of booklet to reload */,
            const char * revRuleName /** Revision Rule to be used */
        );
        /** Saves a DrawingBooklet and its Drawings to TC 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void Save
        (
            const NXString & drawingBookletItemIdIn /** itemId of booklet to save */,
            const NXString & drawingBookletItemRevIdIn /** itemRevId of booklet to save */,
            NXString* drawingBookletItemIdOut /** itemId of saved booklet */,
            NXString* drawingBookletItemRevIdOut /** itemRevId of saved booklet */
        );
        /** Saves a DrawingBooklet and its Drawings to TC 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void Save
        (
            const char * drawingBookletItemIdIn /** itemId of booklet to save */,
            const char * drawingBookletItemRevIdIn /** itemRevId of booklet to save */,
            NXString* drawingBookletItemIdOut /** itemId of saved booklet */,
            NXString* drawingBookletItemRevIdOut /** itemRevId of saved booklet */
        );
        /** Adds Drawing references to an existing DrawingBooklet 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void AddDrawingReferences
        (
            const NXString & drawingBookletItemId /** itemId of booklet */,
            const NXString & drawingBookletItemRevId /** itemRevId of booklet */,
            std::vector<NXString> & drawingPartSpecs /** drawings to add */
        );
        /** Adds Drawing references to an existing DrawingBooklet 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void AddDrawingReferences
        (
            const char * drawingBookletItemId /** itemId of booklet */,
            const char * drawingBookletItemRevId /** itemRevId of booklet */,
            std::vector<NXString> & drawingPartSpecs /** drawings to add */
        );
        /** Removes Drawing references from an existing DrawingBooklet 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveDrawingReferences
        (
            const NXString & drawingBookletItemId /** itemId of booklet */,
            const NXString & drawingBookletItemRevId /** itemRevId of booklet */,
            std::vector<NXString> & drawingPartSpecs /** drawings to remove */
        );
        /** Removes Drawing references from an existing DrawingBooklet 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void RemoveDrawingReferences
        (
            const char * drawingBookletItemId /** itemId of booklet */,
            const char * drawingBookletItemRevId /** itemRevId of booklet */,
            std::vector<NXString> & drawingPartSpecs /** drawings to remove */
        );
        /** Removes All Drawing references from an existing DrawingBooklet 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveAllDrawingReferences
        (
            const NXString & drawingBookletItemId /** itemId of booklet */,
            const NXString & drawingBookletItemRevId /** itemRevId of booklet */
        );
        /** Removes All Drawing references from an existing DrawingBooklet 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void RemoveAllDrawingReferences
        (
            const char * drawingBookletItemId /** itemId of booklet */,
            const char * drawingBookletItemRevId /** itemRevId of booklet */
        );
        /** Revise Drawing references to an existing DrawingBooklet 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void ReviseDrawingReferences
        (
            const NXString & drawingBookletItemId /** itemId of booklet */,
            const NXString & drawingBookletItemRevId /** itemRevId of booklet */,
            std::vector<NXString> & drawingPartSpecs /** drawings to revise */
        );
        /** Revise Drawing references to an existing DrawingBooklet 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void ReviseDrawingReferences
        (
            const char * drawingBookletItemId /** itemId of booklet */,
            const char * drawingBookletItemRevId /** itemRevId of booklet */,
            std::vector<NXString> & drawingPartSpecs /** drawings to revise */
        );
        /** Clear the cache of booklets used by this class 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void ClearCache
        (
        );
    }; //lint !e1712 default constructor not defined for class  


    /// \endcond 
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
