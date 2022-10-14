#ifndef NXOpen_FEATURES_EMBOSSREGION_HXX_INCLUDED
#define NXOpen_FEATURES_EMBOSSREGION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_EmbossRegion.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Features_EmbossLimit.hxx>
#include <NXOpen/Features_EmbossProjection.hxx>
#include <NXOpen/Features_EmbossRegion.hxx>
#include <NXOpen/Features_EmbossSidewall.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class EmbossRegion;
    }
    class Direction;
    namespace Features
    {
        class EmbossLimit;
    }
    namespace Features
    {
        class EmbossProjection;
    }
    namespace Features
    {
        class EmbossSidewall;
    }
    class Section;
    namespace Features
    {
        class _EmbossRegionBuilder;
        /**Emboss region is the top level class to represent emboss feature data 
            and it consists of following attributes:
            --Section
                    NX standard section 
            --Direction
                    NX standard vector
                    
            --Convexity option
                Emboss convexity option to define the final desired shape in some special case.
                    convexity_option_above = 0,   Pad 
                    convexity_option_below = 1,   Pocket 
                    convexity_option_mixed = 2    Mixed 
           
            --Emboss projectin -> EmbossProjection
                Emboss projection represents how to project and to help build sidewall geometry
                    --Projection Option
                                projection_option_endcap = 0,   Endcap 
        	                projection_option_target = 1,   Target 
        	                projection_option_face   = 2,   Face   
        	                projection_option_plane  = 3,   Plane  
        	                projection_option_none   = 4    None   
                    --Projection Face
                        NX standard face collector
                        
                    --Projection Datum Plane	                            
                        NX standard datum plane

            --Emboss sidewall  -> EmbossSidewall
                Emboss sidewall represents emboss side objects. Normally, extrusion, tapered  swept etc methods to creation sidewall geometry.
                    --Sidewall method option
                                sidewall_method_isocline_tapered = 0,   Isocline_tapered       
                                sidewall_method_curve_tapered    = 1,   Curve tapered          
                                sidewall_method_ruled            = 2,   Ruled                  
                                sidewall_method_swept            = 3,   Swept                  
                                sidewall_method_normal           = 4,   Normal to surf tapered 
                                sidewall_method_two_section      = 5,   Two section            
                                sidewall_method_offset           = 6    Offset section               
                    --Sidewall direction
                        NX standard vector
                        
                    --Sidewall default angle
                        NX standard expression
                        
                    
                    --Sidewall joggle -> EmbossJoggle
                        --Joggle direction option
                            joggle_direction_option_sidewall = 0,    Along sidewall direction      
                            joggle_direction_option_normal   = 1,    Normal to target              
                            joggle_direction_option_specify  = 2     Along user specified direction 
                        --Joggle Direction                
                    
                    --Sidewall tapers (array) -> EmbossTaper
                        for each chain of section, it's allowed to assgine with different taper angle.
                        --Taper angle
                            NX standard expression
            
            --Emboss limits (array)  -> EmbossLimit
                 Emboss limit represents emboss start and end objects, meaning, targets and endcap definitions.
                    --Endcap option
                        endcap_option_translation          = 0,   Translation          
                        endcap_option_offset_exact         = 1,   Offset exact         
                        endcap_option_offset_approximation = 2,   Offset approximation 
                        endcap_option_none                 = 3    None                 
                        
                    --Endcap source option
                        endcap_source_target  = 0,      Target  
                        endcap_source_plane   = 1,      Plane   
                        endcap_source_section = 2,      Section     
                        endcap_source_face    = 3       Face    
                        
                    --Emboss targets (array) -> EmbossTarget
                        --Target faces
                              NX standard Face ScCollector
                        --Endcap faces
                              NX standard Face ScCollector
                        --Endcap Plane
                              NX standard ISurface
                        --Endcap offset direction flip
                              NX standard ISurface
                        --taget offset distance
                              NX standard Expression
                    
                    --Endcap direction
                        NX standard vector
                    
                    --distance (translate or offset)
                        NX standard expression
            */
        class NXOPENCPPEXPORT EmbossRegion : public TaggedObject
        {
            /** This enum represents the endcap option of comp limit */
            public: enum ConvexityOption
            {
                ConvexityOptionAbove/** Above */,
                ConvexityOptionBelow/** Below */,
                ConvexityOptionMixed/** Mixed */
            };

            private: friend class  _EmbossRegionBuilder;
            protected: EmbossRegion();
            /**Sets   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSection
            (
                NXOpen::Section * section /**Region section */
            );
            /**Returns   <br> License requirements : None */
            public: NXOpen::Section * Section
            (
            );
            /**Sets   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDirection
            (
                NXOpen::Direction * direction /**Region projection direction */
            );
            /**Returns   <br> License requirements : None */
            public: NXOpen::Direction * Direction
            (
            );
            /**Sets   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetConvexity
            (
                NXOpen::Features::EmbossRegion::ConvexityOption convexity /**Emboss convecity option: mixed/above/below */
            );
            /**Returns   <br> License requirements : None */
            public: NXOpen::Features::EmbossRegion::ConvexityOption Convexity
            (
            );
            /**Sets   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetProjection
            (
                NXOpen::Features::EmbossProjection * projection /**Emboss projection */
            );
            /**Returns   <br> License requirements : None */
            public: NXOpen::Features::EmbossProjection * Projection
            (
            );
            /**Sets   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSidewall
            (
                NXOpen::Features::EmbossSidewall * sidewall /**Emboss sidewall */
            );
            /**Returns   <br> License requirements : None */
            public: NXOpen::Features::EmbossSidewall * Sidewall
            (
            );
            /** Set the emboss limits  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetLimits
            (
                const std::vector<NXOpen::Features::EmbossLimit *> & limits /**Emboss limit */
            );
            /** Get the emboss limits  @return Emboss limit  <br> License requirements : None */
            public: std::vector<NXOpen::Features::EmbossLimit *> GetLimits
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif