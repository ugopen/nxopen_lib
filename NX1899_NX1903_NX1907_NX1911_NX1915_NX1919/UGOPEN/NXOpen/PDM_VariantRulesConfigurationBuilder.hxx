#ifndef NXOpen_PDM_VARIANTRULESCONFIGURATIONBUILDER_HXX_INCLUDED
#define NXOpen_PDM_VARIANTRULESCONFIGURATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_VariantRulesConfigurationBuilder.ja
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
#include <NXOpen/libnxopencpp_pdm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PDM
    {
        class VariantRulesConfigurationBuilder;
    }
    class Builder;
    namespace PDM
    {
        class _VariantRulesConfigurationBuilderBuilder;
        class VariantRulesConfigurationBuilderImpl;
        /**
                Represents an @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink  to be used for variant rules configuration.
             <br> To create a new instance of this class, use @link NXOpen::PDM::ConfigurationManager::CreateVariantRulesConfigurationBuilder  NXOpen::PDM::ConfigurationManager::CreateVariantRulesConfigurationBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  VariantRulesConfigurationBuilder : public NXOpen::Builder
        {
            private: VariantRulesConfigurationBuilderImpl * m_variantrulesconfigurationbuilder_impl;
            private: friend class  _VariantRulesConfigurationBuilderBuilder;
            protected: VariantRulesConfigurationBuilder();
            public: ~VariantRulesConfigurationBuilder();
            /** Returns the saved variant rules for the give context ID
                    The input contextId:
                    In case of default domain: it should be Teamcenter item ID.
                    In case of non-default domain: it should be the multifield key.
                    e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                     @return  variant rules from the given context 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: std::vector<NXString> GetVariantRulesForProductAssembly
            (
                const NXString & contextId /** multifield key in case of product assembly or collaborative design id */,
                const NXString & revId /** itemRev_id in case of product assembly*/
            );
            /** Returns the saved variant rules for the give context ID
                    The input contextId:
                    In case of default domain: it should be Teamcenter item ID.
                    In case of non-default domain: it should be the multifield key.
                    e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                     @return  variant rules from the given context 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            std::vector<NXString> GetVariantRulesForProductAssembly
            (
                const char * contextId /** multifield key in case of product assembly or collaborative design id */,
                const char * revId /** itemRev_id in case of product assembly*/
            );
            /** Returns selected variant rules stored inside @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink 
                    The input contextIds comprising of multifield key and itemRev_id:
                    In case of default domain: contextId should contain Teamcenter item ID.
                    In case of non-default domain: contextId should contain the multifield keys.
                    e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                    
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void GetVariantRulesSelectedForConfiguration
            (
                std::vector<NXString> & contextIds /** array of contextIds comprising of multifield key and itemRev_id from which variant rules are selected */,
                std::vector<NXString> & variantRules /** array of selected variant rules */
            );
            /** Adds given variant rules in case of multiple variant rules to @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink 
                    The input contextIds comprising of multifield key and itemRev_id:
                    In case of default domain: contextId should contain Teamcenter item ID.
                    In case of non-default domain: contextId should contain the multifield keys.
                    e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                    
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void AddVariantRulesToConfigure
            (
                const std::vector<NXString> & contextIds /** context id comprising of multifield key and itemRev_id in which variant rule resides */,
                const std::vector<NXString> & variantRules /** variant rules of corresponding context ids to be added */
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