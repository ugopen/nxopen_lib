#ifndef NXOpen_FACET_FACETEDFACE_HXX_INCLUDED
#define NXOpen_FACET_FACETEDFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Facet_FacetedFace.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/IParameterizedSurface.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Facet
    {
        class FacetedFace;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class DisplayableObject;
    class INXObject;
    class IParameterizedSurface;
    namespace Facet
    {
        class _FacetedFaceBuilder;
        /** Represents a faceted face. Instances of this class may be
                generated when recording a journal, but they cannot be created
                directly. 
            */
        class NXOPENCPPEXPORT FacetedFace : public DisplayableObject, public virtual IParameterizedSurface
        {
            private: friend class  _FacetedFaceBuilder;
            protected: FacetedFace();
        };
    }
}
#undef EXPORTLIBRARY
#endif
