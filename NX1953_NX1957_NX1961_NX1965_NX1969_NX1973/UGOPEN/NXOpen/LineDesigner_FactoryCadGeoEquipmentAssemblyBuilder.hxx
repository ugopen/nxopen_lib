#ifndef NXOpen_LINEDESIGNER_FACTORYCADGEOEQUIPMENTASSEMBLYBUILDER_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_FACTORYCADGEOEQUIPMENTASSEMBLYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_FactoryCadGeoEquipmentAssemblyBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class FactoryCadGeoEquipmentAssemblyBuilder;
    }
    class Builder;
    class TaggedObject;
    namespace LineDesigner
    {
        class _FactoryCadGeoEquipmentAssemblyBuilderBuilder;
        class FactoryCadGeoEquipmentAssemblyBuilderImpl;
        /**    <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateFactorycadgeoequipmentassemblyBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateFactorycadgeoequipmentassemblyBuilder @endlink  <br> 
         <br>  Created in NX11.0.1.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  FactoryCadGeoEquipmentAssemblyBuilder : public NXOpen::Builder
        {
             /** Contains feature update status report */
            public:
            struct UpdatedControlData
            {
                public: /** scontrolname */ NXString SControlName;
                public: /** dcontrolvalue */ double DControlValue;
                public: /** dminvalue */ double DMinValue;
                public: /** dmaxvalue */ double DMaxValue;
                public: /** dincrement */ double DIncrement;
                public: /** vdbllov */ NXString VDblLov;
                public: /** vstrlov */ NXString VStrLov;
                public: /** benforcevalues */ bool BEnforceValues;
                public: /** biseditable */ bool BIsEditable;
                public: /** dconversionfactor */ double DConversionFactor;
                public: UpdatedControlData() :
                    SControlName(),
                    DControlValue(),
                    DMinValue(),
                    DMaxValue(),
                    DIncrement(),
                    VDblLov(),
                    VStrLov(),
                    BEnforceValues(),
                    BIsEditable(),
                    DConversionFactor()
                {
                }
                /** Constructor for the UpdatedControlData struct. */ 
                public: UpdatedControlData(const NXString &sControlNameInitial /** scontrolname */ , 
                        double dControlValueInitial /** dcontrolvalue */ , 
                        double dMinValueInitial /** dminvalue */ , 
                        double dMaxValueInitial /** dmaxvalue */ , 
                        double dIncrementInitial /** dincrement */ , 
                        const NXString &vDblLovInitial /** vdbllov */ , 
                        const NXString &vStrLovInitial /** vstrlov */ , 
                        bool bEnforceValuesInitial /** benforcevalues */ , 
                        bool bIsEditableInitial /** biseditable */ , 
                        double dConversionFactorInitial /** dconversionfactor */ ) :
                    SControlName(sControlNameInitial),
                    DControlValue(dControlValueInitial),
                    DMinValue(dMinValueInitial),
                    DMaxValue(dMaxValueInitial),
                    DIncrement(dIncrementInitial),
                    VDblLov(vDblLovInitial),
                    VStrLov(vStrLovInitial),
                    BEnforceValues(bEnforceValuesInitial),
                    BIsEditable(bIsEditableInitial),
                    DConversionFactor(dConversionFactorInitial)
                {
                }
            };

            private: FactoryCadGeoEquipmentAssemblyBuilderImpl * m_factorycadgeoequipmentassemblybuilder_impl;
            private: friend class  _FactoryCadGeoEquipmentAssemblyBuilderBuilder;
            protected: FactoryCadGeoEquipmentAssemblyBuilder();
            public: ~FactoryCadGeoEquipmentAssemblyBuilder();
            /**    
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void ReadFcadDatasetFiles
            (
            );
            /**    
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void UpdateData
            (
                const std::vector<NXOpen::LineDesigner::FactoryCadGeoEquipmentAssemblyBuilder::UpdatedControlData> & updatedControlDatas /** updatedcontroldatas */ 
            );
            /**    
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetStringToObjectMap
            (
                const NXString & key /** key */ ,
                NXOpen::TaggedObject * tagObject /** tagobject */ 
            );
            /**    
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            void SetStringToObjectMap
            (
                const char * key /** key */ ,
                NXOpen::TaggedObject * tagObject /** tagobject */ 
            );
            /**Read the FactoryCAD files from folder for native mode
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void ReadFcadFiles
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
