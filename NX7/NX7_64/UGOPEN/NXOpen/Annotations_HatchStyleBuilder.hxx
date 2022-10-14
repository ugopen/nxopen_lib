#ifndef NXOpen_ANNOTATIONS_HATCHSTYLEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_HATCHSTYLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_HatchStyleBuilder.ja
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
#include <NXOpen/Annotations_HatchStyleBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class HatchStyleBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXColor;
    namespace Annotations
    {
        class _HatchStyleBuilderBuilder;
        /**
            Represents a @link Annotations::HatchStyleBuilder Annotations::HatchStyleBuilder@endlink .
            This class queries and sets crosshatching and area fill preferences when creating and editing
            crosshatching and area fill drafting annotations.
            */
        class NXOPENCPPEXPORT HatchStyleBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _HatchStyleBuilderBuilder;
            protected: HatchStyleBuilder();
            /**Returns  the distance between crosshatch lines  <br> License requirements : None */
            public: double HatchDistance
            (
            );
            /**Sets  the distance between crosshatch lines  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetHatchDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the angle of the crosshatching lines  <br> License requirements : None */
            public: double HatchAngle
            (
            );
            /**Sets  the angle of the crosshatching lines  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetHatchAngle
            (
                double angle /** angle */ 
            );
            /**Returns  the crosshatch and area fill tolerance  <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the crosshatch and area fill tolerance  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the crosshatch definition file  <br> License requirements : None */
            public: NXString HatchFile
            (
            );
            /**Sets  the crosshatch definition file  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetHatchFile
            (
                const NXString & file /** file */ 
            );
            /**Returns  the crosshatch material  <br> License requirements : None */
            public: NXString HatchMaterial
            (
            );
            /**Sets  the crosshatch material  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetHatchMaterial
            (
                const NXString & material /** material */ 
            );
            /**Returns  the area fill material  <br> License requirements : None */
            public: NXOpen::Annotations::AreaFillMaterial AreaFillMaterial
            (
            );
            /**Sets  the area fill material  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetAreaFillMaterial
            (
                NXOpen::Annotations::AreaFillMaterial areaFillMaterial /** areafillmaterial */ 
            );
            /**Returns  the area fill scale  <br> License requirements : None */
            public: double AreaFillScale
            (
            );
            /**Sets  the area fill scale  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetAreaFillScale
            (
                double areaFillScale /** areafillscale */ 
            );
            /**Returns  the area fill angle  <br> License requirements : None */
            public: double AreaFillAngle
            (
            );
            /**Sets  the area fill angle  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetAreaFillAngle
            (
                double areaFillAngle /** areafillangle */ 
            );
            /**Returns  the color of crosshatch or area fill lines or area fill solid fill color  <br> License requirements : None */
            public: NXOpen::NXColor * Color
            (
            );
            /**Sets  the color of crosshatch or area fill lines or area fill solid fill color  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetColor
            (
                NXOpen::NXColor * color /** color */ 
            );
            /**Returns  the line width for crosshatch lines  <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth LineWidth
            (
            );
            /**Sets  the line width for crosshatch lines  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLineWidth
            (
                NXOpen::Annotations::LineWidth lineWidth /** linewidth */ 
            );
            /**Returns  the automatic text island creation flag.
                        A value of True means a text island will be created when the crosshatch
                        or area fill is created  <br> License requirements : None */
            public: bool AutoTextIsland
            (
            );
            /**Sets  the automatic text island creation flag.
                        A value of True means a text island will be created when the crosshatch
                        or area fill is created  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetAutoTextIsland
            (
                bool autoTextIsland /** autotextisland */ 
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