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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
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
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

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
    class Direction;
    class INXObject;
    class View;
    namespace Annotations
    {
        class _DimensionBuilder;
        class DimensionImpl;
        /** Represents a dimension  <br> Abstract class  <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  Dimension : public Annotations::Annotation, public virtual Annotations::IAppendedText
        {
            private: DimensionImpl * m_dimension_impl;
            private: friend class  _DimensionBuilder;
            protected: Dimension();
            public: ~Dimension();
            /** Returns the dimension preferences  @return  Dimenension preferences 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DimensionPreferences * GetDimensionPreferences
            (
            );
            /** Sets the dimension preferences 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDimensionPreferences
            (
                NXOpen::Annotations::DimensionPreferences * preferences /** New dimension preferences */
            );
            /**Sets  a flag indicating whether the dimension text is centered
                    equally between the extension lines.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetOriginCentered
            (
                bool isOriginCentered /** is origin centered */ 
            );
            /**Returns  a flag indicating whether the dimension text is centered
                    equally between the extension lines.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsOriginCentered
            (
            );
            /** Sets the narrow dimension text offset for the given chain dimension. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetNarrowDimensionTextOffset
            (
                double narrowTextOffset /** narrow text offset */ 
            );
            /** Returns the narrow dimension text offset for the given chain dimension.  @return   
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double GetNarrowDimensionTextOffset
            (
            );
            /** Sets the narrow dimension preferences to the given linear dimension. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetNarrowDimensionPreferences
            (
                const NXOpen::Annotations::NarrowDimensionData & narrowDimensionData /** New narrow dimension preferences */
            );
            /** Returns the narrow dimension preferences for the given linear dimension.  @return  Narrow dimension preferences 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::NarrowDimensionData GetNarrowDimensionPreferences
            (
            );
            /** Returns the first associativity data.  @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::Associativity * GetFirstAssociativity
            (
            );
            /** Sets the first associativity data. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFirstAssociativity
            (
                NXOpen::Annotations::Associativity * newAssociativity /** new associativity */ 
            );
            /** Returns the second associativity data.  @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::Associativity * GetSecondAssociativity
            (
            );
            /** Sets the second associativity data. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSecondAssociativity
            (
                NXOpen::Annotations::Associativity * newAssociativity /** new associativity */ 
            );
            /**Sets  a setting to control the tolerance display style.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetToleranceType
            (
                NXOpen::Annotations::ToleranceType toleranceType /** tolerance type */ 
            );
            /**Returns  a setting to control the tolerance display style.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ToleranceType ToleranceType
            (
            );
            /**Sets  a setting to control the visibility of the reference parenthesis of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetReferenceDimensionFlag
            (
                bool referenceDimensionFlag /** reference dimension flag */ 
            );
            /**Returns  a setting to control the visibility of the reference parenthesis of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReferenceDimensionFlag
            (
            );
            /**Sets  a setting to control the inspection box displayed around the dimension value.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetInspectionDimensionFlag
            (
                bool inspectionDimensionFlag /** inspection dimension flag */ 
            );
            /**Returns  a setting to control the inspection box displayed around the dimension value.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool InspectionDimensionFlag
            (
            );
            /**Returns  the computed size of the dimension. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double ComputedSize
            (
            );
            /** 
             <br>  @deprecated Deprecated in NX8.0.0.  Use @link Annotations::Dimension::SetDimensionText Annotations::Dimension::SetDimensionText@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use Annotations::Dimension::SetDimensionText instead.") void SetComputedSize
            (
                double computedSize /** computed size */ 
            );
            /**Sets  a setting to control the number of decimal places for the primary tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetToleranceDecimalPlaces
            (
                int decimalPlaces /** decimal places */ 
            );
            /**Returns  a setting to control the number of decimal places for the primary tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int ToleranceDecimalPlaces
            (
            );
            /**Sets  a setting to control the number of decimal places for the metric tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetMetricToleranceDecimalPlaces
            (
                int decimalPlaces /** decimal places */ 
            );
            /**Returns  a setting to control the number of decimal places for the metric tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int MetricToleranceDecimalPlaces
            (
            );
            /**Sets  a setting to control the upper tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetUpperToleranceValue
            (
                double upperToleranceValue /** upper tolerance value */ 
            );
            /**Returns  a setting to control the upper tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double UpperToleranceValue
            (
            );
            /**Sets  a setting to control the metric upper tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetUpperMetricToleranceValue
            (
                double toleranceValue /** tolerance value */ 
            );
            /**Returns  a setting to control the metric upper tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double UpperMetricToleranceValue
            (
            );
            /**Sets  a setting to control the lower tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLowerToleranceValue
            (
                double upperToleranceValue /** upper tolerance value */ 
            );
            /**Returns  a setting to control the lower tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double LowerToleranceValue
            (
            );
            /**Sets  a setting to control the metric lower tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLowerMetricToleranceValue
            (
                double toleranceValue /** tolerance value */ 
            );
            /**Returns  a setting to control the metric lower tolerance value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double LowerMetricToleranceValue
            (
            );
            /**Sets  a setting to control the number of decimal places for the nominal value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetNominalDecimalPlaces
            (
                int decimalPlaces /** decimal places */ 
            );
            /**Returns  a setting to control the number of decimal places for the nominal value of a dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int NominalDecimalPlaces
            (
            );
            /**Sets  a setting to control the number of decimal places for the nominal value of a metric dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetMetricNominalDecimalPlaces
            (
                int decimalPlaces /** decimal places */ 
            );
            /**Returns  a setting to control the number of decimal places for the nominal value of a metric dimension.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int MetricNominalDecimalPlaces
            (
            );
            /** Determines if a dimension is driving. A driving dimension is a dimension that is used to constrain
                        geometry created by the sketcher on a drawing. A driving dimension is also referred to as 
                        a sketch dimension.  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsDriving
            (
            );
            /**  Set the main dimension text. 
                         For a dual dimension, the dual dimension text is determined from the main dimension text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDimensionText
            (
                std::vector<NXString> & mainTextLines /** List of main text lines */
            );
            /** Returns the dimension text - both the main text and the dual text. The returned 
                        text may contain just the computed dimension value or manual text including
                        the control characters.        
                         <br> 
                        Note that the text doesn't contain the tolerance text, appended text or text for 
                        flags like inspection/reference. 
                         <br> 
                    
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void GetDimensionText
            (
                std::vector<NXString> & mainTextLines /** List of main text lines */,
                std::vector<NXString> & dualTextLines /** List of dual text lines */
            );
            /**Sets  the measurement direction.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetMeasurementDirection
            (
                NXOpen::Direction * direction /** Direction Object*/
            );
            /**Returns  the measurement direction.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * MeasurementDirection
            (
            );
            /**Sets  the measurement direction view.
                        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetMeasurementDirectionView
            (
                NXOpen::View * view /** View Object*/
            );
            /**Returns  the measurement direction view.
                        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::View * MeasurementDirectionView
            (
            );
            /**Returns  the tolerance limit fit deviation.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString LimitFitDeviation
            (
            );
            /**Sets  the tolerance limit fit deviation.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLimitFitDeviation
            (
                const NXString & fitDeviation /** New limit fit deviation */
            );
            /**Sets  the tolerance limit fit deviation.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            void SetLimitFitDeviation
            (
                const char * fitDeviation /** New limit fit deviation */
            );
            /**Returns  the tolerance limit fit grade.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int LimitFitGrade
            (
            );
            /**Sets  the tolerance limit fit grade.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLimitFitGrade
            (
                int fitGrade /** New limit fit grade */
            );
            /**Returns  the deviation for limit fit representation of shaft tolerance

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString LimitFitShaftDeviation
            (
            );
            /**Sets  the deviation for limit fit representation of shaft tolerance

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLimitFitShaftDeviation
            (
                const NXString & fitShaftDeviation /** New limit fit shaft deviation */
            );
            /**Sets  the deviation for limit fit representation of shaft tolerance

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            void SetLimitFitShaftDeviation
            (
                const char * fitShaftDeviation /** New limit fit shaft deviation */
            );
            /**Returns  the grade for limit fit representation of shaft tolerance

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int LimitFitShaftGrade
            (
            );
            /**Sets  the grade for limit fit representation of shaft tolerance

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLimitFitShaftGrade
            (
                int fitShaftGrade /** New limit fit shaft grade */
            );
            /**Returns  the enhanced limit fit display type.  Used to determine if the tolerance representation is for
                        hole, shaft, or fit tolerance (fit meaning both hole and shaft tolerances are displayed).

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::FitAnsiHoleType LimitFitEnhancedDisplayType
            (
            );
            /**Sets  the enhanced limit fit display type.  Used to determine if the tolerance representation is for
                        hole, shaft, or fit tolerance (fit meaning both hole and shaft tolerances are displayed).

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLimitFitEnhancedDisplayType
            (
                NXOpen::Annotations::FitAnsiHoleType fitEnhancedDisplayType /** New limit fit enhanced tolerance display style */
            );
            /**Returns  the tolerance limit fit display style.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::FitDisplayStyle LimitFitDisplayStyle
            (
            );
            /**Sets  the tolerance limit fit display style.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLimitFitDisplayStyle
            (
                NXOpen::Annotations::FitDisplayStyle fitDisplayStyle /** New limit fit tolerance display style */
            );
            /**Returns  the tolerance limit fit ANSI hole type.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::FitAnsiHoleType LimitFitAnsiHoleType
            (
            );
            /**Sets  the tolerance limit fit ANSI hole type.

                        NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLimitFitAnsiHoleType
            (
                NXOpen::Annotations::FitAnsiHoleType fitHoleType /** New limit fit ansi hole type */
            );
            /** Returns whether or not the given dimension is approximate. A dimension is approximate if
                        it is attached to lightweight view geometry that doesn't have exact data.  @return  TRUE, if dimension is approximate. 
                                                              FALSE, if dimension is not approximate.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsApproximate
            (
            );
            /** Returns the appended text  @return  Appended text 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::Annotations::AppendedText * GetAppendedText
            (
            );
            /** Sets the appended text 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetAppendedText
            (
                NXOpen::Annotations::AppendedText * appendedText /** Appended text */
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