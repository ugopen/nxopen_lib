#ifndef NXOpen_ANNOTATIONS_DRAFTINGSURFACEFINISHBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRAFTINGSURFACEFINISHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DraftingSurfaceFinishBuilder.ja
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
#include <NXOpen/Annotations_BaseSurfaceFinishBuilder.hxx>
#include <NXOpen/Annotations_DraftingSurfaceFinishBuilder.hxx>
#include <NXOpen/Annotations_BaseSurfaceFinishBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class DraftingSurfaceFinishBuilder;
    }
    namespace Annotations
    {
        class BaseSurfaceFinishBuilder;
    }
    namespace Annotations
    {
        class _DraftingSurfaceFinishBuilderBuilder;
        class DraftingSurfaceFinishBuilderImpl;
        /** Represents a @link Annotations::DraftingSurfaceFinish Annotations::DraftingSurfaceFinish@endlink  builder  <br> To create a new instance of this class, use @link Annotations::DraftingSurfaceFinishCollection::CreateDraftingSurfaceFinishBuilder Annotations::DraftingSurfaceFinishCollection::CreateDraftingSurfaceFinishBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  DraftingSurfaceFinishBuilder : public Annotations::BaseSurfaceFinishBuilder
        {
            /** the valid types of finish type*/
            public: enum FinishType
            {
                FinishTypeBasic/** Basic*/,
                FinishTypeModifier/** Modifier */,
                FinishTypeModifierAllAround/** Modifier, All Around*/,
                FinishTypeMaterialRemovalRequired/** Material Removal Required */,
                FinishTypeModifierMaterialRemovalRequired/** Modifier, Material Removal Required */,
                FinishTypeModifierMaterialRemovalRequiredAllAround/** Modifier, Material Removal Required, All Around*/,
                FinishTypeMaterialRemovalProhibited/** Material Removal Prohibited*/,
                FinishTypeModifierMaterialRemovalProhibited/** Modifier, Material Removal Prohibited*/,
                FinishTypeModifierMaterialRemovalProhibitedAllAround/** Modifier, Material Removal Prohibited, All Around*/
            };

            private: DraftingSurfaceFinishBuilderImpl * m_draftingsurfacefinishbuilder_impl;
            private: friend class  _DraftingSurfaceFinishBuilderBuilder;
            protected: DraftingSurfaceFinishBuilder();
            public: ~DraftingSurfaceFinishBuilder();
            /**Returns  the finish  <br> License requirements : None */
            public: NXOpen::Annotations::DraftingSurfaceFinishBuilder::FinishType Finish
            (
            );
            /**Sets  the finish  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFinish
            (
                NXOpen::Annotations::DraftingSurfaceFinishBuilder::FinishType finish /** finish */ 
            );
            /**Returns  the a1  <br> License requirements : None */
            public: NXString A1
            (
            );
            /**Sets  the a1  <br> License requirements : drafting ("DRAFTING") */
            public: void SetA1
            (
                const NXString & a1 /** a1 */ 
            );
            /**Returns  the a2  <br> License requirements : None */
            public: NXString A2
            (
            );
            /**Sets  the a2  <br> License requirements : drafting ("DRAFTING") */
            public: void SetA2
            (
                const NXString & a2 /** a2 */ 
            );
            /**Returns  the b  <br> License requirements : None */
            public: NXString B
            (
            );
            /**Sets  the b  <br> License requirements : drafting ("DRAFTING") */
            public: void SetB
            (
                const NXString & b /** b */ 
            );
            /**Returns  the c  <br> License requirements : None */
            public: NXString C
            (
            );
            /**Sets  the c  <br> License requirements : drafting ("DRAFTING") */
            public: void SetC
            (
                const NXString & c /** c */ 
            );
            /**Returns  the d  <br> License requirements : None */
            public: NXString D
            (
            );
            /**Sets  the d  <br> License requirements : drafting ("DRAFTING") */
            public: void SetD
            (
                const NXString & d /** d */ 
            );
            /**Returns  the e  <br> License requirements : None */
            public: NXString E
            (
            );
            /**Sets  the e  <br> License requirements : drafting ("DRAFTING") */
            public: void SetE
            (
                const NXString & e /** e */ 
            );
            /**Returns  the f1  <br> License requirements : None */
            public: NXString F1
            (
            );
            /**Sets  the f1  <br> License requirements : drafting ("DRAFTING") */
            public: void SetF1
            (
                const NXString & f1 /** f1 */ 
            );
            /**Returns  the f2  <br> License requirements : None */
            public: NXString F2
            (
            );
            /**Sets  the f2  <br> License requirements : drafting ("DRAFTING") */
            public: void SetF2
            (
                const NXString & f2 /** f2 */ 
            );
            /**Returns  the tolerance type applicable only for all the 3 cases of finish type where Material Removal Required <br> License requirements : None */
            public: NXOpen::Annotations::BaseSurfaceFinishBuilder::ToleranceOption ToleranceType
            (
            );
            /**Sets  the tolerance type applicable only for all the 3 cases of finish type where Material Removal Required <br> License requirements : drafting ("DRAFTING") */
            public: void SetToleranceType
            (
                NXOpen::Annotations::BaseSurfaceFinishBuilder::ToleranceOption toleranceType /** tolerancetype */ 
            );
            /**Returns  the tolerance in case of bilateral tolerance type otherwise upper tolerance  <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance in case of bilateral tolerance type otherwise upper tolerance  <br> License requirements : drafting ("DRAFTING") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the lower tolerance applicable for all the tolerance types other than Bilateral <br> License requirements : None */
            public: double LowerTolerance
            (
            );
            /**Sets  the lower tolerance applicable for all the tolerance types other than Bilateral <br> License requirements : drafting ("DRAFTING") */
            public: void SetLowerTolerance
            (
                double lowerTolerance /** lowertolerance */ 
            );
            /**Returns  the angle <br> License requirements : None */
            public: double Angle
            (
            );
            /**Sets  the angle <br> License requirements : drafting ("DRAFTING") */
            public: void SetAngle
            (
                double angle /** angle */ 
            );
            /**Returns  the invert Text  <br> License requirements : None */
            public: bool InvertText
            (
            );
            /**Sets  the invert Text  <br> License requirements : drafting ("DRAFTING") */
            public: void SetInvertText
            (
                bool invertText /** inverttext */ 
            );
            /**Returns  the parantheses  <br> License requirements : None */
            public: NXOpen::Annotations::BaseSurfaceFinishBuilder::ParanthesesType Parantheses
            (
            );
            /**Sets  the parantheses  <br> License requirements : drafting ("DRAFTING") */
            public: void SetParantheses
            (
                NXOpen::Annotations::BaseSurfaceFinishBuilder::ParanthesesType paranthesesType /** paranthesestype */ 
            );
            /**Returns  the invert symbol  <br> License requirements : None */
            public: bool InvertSymbol
            (
            );
            /**Sets  the invert symbol  <br> License requirements : drafting ("DRAFTING") */
            public: void SetInvertSymbol
            (
                bool invertSymbol /** invertsymbol */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif