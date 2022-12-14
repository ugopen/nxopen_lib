#ifndef NXOpen_MECHATRONICS_MATLABSIGNALCONNECTIONBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_MATLABSIGNALCONNECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_MATLABSignalConnectionBuilder.ja
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
#include <NXOpen/Mechatronics_MATLABClientBuilder.hxx>
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
        class MATLABSignalConnectionBuilder;
    }
    class Builder;
    namespace Mechatronics
    {
        class SignalAdapter;
    }
    class NXObject;
    namespace Mechatronics
    {
        class _MATLABSignalConnectionBuilderBuilder;
        class MATLABSignalConnectionBuilderImpl;
        /** Represents a @link Mechatronics::MATLABSignalConnectionBuilder Mechatronics::MATLABSignalConnectionBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Mechatronics::MATLABSignalConnectionCollection::CreateSignalConnectionBuilder  NXOpen::Mechatronics::MATLABSignalConnectionCollection::CreateSignalConnectionBuilder @endlink  <br> 
         <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder NXOpen::Mechatronics::SignalMappingConnectionBuilder@endlink  instead. <br>  

         <br>  Created in NX11.0.0.  <br>  
        */
        class NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder instead.") NXOPENCPP_MECHATRONICSEXPORT  MATLABSignalConnectionBuilder : public NXOpen::Builder
        {
            /** Represents the OPC signal data type. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This enum has no replacement. It is no longer supported. <br>  
            */
            public: enum NX_DEPRECATED("Deprecated in NX1899.0.0.  This enum has no replacement. It is no longer supported.") DataType
            {
                DataTypeUnknown/** unknown */,
                DataTypeInt/** integer */,
                DataTypeDouble/** float   */,
                DataTypeBool/** boolean */,
                DataTypeString/** string  */
            };

            private: MATLABSignalConnectionBuilderImpl * m_matlabsignalconnectionbuilder_impl;
            private: friend class  _MATLABSignalConnectionBuilderBuilder;
            protected: MATLABSignalConnectionBuilder();
            public: ~MATLABSignalConnectionBuilder();
            /**Returns  the adapter object. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder::Adapter NXOpen::Mechatronics::SignalMappingConnectionBuilder::Adapter@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder::Adapter instead.") NXOpen::Mechatronics::SignalAdapter * AdapterIdentify
            (
            );
            /**Sets  the adapter object. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetAdapter NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetAdapter@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetAdapter instead.") void SetAdapterIdentify
            (
                NXOpen::Mechatronics::SignalAdapter * adapterIdentify /** adapteridentify */ 
            );
            /**Returns  the signal object. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder::Signal NXOpen::Mechatronics::SignalMappingConnectionBuilder::Signal@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder::Signal instead.") NXOpen::NXObject * SignalIdentify
            (
            );
            /**Sets  the signal object. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetSignal NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetSignal@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetSignal instead.") void SetSignalIdentify
            (
                NXOpen::NXObject * signalIdentify /** signalidentify */ 
            );
            /**Returns  the MATLAB signal name. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder::ExternalSignalName NXOpen::Mechatronics::SignalMappingConnectionBuilder::ExternalSignalName@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder::ExternalSignalName instead.") NXString MATLABSignalName
            (
            );
            /**Sets  the MATLAB signal name. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetExternalSignalName NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetExternalSignalName@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Please use NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetExternalSignalName instead.") void SetMATLABSignalName
            (
                const NXString & matlabsignalName /** matlabsignalname */ 
            );
            /**Sets  the MATLAB signal name. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Please use @link NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetExternalSignalName NXOpen::Mechatronics::SignalMappingConnectionBuilder::SetExternalSignalName@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetMATLABSignalName
            (
                const char * matlabsignalName /** matlabsignalname */ 
            );
            /**Returns  the MATLAB signal type. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") NXOpen::Mechatronics::MATLABSignalConnectionBuilder::DataType MATLABSignalType
            (
            );
            /**Sets  the MATLAB signal type. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") void SetMATLABSignalType
            (
                NXOpen::Mechatronics::MATLABSignalConnectionBuilder::DataType matlabSignalType /** matlabsignaltype */ 
            );
            /**Returns  the MATLAB signal port type. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") NXOpen::Mechatronics::MATLABClientBuilder::DataPortType MATLABSignalPort
            (
            );
            /**Sets  the MATLAB signal port type. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") void SetMATLABSignalPort
            (
                NXOpen::Mechatronics::MATLABClientBuilder::DataPortType matlabSignalPort /** matlabsignalport */ 
            );
            /**Returns  the mapping result name. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") NXString ResultName
            (
            );
            /**Sets  the mapping result name. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") void SetResultName
            (
                const NXString & resultName /** resultname */ 
            );
            /**Sets  the mapping result name. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetResultName
            (
                const char * resultName /** resultname */ 
            );
            /**Returns  the mapping direction. 0 represent input, 1 represent output 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") int StreamIO
            (
            );
            /**Sets  the mapping direction. 0 represent input, 1 represent output 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") void SetStreamIO
            (
                int streamIO /** streamio */ 
            );
            /**Returns  the matlab model name. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") NXString ModelName
            (
            );
            /**Sets  the matlab model name. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported.") void SetModelName
            (
                const NXString & modelName /** modelname */ 
            );
            /**Sets  the matlab model name. 
             <br>  @deprecated Deprecated in NX1899.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetModelName
            (
                const char * modelName /** modelname */ 
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
