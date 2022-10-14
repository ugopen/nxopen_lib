#ifndef NXOpen_AUTOTESTPREFERENCESBUILDER_HXX_INCLUDED
#define NXOpen_AUTOTESTPREFERENCESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AutotestPreferencesBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/AutotestPreferencesBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    class AutotestPreferencesBuilder;
    class Builder;
    class _AutotestPreferencesBuilderBuilder;
    /** 
        Represents a class that is used for defining preferences when recording Autotest 
         <br> To create a new instance of this class, use @link DebugSession::CreateAutotestPreferencesBuilder DebugSession::CreateAutotestPreferencesBuilder@endlink  <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT AutotestPreferencesBuilder : public Builder
    {
        /** Enumeration used to define the language type when recording an Autotest journal */
        public: enum LanguageType
        {
            LanguageTypeVisualBasic/** Language type to Visual Basic output */,
            LanguageTypeCPlusPlus/** Language type to C++ output */,
            LanguageTypeJava/** Language type to Java output */,
            LanguageTypeCSharp/** Language type to C# output */
        };

        /** Enumeration used to define the language type when recording an Autotest journal. */
        public: enum ValidationOption
        {
            ValidationOptionNone/** Indicates that no auto validation statements are generated. */,
            ValidationOptionAtEnd/** Indicates that auto validation statements are generated at end of journal */,
            ValidationOptionAtEndAndAtUpdate/** Indicates that auto validation statements are generated at end of journal and updates */
        };

        /** Enumeration used to define subobject nesting type. */
        public: enum SubobjectNestingOption
        {
            SubobjectNestingOptionNone/** Do not nest subobjects inside their containing object's XML output. */,
            SubobjectNestingOptionNestSubobjects/** Nest subobjects inside their containing object's XML output. */
        };

        /** Enumeration used to define object details type. */
        public: enum ObjectDetailsOption
        {
            ObjectDetailsOptionHideDetails/** Hide the details of an object in its XML output. */,
            ObjectDetailsOptionShowDetails/** Show the details of an object in its XML output. */
        };

        /** Enumeration used to define collector validation. */
        public: enum CollectorValidationOption
        {
            CollectorValidationOptionNone/** Do not validate collectors. */,
            CollectorValidationOptionAll/** Validate all collectors */
        };

        private: friend class  _AutotestPreferencesBuilderBuilder;
        protected: AutotestPreferencesBuilder();
        /**Returns  the language being used for recording.  <br> License requirements : None */
        public: NXOpen::AutotestPreferencesBuilder::LanguageType Language
        (
        );
        /**Sets  the language being used for recording.  <br> License requirements : None */
        public: void SetLanguage
        (
            NXOpen::AutotestPreferencesBuilder::LanguageType language /** language */ 
        );
        /**Returns  the autovalidate  <br> License requirements : None */
        public: NXOpen::AutotestPreferencesBuilder::ValidationOption Autovalidate
        (
        );
        /**Sets  the autovalidate  <br> License requirements : None */
        public: void SetAutovalidate
        (
            NXOpen::AutotestPreferencesBuilder::ValidationOption autovalidate /** autovalidate */ 
        );
        /**Returns  the collector validation option  <br> License requirements : None */
        public: NXOpen::AutotestPreferencesBuilder::CollectorValidationOption CollectorValidation
        (
        );
        /**Sets  the collector validation option  <br> License requirements : None */
        public: void SetCollectorValidation
        (
            NXOpen::AutotestPreferencesBuilder::CollectorValidationOption collectorValidation /** collectorvalidation */ 
        );
        /**Returns  the subobject nesting option  <br> License requirements : None */
        public: NXOpen::AutotestPreferencesBuilder::SubobjectNestingOption SubobjectNesting
        (
        );
        /**Sets  the subobject nesting option  <br> License requirements : None */
        public: void SetSubobjectNesting
        (
            NXOpen::AutotestPreferencesBuilder::SubobjectNestingOption subobjectNesting /** subobjectnesting */ 
        );
        /**Returns  the object details option  <br> License requirements : None */
        public: NXOpen::AutotestPreferencesBuilder::ObjectDetailsOption ObjectDetails
        (
        );
        /**Sets  the object details option  <br> License requirements : None */
        public: void SetObjectDetails
        (
            NXOpen::AutotestPreferencesBuilder::ObjectDetailsOption objectDetails /** objectdetails */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif