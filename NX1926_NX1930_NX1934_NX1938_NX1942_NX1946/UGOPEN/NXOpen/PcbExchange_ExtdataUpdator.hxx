#ifndef NXOpen_PCBEXCHANGE_EXTDATAUPDATOR_HXX_INCLUDED
#define NXOpen_PCBEXCHANGE_EXTDATAUPDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PcbExchange_ExtdataUpdator.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_pcbexchange_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PcbExchange
    {
        class ExtdataUpdator;
    }
    class Session;
    namespace PcbExchange
    {
        class ExtdataUpdatorImpl;
        /** Represents  a @link NXOpen::PcbExchange::ExtdataUpdator NXOpen::PcbExchange::ExtdataUpdator@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_PCBEXCHANGEEXPORT  ExtdataUpdator
        {
            private: ExtdataUpdatorImpl * m_extdataupdator_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ExtdataUpdator(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static ExtdataUpdator* theExtdataUpdator;
            /** Returns the ExtdataUpdator object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static ExtdataUpdator* GetExtdataUpdator(NXOpen::Session *owner);
            public: ~ExtdataUpdator();
            /** Method to import external data 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> Read
            (
                const NXString & fName /** fname */ ,
                std::vector<NXString> & layerNames /** layernames */ 
            );
            /** Method to import external data 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            std::vector<NXString> Read
            (
                const char * fName /** fname */ ,
                std::vector<NXString> & layerNames /** layernames */ 
            );
            /** Method to update external data 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void Update
            (
                const NXString & fName /** fname */ ,
                std::vector<NXString> & layerNames /** layernames */ ,
                std::vector<NXString> & netNames /** netnames */ ,
                bool bTextualFilter /** btextualfilter */ ,
                const NXString & textualFilterStr /** textualfilterstr */ 
            );
            /** Method to update external data 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            void Update
            (
                const char * fName /** fname */ ,
                std::vector<NXString> & layerNames /** layernames */ ,
                std::vector<NXString> & netNames /** netnames */ ,
                bool bTextualFilter /** btextualfilter */ ,
                const char * textualFilterStr /** textualfilterstr */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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
