#ifndef NXOpen_DRAFTING_CUTCOPYPASTEBUILDER_HXX_INCLUDED
#define NXOpen_DRAFTING_CUTCOPYPASTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drafting_CutCopyPasteBuilder.ja
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
#include <NXOpen/Drafting_CutCopyPasteLeaderBuilder.hxx>
#include <NXOpen/GeometricUtilities_ModlMotion.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_drafting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drafting
    {
        class CutCopyPasteBuilder;
    }
    class Builder;
    namespace Drafting
    {
        class CutCopyPasteLeaderBuilder;
    }
    namespace GeometricUtilities
    {
        class ModlMotion;
    }
    class Plane;
    class SelectTaggedObjectList;
    class View;
    namespace Drafting
    {
        class _CutCopyPasteBuilderBuilder;
        class CutCopyPasteBuilderImpl;
        /**
                Represents a paste in Drafting.
             <br> To create a new instance of this class, use @link NXOpen::Drafting::DraftingApplicationManager::CreateCutCopyPasteBuilder  NXOpen::Drafting::DraftingApplicationManager::CreateCutCopyPasteBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Transform.DeltaEnum </term> <description> 
         
        ReferenceWcsWorkPart </description> </item> 

        <item><term> 
         
        Transform.DeltaXc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        Transform.DeltaYc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        Transform.DeltaZc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        Transform.Option </term> <description> 
         
        Distance </description> </item> 

        </list> 

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_DRAFTINGEXPORT  CutCopyPasteBuilder : public NXOpen::Builder
        {
            /** Specifies the paste type. */
            public: enum TypePaste
            {
                TypePasteTransform/** Transform type */,
                TypePasteTracking/** Tracking type */
            };

            /** Specifies the copy cut operation type. */
            public: enum TypeOperation
            {
                TypeOperationCopy/** Copy type */,
                TypeOperationCut/** Cut type */
            };

            private: CutCopyPasteBuilderImpl * m_cutcopypastebuilder_impl;
            private: friend class  _CutCopyPasteBuilderBuilder;
            protected: CutCopyPasteBuilder();
            public: ~CutCopyPasteBuilder();
            /**Returns  the paste type 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drafting::CutCopyPasteBuilder::TypePaste PasteType
            (
            );
            /**Sets  the paste type 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPasteType
            (
                NXOpen::Drafting::CutCopyPasteBuilder::TypePaste pasteType /** pastetype */ 
            );
            /**Returns  the motion from the default paste position 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ModlMotion * Transform
            (
            );
            /**Returns  the destination view.  Either a drafting view or sheet view. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::View * DestinationView
            (
            );
            /**Sets  the destination view.  Either a drafting view or sheet view. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDestinationView
            (
                NXOpen::View * destinationView /** destinationview */ 
            );
            /** Get the default to point. The drop location.  @return  the drop location 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d GetDefaultToPoint
            (
            );
            /** Set the default to point.  The drop location. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDefaultToPoint
            (
                const NXOpen::Point3d & dropLocation /** the drop location */
            );
            /**Returns  the objects list to copy. May include drafting geometry, sketch objects
                        and simple annotations. Note that PMI, feature, view, and table objects
                        are not supported by this class. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * ObjectsToCopy
            (
            );
            /**Returns   the output Objects 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * OutputObjects
            (
            );
            /**Returns   the plane to restrict motion 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * PlaneToRestrictMotion
            (
            );
            /**Sets   the plane to restrict motion 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetPlaneToRestrictMotion
            (
                NXOpen::Plane * plan /** plan */ 
            );
            /** Set the final motion from the drop location. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetMoveOnCommit
            (
                const NXOpen::Matrix3x3 & rot /** rotational part of motion */,
                const NXOpen::Vector3d & trans /** translation part of motion */
            );
            /** Make the initial drop. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void InitPaste
            (
            );
            /**Returns  the operation type. If it is copy, we will keept the originals. If it is cut, we will delete the originals 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drafting::CutCopyPasteBuilder::TypeOperation Originals
            (
            );
            /**Sets  the operation type. If it is copy, we will keept the originals. If it is cut, we will delete the originals 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetOriginals
            (
                NXOpen::Drafting::CutCopyPasteBuilder::TypeOperation originals /** originals */ 
            );
            /**Returns  the leader builder. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drafting::CutCopyPasteLeaderBuilder * CutCopyPasteLeader
            (
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