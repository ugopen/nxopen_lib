#ifndef NXOpen_FEATURES_MATHINTEGRATIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_MATHINTEGRATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MathIntegrationBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class MathIntegrationBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class _MathIntegrationBuilderBuilder;
        class MathIntegrationBuilderImpl;
        /**
            Represents a @link NXOpen::Features::MathIntegration NXOpen::Features::MathIntegration@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateMathIntegrationBuilder  NXOpen::Features::FeatureCollection::CreateMathIntegrationBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Associative </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        AssociativityType </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        EmbedWorksheet </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ShowInformationWindow </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  MathIntegrationBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** The option to specify where the NX Maple or Maple worksheet exists. */
            public: enum LocationTypes
            {
                LocationTypesOperatingSystem/** Worksheet is on the native OS file system. */,
                LocationTypesTeamcenter/** Worksheet is in Teamcenter. */,
                LocationTypesEmbedded/** Worksheet is embedded in part. */
            };

            /** the associativity */
            public: enum AssociativityTypes
            {
                AssociativityTypesNone/** No associativity to the worksheet */,
                AssociativityTypesNew/** Make associative to the worksheet */,
                AssociativityTypesExisting/** Maintain associativity to the worksheet */
            };

            private: MathIntegrationBuilderImpl * m_mathintegrationbuilder_impl;
            private: friend class  _MathIntegrationBuilderBuilder;
            protected: MathIntegrationBuilder();
            public: ~MathIntegrationBuilder();
            /**Returns  the source location of the NX Maple or Maple worksheet.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::MathIntegrationBuilder::LocationTypes Location
            (
            );
            /**Sets  the source location of the NX Maple or Maple worksheet.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetLocation
            (
                NXOpen::Features::MathIntegrationBuilder::LocationTypes location /** location */ 
            );
            /**Returns  the file name returned by the Browser 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FileBrowser
            (
            );
            /**Sets  the file name returned by the Browser 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFileBrowser
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the file name returned by the Browser 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetFileBrowser
            (
                const char * filename /** filename */ 
            );
            /**Returns  the native OS file name returned by the Browser. Used when the session is Teamcenter, but the location is @link NXOpen::Features::MathIntegrationBuilder::LocationTypesOperatingSystem NXOpen::Features::MathIntegrationBuilder::LocationTypesOperatingSystem@endlink . 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString NativeFileBrowser
            (
            );
            /**Sets  the native OS file name returned by the Browser. Used when the session is Teamcenter, but the location is @link NXOpen::Features::MathIntegrationBuilder::LocationTypesOperatingSystem NXOpen::Features::MathIntegrationBuilder::LocationTypesOperatingSystem@endlink . 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetNativeFileBrowser
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the native OS file name returned by the Browser. Used when the session is Teamcenter, but the location is @link NXOpen::Features::MathIntegrationBuilder::LocationTypesOperatingSystem NXOpen::Features::MathIntegrationBuilder::LocationTypesOperatingSystem@endlink . 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetNativeFileBrowser
            (
                const char * filename /** filename */ 
            );
            /**Returns  the currently selected embedded worksheet index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int EmbeddedWorksheet
            (
            );
            /**Sets  the currently selected embedded worksheet index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEmbeddedWorksheet
            (
                int embeddedWorksheet /** embeddedworksheet */ 
            );
            /**Returns  the option to embed worksheet in the feature 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool EmbedWorksheet
            (
            );
            /**Sets  the option to embed worksheet in the feature 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEmbedWorksheet
            (
                bool embedWorksheet /** embedworksheet */ 
            );
            /**Returns  the associativity of the expression in the feature to the NX Maple or Maple worksheet 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associativity of the expression in the feature to the NX Maple or Maple worksheet 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the option to control associativity to the equation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::MathIntegrationBuilder::AssociativityTypes AssociativityType
            (
            );
            /**Sets  the option to control associativity to the equation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociativityType
            (
                NXOpen::Features::MathIntegrationBuilder::AssociativityTypes associativityType /** associativitytype */ 
            );
            /**Returns  the option to show the information window 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowInformationWindow
            (
            );
            /**Sets  the option to show the information window 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetShowInformationWindow
            (
                bool showInformationWindow /** showinformationwindow */ 
            );
            /**Returns  the number of input expressions 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int Inputs
            (
            );
            /**Sets  the number of input expressions 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetInputs
            (
                int numInputExpressions /** num input expressions */ 
            );
            /** The array of expressions  @return  array of expressions 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Expression *> GetExpressions
            (
            );
            /** Set the expressions in the Math Interface Builder 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetExpressions
            (
                const std::vector<NXOpen::Expression *> & expressions /** array of expressions */
            );
            /** The array of math names  @return  array of names 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetMathNames
            (
            );
            /** Set the math names corresponding to expressions in the Math Interface Builder
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMathNames
            (
                const std::vector<NXString> & names /** array of names */
            );
            /**Returns  the name of the selected sheet inside of a maple workbook file 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Worksheet
            (
            );
            /**Sets  the name of the selected sheet inside of a maple workbook file 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetWorksheet
            (
                const NXString & sheetName /** sheetname */ 
            );
            /**Sets  the name of the selected sheet inside of a maple workbook file 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetWorksheet
            (
                const char * sheetName /** sheetname */ 
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
