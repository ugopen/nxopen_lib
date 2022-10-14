#ifndef NXOpen_DRAWINGCOMPAREMANAGER_HXX_INCLUDED
#define NXOpen_DRAWINGCOMPAREMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DrawingCompareManager.ja
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
#include <NXOpen/Annotations_IdSymbol.hxx>
#include <NXOpen/Drawings_CompareReportBuilder.hxx>
#include <NXOpen/Drawings_DrawingCompareSettingsBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
    class DrawingCompareManager;
    class Part;
    namespace Annotations
    {
        class IdSymbol;
    }
    namespace Drawings
    {
        class CompareReportBuilder;
    }
    namespace Drawings
    {
        class DrawingCompareSettingsBuilder;
    }
    class NXObject;
    class DrawingCompareManagerImpl;
    /** Represents an object that manages drawing compare.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
     <br>  Created in NX7.5.0.  <br>  
    */
    class NXOPENCPPEXPORT  DrawingCompareManager
    {
        private: DrawingCompareManagerImpl * m_drawingcomparemanager_impl;
        private: NXOpen::Part* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit DrawingCompareManager(NXOpen::Part *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~DrawingCompareManager();
        /** Caches data for drafting objects in the drawing part. 
                Creates overlay data if the status of toggle "Create Overlay Data with Snapshot Data" in Customer Default is on.
                Use @link DrawingCompareManager::CreateOverlayData DrawingCompareManager::CreateOverlayData@endlink  to create overlay data. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void CreateSnapshot
        (
        );
        /** Create track changes data for drafting objects in the drawing part 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void CreateTrackChanges
        (
        );
        /** Delete track changes data for drafting objects in the drawing part 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void DeleteTrackChanges
        (
        );
        /** Deletes the cached data for drafting objects. 
                Does not delete the overlay data.
                Use @link DrawingCompareManager::DeleteOverlayData DrawingCompareManager::DeleteOverlayData@endlink  to delete overlay data.
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void DeleteSnapshot
        (
        );
        /** Deletes part comparison report. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void DeleteComparisonReport
        (
        );
        /** Gets the entity for the given ID.  @return  The object of entity 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::NXObject * GetEntityObjectFromId
        (
            int subfileID /** The ID of entity */
        );
        /** Creates a @link NXOpen::Drawings::DrawingCompareSettingsBuilder NXOpen::Drawings::DrawingCompareSettingsBuilder@endlink  
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : drafting ("DRAFTING") */
        public: NXOpen::Drawings::DrawingCompareSettingsBuilder * CreateDrawingCompareSettingsBuilder
        (
        );
        /** Creates a @link NXOpen::Drawings::CompareReportBuilder NXOpen::Drawings::CompareReportBuilder@endlink  
         <br>  @deprecated Deprecated in NX11.0.0.  Use @link DrawingCompareManager::CreateCompareReportBuilder DrawingCompareManager::CreateCompareReportBuilder@endlink  instead. <br>  

         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : drafting ("DRAFTING") */
        public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use DrawingCompareManager::CreateCompareReportBuilder instead.") NXOpen::Drawings::CompareReportBuilder * CreateCompareReportBuilder
        (
        );
        /** Creates a @link NXOpen::Drawings::CompareReportBuilder NXOpen::Drawings::CompareReportBuilder@endlink  
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : drafting ("DRAFTING") */
        public: NXOpen::Drawings::CompareReportBuilder * CreateCompareReportBuilder
        (
            const NXString & partFileNameToCompare /** partfilenametocompare */ ,
            bool reuseExistingSnapshot /** reuseexistingsnapshot */ 
        );
        /** Creates a @link NXOpen::Drawings::CompareReportBuilder NXOpen::Drawings::CompareReportBuilder@endlink  
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : drafting ("DRAFTING") */
        NXOpen::Drawings::CompareReportBuilder * CreateCompareReportBuilder
        (
            const char * partFileNameToCompare /** partfilenametocompare */ ,
            bool reuseExistingSnapshot /** reuseexistingsnapshot */ 
        );
        /** Creates Overlay data of a part. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : drafting ("DRAFTING") */
        public: void CreateOverlayData
        (
        );
        /** Deletes Overlay data of a part. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : drafting ("DRAFTING") */
        public: void DeleteOverlayData
        (
        );
        /** Preserves the change symbol settings of the objects passed to it. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : drafting ("DRAFTING") */
        public: void PreserveChangeSymbol
        (
            const std::vector<NXOpen::Annotations::IdSymbol *> & idSymbols /** a list of change symbols */
        );
        /** Unpreserves the change symbol settings of the objects passed to it. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : drafting ("DRAFTING") */
        public: void UnpreserveChangeSymbol
        (
            const std::vector<NXOpen::Annotations::IdSymbol *> & idSymbols /** a list of change symbols */
        );

        /// \cond NX_NO_DOC 
        /** Set removing undo marks to false for the tempTDCReportUtils 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : drafting ("DRAFTING") */
        public: void SetRemoveUndoMarks
        (
            bool removeUndoMarks /** removeundomarks */ 
        );

        /// \endcond 
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