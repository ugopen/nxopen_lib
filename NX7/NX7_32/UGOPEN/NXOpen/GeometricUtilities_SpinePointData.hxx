#ifndef NXOpen_GEOMETRICUTILITIES_SPINEPOINTDATA_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_SPINEPOINTDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_SpinePointData.ja
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
#include <NXOpen/GeometricUtilities_SpinePointData.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class SpinePointData;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Section;
    namespace GeometricUtilities
    {
        class _SpinePointDataBuilder;
        /** Represents a spine point def object
             <br> To create an instance of this class, see @link GeometricUtilities::SpinePointDataCollection GeometricUtilities::SpinePointDataCollection@endlink  <br> */
        class NXOPENCPPEXPORT SpinePointData : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** Parameter type */
            public: enum ParameterType
            {
                ParameterTypeNormal/** normal */ ,
                ParameterTypePercent/** Parameter expressed as percent arc length*/,
                ParameterTypeLength/** Parameter expressed as arc length */
            };

            private: friend class  _SpinePointDataBuilder;
            protected: SpinePointData();
            /**Returns  the parameter in percent arc length  <br> License requirements : None */
            public: double ParameterPercent
            (
            );
            /**Sets  the parameter in percent arc length  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetParameterPercent
            (
                double percentParameter /** percent parameter */ 
            );
            /**Returns  the parameter in arc length  <br> License requirements : None */
            public: double ParameterLength
            (
            );
            /**Sets  the parameter in arc length  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetParameterLength
            (
                double lengthParameter /** length parameter */ 
            );
            /** Returns the law value at the specified point  @return  Law value Expression Object  <br> License requirements : None */
            public: NXOpen::Expression * GetLawValueAtPoint
            (
            );
            /** Sets the law value at the specified point  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetLawValueAtPoint
            (
                const NXString & valString /** Law value string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Returns the parent spine on which spine point is defined     @return  section object <br> License requirements : None */
            public: NXOpen::Section * GetParentSpine
            (
            );
            /** Sets the parent spine on which spine point is defined     <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetParentSpine
            (
                NXOpen::Section * parent /** Parent section path on which spine point is defined */
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