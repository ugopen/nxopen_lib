#ifndef NXOpen_GEOMETRICUTILITIES_CURVEEXTENDDATA_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_CURVEEXTENDDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_CurveExtendData.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_CurveExtendData.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class CurveExtendData;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class SelectDisplayableObject;
    namespace GeometricUtilities
    {
        class _CurveExtendDataBuilder;
        /** Represents a @link GeometricUtilities::CurveExtendData GeometricUtilities::CurveExtendData@endlink  */
        class NXOPENCPPEXPORT CurveExtendData : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** Represents the curve extend options for associative basic curves*/
            public: enum LimitOptions
            {
                LimitOptionsValue/** Value */,
                LimitOptionsAtPoint/** At Point */,
                LimitOptionsUntilSelected/** Until Selected */
            };

            private: friend class  _CurveExtendDataBuilder;
            protected: CurveExtendData();
            /**Returns  the limit option  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveExtendData::LimitOptions LimitOption
            (
            );
            /**Sets  the limit option  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetLimitOption
            (
                NXOpen::GeometricUtilities::CurveExtendData::LimitOptions limitOption /** limitoption */ 
            );
            /**Returns  the distance  <br> License requirements : None */
            public: NXOpen::Expression * Distance
            (
            );
            /**Returns  the until selected object  <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * UntilSelectedObject
            (
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
