#ifndef NXOpen_MFG_AM_MOVEPARTBUILDER_HXX_INCLUDED
#define NXOpen_MFG_AM_MOVEPARTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_AM_MovePartBuilder.ja
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
#include <NXOpen/GeometricUtilities_ModlMotion.hxx>
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
            class MovePartBuilder;
        }
    }
    class Builder;
    namespace GeometricUtilities
    {
        class ModlMotion;
    }
    class SelectNXObjectList;
    namespace Mfg
    {
        namespace AM
        {
            class _MovePartBuilderBuilder;
            class MovePartBuilderImpl;
            /** Represents a @link Mfg::AM::MovePartBuilder Mfg::AM::MovePartBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::CreateMovePartBuilder  NXOpen::Mfg::AM::ApplicationManager::CreateMovePartBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            Divisions </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            MoveType </term> <description> 
             
            MoveOriginal </description> </item> 

            <item><term> 
             
            NumberOfCopies </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            TransformMotion.DeltaEnum </term> <description> 
             
            ReferenceWcsWorkPart </description> </item> 

            <item><term> 
             
            TransformMotion.DeltaXc.Value </term> <description> 
             
            0.0 </description> </item> 

            <item><term> 
             
            TransformMotion.DeltaYc.Value </term> <description> 
             
            0.0 </description> </item> 

            <item><term> 
             
            TransformMotion.DeltaZc.Value </term> <description> 
             
            0.0 </description> </item> 

            <item><term> 
             
            TransformMotion.Option </term> <description> 
             
            Dynamic </description> </item> 

            </list> 

             <br>  Created in NX1926.0.0.  <br>  
            */
            class MFGAMOPENCPPEXPORT  MovePartBuilder : public NXOpen::Builder
            {
                /** Indicates whether to move or copy objects */
                public: enum MoveTypeOption
                {
                    MoveTypeOptionMoveOriginal/** move part */,
                    MoveTypeOptionCopyOriginal/** copy part*/
                };

                private: MovePartBuilderImpl * m_movepartbuilder_impl;
                private: friend class  _MovePartBuilderBuilder;
                protected: MovePartBuilder();
                public: ~MovePartBuilder();
                /**Returns  the objects to move-rotate 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * ObjectToMoveObject
                (
                );
                /**Returns  the transform 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::ModlMotion * TransformMotion
                (
                );
                /**Returns  the move rotate result 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::AM::MovePartBuilder::MoveTypeOption MoveType
                (
                );
                /**Sets  the move rotate result 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application") */
                public: void SetMoveType
                (
                    NXOpen::Mfg::AM::MovePartBuilder::MoveTypeOption moveType /** movetype */ 
                );
                /**Returns  the distance or angle divisions 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: int Divisions
                (
                );
                /**Sets  the distance or angle divisions 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application") */
                public: void SetDivisions
                (
                    int distanceOrAngleDivisions /** distanceorangledivisions */ 
                );
                /**Returns  the number of copies 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: int NumberOfCopies
                (
                );
                /**Sets  the number of copies 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application") */
                public: void SetNumberOfCopies
                (
                    int numCopies /** numcopies */ 
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