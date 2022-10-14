#ifndef NXOpen_MECHATRONICS_OPCUACLIENTBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_OPCUACLIENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_OPCUAClientBuilder.ja
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
#include <NXOpen/Mechatronics_SignalBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class OPCUAClientBuilder;
    }
    class Builder;
    class Part;
    namespace Mechatronics
    {
        class _OPCUAClientBuilderBuilder;
        class OPCUAClientBuilderImpl;
        /**
                Represents a @link NXOpen::Mechatronics::OPCUAClientBuilder NXOpen::Mechatronics::OPCUAClientBuilder@endlink  builder. 
             <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  OPCUAClientBuilder : public NXOpen::Builder
        {
             /**  @brief  Represents OPCUATag info definition structure.  

              */
            public:
            struct TagInfo
            {
                public: /** PLCTag Name          */NXString Name;
                public: /** IO type              */NXOpen::Mechatronics::SignalBuilder::ExternalSignalIOType EIOType;
                public: /** Data type            */NXOpen::Mechatronics::SignalBuilder::DataType EDataType;
                public: TagInfo() :
                    Name(),
                    EIOType((NXOpen::Mechatronics::SignalBuilder::ExternalSignalIOType)0),
                    EDataType((NXOpen::Mechatronics::SignalBuilder::DataType)0)
                {
                }
                /** Constructor for the TagInfo struct. */ 
                public: TagInfo(const NXString &nameInitial /** PLCTag Name          */, 
                        NXOpen::Mechatronics::SignalBuilder::ExternalSignalIOType eIOTypeInitial /** IO type              */, 
                        NXOpen::Mechatronics::SignalBuilder::DataType eDataTypeInitial /** Data type            */) :
                    Name(nameInitial),
                    EIOType(eIOTypeInitial),
                    EDataType(eDataTypeInitial)
                {
                }
            };

            private: OPCUAClientBuilderImpl * m_opcuaclientbuilder_impl;
            private: friend class  _OPCUAClientBuilderBuilder;
            protected: OPCUAClientBuilder();
            public: ~OPCUAClientBuilder();
            /**  @brief  Gets OPC UA instance names  

               @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: std::vector<NXString> GetServerNames
            (
            );
            /**  @brief  Sets OPC UA instance names  

              
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetServerNames
            (
                std::vector<NXString> & names /** names */ 
            );
            /**  @brief  Gets OPC UA instance Tags  

               @return  Array of TagInfos 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: std::vector<NXOpen::Mechatronics::OPCUAClientBuilder::TagInfo> GetServerTags
            (
                const NXString & serverName /** servername */ 
            );
            /**  @brief  Gets OPC UA instance Tags  

               @return  Array of TagInfos 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            std::vector<NXOpen::Mechatronics::OPCUAClientBuilder::TagInfo> GetServerTags
            (
                const char * serverName /** servername */ 
            );
            /**  @brief  Sets OPC UA instance Tags  

              
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetServerTags
            (
                const NXString & serverName /** servername */ ,
                const std::vector<NXOpen::Mechatronics::OPCUAClientBuilder::TagInfo> & tagInfos /** Array of TagInfos */
            );
            /**  @brief  Sets OPC UA instance Tags  

              
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetServerTags
            (
                const char * serverName /** servername */ ,
                const std::vector<NXOpen::Mechatronics::OPCUAClientBuilder::TagInfo> & tagInfos /** Array of TagInfos */
            );
            /**Returns   @brief  the selected configuration name  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SelectedConfigurationName
            (
            );
            /**Sets   @brief  the selected configuration name  

              
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetSelectedConfigurationName
            (
                const NXString & configurationName /** configurationname */ 
            );
            /**Sets   @brief  the selected configuration name  

              
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetSelectedConfigurationName
            (
                const char * configurationName /** configurationname */ 
            );
            /**Returns   @brief  the selected configuration part  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Part * SelectedConfigurationPart
            (
            );
            /**Sets   @brief  the selected configuration part  

              
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetSelectedConfigurationPart
            (
                NXOpen::Part * ownerPart /** ownerpart */ 
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