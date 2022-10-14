#ifndef NXOpen_FEATURES_SHIPDESIGN_SHIPPAINTPARAMETERSBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_SHIPPAINTPARAMETERSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_ShipPaintParametersBuilder.ja
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
#include <NXOpen/Features_PaintParametersBuilder.hxx>
#include <NXOpen/ShipDesign_PaintParametersData.hxx>
#include <NXOpen/ShipDesign_PaintParametersParameterValue.hxx>
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
        namespace ShipDesign
        {
            class ShipPaintParametersBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        class PaintParametersBuilder;
    }
    namespace ShipDesign
    {
        class PaintParametersData;
    }
    namespace ShipDesign
    {
        class PaintParametersParameterValue;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _ShipPaintParametersBuilderBuilder;
            class ShipPaintParametersBuilderImpl;
            /**
                    Represents a paint feature parameters builder. The paint parameters does not
                    create a feature, but assists to copy parameters from one feature, called source feature, and 
                    apply them to other features, called target features. Features Parameters would be copied from
                    the source feature to the target features. 
                     <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateShipPaintParametersBuilder  NXOpen::Features::ShipCollection::CreateShipPaintParametersBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            TargetComponentSelection </term> <description> 
             
            0 </description> </item> 

            </list> 

             <br>  Created in NX1980.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ShipPaintParametersBuilder : public NXOpen::Features::PaintParametersBuilder
            {
                private: ShipPaintParametersBuilderImpl * m_shippaintparametersbuilder_impl;
                private: friend class  _ShipPaintParametersBuilderBuilder;
                protected: ShipPaintParametersBuilder();
                public: ~ShipPaintParametersBuilder();
                /** The parameters of the source object 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ShipDesign::PaintParametersData * GetSourceObjectParameters
                (
                );
                /** Modify the section type parameter. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionType
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const NXString & strSectionType /** strsectiontype */ ,
                    const NXString & categoryName /** categoryname */ 
                );
                /** Modify the section type parameter. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void SetSectionType
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const char * strSectionType /** strsectiontype */ ,
                    const char * categoryName /** categoryname */ 
                );
                /** Modify the section subtype1 parameter. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionSubType1
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const NXString & strSectionType /** strsectiontype */ ,
                    const NXString & categoryName /** categoryname */ 
                );
                /** Modify the section subtype1 parameter. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void SetSectionSubType1
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const char * strSectionType /** strsectiontype */ ,
                    const char * categoryName /** categoryname */ 
                );
                /** Modify the section subtype2 parameter. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionSubType2
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const NXString & strSectionType /** strsectiontype */ ,
                    const NXString & categoryName /** categoryname */ 
                );
                /** Modify the section subtype2 parameter. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void SetSectionSubType2
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const char * strSectionType /** strsectiontype */ ,
                    const char * categoryName /** categoryname */ 
                );
                /** Modify the parameter which impace section type/subtype1/subtype2. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void ModifyParameterImpactTypes
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const NXString & strParameterName /** strparametername */ ,
                    const NXString & strParameterValue /** strparametervalue */ 
                );
                /** Modify the parameter which impace section type/subtype1/subtype2. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void ModifyParameterImpactTypes
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const char * strParameterName /** strparametername */ ,
                    const char * strParameterValue /** strparametervalue */ 
                );
                /** This is used to set the paint parameters data. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetPaintParametersData
                (
                    NXOpen::ShipDesign::PaintParametersData * pPaintParametersData /** ppaintparametersdata */ 
                );
                /** This is used to set the frec builder tag created for the paintable object. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetFrecBuilder
                (
                    NXOpen::Builder * builderTag /** buildertag */ 
                );
                /** This is used to update parameters. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: std::vector<NXOpen::ShipDesign::PaintParametersParameterValue *> UpdateParameters
                (
                    NXOpen::ShipDesign::PaintParametersData * pPaintParametersData /** ppaintparametersdata */ ,
                    const std::vector<NXOpen::ShipDesign::PaintParametersParameterValue *> & checkedPara /** checkedpara */ 
                );
                /** Modifies the connection type parameter. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetPrimaryParameterValue
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const NXString & parameterName /** parametername */ ,
                    const NXString & categoryName /** categoryname */ ,
                    const NXString & parameterValue /** parametervalue */ 
                );
                /** Modifies the connection type parameter. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void SetPrimaryParameterValue
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const char * parameterName /** parametername */ ,
                    const char * categoryName /** categoryname */ ,
                    const char * parameterValue /** parametervalue */ 
                );
                /** Updates possible attributes. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void UpdatePossibleContextAttributes
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const NXString & categoryName /** categoryname */ 
                );
                /** Updates possible attributes. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void UpdatePossibleContextAttributes
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const char * categoryName /** categoryname */ 
                );
                /** Updates parameters using rules. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void UpdateParametersUsingRules
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ 
                );
                /** Edits primary parameters. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void EditPrimaryParameter
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const NXString & categoryName /** categoryname */ ,
                    const NXString & parameterName /** parametername */ ,
                    const NXString & parameterValue /** parametervalue */ 
                );
                /** Edits primary parameters. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void EditPrimaryParameter
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const char * categoryName /** categoryname */ ,
                    const char * parameterName /** parametername */ ,
                    const char * parameterValue /** parametervalue */ 
                );
                /** Edits general parameters. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void EditParameter
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const NXString & categoryName /** categoryname */ ,
                    const NXString & parameterName /** parametername */ ,
                    const NXString & parameterValue /** parametervalue */ 
                );
                /** Edits general parameters. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void EditParameter
                (
                    NXOpen::ShipDesign::PaintParametersData * spreadsheetData /** spreadsheetdata */ ,
                    const char * categoryName /** categoryname */ ,
                    const char * parameterName /** parametername */ ,
                    const char * parameterValue /** parametervalue */ 
                );
                /** Sets suppress flag. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSuppressFlag
                (
                );
                /** Unsets suppress flag. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void UnsetSuppressFlag
                (
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