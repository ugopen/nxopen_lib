#ifndef NXOpen_SIM_SMKMACHINEKITEDITORBUILDER_HXX_INCLUDED
#define NXOpen_SIM_SMKMACHINEKITEDITORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_SmkMachineKitEditorBuilder.ja
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
#include <NXOpen/libnxopencpp_sim_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace SIM
    {
        class SmkMachineKitEditorBuilder;
    }
    class Builder;
    namespace SIM
    {
        class _SmkMachineKitEditorBuilderBuilder;
        class SmkMachineKitEditorBuilderImpl;
        /**  @brief  Represents the SmkMachineKitEditorBuilder class object  

            <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a SmkMachineKitEditorBuilder object.  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_SIMEXPORT  SmkMachineKitEditorBuilder : public NXOpen::Builder
        {
            /** The data type */
            public: enum DataType
            {
                DataTypeString/** string */ ,
                DataTypeInt/** int */ ,
                DataTypeDouble/** double */ ,
                DataTypeEnum/** enum */ ,
                DataTypeMultiString/** multi string */ 
            };

            /** The data classification */
            public: enum DataClassification
            {
                DataClassificationGeneral/** general */ ,
                DataClassificationPost/** post */ ,
                DataClassificationSim/** sim */ ,
                DataClassificationPostAndSim/** post and sim */ ,
                DataClassificationNc/** nc */ 
            };

            private: SmkMachineKitEditorBuilderImpl * m_smkmachinekiteditorbuilder_impl;
            private: friend class  _SmkMachineKitEditorBuilderBuilder;
            protected: SmkMachineKitEditorBuilder();
            public: ~SmkMachineKitEditorBuilder();
            /** Gets   @return  The attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: int GetIntegerAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */
            );
            /** Gets   @return  The attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            int GetIntegerAttribute
            (
                const char * attributeFullname /** The attribute fullname */
            );
            /** Sets the double attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void SetIntegerAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */,
                int value /** The attribute value */
            );
            /** Sets the double attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void SetIntegerAttribute
            (
                const char * attributeFullname /** The attribute fullname */,
                int value /** The attribute value */
            );
            /** Gets  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetEnumAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */,
                NXString* currentValue /** The attribute value    */,
                std::vector<NXString> & values /** options for enum       */
            );
            /** Gets  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void GetEnumAttribute
            (
                const char * attributeFullname /** The attribute fullname */,
                NXString* currentValue /** The attribute value    */,
                std::vector<NXString> & values /** options for enum       */
            );
            /** Sets the double attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void SetEnumAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */,
                const NXString & value /** The attribute value */
            );
            /** Sets the double attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void SetEnumAttribute
            (
                const char * attributeFullname /** The attribute fullname */,
                const char * value /** The attribute value */
            );
            /** Gets   @return  The attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double GetDoubleAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */
            );
            /** Gets   @return  The attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            double GetDoubleAttribute
            (
                const char * attributeFullname /** The attribute fullname */
            );
            /** Sets the double attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void SetDoubleAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */,
                double value /** The attribute value */
            );
            /** Sets the double attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void SetDoubleAttribute
            (
                const char * attributeFullname /** The attribute fullname */,
                double value /** The attribute value */
            );
            /** Gets   @return  The attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetStringAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */
            );
            /** Gets   @return  The attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            NXString GetStringAttribute
            (
                const char * attributeFullname /** The attribute fullname */
            );
            /** Sets the string attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void SetStringAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */,
                const NXString & value /** The attribute value */
            );
            /** Sets the string attribute value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void SetStringAttribute
            (
                const char * attributeFullname /** The attribute fullname */,
                const char * value /** The attribute value */
            );
            /** Sets the multi string attribute values 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void SetMultiStringAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */,
                std::vector<NXString> & values /** The attribute values   */
            );
            /** Sets the multi string attribute values 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void SetMultiStringAttribute
            (
                const char * attributeFullname /** The attribute fullname */,
                std::vector<NXString> & values /** The attribute values   */
            );
            /** Gets  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetMultiStringAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */,
                std::vector<NXString> & value /** The attribute value    */
            );
            /** Gets  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void GetMultiStringAttribute
            (
                const char * attributeFullname /** The attribute fullname */,
                std::vector<NXString> & value /** The attribute value    */
            );
            /** Deletes the attribute item 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void DeleteAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */
            );
            /** Deletes the attribute item 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void DeleteAttribute
            (
                const char * attributeFullname /** The attribute fullname */
            );
            /** Adds a new attribute item 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void AddAttribute
            (
                const NXString & attributeFullname /** The attribute fullname */
            );
            /** Adds a new attribute item 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void AddAttribute
            (
                const char * attributeFullname /** The attribute fullname */
            );
            /** Sets the attribute name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void SetAttributeName
            (
                const NXString & attributeFullname /** The attribute fullname */,
                const NXString & newName /** The new name */
            );
            /** Sets the attribute name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void SetAttributeName
            (
                const char * attributeFullname /** The attribute fullname */,
                const char * newName /** The new name */
            );
            /** Sets the attribute type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void SetAttributeType
            (
                const NXString & attributeFullname /** The attribute fullname */,
                NXOpen::SIM::SmkMachineKitEditorBuilder::DataType type /** The attribute type */
            );
            /** Sets the attribute type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void SetAttributeType
            (
                const char * attributeFullname /** The attribute fullname */,
                NXOpen::SIM::SmkMachineKitEditorBuilder::DataType type /** The attribute type */
            );
            /** Gets   @return  The attribute type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SIM::SmkMachineKitEditorBuilder::DataType GetAttributeType
            (
                const NXString & attributeFullname /** The attribute fullname */
            );
            /** Gets   @return  The attribute type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::SIM::SmkMachineKitEditorBuilder::DataType GetAttributeType
            (
                const char * attributeFullname /** The attribute fullname */
            );
            /** Sets the attribute classification 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void SetAttributeClassification
            (
                const NXString & attributeFullname /** The attribute fullname */,
                NXOpen::SIM::SmkMachineKitEditorBuilder::DataClassification classification /** The attribute classification */
            );
            /** Sets the attribute classification 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void SetAttributeClassification
            (
                const char * attributeFullname /** The attribute fullname */,
                NXOpen::SIM::SmkMachineKitEditorBuilder::DataClassification classification /** The attribute classification */
            );
            /** Gets   @return  The attribute classification 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SIM::SmkMachineKitEditorBuilder::DataClassification GetAttributeClassification
            (
                const NXString & attributeFullname /** The attribute fullname */
            );
            /** Gets   @return  The attribute classification 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::SIM::SmkMachineKitEditorBuilder::DataClassification GetAttributeClassification
            (
                const char * attributeFullname /** The attribute fullname */
            );
            /** Sets the variable name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            public: void SetAttributeVariableName
            (
                const NXString & attributeFullname /** The attribute fullname */,
                const NXString & variableName /** The variable variable name */
            );
            /** Sets the variable name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") */
            void SetAttributeVariableName
            (
                const char * attributeFullname /** The attribute fullname */,
                const char * variableName /** The variable variable name */
            );
            /** Gets   @return  The attribute variable name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetAttributeVariableName
            (
                const NXString & attributeFullname /** The attribute fullname */
            );
            /** Gets   @return  The attribute variable name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            NXString GetAttributeVariableName
            (
                const char * attributeFullname /** The attribute fullname */
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
