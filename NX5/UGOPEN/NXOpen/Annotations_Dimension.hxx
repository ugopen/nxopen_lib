#ifndef NXOpen_ANNOTATIONS_DIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_Dimension.ja
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
#include <NXOpen/Annotations_Annotation.hxx>
#include <NXOpen/Annotations_IAppendedText.hxx>
#include <NXOpen/Annotations_AppendedText.hxx>
#include <NXOpen/Annotations_Associativity.hxx>
#include <NXOpen/Annotations_DimensionPreferences.hxx>
#include <NXOpen/Dimensions.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class Dimension;
    }
    namespace Annotations
    {
        class Annotation;
    }
    namespace Annotations
    {
        class AppendedText;
    }
    namespace Annotations
    {
        class Associativity;
    }
    namespace Annotations
    {
        class DimensionPreferences;
    }
    namespace Annotations
    {
        class IAppendedText;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _DimensionBuilder;
        /** Represents a dimension  <br> Abstract class <br> */
        class NXOPENCPPEXPORT Dimension : public Annotations::Annotation, public virtual Annotations::IAppendedText
        {
            private: friend class  _DimensionBuilder;
            protected: Dimension();
            /** Returns the dimension preferences  @return  Dimenension preferences  <br> License requirements : None */
            public: NXOpen::Annotations::DimensionPreferences * GetDimensionPreferences
            (
            );
            /** Sets the dimension preferences  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDimensionPreferences
            (
                NXOpen::Annotations::DimensionPreferences * preferences /** New dimension preferences */
            );
            /**Sets  a flag indicating whether the dimension text is centered
            	    equally between the extension lines.
                     <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetOriginCentered
            (
                bool is_origin_centered /** is origin centered */ 
            );
            /**Returns  a flag indicating whether the dimension text is centered
            	    equally between the extension lines.
                     <br> License requirements : None */
            public: bool IsOriginCentered
            (
            );
            /** Sets the narrow dimension text offset for the given chain dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetNarrowDimensionTextOffset
            (
                double narrow_text_offset /** narrow text offset */ 
            );
            /** Returns the narrow dimension text offset for the given chain dimension.  @return    <br> License requirements : None */
            public: double GetNarrowDimensionTextOffset
            (
            );
            /** Sets the narrow dimension preferences to the given linear dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetNarrowDimensionPreferences
            (
                const NXOpen::Annotations::NarrowDimensionData & narrow_dimension_data /** New narrow dimension preferences */
            );
            /** Returns the narrow dimension preferences for the given linear dimension.  @return  Narrow dimension preferences  <br> License requirements : None */
            public: NXOpen::Annotations::NarrowDimensionData GetNarrowDimensionPreferences
            (
            );
            /**Sets  a setting to control the tolerance display style.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetToleranceType
            (
                NXOpen::Annotations::ToleranceType tolerance_type /** tolerance type */ 
            );
            /**Returns  a setting to control the tolerance display style.  <br> License requirements : None */
            public: NXOpen::Annotations::ToleranceType ToleranceType
            (
            );
            /**Sets  a setting to control the visibility of the reference parenthesis of a dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetReferenceDimensionFlag
            (
                bool reference_dimension_flag /** reference dimension flag */ 
            );
            /**Returns  a setting to control the visibility of the reference parenthesis of a dimension.  <br> License requirements : None */
            public: bool ReferenceDimensionFlag
            (
            );
            /**Sets  a setting to control the inspection box displayed around the dimension value.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetInspectionDimensionFlag
            (
                bool inspection_dimension_flag /** inspection dimension flag */ 
            );
            /**Returns  a setting to control the inspection box displayed around the dimension value.  <br> License requirements : None */
            public: bool InspectionDimensionFlag
            (
            );
            /**Returns  the computed size of the dimension.  <br> License requirements : None */
            public: double ComputedSize
            (
            );
            /**Sets  the computed size of the dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetComputedSize
            (
                double computed_size /** computed size */ 
            );
            /**Sets  a setting to control the number of decimal places for the primary tolerance value of a dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetToleranceDecimalPlaces
            (
                int decimal_places /** decimal places */ 
            );
            /**Returns  a setting to control the number of decimal places for the primary tolerance value of a dimension.  <br> License requirements : None */
            public: int ToleranceDecimalPlaces
            (
            );
            /**Sets  a setting to control the number of decimal places for the metric tolerance value of a dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetMetricToleranceDecimalPlaces
            (
                int decimal_places /** decimal places */ 
            );
            /**Returns  a setting to control the number of decimal places for the metric tolerance value of a dimension.  <br> License requirements : None */
            public: int MetricToleranceDecimalPlaces
            (
            );
            /**Sets  a setting to control the upper tolerance value of a dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetUpperToleranceValue
            (
                double upper_tolerance_value /** upper tolerance value */ 
            );
            /**Returns  a setting to control the upper tolerance value of a dimension.  <br> License requirements : None */
            public: double UpperToleranceValue
            (
            );
            /**Sets  a setting to control the metric upper tolerance value of a dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetUpperMetricToleranceValue
            (
                double tolerance_value /** tolerance value */ 
            );
            /**Returns  a setting to control the metric upper tolerance value of a dimension.  <br> License requirements : None */
            public: double UpperMetricToleranceValue
            (
            );
            /**Sets  a setting to control the lower tolerance value of a dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLowerToleranceValue
            (
                double upper_tolerance_value /** upper tolerance value */ 
            );
            /**Returns  a setting to control the lower tolerance value of a dimension.  <br> License requirements : None */
            public: double LowerToleranceValue
            (
            );
            /**Sets  a setting to control the metric lower tolerance value of a dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLowerMetricToleranceValue
            (
                double tolerance_value /** tolerance value */ 
            );
            /**Returns  a setting to control the metric lower tolerance value of a dimension.  <br> License requirements : None */
            public: double LowerMetricToleranceValue
            (
            );
            /**Sets  a setting to control the number of decimal places for the nominal value of a dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetNominalDecimalPlaces
            (
                int decimal_places /** decimal places */ 
            );
            /**Returns  a setting to control the number of decimal places for the nominal value of a dimension.  <br> License requirements : None */
            public: int NominalDecimalPlaces
            (
            );
            /**Sets  a setting to control the number of decimal places for the nominal value of a metric dimension.  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetMetricNominalDecimalPlaces
            (
                int decimal_places /** decimal places */ 
            );
            /**Returns  a setting to control the number of decimal places for the nominal value of a metric dimension.  <br> License requirements : None */
            public: int MetricNominalDecimalPlaces
            (
            );
            /** Returns the appended text  @return  Appended text  <br> License requirements : None */
            public: virtual NXOpen::Annotations::AppendedText * GetAppendedText
            (
            );
            /** Sets the appended text  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetAppendedText
            (
                NXOpen::Annotations::AppendedText * appended_text /** Appended text */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif