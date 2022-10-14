#ifndef NXOpen_PDM_VARIANTCONFIGURATIONBUILDER_HXX_INCLUDED
#define NXOpen_PDM_VARIANTCONFIGURATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_VariantConfigurationBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/PDM_VariantConfigurationBuilder.hxx>
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
        class VariantConfigurationBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace PDM
    {
        class _VariantConfigurationBuilderBuilder;
        class VariantConfigurationBuilderImpl;
        /** Represents a builder class that performs variant rule configuration. 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  VariantConfigurationBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: VariantConfigurationBuilderImpl * m_variantconfigurationbuilder_impl;
            private: friend class  _VariantConfigurationBuilderBuilder;
            protected: VariantConfigurationBuilder();
            public: ~VariantConfigurationBuilder();
            /** Returns the saved variant rules for the give context ID
                    The input contextId:
                    In case of default domain: it should be Teamcenter item ID.
                    In case of non-default domain: it should be the multifield key.
                    e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                     @return  variant rules from the given context 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: std::vector<NXString> AskAvailableVariantRules
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
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            std::vector<NXString> AskAvailableVariantRules
            (
                const char * contextId /** multifield key in case of product assembly or collaborative design id */,
                const char * revId /** itemRev_id in case of product assembly*/
            );
            /** Returns selected variant rules stored inside @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink 
                    The input contextIds comprising of multifield key and itemRev_id:
                    In case of default domain: contextId should contain Teamcenter item ID.
                    In case of non-default domain: contextId should contain the multifield keys.
                    e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void GetVariantRuleTableInformation
            (
                std::vector<NXString> & contextIds /** array of contextIds comprising of multifield key and itemRev_id from which variant rules are selected */,
                std::vector<NXString> & variantRules /** array of selected variant rules */
            );
            /** Removes the given variant rule from @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink  if applicable
                    The input contextId comprising of multifield key and itemRev_id:
                   In case of default domain: contextId should contain Teamcenter item ID.
                    In case of non-default domain: contextId should contain the multifield keys.
                    e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void RemoveVariantRule
            (
                const NXString & contextId /** context id comprising of multifield key and itemRev_id in which variant rule resides */,
                const NXString & variantRule /** variant rule to be removed */
            );
            /** Removes the given variant rule from @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink  if applicable
                    The input contextId comprising of multifield key and itemRev_id:
                   In case of default domain: contextId should contain Teamcenter item ID.
                    In case of non-default domain: contextId should contain the multifield keys.
                    e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            void RemoveVariantRule
            (
                const char * contextId /** context id comprising of multifield key and itemRev_id in which variant rule resides */,
                const char * variantRule /** variant rule to be removed */
            );
            /** Adds given variant rules in case of multiple variant rules to @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink 
                    The input contextIds comprising of multifield key and itemRev_id:
                    In case of default domain: contextId should contain Teamcenter item ID.
                    In case of non-default domain: contextId should contain the multifield keys.
                    e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void AddMultipleVariantRules
            (
                const std::vector<NXString> & contextIds /** context id comprising of multifield key and itemRev_id in which variant rule resides */,
                const std::vector<NXString> & variantRules /** variant rules of corresponding context ids to be added */
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