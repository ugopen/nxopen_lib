#ifndef NXOpen_PDM_SOAQUERY_HXX_INCLUDED
#define NXOpen_PDM_SOAQUERY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_SoaQuery.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/PDM_ListOfValues.hxx>
#include <NXOpen/PDM_PdmSearch.hxx>
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
        class SoaQuery;
    }
    namespace PDM
    {
        class ListOfValues;
    }
    namespace PDM
    {
        class PdmSearch;
    }
    namespace PDM
    {
        /** NX Manager search field data type */
        enum PdmSoaqueryNxmgrfielddatatype
        {
            PdmSoaqueryNxmgrfielddatatypeChar = 2001/** Char type */,
            PdmSoaqueryNxmgrfielddatatypeDate/** Date */,
            PdmSoaqueryNxmgrfielddatatypeDouble/** Double */,
            PdmSoaqueryNxmgrfielddatatypeFloat/** Float */,
            PdmSoaqueryNxmgrfielddatatypeInt/** Integer */,
            PdmSoaqueryNxmgrfielddatatypeBool/** Boolean */,
            PdmSoaqueryNxmgrfielddatatypeShort/** Short */,
            PdmSoaqueryNxmgrfielddatatypeString/** String */,
            PdmSoaqueryNxmgrfielddatatypeReference/** Reference */,
            PdmSoaqueryNxmgrfielddatatypeUntypedReference/** Untyped reference */,
            PdmSoaqueryNxmgrfielddatatypeExternalReference/** External reference */
        };

    }
    namespace PDM
    {
        class SoaQueryImpl;
        /** Represents search soa query to perform Teamcenter search
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  SoaQuery : public NXOpen::TransientObject
        {
            private: SoaQueryImpl * m_soaquery_impl;
            /// \cond NX_NO_DOC 
            public: explicit SoaQuery(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~SoaQuery();
            /** Add the field description to create an SOA query 
             <br>  @deprecated Deprecated in NX8.0.0.  It's not needed in any context of search based on queries. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  It's not needed in any context of search based on queries.") void AddFieldDescription
            (
                NXOpen::PDM::PdmSearch * searchVar /** pdm search structure */,
                NXOpen::PDM::PdmSoaqueryNxmgrfielddatatype type /** search field data type */,
                const NXString & name /** name of search   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & attrName /** search attribute  name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & defaultValue /** default value   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & logicalOperation /** logical operation for search criteria   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & mathOperation /** math operation for search criteria   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::PDM::ListOfValues * lov /** List of values */
            );
            /** Add the field description to create an SOA query 
             <br>  @deprecated Deprecated in NX8.0.0.  It's not needed in any context of search based on queries. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            void AddFieldDescription
            (
                NXOpen::PDM::PdmSearch * searchVar /** pdm search structure */,
                NXOpen::PDM::PdmSoaqueryNxmgrfielddatatype type /** search field data type */,
                const char * name /** name of search   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * attrName /** search attribute  name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * defaultValue /** default value   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * logicalOperation /** logical operation for search criteria   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * mathOperation /** math operation for search criteria   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::PDM::ListOfValues * lov /** List of values */
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