#ifndef NXOpen_DRAWINGS_VIEWSTYLEORIENTATIONBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWSTYLEORIENTATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewStyleOrientationBuilder.ja
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
#include <NXOpen/Drawings_HingeLineBuilder.hxx>
#include <NXOpen/Drawings_OvtBuilder.hxx>
#include <NXOpen/Drawings_ViewStyleOrientationBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ViewStyleOrientationBuilder;
    }
    namespace Drawings
    {
        class HingeLineBuilder;
    }
    namespace Drawings
    {
        class OvtBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _ViewStyleOrientationBuilderBuilder;
        /** Represents the ORIENTATION tab on the View Style Dialog (Drawings.ViewStyleOrientationBuilder)
            */
        class NXOPENCPPEXPORT ViewStyleOrientationBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _ViewStyleOrientationBuilderBuilder;
            protected: ViewStyleOrientationBuilder();
            /**Returns  the view hinge line definition on the ORIENTATION tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::Drawings::HingeLineBuilder * HingeLine
            (
            );
            /**Returns  the view orientation definition on the ORIENTATION tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::Drawings::OvtBuilder * Ovt
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