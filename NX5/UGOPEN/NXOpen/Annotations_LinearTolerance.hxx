#ifndef NXOpen_ANNOTATIONS_LINEARTOLERANCE_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_LINEARTOLERANCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_LinearTolerance.ja
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
#include <NXOpen/Annotations.hxx>
#include <NXOpen/Dimensions.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class LinearTolerance;
    }
    class Expression;
    namespace Annotations
    {
    }
    namespace Annotations
    {
        /** Represents linear tolerance */
        class NXOPENCPPEXPORT LinearTolerance : public TransientObject
        {
            public: explicit LinearTolerance(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~LinearTolerance();
            /**Returns  the tolerance type  <br> License requirements : None */
            public: NXOpen::Annotations::ToleranceType ToleranceType
            (
            );
            /**Sets  the tolerance type  <br> License requirements : None */
            public: void SetToleranceType
            (
                NXOpen::Annotations::ToleranceType type /** New tolerance type */
            );
            /** Returns the upper tolerance in inches  @return  Upper tolerance in inches  <br> License requirements : None */
            public: NXOpen::Annotations::Value GetUpperToleranceInches
            (
            );
            /** Sets the upper tolerance in inches  <br> License requirements : None */
            public: void SetUpperToleranceInches
            (
                const NXOpen::Annotations::Value & upper_tolerance_inches /**  New upper tolerance in inches */
            );
            /** Returns the lower tolerance value in inches  @return  Lower tolerance in inches  <br> License requirements : None */
            public: NXOpen::Annotations::Value GetLowerToleranceInches
            (
            );
            /** Sets the lower tolerance value in inches  <br> License requirements : None */
            public: void SetLowerToleranceInches
            (
                const NXOpen::Annotations::Value & lower_tolerance_inches /** New lower tolerance in inches */
            );
            /** Returns the upper tolerance in millimeters(MM)  @return  Upper tolerance in millimeters  <br> License requirements : None */
            public: NXOpen::Annotations::Value GetUpperToleranceMm
            (
            );
            /** Sets the upper tolerance in millimeters(MM)  <br> License requirements : None */
            public: void SetUpperToleranceMm
            (
                const NXOpen::Annotations::Value & upper_tolerance_mm /** New upper tolerance in millimeters */
            );
            /** Returns the lower tolerance in millimeters(MM)  @return  Lower tolerance in millimeters  <br> License requirements : None */
            public: NXOpen::Annotations::Value GetLowerToleranceMm
            (
            );
            /** Sets the lower tolerance in millimeters(MM)  <br> License requirements : None */
            public: void SetLowerToleranceMm
            (
                const NXOpen::Annotations::Value & lower_tolerance_mm /** New lower tolerance in millimeters */
            );
            /**Returns  the number of decimal places for primary dimension  <br> License requirements : None */
            public: int PrimaryDimensionDecimalPlaces
            (
            );
            /**Sets  the number of decimal places for primary dimension  <br> License requirements : None */
            public: void SetPrimaryDimensionDecimalPlaces
            (
                int primary_dimension_decimal_places /** New number of primary dimension decimal places */
            );
            /**Returns  the number of decimal places for dual dimension  <br> License requirements : None */
            public: int DualDimensionDecimalPlaces
            (
            );
            /**Sets  the number of decimal places for dual dimension  <br> License requirements : None */
            public: void SetDualDimensionDecimalPlaces
            (
                int dual_dimension_decimal_places /** New number of dual dimension decimal places */
            );
            /**Returns  the number of decimal places for dual tolerance  <br> License requirements : None */
            public: int DualToleranceDecimalPlaces
            (
            );
            /**Sets  the number of decimal places for dual tolerance  <br> License requirements : None */
            public: void SetDualToleranceDecimalPlaces
            (
                int dual_tolerance_decimal_places /** New number of dual tolerance decimal places */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
