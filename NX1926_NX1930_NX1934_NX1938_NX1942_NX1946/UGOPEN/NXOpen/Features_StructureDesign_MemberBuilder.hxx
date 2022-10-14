#ifndef NXOpen_FEATURES_STRUCTUREDESIGN_MEMBERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_STRUCTUREDESIGN_MEMBERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_StructureDesign_MemberBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_StructureDesign_FeatureSpreadsheetBuilder.hxx>
#include <NXOpen/Features_StructureDesign_FeatureParmsBuilder.hxx>
#include <NXOpen/Section.hxx>
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
        namespace StructureDesign
        {
            class MemberBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        namespace StructureDesign
        {
            class FeatureParmsBuilder;
        }
    }
    namespace Features
    {
        namespace StructureDesign
        {
            class FeatureSpreadsheetBuilder;
        }
    }
    class Section;
    namespace Features
    {
        namespace StructureDesign
        {
            class _MemberBuilderBuilder;
            class MemberBuilderImpl;
            /**
                Represents a builder which is used to create or edit a Structure Design Member feature.
                 <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignMemberBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignMemberBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            RotateAngle.Value </term> <description> 
             
            0 </description> </item> 

            </list> 

             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  MemberBuilder : public NXOpen::Features::StructureDesign::FeatureParmsBuilder
            {
                /** The settings to define the corner at the start and end of the member. */
                public: enum EndCornerTypes
                {
                    EndCornerTypesNone/** none */ ,
                    EndCornerTypesMiter/** miter */ ,
                    EndCornerTypesButt/** butt */ ,
                    EndCornerTypesCope/** cope */ ,
                    EndCornerTypesMatchedCope/** matched cope */ ,
                    EndCornerTypesSmartExtend/** smart extend */ 
                };

                private: MemberBuilderImpl * m_memberbuilder_impl;
                private: friend class  _MemberBuilderBuilder;
                protected: MemberBuilder();
                public: ~MemberBuilder();
                /**Returns  the stock data used to define the stock information of the member.
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::StructureDesign::FeatureSpreadsheetBuilder * StockData
                (
                );
                /**Returns  the index number of the alternate sketch origin to use. This number is retrieved
                        from points in the sketch that have an integer user attribute with a title of "SD_ANCHOR_POINT".
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: int AlternateOrigin
                (
                );
                /**Sets  the index number of the alternate sketch origin to use. This number is retrieved
                        from points in the sketch that have an integer user attribute with a title of "SD_ANCHOR_POINT".
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetAlternateOrigin
                (
                    int alternateOrigin /** alternateorigin */ 
                );
                /**Returns  the path geometry. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * PathGeometry
                (
                );
                /**Returns  the corner to be used at the start of the member. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::StructureDesign::MemberBuilder::EndCornerTypes EndCornerStart
                (
                );
                /**Sets  the corner to be used at the start of the member. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetEndCornerStart
                (
                    NXOpen::Features::StructureDesign::MemberBuilder::EndCornerTypes endCornerStart /** endcornerstart */ 
                );
                /**Returns  the corner to be used at the end of the member. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::StructureDesign::MemberBuilder::EndCornerTypes EndCornerEnd
                (
                );
                /**Sets  the corner to be used at the end of the member. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetEndCornerEnd
                (
                    NXOpen::Features::StructureDesign::MemberBuilder::EndCornerTypes endCornerEnd /** endcornerend */ 
                );
                /**Returns  the name used for the created component file. If a duplicate name, will append a number to this name. This
                        property is only used during creation of the member. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString FileName
                (
                );
                /**Sets  the name used for the created component file. If a duplicate name, will append a number to this name. This
                        property is only used during creation of the member. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetFileName
                (
                    const NXString & fileName /** filename */ 
                );
                /**Sets  the name used for the created component file. If a duplicate name, will append a number to this name. This
                        property is only used during creation of the member. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                void SetFileName
                (
                    const char * fileName /** filename */ 
                );
                /** Rotate the sketch 180 degrees around the X axis. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void FlipX
                (
                );
                /** Rotate the sketch 180 degrees around the Y axis. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void FlipY
                (
                );
                /**Returns  the rotate angle period
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * RotateAngle
                (
                );
                /**Returns  the flag to enable auto merge colinear path. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: bool EnableMergeColinearPath
                (
                );
                /**Sets  the flag to enable auto merge colinear path. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetEnableMergeColinearPath
                (
                    bool bEnableMergeColinearPath /** benablemergecolinearpath */ 
                );
            };
        }
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