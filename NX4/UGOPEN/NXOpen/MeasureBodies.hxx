#ifndef NXOpen_MEASUREBODIES_HXX_INCLUDED
#define NXOpen_MEASUREBODIES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MeasureBodies.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/GenericMeasure.hxx>
#include <NXOpen/MeasureManager.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class MeasureBodies;
    class GenericMeasure;
    class Measure;
    /** Represents the measurement specific mass properties for a set of bodies */
    class NXOPENCPPEXPORT MeasureBodies : public GenericMeasure
    {
        /** Indicates the type of embedded measurement to create */
        public: enum ActiveValue
        {
            ActiveValueVolume/** */,
            ActiveValueArea/** */,
            ActiveValueMass/** */,
            ActiveValueRadiusOfGyration/** */,
            ActiveValueWeight/** */,
            ActiveValueCentroid/** */
        };

        /** Indicates the family of units used in mass property information listings */
        public: enum AnalysisUnit
        {
            AnalysisUnitPoundInch/** */,
            AnalysisUnitPoundFoot/** */,
            AnalysisUnitGramMillimeter/** */,
            AnalysisUnitGramCentimeter/** */,
            AnalysisUnitKilogramMeter/** */,
            AnalysisUnitCustomUnit/** */
        };

        public: explicit MeasureBodies(void *ptr);
        /**Returns  the family of units for mass properties in the information window  <br> License requirements : None */
        public: NXOpen::MeasureBodies::AnalysisUnit InformationUnit
        (
        );
        /**Sets  the family of units for mass properties in the information window  <br> License requirements : None */
        public: void SetInformationUnit
        (
            NXOpen::MeasureBodies::AnalysisUnit unit_value /** */
        );
        /**Returns  the value for volume of the measurement  <br> License requirements : None */
        public: double Volume
        (
        );
        /**Returns  the value for area of the measurement  <br> License requirements : None */
        public: double Area
        (
        );
        /**Returns  the value for mass of the measurement  <br> License requirements : None */
        public: double Mass
        (
        );
        /**Returns  the value for radius of gyration of the measurement  <br> License requirements : None */
        public: double RadiusOfGyration
        (
        );
        /**Returns  the value for weight of the measurement  <br> License requirements : None */
        public: double Weight
        (
        );
        /**Returns  the centroid point of the measurement  <br> License requirements : None */
        public: NXOpen::Point3d Centroid
        (
        );
        /** Creates and returns a measurement feature  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::Measure * CreateFeature
        (
        );
        /** Creates and returns an embedded measurement expression  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXString CreateEmbedded
        (
            NXOpen::MeasureBodies::ActiveValue measurement_type /** */
        );
    };
}
#undef EXPORTLIBRARY
#endif
