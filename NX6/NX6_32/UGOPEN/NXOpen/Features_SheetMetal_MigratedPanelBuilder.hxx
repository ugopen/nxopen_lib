#ifndef NXOpen_FEATURES_SHEETMETAL_MIGRATEDPANELBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_MIGRATEDPANELBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_MigratedPanelBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_SheetMetal_BendOptions.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class MigratedPanelBuilder;
        }
    }
    class Body;
    class ExpressionCollectorSet;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BendOptions;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class _MigratedPanelBuilderBuilder;
            /**
                    Represents an I-DEAS Migrated Panel feature builder
                 <br> This builder cannot be instantiated separately. <br> */
            class NXOPENCPPEXPORT MigratedPanelBuilder : public Features::FeatureBuilder
            {
                private: friend class  _MigratedPanelBuilderBuilder;
                protected: MigratedPanelBuilder();
                /**Returns 
                          the parent stationary face.  This face cannot be NULL.

                           <br> 
                              The set method is only available inside the I-DEAS to NX Content Migration Manager.
                           <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Face * StationaryFace
                (
                );
                /**Sets 
                          the parent stationary face.  This face cannot be NULL.

                           <br> 
                              The set method is only available inside the I-DEAS to NX Content Migration Manager.
                           <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetStationaryFace
                (
                    NXOpen::Face * stationaryFace /** The stationary face */
                );
                /**Returns 
                          the parent bend face.  This face will usually be NULL.  It will
                          be non-NULL if this Migrated Panel was defined using the BFCS
                          (Bend From Cylindrical Surface) method.

                       <br> 
                          The set method is only available inside the I-DEAS to NX Content Migration Manager.
                       <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Face * BendFace
                (
                );
                /**Sets 
                          the parent bend face.  This face will usually be NULL.  It will
                          be non-NULL if this Migrated Panel was defined using the BFCS
                          (Bend From Cylindrical Surface) method.

                       <br> 
                          The set method is only available inside the I-DEAS to NX Content Migration Manager.
                       <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBendFace
                (
                    NXOpen::Face * bendFace /** The bend face */
                );
                /**Returns 
                          the parent moving face.  This face will be NULL for the ground panel.
                          If non-NULL, the face must be planar.
                       <br> 
                          The set method is only available inside the I-DEAS to NX Content Migration Manager.
                       <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Face * MovingFace
                (
                );
                /**Sets 
                          the parent moving face.  This face will be NULL for the ground panel.
                          If non-NULL, the face must be planar.
                       <br> 
                          The set method is only available inside the I-DEAS to NX Content Migration Manager.
                       <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetMovingFace
                (
                    NXOpen::Face * moveFace /** The moving face */
                );
                /**Returns 
                          the parent sheet metal body.  The Migrated Panel is applied to this
                          body.  The body must be made up of other Migrated Panel features. This
                          body will be NULL for the ground panel.
                       <br> 
                          The set method is only available inside the I-DEAS to NX Content Migration Manager.
                       <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Body * ParentSmBody
                (
                );
                /**Sets 
                          the parent sheet metal body.  The Migrated Panel is applied to this
                          body.  The body must be made up of other Migrated Panel features. This
                          body will be NULL for the ground panel.
                       <br> 
                          The set method is only available inside the I-DEAS to NX Content Migration Manager.
                       <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetParentSmBody
                (
                    NXOpen::Body * sheetMetalBody /** Parent Sheet Metal Body */
                );
                /**Returns 
                         the bend radius expression.
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXString BendRadius
                (
                );
                /**Sets 
                         the bend radius expression.
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBendRadius
                (
                    const NXString & bendRadius /** Gap tolerance */
                );
                /**Returns 
                          the neutral offset (i.e., K Factor) expression.
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXString NeutralOffset
                (
                );
                /**Sets 
                          the neutral offset (i.e., K Factor) expression.
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetNeutralOffset
                (
                    const NXString & gapTolerance /** Gap tolerance */
                );
                /**Returns 
                          the gap tolerance expression.  This is the size of the gap introduced
                          between this panel and neighboring features.
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXString GapTolerance
                (
                );
                /**Sets 
                          the gap tolerance expression.  This is the size of the gap introduced
                          between this panel and neighboring features.
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetGapTolerance
                (
                    const NXString & gapTolerance /** Gap tolerance */
                );
                /**Returns 
                          the cutoff angle expression.
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXString CutoffAngle
                (
                );
                /**Sets 
                          the cutoff angle expression.
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetCutoffAngle
                (
                    const NXString & cutoffAngle /** Cutoff angle */
                );
                /**Returns 
                         the along face normal flag. This value only has meaning
                         for the ground panel.
                          <br> 
                          The edge that defines an end condition must be linear and must be on the
                          stationary face for the Ground Panel and the moving face for other panels.
                          The index indicates the position of the End Condition that will be
                          modified.  The first End Condition has an index of zero.
                          <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: bool AlongFaceNormal
                (
                );
                /**Sets 
                         the along face normal flag. This value only has meaning
                         for the ground panel.
                          <br> 
                          The edge that defines an end condition must be linear and must be on the
                          stationary face for the Ground Panel and the moving face for other panels.
                          The index indicates the position of the End Condition that will be
                          modified.  The first End Condition has an index of zero.
                          <br> 
                       <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetAlongFaceNormal
                (
                    bool alongFaceNormal /** Along Face Normal flag */
                );
                /**Returns  the end conditions  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::ExpressionCollectorSet * EndConditions
                (
                );
                /**Returns  the bend options for the panel feature.
                     <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BendOptions * BendOptions
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif