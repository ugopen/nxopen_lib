#ifndef NXOpen_CAE_MMCCREATEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MMCCREATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MMCCreateBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class MMCCreateBuilder;
    }
    class Builder;
    namespace CAE
    {
        class MeshMate;
    }
    class Expression;
    class SelectDisplayableObjectList;
    class SelectIParameterizedSurface;
    namespace CAE
    {
        class _MMCCreateBuilderBuilder;
        class MMCCreateBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::MMCCreateBuilder NXOpen::CAE::MMCCreateBuilder@endlink  which can be used to create or edit 
             @link NXOpen::CAE::MeshMate NXOpen::CAE::MeshMate@endlink  objects. 
             <br> To create a new instance of this class, use @link NXOpen::CAE::MeshControlCollection::CreateMmcCreateBuilder  NXOpen::CAE::MeshControlCollection::CreateMmcCreateBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  MMCCreateBuilder : public NXOpen::Builder
        {
            /**  Type of the Creation Methods for MMC */
            public: enum Types
            {
                TypesAutoCreate/** Auto Create*/,
                TypesManual/** Manual Create*/
            };

            /**  Types of Mesh Mating Conditions */
            public: enum MeshMatingType
            {
                MeshMatingTypeGlueCoincident/** glue coincident*/,
                MeshMatingTypeGlueNonCoincident/** glue non-coincident*/,
                MeshMatingTypeFreeCoincident/** free coincident*/
            };

            /**  Types of Face Serach Operations */
            public: enum FaceSearchType
            {
                FaceSearchTypeAllPairs/** all pairs*/,
                FaceSearchTypeIdenticalPairsOnly/** identical pairs only*/
            };

            private: MMCCreateBuilderImpl * m_mmccreatebuilder_impl;
            private: friend class  _MMCCreateBuilderBuilder;
            protected: MMCCreateBuilder();
            public: ~MMCCreateBuilder();
            /**Returns  the bodies/faces used when @link NXOpen::CAE::MMCCreateBuilder::Type NXOpen::CAE::MMCCreateBuilder::Type@endlink  is set to @link NXOpen::CAE::MMCCreateBuilder::TypesAutoCreate NXOpen::CAE::MMCCreateBuilder::TypesAutoCreate@endlink .  
                        
             <br>  Created in NX6.0.5.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * AutoSelection
            (
            );
            /**Returns  the source face used when @link NXOpen::CAE::MMCCreateBuilder::Type NXOpen::CAE::MMCCreateBuilder::Type@endlink  is set to @link NXOpen::CAE::MMCCreateBuilder::TypesManual NXOpen::CAE::MMCCreateBuilder::TypesManual@endlink .  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectIParameterizedSurface * SourceFace
            (
            );
            /**Returns  the target face  used when @link NXOpen::CAE::MMCCreateBuilder::Type NXOpen::CAE::MMCCreateBuilder::Type@endlink  is set to @link NXOpen::CAE::MMCCreateBuilder::TypesManual NXOpen::CAE::MMCCreateBuilder::TypesManual@endlink .  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectIParameterizedSurface * TargetFace
            (
            );
            /**Returns  the mmc creation type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::MMCCreateBuilder::Types Type
            (
            );
            /**Sets  the mmc creation type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetType
            (
                NXOpen::CAE::MMCCreateBuilder::Types type /** type */ 
            );
            /**Returns  the mesh mating type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::MMCCreateBuilder::MeshMatingType MeshMatingOption
            (
            );
            /**Sets  the mesh mating type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMeshMatingOption
            (
                NXOpen::CAE::MMCCreateBuilder::MeshMatingType meshMatingOption /** meshmatingoption */ 
            );
            /**Returns  the face search option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::MMCCreateBuilder::FaceSearchType FaceSearchOption
            (
            );
            /**Sets  the face search option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetFaceSearchOption
            (
                NXOpen::CAE::MMCCreateBuilder::FaceSearchType faceSearchOption /** facesearchoption */ 
            );
            /**Returns  the dist tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DistTolerance
            (
            );
            /**Returns  the snap tolerance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SnapTolerance
            (
            );
            /**Returns  the reverse direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  the Mesh Mating Condition 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::MeshMate * Mmc
            (
            );
            /**Sets  the Mesh Mating Condition 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMmc
            (
                NXOpen::CAE::MeshMate * mmc /** mmc */ 
            );
            /** Commits the creation of the @link NXOpen::CAE::MeshMate NXOpen::CAE::MeshMate@endlink  objects
                        or Commits the changes made to the @link NXOpen::CAE::MeshMate NXOpen::CAE::MeshMate@endlink  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::CAE::MeshMate *> CommitMmcs
            (
            );
            /** Print MMC log on info window. Supersedes customer default. Call function before commit. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void PrintLogOnInfoWindow
            (
                bool fValue /** fvalue */ 
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