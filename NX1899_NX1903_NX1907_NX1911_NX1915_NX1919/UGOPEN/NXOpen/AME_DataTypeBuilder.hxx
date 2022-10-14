#ifndef NXOpen_AME_DATATYPEBUILDER_HXX_INCLUDED
#define NXOpen_AME_DATATYPEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_DataTypeBuilder.ja
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
#include <NXOpen/AME_PlcTypes.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class DataTypeBuilder;
    }
    namespace AME
    {
        class SelectAMEBaseNode;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _DataTypeBuilderBuilder;
        class DataTypeBuilderImpl;
        /** JA class for the data type dialog <br> This object does not need a creator.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  DataTypeBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: DataTypeBuilderImpl * m_datatypebuilder_impl;
            private: friend class  _DataTypeBuilderBuilder;
            protected: DataTypeBuilder();
            public: ~DataTypeBuilder();
            /** The PopulatedDataTypes 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: std::vector<NXString> GetPopulatedDataTypes
            (
                NXOpen::AME::MemorySectionType sectionType /** sectiontype */ 
            );
            /**Returns the  DataType 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int SelectedDataTypePosition
            (
            );
            /**Sets the  DataType 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSelectedDataTypePosition
            (
                int dataTypePos /** datatypepos */ 
            );
            /**Returns  the DataTypeSource 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::PlcDataTypeSource DataTypeSource
            (
            );
            /**Sets  the DataTypeSource 
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
            /**Sets  the int datalength  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetDataLength
            (
                int dataLength /** datalength */ 
            );
            /**Returns  the int datalength  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int DataLength
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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