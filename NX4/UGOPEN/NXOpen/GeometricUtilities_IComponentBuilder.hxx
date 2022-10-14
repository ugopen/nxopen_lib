#ifndef NXOpen_GEOMETRICUTILITIES_ICOMPONENTBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_ICOMPONENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_IComponentBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        /** Represents a IComponentBuilder Abstract Interface . 
            */
        class NXOPENCPPEXPORT IComponentBuilder
        {
            virtual void EnsureVtableExists() {}
            /** Validate Self
                 @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            ) = 0;
        };
    }
}
#undef EXPORTLIBRARY
#endif