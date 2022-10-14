#ifndef NXOpen_AME_DB_DOCUMENTSTRUCTURE_HXX_INCLUDED
#define NXOpen_AME_DB_DOCUMENTSTRUCTURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_DB_DocumentStructure.ja
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
#include <NXOpen/AME_DB_DocumentStructure.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        namespace DB
        {
            class DocumentStructure;
        }
    }
    namespace AME
    {
        namespace DB
        {
            class _DocumentStructureBuilder;
            class DocumentStructureImpl;
            /** Class to define Document Structure object <br> This object does not need a creator.  <br> 
             <br>  Created in NX11.0.0.  <br>  
            */
            class AMEOPENCPPEXPORT  DocumentStructure : public NXOpen::TaggedObject
            {
                /** Represents the attribute for Document Structure */
                public: enum Attribute
                {
                    AttributeNone/** none */ ,
                    AttributeFunction/** function */ ,
                    AttributeLocation/** location */ ,
                    AttributeProduct/** product */ ,
                    AttributeDcc/** dcc */ 
                };

                private: DocumentStructureImpl * m_documentstructure_impl;
                private: friend class  _DocumentStructureBuilder;
                protected: DocumentStructure();
                public: ~DocumentStructure();
                /** Set all four attributes of Document Structure order in sequence. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
                public: void SetDocumentStructure
                (
                    NXOpen::AME::DB::DocumentStructure::Attribute firstAttr /** firstattr */ ,
                    NXOpen::AME::DB::DocumentStructure::Attribute secondAttr /** secondattr */ ,
                    NXOpen::AME::DB::DocumentStructure::Attribute thirdAttr /** thirdattr */ ,
                    NXOpen::AME::DB::DocumentStructure::Attribute fourthAttr /** fourthattr */ 
                );
                /** Set any three attributes of Document Structure order in sequence 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
                public: void SetDocumentStructure
                (
                    NXOpen::AME::DB::DocumentStructure::Attribute firstAttr /** firstattr */ ,
                    NXOpen::AME::DB::DocumentStructure::Attribute secondAttr /** secondattr */ ,
                    NXOpen::AME::DB::DocumentStructure::Attribute thirdAttr /** thirdattr */ 
                );
                /** Set any two attributes of Document Structure order in sequence. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
                public: void SetDocumentStructure
                (
                    NXOpen::AME::DB::DocumentStructure::Attribute firstAttr /** firstattr */ ,
                    NXOpen::AME::DB::DocumentStructure::Attribute secondAttr /** secondattr */ 
                );
                /** Set any one attribute of Document Structure order. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
                public: void SetDocumentStructure
                (
                    NXOpen::AME::DB::DocumentStructure::Attribute firstAttr /** firstattr */ 
                );
                /** Get the Document Structure string from Document Structur object.  @return  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
                public: NXString GetDocumentStructureString
                (
                );
                /** Set the Classification Code. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
                public: void SetClassificationCode
                (
                    const NXString & dccString /** dccstring */ 
                );
                /** Set the Classification Code. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
                void SetClassificationCode
                (
                    const char * dccString /** dccstring */ 
                );
                /** Get the Classification Code.  @return  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
                public: NXString GetClassificationCode
                (
                );
            };
        }
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