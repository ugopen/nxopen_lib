#ifndef NXOpen_FEATURES_RODTHICKNESSBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_RODTHICKNESSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_RodThicknessBuilder.ja
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
#include <NXOpen/Fields_ScalarFieldWrapper.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class RodThicknessBuilder;
    }
    class Builder;
    namespace Fields
    {
        class ScalarFieldWrapper;
    }
    class ScCollector;
    namespace Features
    {
        class _RodThicknessBuilderBuilder;
        class RodThicknessBuilderImpl;
        /** Changes rod diameters of exisiting lattice bodies based on the specified rod diameter. <br> To create a new instance of this class, use @link NXOpen::Features::LatticeFeatureCollection::CreateRodThicknessBuilder  NXOpen::Features::LatticeFeatureCollection::CreateRodThicknessBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        TessellationFactor </td> <td> 
         
        0.5 </td> </tr> 

        </table>  

         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  RodThicknessBuilder : public NXOpen::Builder
        {
            /** These represent the options for handling the input bodies */
            public: enum OriginalBodyOptions
            {
                OriginalBodyOptionsDelete/** Delete Bodies */
            };

            private: RodThicknessBuilderImpl * m_rodthicknessbuilder_impl;
            private: friend class  _RodThicknessBuilderBuilder;
            protected: RodThicknessBuilder();
            public: ~RodThicknessBuilder();
            /**Returns  @brief  the lattice bodies whose diamaeters are to be modified.  

             
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * LatticeBodies
            (
            );
            /**Returns   @brief the tessellation factor of the lattice creation. 

             
                    
                    A tessellation tolerance specifies the maximum deviation between the ideal rod and their final tessellated
                    representation of the lattice body. Since the result heavily depends on the relation between rod diameter
                    and tessellation tolerance, the tessellation factor is only a unitless factor. The actual tessellation tolerance
                    will determined by
                    (@link Features::LatticeBuilder::TessellationFactor Features::LatticeBuilder::TessellationFactor @endlink and @link Features::LatticeBuilder::SetTessellationFactor Features::LatticeBuilder::SetTessellationFactor @endlink ) X (@link Features::LatticeBuilder::RodDiameter Features::LatticeBuilder::RodDiameter@endlink )  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double TessellationFactor
            (
            );
            /**Sets   @brief the tessellation factor of the lattice creation. 

             
                    
                    A tessellation tolerance specifies the maximum deviation between the ideal rod and their final tessellated
                    representation of the lattice body. Since the result heavily depends on the relation between rod diameter
                    and tessellation tolerance, the tessellation factor is only a unitless factor. The actual tessellation tolerance
                    will determined by
                    (@link Features::LatticeBuilder::TessellationFactor Features::LatticeBuilder::TessellationFactor @endlink and @link Features::LatticeBuilder::SetTessellationFactor Features::LatticeBuilder::SetTessellationFactor @endlink ) X (@link Features::LatticeBuilder::RodDiameter Features::LatticeBuilder::RodDiameter@endlink )  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetTessellationFactor
            (
                double factor /** factor */ 
            );
            /**Returns  the diameter/thickness scalar field of the rods in the lattice graph
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Fields::ScalarFieldWrapper * RodDiameter
            (
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