#ifndef NXOpen_DIE_ROTORBUILDER_HXX_INCLUDED
#define NXOpen_DIE_ROTORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_RotorBuilder.ja
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
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class RotorBuilder;
    }
    class Body;
    class CartesianCoordinateSystem;
    namespace Die
    {
        class HoleParentBuilder;
    }
    namespace Die
    {
        class PadParentBuilder;
    }
    namespace Die
    {
        class RotorSectionBuilder;
    }
    namespace Die
    {
        class ThroatParentBuilder;
    }
    namespace Die
    {
        class WearPlateLocParentBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class IProfile;
    class IReferenceAxis;
    class ISurface;
    namespace Die
    {
        class _RotorBuilderBuilder;
        class RotorBuilderImpl;
        /** Represents a CAM Rotor feature builder.  <br> To create a new instance of this class, use @link Die::DieCollection::Rotor Die::DieCollection::Rotor@endlink  <br> */
        class NXOPENCPPEXPORT  RotorBuilder : public Features::FeatureBuilder
        {
            private: RotorBuilderImpl * m_rotorbuilder_impl;
            private: friend class  _RotorBuilderBuilder;
            protected: RotorBuilder();
            public: ~RotorBuilder();
            /**Sets  the rotor solid of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetRotorSolid
            (
                NXOpen::Body * rotorSolid /** rotor solid */ 
            );
            /**Returns  the rotor solid of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Body * RotorSolid
            (
            );
            /**Sets  the throat orientation of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetThroatOrientation
            (
                NXOpen::CartesianCoordinateSystem * throatOrientation /** throat orientation */ 
            );
            /**Returns  the throat orientation of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::CartesianCoordinateSystem * ThroatOrientation
            (
            );
            /**Sets  the press direction of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetPressDirection
            (
                NXOpen::IReferenceAxis * pressDirection /** press direction */ 
            );
            /**Returns  the press direction of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::IReferenceAxis * PressDirection
            (
            );
            /**Sets  the sheet metal of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSheetMetal
            (
                NXOpen::Body * sheetMetal /** sheet metal */ 
            );
            /**Returns  the sheet metal of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Body * SheetMetal
            (
            );
            /** Sets the flange bend profile of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetFlangeBendProfile
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the flange bend profile of the rotor casting.  @return  The profile entries, will be curves, edges, faces, sketches or curve features.  <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetFlangeBendProfile
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /** Sets the end of flange profile of the die rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetEndOfFlangeProfile
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the end of flange profile of the die rotor casting.  @return  The profile entries, will be curves, edges, faces, sketches or curve features.  <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetEndOfFlangeProfile
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /** Sets the start orientation of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetStartOrientation
            (
                const std::vector<NXOpen::ISurface *> & startEntries /** start entries */ 
            );
            /** Gets the start orientation of the rotor casting.  @return   <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::ISurface *> GetStartOrientation
            (
            );
            /** Sets the end orientation of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetEndOrientation
            (
                const std::vector<NXOpen::ISurface *> & endEntries /** end entries */ 
            );
            /** Gets the end orientation of the rotor casting.  @return   <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::ISurface *> GetEndOrientation
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetRotorRotationAngle
            (
                const NXString & degrees /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the rotor rotation angle value of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * RotorRotationAngle
            (
            );
            /**Sets  the display holes of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayHoles
            (
                bool displayHoles /** display holes */ 
            );
            /**Returns  the display holes of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayHoles
            (
            );
            /**Sets  the distance tolerance of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distance tolerance */ 
            );
            /**Returns  the distance tolerance of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double DistanceTolerance
            (
            );
            /**Sets  the angle tolerance of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angle tolerance */ 
            );
            /**Returns  the angle tolerance of the rotor casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double AngleTolerance
            (
            );
            /**Returns  the section builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::RotorSectionBuilder * Section
            (
            );
            /**Returns  the throat definition parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::ThroatParentBuilder * ThroatDefinitionParent
            (
            );
            /**Returns  the wear plate and locator parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::WearPlateLocParentBuilder * WearPlateLocatorsParent
            (
            );
            /**Returns  the air cylinder parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::PadParentBuilder * AirCylinderParent
            (
            );
            /**Returns  the sensor parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::PadParentBuilder * SensorParent
            (
            );
            /**Returns  the end stops parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::PadParentBuilder * EndStopsParent
            (
            );
            /**Returns  the setup blocks parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::PadParentBuilder * SetupBlocksParent
            (
            );
            /**Returns  the T-bar holes parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::HoleParentBuilder * TbarHoleParent
            (
            );
            /**Returns  the handling holes parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::HoleParentBuilder * HandlingHoleParent
            (
            );
            /**Returns  the dowel holes parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::HoleParentBuilder * DowelHoleParent
            (
            );
            /**Returns  the bolt holes parent builder of the rotor.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::HoleParentBuilder * BoltHoleParent
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif