#ifndef NXOpen_FEATURES_CHANGESHELLTHICKNESSBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_CHANGESHELLTHICKNESSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ChangeShellThicknessBuilder.ja
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
#include <NXOpen/Features_FaceRecognitionBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class ChangeShellThicknessBuilder;
    }
    class Expression;
    namespace Features
    {
        class FaceRecognitionBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class NXObject;
    namespace Features
    {
        class _ChangeShellThicknessBuilderBuilder;
        class ChangeShellThicknessBuilderImpl;
        /** Represents a @link NXOpen::Features::ChangeShellThickness NXOpen::Features::ChangeShellThickness@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateChangeShellThicknessBuilder  NXOpen::Features::FeatureCollection::CreateChangeShellThicknessBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        FacesToChangeThickness.CoaxialEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.CoplanarAxesEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.CoplanarEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.EqualDiameterEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.OffsetEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.ParallelEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.PerpendicularEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.SameOrbitEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.SymmetricEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.TangentEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.ThicknessChainEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FacesToChangeThickness.UseFaceBrowse </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        NeighborsEnabled </term> <description> 
         
        True </description> </item> 

        <item><term> 
         
        WallThickness.Value </term> <description> 
         
        5.0 (millimeters part), 0.5 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  ChangeShellThicknessBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: ChangeShellThicknessBuilderImpl * m_changeshellthicknessbuilder_impl;
            private: friend class  _ChangeShellThicknessBuilderBuilder;
            protected: ChangeShellThicknessBuilder();
            public: ~ChangeShellThicknessBuilder();
            /**Returns  the faces to be selected to change thickness 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::FaceRecognitionBuilder * FacesToChangeThickness
            (
            );
            /**Returns  the flag to select neighbor faces that have the same wall thickness value as the face selected. 
                        If true, neighbor faces with same wall thickness value as the face selected will be included automatically. 
                    
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool NeighborsEnabled
            (
            );
            /**Sets  the flag to select neighbor faces that have the same wall thickness value as the face selected. 
                        If true, neighbor faces with same wall thickness value as the face selected will be included automatically. 
                    
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNeighborsEnabled
            (
                bool selectNeighbors /** selectneighbors */ 
            );
            /**Returns  the wall thickness 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallThickness
            (
            );
            /** Adds entities which have same wall thickness value as the selected face 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void AddEntities
            (
                const std::vector<NXOpen::NXObject *> & entities /** Objects to add */
            );
            /** Removes entities 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void RemoveEntities
            (
                const std::vector<NXOpen::NXObject *> & entities /** Objects to remove */
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