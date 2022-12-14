#ifndef NXOpen_MFG_AM_NESTER3D_HXX_INCLUDED
#define NXOpen_MFG_AM_NESTER3D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_AM_Nester3D.ja
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
#include <NXOpen/Mfg_AM_NestingStatus.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libmfgamopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mfg
    {
        namespace AM
        {
            class Nester3D;
        }
    }
    class Builder;
    namespace Mfg
    {
        namespace AM
        {
            class NestingStatus;
        }
    }
    namespace Mfg
    {
        namespace AM
        {
            class SelectPartList;
        }
    }
    namespace Mfg
    {
        namespace AM
        {
            class _Nester3DBuilder;
            class Nester3DImpl;
            /** Interface for AM Nesting Dialog Builder  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::Get3DNester  NXOpen::Mfg::AM::ApplicationManager::Get3DNester @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            Accuracy </term> <description> 
             
            1 (millimeters part), 1 (inches part) </description> </item> 

            <item><term> 
             
            BottomDistance </term> <description> 
             
            2.0 (millimeters part), 0.1 (inches part) </description> </item> 

            <item><term> 
             
            ConstraintType </term> <description> 
             
            FixedRotation </description> </item> 

            <item><term> 
             
            InterlockingType </term> <description> 
             
            AllowInterlocks </description> </item> 

            <item><term> 
             
            SolutionType </term> <description> 
             
            OptimizeHeight </description> </item> 

            <item><term> 
             
            Spacing </term> <description> 
             
            5.0 (millimeters part), 0.2 (inches part) </description> </item> 

            <item><term> 
             
            StartFromEmptyBuildtray </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            StopAfter </term> <description> 
             
            2 </description> </item> 

            <item><term> 
             
            TargetDensity </term> <description> 
             
            10.0 </description> </item> 

            <item><term> 
             
            ViewProgress </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            WallDistance </term> <description> 
             
            2.0 (millimeters part), 0.1 (inches part) </description> </item> 

            </list> 

             <br>  Created in NX11.0.1.  <br>  
            */
            class MFGAMOPENCPPEXPORT  Nester3D : public NXOpen::Builder
            {
                /** Interface for AM Nesting Dialog Builder */
                public: enum NesterType
                {
                    NesterTypeTwoD/** two d */ ,
                    NesterTypeThreeD/** three d */ 
                };

                /** Interface for AM Nesting Dialog Builder */
                public: enum Constraint
                {
                    ConstraintFree/** free */ ,
                    ConstraintFixedZDirection/** fixed zdirection */ ,
                    ConstraintFixedFloorPlane/** fixed floor plane */ ,
                    ConstraintRotate180/** rotate180 */ ,
                    ConstraintFixedBottomAndXY/** fixed bottom and xy */ ,
                    ConstraintFixedRotation/** fixed rotation */ ,
                    ConstraintFixed/** fixed */ 
                };

                /** Interface for AM Nesting Dialog Builder */
                public: enum Solution
                {
                    SolutionOptimizeHeight/** optimize height */ ,
                    SolutionDistributeHeight/** distribute height */ ,
                    SolutionOptimizeSliceVolume/** optimize slice volume */ ,
                    SolutionOptimizeHeightAndSliceVolume/** optimize height and slice volume */ 
                };

                /** Interface for AM Nesting Dialog Builder */
                public: enum Interlocking
                {
                    InterlockingAllowInterlocks/** allow interlocks */ ,
                    InterlockingAvoidTunnels/** avoid tunnels */ ,
                    InterlockingAvoidAllInterlocks/** avoid all interlocks */ 
                };

                private: Nester3DImpl * m_nester3d_impl;
                private: friend class  _Nester3DBuilder;
                protected: Nester3D();
                public: ~Nester3D();
                /**Returns  the spacing between parts 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: double Spacing
                (
                );
                /**Sets  the spacing between parts 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetSpacing
                (
                    double spacing /** spacing */ 
                );
                /**Returns  the spacing between parts 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: double WallDistance
                (
                );
                /**Sets  the spacing between parts 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetWallDistance
                (
                    double wallDistance /** walldistance */ 
                );
                /**Returns  the spacing between parts 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: double BottomDistance
                (
                );
                /**Sets  the spacing between parts 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetBottomDistance
                (
                    double bottomDistance /** bottomdistance */ 
                );
                /**Returns  the constraints 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::AM::Nester3D::Constraint ConstraintType
                (
                );
                /**Sets  the constraints 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetConstraintType
                (
                    NXOpen::Mfg::AM::Nester3D::Constraint constraint /** constraint */ 
                );
                /**Returns  the view progress 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: bool ViewProgress
                (
                );
                /**Sets  the view progress 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetViewProgress
                (
                    bool viewProgress /** viewprogress */ 
                );
                /**Returns  the StartFromEmptyBuildtray 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: bool StartFromEmptyBuildtray
                (
                );
                /**Sets  the StartFromEmptyBuildtray 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetStartFromEmptyBuildtray
                (
                    bool startFromEmptyBuildtray /** startfromemptybuildtray */ 
                );
                /**Returns  the solution type 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::AM::Nester3D::Solution SolutionType
                (
                );
                /**Sets  the solution type 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetSolutionType
                (
                    NXOpen::Mfg::AM::Nester3D::Solution solutionType /** solutiontype */ 
                );
                /**Returns  the solution type 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::AM::Nester3D::Interlocking InterlockingType
                (
                );
                /**Sets  the solution type 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetInterlockingType
                (
                    NXOpen::Mfg::AM::Nester3D::Interlocking interlockingType /** interlockingtype */ 
                );
                /**Returns  the accuracy 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: double Accuracy
                (
                );
                /**Sets  the accuracy 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetAccuracy
                (
                    double accuracy /** accuracy */ 
                );
                /**Returns  the targetDensity 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: double TargetDensity
                (
                );
                /**Sets  the targetDensity 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetTargetDensity
                (
                    double targetDensity /** targetdensity */ 
                );
                /**Returns  the stop after 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: int StopAfter
                (
                );
                /**Sets  the stop after 
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetStopAfter
                (
                    int stopAfter /** stopafter */ 
                );
                /** Execute the Nesting  @return  Nesting Status
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: NXOpen::Mfg::AM::NestingStatus * ExecuteNesting
                (
                );
                /**Returns  the nesting type 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::AM::Nester3D::NesterType NestingType
                (
                );
                /**Sets  the nesting type 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetNestingType
                (
                    NXOpen::Mfg::AM::Nester3D::NesterType nestingType /** nestingtype */ 
                );
                /**Returns  the parts to nest 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::AM::SelectPartList * PartsToNest
                (
                );
                /** Sets the (sub) nesting box 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetNesting
                (
                    double dLength /** dlength */ ,
                    double dWidth /** dwidth */ ,
                    double dHeight /** dheight */ 
                );
                /** Sets the (sub) nesting cylinder 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") */
                public: void SetNesting
                (
                    double dDiameter /** ddiameter */ ,
                    double dHeight /** dheight */ 
                );
            };
        }
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
