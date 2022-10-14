#ifndef NXOpen_PARAMETERTABLE_HXX_INCLUDED
#define NXOpen_PARAMETERTABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ParameterTable.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class ParameterTable;
    class NXObject;
    class _ParameterTableBuilder;
    class ParameterTableImpl;
    /** Represents a parameter table.  <br> To create a new instance of this class, use @link NXOpen::ParameterTableCollection::Create  NXOpen::ParameterTableCollection::Create @endlink  <br> 
     <br>  Created in NX1899.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ParameterTable : public NXOpen::NXObject
    {
        private: ParameterTableImpl * m_parametertable_impl;
        private: friend class  _ParameterTableBuilder;
        protected: ParameterTable();
        public: ~ParameterTable();
        /**Returns  the table name.
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXString TableName
        (
        );
        /**Sets  the table name.
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetTableName
        (
            const NXString & tableName /** The name of the table. Must be unique*/
        );
        /**Sets  the table name.
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void SetTableName
        (
            const char * tableName /** The name of the table. Must be unique*/
        );
        /** Rename the table with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void RenameTable
        (
            const NXString & tableName /** The new name of the table. Must be unique*/
        );
        /** Rename the table with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void RenameTable
        (
            const char * tableName /** The new name of the table. Must be unique*/
        );
        /** Remove the table 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveTable
        (
        );
        /** Deactivate active configuration 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void DeactivateTable
        (
        );
        /** Get the number of configurations in the table @return  The number of configurations
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: int GetNumberOfConfigurations
        (
        );
        /** Add a new configuration with the specified name  @return  The index of new added configuration in the table
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: int AddConfiguration
        (
            const NXString & configurationName /** The name of the configuration. Must be unique into its table*/
        );
        /** Add a new configuration with the specified name  @return  The index of new added configuration in the table
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        int AddConfiguration
        (
            const char * configurationName /** The name of the configuration. Must be unique into its table*/
        );
        /** Remove a configuration with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveConfiguration
        (
            const NXString & configurationName /**  The name of the configuration to remove*/
        );
        /** Remove a configuration with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void RemoveConfiguration
        (
            const char * configurationName /**  The name of the configuration to remove*/
        );
        /** Set the name of a configuration 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetConfigurationName
        (
            int configIndex /** The index of the configuration to rename*/,
            const NXString & configurationName /** The new name of the configuration. Must be unique into its table */
        );
        /** Set the name of a configuration 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void SetConfigurationName
        (
            int configIndex /** The index of the configuration to rename*/,
            const char * configurationName /** The new name of the configuration. Must be unique into its table */
        );
        /** Rename a configuration with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void RenameConfiguration
        (
            const NXString & oldConfigurationName /** The name of the configuration to rename*/,
            const NXString & configurationName /** The new name of the configuration. Must be unique into its table */
        );
        /** Rename a configuration with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void RenameConfiguration
        (
            const char * oldConfigurationName /** The name of the configuration to rename*/,
            const char * configurationName /** The new name of the configuration. Must be unique into its table */
        );
        /** Get the number of expression in the table @return  The number of expressions
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: int GetNumberOfExpressions
        (
        );
        /** Get the name and label of the expression in the table @return  The expression name
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXString GetExpressionName
        (
            int index /** The index of the expression*/
        );
        /** Get the label of the expression in the table @return  The expression label
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXString GetExpressionLabel
        (
            int index /** The index of the expression*/
        );
        /** Add an expression with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void AddExpression
        (
            const NXString & expressionName /** The name of the expression to add*/
        );
        /** Add an expression with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void AddExpression
        (
            const char * expressionName /** The name of the expression to add*/
        );
        /** Remove an expression with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveExpression
        (
            const NXString & expressionName /** The name of the expression to remove*/
        );
        /** Remove an expression with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void RemoveExpression
        (
            const char * expressionName /** The name of the expression to remove*/
        );
        /** Replace an expression with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void ReplaceExpression
        (
            const NXString & oldExpressionName /** The name of the expression to rename*/,
            const NXString & expressionName /** The new name of the expression*/
        );
        /** Replace an expression with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void ReplaceExpression
        (
            const char * oldExpressionName /** The name of the expression to rename*/,
            const char * expressionName /** The new name of the expression*/
        );
        /** Replace an expression label with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void ReplaceExpressionLabel
        (
            const NXString & expressionName /** The name of the expression to replace*/,
            const NXString & labelName /** The new name of the expression*/
        );
        /** Replace an expression label with the specified name 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void ReplaceExpressionLabel
        (
            const char * expressionName /** The name of the expression to replace*/,
            const char * labelName /** The new name of the expression*/
        );
        /** Check if an expression is used by table  @return  If the expression is used by the table or not
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool IsExpressionUsedByTable
        (
            const NXString & expressionName /** The name of the expression to check*/
        );
        /** Check if an expression is used by table  @return  If the expression is used by the table or not
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        bool IsExpressionUsedByTable
        (
            const char * expressionName /** The name of the expression to check*/
        );
        /** Get an expression value of a configuration  @return  The value
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXString GetConfigurationValue
        (
            const NXString & configurationName /** The configuration name*/,
            const NXString & expressionName /** The name of the expression to get value*/
        );
        /** Get an expression value of a configuration  @return  The value
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        NXString GetConfigurationValue
        (
            const char * configurationName /** The configuration name*/,
            const char * expressionName /** The name of the expression to get value*/
        );
        /** Set an expression value into a configuration 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetConfigurationValue
        (
            int configIndex /** The configuration index*/,
            const NXString & expressionName /** The name of the expression to set value*/,
            const NXString & value /** The new value*/
        );
        /** Set an expression value into a configuration 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void SetConfigurationValue
        (
            int configIndex /** The configuration index*/,
            const char * expressionName /** The name of the expression to set value*/,
            const char * value /** The new value*/
        );
        /** Get a configuration index by name @return  The configuration name
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXString GetConfigurationName
        (
            int index /** The configuration index*/
        );
        /** Activate a configuration by index
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void ActivateConfiguration
        (
            int configIndex /** The configuration index*/,
            bool activate /** The active status*/
        );
        /** Activate a configuration by name
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void ActivateConfiguration
        (
            const NXString & configurationName /** The configuration name*/,
            bool activate /** The active status*/
        );
        /** Activate a configuration by name
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void ActivateConfiguration
        (
            const char * configurationName /** The configuration name*/,
            bool activate /** The active status*/
        );
        /** Returns if the configuration is active. @return  The active status
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool ConfigurationIsActive
        (
            int configIndex /** The configuration index*/
        );
        /** Returns if the configuration is active. @return  The active status
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool ConfigurationIsActive
        (
            const NXString & configurationName /** The configuration name*/
        );
        /** Returns if the configuration is active. @return  The active status
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        bool ConfigurationIsActive
        (
            const char * configurationName /** The configuration name*/
        );
        /** Returns the index of the active configuration. @return  The active configuration index
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: int GetActiveConfigurationIndex
        (
        );
        /** Sets table parameters.
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveReference
        (
        );
        /** Update the table from the external referenced file.
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void UpdateFromFile
        (
        );
        /** Update the model.
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void UpdateModel
        (
        );
    };
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