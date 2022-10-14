#ifndef NXOpen_IMPORTER3MF_HXX_INCLUDED
#define NXOpen_IMPORTER3MF_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Importer3MF.ja
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
#include <NXOpen/DexBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class Importer3MF;
    class DexBuilder;
    class _Importer3MFBuilder;
    class Importer3MFImpl;
    /**
        Represents a @link NXOpen::Importer3MF NXOpen::Importer3MF@endlink  to be used when importing 3MF Data
        This class is created using @link NXOpen::DexManager NXOpen::DexManager@endlink .
        NULL object will be returned from Commit()  <br> To create a new instance of this class, use @link NXOpen::DexManager::CreateImporter3mf  NXOpen::DexManager::CreateImporter3mf @endlink  <br> 
    Default values.
    <list type="table"> 
     
    <listheader><term> 
    Property</term>  <description> 
    Value</description> </listheader>
    <item><term> 
     
    CreateClipLatticeFeature </term> <description> 
     
    True </description> </item> 

    <item><term> 
     
    FacetBodyType </term> <description> 
     
    Psm </description> </item> 

    <item><term> 
     
    MinimumAngleFoldedFacets </term> <description> 
     
    15.0 </description> </item> 

    <item><term> 
     
    MinimumFacetNumber </term> <description> 
     
    100 </description> </item> 

    <item><term> 
     
    ShowInformationWindow </term> <description> 
     
    False </description> </item> 

    <item><term> 
     
    TessellationFactor </term> <description> 
     
    0.5 </description> </item> 

    </list> 

     <br>  Usable only on Windows <br> 
     <br>  Created in NX12.0.1.  <br>  
    */
    class NXOPENCPPEXPORT  Importer3MF : public NXOpen::DexBuilder
    {
        /** These represent the type of body that will get created on importing the 3MF file */
        public: enum FacetBodyTypes
        {
            FacetBodyTypesPsm/** Import as Convergent Body */,
            FacetBodyTypesNx/** Import as NX Facet Body */
        };

        private: Importer3MFImpl * m_importer3mf_impl;
        private: friend class  _Importer3MFBuilder;
        protected: Importer3MF();
        public: ~Importer3MF();
        /**Returns  an input 3MF file to be imported  
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : None */
        public: NXString InputFile
        (
        );
        /**Sets  an input 3MF file to be imported  
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : nx_additive_design (" NX Additive Design") */
        public: void SetInputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  an input 3MF file to be imported  
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : nx_additive_design (" NX Additive Design") */
        void SetInputFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the facet body type 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : None */
        public: NXOpen::Importer3MF::FacetBodyTypes FacetBodyType
        (
        );
        /**Sets  the facet body type 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : nx_additive_design (" NX Additive Design") */
        public: void SetFacetBodyType
        (
            NXOpen::Importer3MF::FacetBodyTypes facetBodyType /** facetbodytype */ 
        );
        /**Returns  the option to clean up all mesh defects on import 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : None */
        public: bool Cleanup
        (
        );
        /**Sets  the option to clean up all mesh defects on import 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : nx_additive_design (" NX Additive Design") */
        public: void SetCleanup
        (
            bool cleanup /** cleanup */ 
        );
        /**Returns  the value for minimum angle for folded facets for a 3MF file to be imported 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : None */
        public: double MinimumAngleFoldedFacets
        (
        );
        /**Sets  the value for minimum angle for folded facets for a 3MF file to be imported 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : nx_additive_design (" NX Additive Design") */
        public: void SetMinimumAngleFoldedFacets
        (
            double minimumAngleFoldedFacets /** minimumanglefoldedfacets */ 
        );
        /**Returns  the value for minimum number of facets for a 3MF file to be imported 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : None */
        public: int MinimumFacetNumber
        (
        );
        /**Sets  the value for minimum number of facets for a 3MF file to be imported 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : nx_additive_design (" NX Additive Design") */
        public: void SetMinimumFacetNumber
        (
            int minimumFacetNumber /** minimumfacetnumber */ 
        );
        /**Returns   @brief the tessellation factor of the lattice creation. 

          
                     
                    A tessellation tolerance specifies the maximum deviation between the ideal rod and their final tessellated 
                    representation of the lattice body. Since the result heavily depends on the relation between rod diameter 
                    and tessellation tolerance, the tessellation factor is only a unitless factor. The actual tessellation tolerance 
                    will be determined by the rod diameters.
                      
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: double TessellationFactor
        (
        );
        /**Sets   @brief the tessellation factor of the lattice creation. 

          
                     
                    A tessellation tolerance specifies the maximum deviation between the ideal rod and their final tessellated 
                    representation of the lattice body. Since the result heavily depends on the relation between rod diameter 
                    and tessellation tolerance, the tessellation factor is only a unitless factor. The actual tessellation tolerance 
                    will be determined by the rod diameters.
                      
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : nx_additive_design (" NX Additive Design") */
        public: void SetTessellationFactor
        (
            double tessellationFactor /** tessellationfactor */ 
        );
        /**Returns  the option to create clip lattice features if the clipping information exists in the file 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: bool CreateClipLatticeFeature
        (
        );
        /**Sets  the option to create clip lattice features if the clipping information exists in the file 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : nx_additive_design (" NX Additive Design") */
        public: void SetCreateClipLatticeFeature
        (
            bool createClipLatticeFeature /** createcliplatticefeature */ 
        );
        /**Returns  the indicator for whether to show information window 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : None */
        public: bool ShowInformationWindow
        (
        );
        /**Sets  the indicator for whether to show information window 
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : nx_additive_design (" NX Additive Design") */
        public: void SetShowInformationWindow
        (
            bool showInformationWindow /** showinformationwindow */ 
        );
    };
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