#ifndef NXOpen_VISUALREPORTING_CONDITION_HXX_INCLUDED
#define NXOpen_VISUALREPORTING_CONDITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     VisualReporting_Condition.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/VisualReporting_Property.hxx>
#include <NXOpen/libnxopencpp_visualreporting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace VisualReporting
    {
        class Condition;
    }
    class NXObject;
    namespace VisualReporting
    {
        class Property;
    }
    namespace VisualReporting
    {
        class _ConditionBuilder;
        class ConditionImpl;
        /** A Condition within a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
            
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_VISUALREPORTINGEXPORT  Condition : public NXOpen::NXObject
        {
            /** Represents the possible type options
                       for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . If the type is a
                       @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                       the type of value can be found from @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink .
                    */
            public: enum TypeOption
            {
                TypeOptionAndCondition/** and condition */ ,
                TypeOptionOrCondition/** or condition */ ,
                TypeOptionNotCondition/** not condition */ ,
                TypeOptionValueCondition/** value condition */ 
            };

            /** Represents the possible operator type options.
                       for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                    */
            public: enum OperatorOption
            {
                OperatorOptionEqualOperator/** equal operator */ ,
                OperatorOptionLessThanOperator/** less than operator */ ,
                OperatorOptionNotLessThanOperator/** not less than operator */ ,
                OperatorOptionGreaterThanOperator/** greater than operator */ ,
                OperatorOptionNotGreaterThanOperator/** not greater than operator */ ,
                OperatorOptionNotEqualOperator/** not equal operator */ ,
                OperatorOptionRegularExpressionOperator/** regular expression operator */ ,
                OperatorOptionContainsOperator/** contains operator */ ,
                OperatorOptionDoesNotContainOperator/** does not contain operator */ ,
                OperatorOptionOnOrBeforeOperator/** on or before operator */ ,
                OperatorOptionOnOrAfterOperator/** on or after operator */ 
            };

            private: ConditionImpl * m_condition_impl;
            private: friend class  _ConditionBuilder;
            protected: Condition();
            public: ~Condition();
            /**Returns  the @link NXOpen::VisualReporting::Condition::TypeOption NXOpen::VisualReporting::Condition::TypeOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 

                        Note that this @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  cannot be modified. 
                        Instead it is determined when creating this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  by using the appropriate function:
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::VisualReporting::Condition::TypeOption Type
            (
            );
            /**Returns  the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . If the
                        @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
                        deleted.
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::VisualReporting::Property * Property
            (
            );
            /**Sets  the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . If the
                        @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
                        deleted.
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: void SetProperty
            (
                NXOpen::VisualReporting::Property * property /** property */ 
            );
            /**Returns  the @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .

                        The returned data type will never be
                        @link NXOpen::VisualReporting::Property::DatatypeOptionUnknown NXOpen::VisualReporting::Property::DatatypeOptionUnknown@endlink .
                    
                        Note that this @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  cannot be modified. 
                        Instead it is specified when creating this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  by using the appropriate function:
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition@endlink 

                        Note that the @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink s created using the following functions do not
                        have @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink s and calling this function will cause an error for these:
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::VisualReporting::Property::DatatypeOption Datatype
            (
            );
            /**Returns  whether this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  requires user input.
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool HasUserSpecifiedValue
            (
            );
            /**Sets  whether this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  requires user input.
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: void SetHasUserSpecifiedValue
            (
                bool isUserSpecified /** isuserspecified */ 
            );
            /**Returns  the user prompt for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . Only useful for a condition where
                        @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  is true.
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString UserPrompt
            (
            );
            /**Sets  the user prompt for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . Only useful for a condition where
                        @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  is true.
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: void SetUserPrompt
            (
                const NXString & userPrompt /** userprompt */ 
            );
            /**Sets  the user prompt for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . Only useful for a condition where
                        @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  is true.
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            void SetUserPrompt
            (
                const char * userPrompt /** userprompt */ 
            );
            /**Returns  the description for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Description
            (
            );
            /**Sets  the description for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /**Sets  the description for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            void SetDescription
            (
                const char * description /** description */ 
            );
            /**Returns  the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Value
            (
            );
            /**Sets  the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: void SetValue
            (
                const NXString & conditionValue /** conditionvalue */ 
            );
            /**Sets  the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            void SetValue
            (
                const char * conditionValue /** conditionvalue */ 
            );
            /**Returns  the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::VisualReporting::Condition::OperatorOption OperatorType
            (
            );
            /**Sets  the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
                        Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                        @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: void SetOperatorType
            (
                NXOpen::VisualReporting::Condition::OperatorOption operatorType /** operatortype */ 
            );
            /**Returns  the parent condition of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . If this
                        condition has no parent or if the parent isn't a condition
                        then this returns NULL.

                        Note that this @link NXOpen::VisualReporting::Condition::ParentCondition NXOpen::VisualReporting::Condition::ParentCondition@endlink  cannot be modified. 
                        Instead it is determined when inserting this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  in the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
                        by using the appropriate function:
                         - @link NXOpen::VisualReporting::VisualReportBuilder::SetFilterConditionOfRule NXOpen::VisualReporting::VisualReportBuilder::SetFilterConditionOfRule@endlink 
                         - @link NXOpen::VisualReporting::VisualReportBuilder::AddChildToCondition NXOpen::VisualReporting::VisualReportBuilder::AddChildToCondition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::VisualReporting::Condition * ParentCondition
            (
            );
            /** Returns whether the given @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  is an immediate child of this condition
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsChildCondition
            (
                NXOpen::VisualReporting::Condition * childCondition /** The possible child Condition */
            );
            /** Return the specified child Condition from this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::VisualReporting::Condition * GetChildCondition
            (
                int index /** The index of the returned Condition. */
            );
            /** Returns all the child Conditions in this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::VisualReporting::Condition *> GetChildConditions
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
