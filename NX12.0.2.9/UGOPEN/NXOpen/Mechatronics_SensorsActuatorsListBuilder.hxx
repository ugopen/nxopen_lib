#ifndef NXOpen_MECHATRONICS_SENSORSACTUATORSLISTBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_SENSORSACTUATORSLISTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_SensorsActuatorsListBuilder.ja
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
        class SensorsActuatorsListBuilder;
    }
    class Builder;
    namespace Mechatronics
    {
        class _SensorsActuatorsListBuilderBuilder;
        class SensorsActuatorsListBuilderImpl;
        /**  @brief  Represents a @link NXOpen::Mechatronics::SensorsActuatorsListBuilder NXOpen::Mechatronics::SensorsActuatorsListBuilder@endlink .  

           <br> To create a new instance of this class, use @link NXOpen::Mechatronics::PhysicsManager::CreateSensorsActuatorsListBuilder  NXOpen::Mechatronics::PhysicsManager::CreateSensorsActuatorsListBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  SensorsActuatorsListBuilder : public NXOpen::Builder
        {
             /**  @brief  Defines the parameter data.  

              */
            public:
            struct ParameterData
            {
                public: /** Parameter Name Text   */NXString Name;
                public: /** Parameter Value Text  */NXString Value;
                public: ParameterData() :
                    Name(),
                    Value()
                {
                }
                /** Constructor for the ParameterData struct. */ 
                public: ParameterData(const NXString &nameInitial /** Parameter Name Text   */, 
                        const NXString &valueInitial /** Parameter Value Text  */) :
                    Name(nameInitial),
                    Value(valueInitial)
                {
                }
            };

            private: SensorsActuatorsListBuilderImpl * m_sensorsactuatorslistbuilder_impl;
            private: friend class  _SensorsActuatorsListBuilderBuilder;
            protected: SensorsActuatorsListBuilder();
            public: ~SensorsActuatorsListBuilder();
            /**  @brief  Gets all parameter data.  

               @return  Array of Parameter data 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: std::vector<NXOpen::Mechatronics::SensorsActuatorsListBuilder::ParameterData> GetParameterData
            (
            );
            /**  @brief  Sets all parameter data.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetParameterData
            (
                const std::vector<NXOpen::Mechatronics::SensorsActuatorsListBuilder::ParameterData> & parameterData /** Array of Parameter data */
            );
            /**Returns   @brief  the simit template name  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString SimitTemplate
            (
            );
            /**Sets   @brief  the simit template name  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetSimitTemplate
            (
                const NXString & simitTemplate /** simittemplate */ 
            );
            /**Sets   @brief  the simit template name  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetSimitTemplate
            (
                const char * simitTemplate /** simittemplate */ 
            );
            /**Returns   @brief  the simit folder name  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString SimitFolder
            (
            );
            /**Sets   @brief  the simit folder name  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetSimitFolder
            (
                const NXString & simitTemplate /** simittemplate */ 
            );
            /**Sets   @brief  the simit folder name  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetSimitFolder
            (
                const char * simitTemplate /** simittemplate */ 
            );
            /**Returns   @brief  the object name  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString ObjectName
            (
            );
            /**Sets   @brief  the object name  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetObjectName
            (
                const NXString & objectName /** objectname */ 
            );
            /**Sets   @brief  the object name  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetObjectName
            (
                const char * objectName /** objectname */ 
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
