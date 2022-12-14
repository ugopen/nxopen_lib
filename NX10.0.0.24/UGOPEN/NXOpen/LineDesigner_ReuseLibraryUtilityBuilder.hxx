#ifndef NXOpen_LINEDESIGNER_REUSELIBRARYUTILITYBUILDER_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_REUSELIBRARYUTILITYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_ReuseLibraryUtilityBuilder.ja
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
#include <NXOpen/LineDesigner_ReuseLibraryDragData.hxx>
#include <NXOpen/LineDesigner_ReuseLibraryUtilityBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class ReuseLibraryUtilityBuilder;
    }
    namespace LineDesigner
    {
        class ReuseLibraryDragData;
    }
    class NXObject;
    class TaggedObject;
    namespace LineDesigner
    {
        class _ReuseLibraryUtilityBuilderBuilder;
        class ReuseLibraryUtilityBuilderImpl;
        /** Represents a JA for ReuseLibraryUtility  <br> Established by LineDesigner_LineDesignerManager whenever it is needed.  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  ReuseLibraryUtilityBuilder : public NXOpen::TaggedObject
        {
            private: ReuseLibraryUtilityBuilderImpl * m_reuselibraryutilitybuilder_impl;
            private: friend class  _ReuseLibraryUtilityBuilderBuilder;
            protected: ReuseLibraryUtilityBuilder();
            public: ~ReuseLibraryUtilityBuilder();
            /**  Create Drag Data  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::LineDesigner::ReuseLibraryDragData * CreateDragData
            (
            );
            /**  Handle Dropping LD Smart Part  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::NXObject * DropLDSmartPart
            (
                NXOpen::LineDesigner::ReuseLibraryDragData * reuseLibraryDragData /** reuselibrarydragdata */ ,
                const NXOpen::Vector3d & dropPoint /** droppoint */ 
            );
            /**  Handle Dropping PTS Part  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::NXObject * DropPTSPart
            (
                NXOpen::LineDesigner::ReuseLibraryDragData * reuseLibraryDragData /** reuselibrarydragdata */ ,
                const NXOpen::Vector3d & dropPoint /** droppoint */ 
            );
            /**  Handle Dropping Normal Part  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::NXObject * DropNormalPart
            (
                NXOpen::LineDesigner::ReuseLibraryDragData * reuseLibraryDragData /** reuselibrarydragdata */ ,
                const NXOpen::Vector3d & dropPoint /** droppoint */ 
            );
            /**  Handle Dropping Other Part 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void DropOtherPart
            (
                NXOpen::LineDesigner::ReuseLibraryDragData * reuseLibraryDragData /** reuselibrarydragdata */ ,
                const NXOpen::Vector3d & dropPoint /** droppoint */ 
            );
            /**  Keep Source Library Item ID 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void KeepSourceLibraryID
            (
                NXOpen::NXObject * part /** part */ 
            );
            /**  Execute the renaming of the cloned component when it is added under an assembly 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void ExecuteRenameAssembly
            (
            );
            /**  Move Component To The Location 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void MoveComponentToLocation
            (
                NXOpen::NXObject * part /** part */ ,
                const NXOpen::Vector3d & position /** position */ 
            );
            /**  Place Part from Library  Using Connector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void PlacementByConnector
            (
                NXOpen::NXObject * part /** part */ ,
                NXOpen::TaggedObject * connectorFaceTag /** connectorfacetag */ 
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
