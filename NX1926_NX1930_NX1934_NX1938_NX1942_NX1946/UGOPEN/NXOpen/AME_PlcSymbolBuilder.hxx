#ifndef NXOpen_AME_PLCSYMBOLBUILDER_HXX_INCLUDED
#define NXOpen_AME_PLCSYMBOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_PlcSymbolBuilder.ja
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
#include <NXOpen/AME_DataTypeBuilder.hxx>
#include <NXOpen/AME_PlcTypes.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/Tooling_SelectReuseLibraryItemBuilder.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class PlcSymbolBuilder;
    }
    namespace AME
    {
        class DataTypeBuilder;
    }
    namespace AME
    {
        class SelectAMEBaseNode;
    }
    namespace AME
    {
        class SelectINodeObject;
    }
    class Builder;
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _PlcSymbolBuilderBuilder;
        class PlcSymbolBuilderImpl;
        /** Class to create Functional Tags and assign them to PLC Channels  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreatePlcSymbolBuilder  NXOpen::AME::AMEManager::CreatePlcSymbolBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  PlcSymbolBuilder : public NXOpen::Builder
        {
            private: PlcSymbolBuilderImpl * m_plcsymbolbuilder_impl;
            private: friend class  _PlcSymbolBuilderBuilder;
            protected: PlcSymbolBuilder();
            public: ~PlcSymbolBuilder();
            /**Returns  the selection ParentObject (parent of the plc symbol) 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectINodeObject * SelectionParentObject
            (
            );
            /**Returns  the enum io type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::MemorySectionType MemorySection
            (
            );
            /**Sets  the enum io type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetMemorySection
            (
                NXOpen::AME::MemorySectionType memorySection /** memorysection */ 
            );
            /**Returns  the string symbol name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString SymbolName
            (
            );
            /**Sets  the string symbol name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSymbolName
            (
                const NXString & symbolName /** symbolname */ 
            );
            /**Sets  the string symbol name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetSymbolName
            (
                const char * symbolName /** symbolname */ 
            );
            /**Returns  the string description 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString Description
            (
            );
            /**Sets  the string description 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /**Sets  the string description 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetDescription
            (
                const char * description /** description */ 
            );
            /**Returns  the string hwaddress 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString HWAddress
            (
            );
            /**Sets  the string hwaddress 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetHWAddress
            (
                const NXString & hWAddress /** hwaddress */ 
            );
            /**Sets  the string hwaddress 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetHWAddress
            (
                const char * hWAddress /** hwaddress */ 
            );
            /**Returns  the int hwaddress offset byte 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int HWAddressOffsetByte
            (
            );
            /**Sets  the int hwaddress offset byte 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetHWAddressOffsetByte
            (
                int hWAddress /** hwaddress */ 
            );
            /**Returns  the int hwaddress offset bit 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int HWAddressOffsetBit
            (
            );
            /**Sets  the int hwaddress offset bit 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetHWAddressOffsetBit
            (
                int hWAddressOffsetBit /** hwaddressoffsetbit */ 
            );
            /** Get data type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::PlcDataType GetDataType
            (
            );
            /** Set data type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetDataType
            (
                NXOpen::AME::PlcDataType dataType /** datatype */ 
            );
            /**Returns  the string indicator 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString Indicator
            (
            );
            /**Sets  the string indicator 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetIndicator
            (
                const NXString & indicator /** indicator */ 
            );
            /**Sets  the string indicator 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetIndicator
            (
                const char * indicator /** indicator */ 
            );
            /**Returns  the object data type builder
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::DataTypeBuilder * DataTypeComp
            (
            );
            /**Returns  the data type source 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::PlcDataTypeSource DataTypeSource
            (
            );
            /**Sets  the data type source 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetDataTypeSource
            (
                NXOpen::AME::PlcDataTypeSource dataTypeSource /** datatypesource */ 
            );
            /**Returns  the project UDT selection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAMEBaseNode * UdtFromProject
            (
            );
            /**Returns  the library UDT selection
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Tooling::SelectReuseLibraryItemBuilder * SelectedUDTFromLibrary
            (
            );
            /**Returns  the string udt by name data type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString UdtByName
            (
            );
            /**Sets  the string udt by name data type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetUdtByName
            (
                const NXString & udtByName /** udtbyname */ 
            );
            /**Sets  the string udt by name data type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetUdtByName
            (
                const char * udtByName /** udtbyname */ 
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