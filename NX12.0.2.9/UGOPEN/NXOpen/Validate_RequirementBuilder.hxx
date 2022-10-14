#ifndef NXOpen_VALIDATE_REQUIREMENTBUILDER_HXX_INCLUDED
#define NXOpen_VALIDATE_REQUIREMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_RequirementBuilder.ja
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
#include <NXOpen/libnxopencpp_validate_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Validate
    {
        class RequirementBuilder;
    }
    class Builder;
    namespace Validate
    {
        class _RequirementBuilderBuilder;
        class RequirementBuilderImpl;
        /** Represents a @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Validate::RequirementCollection::CreateRequirementBuilder  NXOpen::Validate::RequirementCollection::CreateRequirementBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        DataTypeOption </td> <td> 
         
        Number </td> </tr> 

        <tr><td> 
         
        DefinitionMethodOption </td> <td> 
         
        SingleSidedComparison </td> </tr> 

        <tr><td> 
         
        RelationalOperatorOption </td> <td> 
         
        Equal </td> </tr> 

        <tr><td> 
         
        RelationalOperatorOptionOnMaximumValue </td> <td> 
         
        LessThan </td> </tr> 

        <tr><td> 
         
        RelationalOperatorOptionOnMinimumValue </td> <td> 
         
        LessThan </td> </tr> 

        <tr><td> 
         
        SeverityOption </td> <td> 
         
        Error </td> </tr> 

        </table>  

         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  RequirementBuilder : public NXOpen::Builder
        {
            /** This enum represents the severity level when a requirement is not satisfied */
            public: enum SeverityOptions
            {
                SeverityOptionsError/** error */ ,
                SeverityOptionsWarning/** warning */ ,
                SeverityOptionsInformation/** information */ 
            };

            /** This enum represents the data type of the value in requirement */
            public: enum DataTypeOptions
            {
                DataTypeOptionsNumber/** number */ ,
                DataTypeOptionsString/** string */ ,
                DataTypeOptionsBoolean/** boolean */ ,
                DataTypeOptionsInteger/** integer */ ,
                DataTypeOptionsPoint/** point */ 
            };

            /** This enum represents the type of requirement definition method */
            public: enum DefinitionMethodOptions
            {
                DefinitionMethodOptionsSingleSidedComparison/** single sided comparison */ ,
                DefinitionMethodOptionsDoubleSidedComparison/** double sided comparison */ ,
                DefinitionMethodOptionsSetOfValues/** set of values */ ,
                DefinitionMethodOptionsFormula/** formula */ 
            };

            /**  This enum represents the relational operator for comparing values */
            public: enum RelationalOperatorOptions
            {
                RelationalOperatorOptionsEqual/** equal */ ,
                RelationalOperatorOptionsNotEqual/** not equal */ ,
                RelationalOperatorOptionsLessThan/** less than */ ,
                RelationalOperatorOptionsLessThanOrEqual/** less than or equal */ ,
                RelationalOperatorOptionsGreaterThan/** greater than */ ,
                RelationalOperatorOptionsGreaterThanOrEqual/** greater than or equal */ 
            };

            /**  This enum represents the type of requirement */
            public: enum RequirementTypeOptions
            {
                RequirementTypeOptionsValidationLimit/** validation limit */ ,
                RequirementTypeOptionsDesignLimit/** design limit */ 
            };

            private: RequirementBuilderImpl * m_requirementbuilder_impl;
            private: friend class  _RequirementBuilderBuilder;
            protected: RequirementBuilder();
            public: ~RequirementBuilder();
            /**Returns  the name of requirement 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name of requirement 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name of requirement 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the severity option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::RequirementBuilder::SeverityOptions SeverityOption
            (
            );
            /**Sets  the severity option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSeverityOption
            (
                NXOpen::Validate::RequirementBuilder::SeverityOptions severityOption /** severityoption */ 
            );
            /**Returns  the data type option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::RequirementBuilder::DataTypeOptions DataTypeOption
            (
            );
            /**Sets  the data type option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDataTypeOption
            (
                NXOpen::Validate::RequirementBuilder::DataTypeOptions dataTypeOption /** datatypeoption */ 
            );
            /**Returns  the definition method option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::RequirementBuilder::DefinitionMethodOptions DefinitionMethodOption
            (
            );
            /**Sets  the definition method option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDefinitionMethodOption
            (
                NXOpen::Validate::RequirementBuilder::DefinitionMethodOptions definitionMethodOption /** definitionmethodoption */ 
            );
            /**Returns  the relational operator option between expression label and the value in single sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::RequirementBuilder::RelationalOperatorOptions RelationalOperatorOption
            (
            );
            /**Sets  the relational operator option between expression label and the value in single sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetRelationalOperatorOption
            (
                NXOpen::Validate::RequirementBuilder::RelationalOperatorOptions relationalOperatorOption /** relationaloperatoroption */ 
            );
            /**Returns  the value for single sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString SingleSidedValue
            (
            );
            /**Sets  the value for single sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSingleSidedValue
            (
                const NXString & singleSidedValue /** singlesidedvalue */ 
            );
            /**Sets  the value for single sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetSingleSidedValue
            (
                const char * singleSidedValue /** singlesidedvalue */ 
            );
            /**Returns  the minimum value in double sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString DoubleSidedMinimumValue
            (
            );
            /**Sets  the minimum value in double sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDoubleSidedMinimumValue
            (
                const NXString & doubleSidedMinimumValue /** doublesidedminimumvalue */ 
            );
            /**Sets  the minimum value in double sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetDoubleSidedMinimumValue
            (
                const char * doubleSidedMinimumValue /** doublesidedminimumvalue */ 
            );
            /**Returns  the relational operator between minimum value and expression label in double sided comparison:
                         minimum value &lt; or &lt;= [expression].
                        The valid operator is either LessThan or LessThanOrEqual.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::RequirementBuilder::RelationalOperatorOptions RelationalOperatorOptionOnMinimumValue
            (
            );
            /**Sets  the relational operator between minimum value and expression label in double sided comparison:
                         minimum value &lt; or &lt;= [expression].
                        The valid operator is either LessThan or LessThanOrEqual.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetRelationalOperatorOptionOnMinimumValue
            (
                NXOpen::Validate::RequirementBuilder::RelationalOperatorOptions relationalOperatorOnMinimumValue /** relationaloperatoronminimumvalue */ 
            );
            /**Returns  the relational operator between expression label and maximum value in double sided comparison:
                         [expression] &lt; or &lt;= maximum value.
                        The valid operator is either LessThan or LessThanOrEqual.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::RequirementBuilder::RelationalOperatorOptions RelationalOperatorOptionOnMaximumValue
            (
            );
            /**Sets  the relational operator between expression label and maximum value in double sided comparison:
                         [expression] &lt; or &lt;= maximum value.
                        The valid operator is either LessThan or LessThanOrEqual.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetRelationalOperatorOptionOnMaximumValue
            (
                NXOpen::Validate::RequirementBuilder::RelationalOperatorOptions relationalOperatorOnMaximumValue /** relationaloperatoronmaximumvalue */ 
            );
            /**Returns  the maximum value in double sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString DoubleSidedMaximumValue
            (
            );
            /**Sets  the maximum value in double sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDoubleSidedMaximumValue
            (
                const NXString & doubleSidedMaximumValue /** doublesidedmaximumvalue */ 
            );
            /**Sets  the maximum value in double sided comparison 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetDoubleSidedMaximumValue
            (
                const char * doubleSidedMaximumValue /** doublesidedmaximumvalue */ 
            );
            /** Returns the valid values  @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetValidValues
            (
            );
            /** Sets the valid values 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetValidValues
            (
                const std::vector<NXString> & validValues /** validvalues */ 
            );
            /**Returns   @brief  the user defined formula. Only effective when 
                    @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOption NXOpen::Validate::RequirementBuilder::DefinitionMethodOption @endlink and @link NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption @endlink  is set to 
                    @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula@endlink .  

             
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Formula
            (
            );
            /**Sets   @brief  the user defined formula. Only effective when 
                    @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOption NXOpen::Validate::RequirementBuilder::DefinitionMethodOption @endlink and @link NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption @endlink  is set to 
                    @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula@endlink .  

             
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetFormula
            (
                const NXString & formula /** formula */ 
            );
            /**Sets   @brief  the user defined formula. Only effective when 
                    @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOption NXOpen::Validate::RequirementBuilder::DefinitionMethodOption @endlink and @link NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption @endlink  is set to 
                    @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula@endlink .  

             
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetFormula
            (
                const char * formula /** formula */ 
            );
            /** Returns the requirement description  @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetRequirementDescription
            (
            );
            /** Sets the requirement description 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetRequirementDescription
            (
                const std::vector<NXString> & requirementDescription /** requirementdescription */ 
            );
            /**Returns  the requirement type option 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::RequirementBuilder::RequirementTypeOptions RequirementTypeOption
            (
            );
            /**Sets  the requirement type option 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRequirementTypeOption
            (
                NXOpen::Validate::RequirementBuilder::RequirementTypeOptions requirementTypeOption /** type to set on requirement*/
            );
            /**Returns  the tolerance for point type requirement 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: double RequirementTolerance
            (
            );
            /**Sets  the tolerance for point type requirement 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRequirementTolerance
            (
                double requirementTolerance /** tolerance value to be set on requirement */
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