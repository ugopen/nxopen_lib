#ifndef NXOpen_DRAWINGS_VIEWSTYLEINHERITPMIBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWSTYLEINHERITPMIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewStyleInheritPmiBuilder.ja
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
#include <NXOpen/Drawings_ViewStyleInheritPmiBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ViewStyleInheritPmiBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _ViewStyleInheritPmiBuilderBuilder;
        /** Represents the INHERIT PMI tab on the View Style Dialog (Drawings.ViewStyleInheritPmiBuilder)
            */
        class NXOPENCPPEXPORT ViewStyleInheritPmiBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _ViewStyleInheritPmiBuilderBuilder;
            protected: ViewStyleInheritPmiBuilder();
            /**Returns  the pmi option on the INHERIT PMI tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::Preferences::PmiOption Pmi
            (
            );
            /**Sets  the pmi option on the INHERIT PMI tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetPmi
            (
                NXOpen::Preferences::PmiOption pmiOption /** Sets a new pmi option on the inherit pmi sub-builder */
            );
            /**Returns  the 'pmi to drawing' toggle on the INHERIT PMI tab of the View Style Dialog  <br> License requirements : None */
            public: bool PmiToDrawing
            (
            );
            /**Sets  the 'pmi to drawing' toggle on the INHERIT PMI tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetPmiToDrawing
            (
                bool pmiToDrawingToggle /** Sets a new pmi to drawing toggle value on the inherit pmi sub-builder */
            );
            /**Returns  the type mask on the INHERIT PMI tab of the View Style Dialog  <br> License requirements : None */
            public: int PmiTypeMask
            (
            );
            /**Sets  the type mask on the INHERIT PMI tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetPmiTypeMask
            (
                int pmiTypeMask /** Sets a new pmi type mask on the inherit pmi sub-builder */
            );
            /**Returns  the gdt option on the INHERIT PMI tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::Preferences::GdtOption Gdt
            (
            );
            /**Sets  the gdt option on the INHERIT PMI tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetGdt
            (
                NXOpen::Preferences::GdtOption gdtOption /** Sets a new gdt option on the inherit pmi sub-builder */
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
