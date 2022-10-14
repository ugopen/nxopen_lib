#ifndef NXOpen_VALIDATE_CHECKERNODE_HXX_INCLUDED
#define NXOpen_VALIDATE_CHECKERNODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_CheckerNode.ja
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
#include <NXOpen/Validate_Logger.hxx>
#include <NXOpen/Validate_Parameter.hxx>
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
        class CheckerNode;
    }
    namespace Validate
    {
        class Logger;
    }
    namespace Validate
    {
        class Parameter;
    }
    namespace Validate
    {
        class CheckerNodeImpl;
        /**  @brief Represents a checker that validator will use to check against part node.  

         
              <br> Checker node contains the information of checker class name and checker parameter attribute values. 
             If the checker class is a profile which contains child checker instances, you can set the enable flags to
             the child checker instances in the profile checker class to turn on or off the child checker instances. <br> 
            
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  CheckerNode : public NXOpen::TransientObject
        {
            private: CheckerNodeImpl * m_checkernode_impl;
            /// \cond NX_NO_DOC 
            public: explicit CheckerNode(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: virtual ~CheckerNode();
            /**Returns  the checker class name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString ClassName
            (
            );
            /**Sets  the checker class name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetClassName
            (
                const NXString & className /** checker class name */
            );
            /**Sets  the checker class name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetClassName
            (
                const char * className /** checker class name */
            );
            /**Returns  the customized formula lines of checker.
                     <br> For example: <br> 
                     <br> "Disabled?;False;save_log_in_part;True" <br> 
                     <br> For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help. <br> 
                    
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString AttributeCustomizedFormulas
            (
            );
            /**Sets  the customized formula lines of checker.
                     <br> For example: <br> 
                     <br> "Disabled?;False;save_log_in_part;True" <br> 
                     <br> For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help. <br> 
                    
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAttributeCustomizedFormulas
            (
                const NXString & formulaLines /** The formula lines of checker */
            );
            /**Sets  the customized formula lines of checker.
                     <br> For example: <br> 
                     <br> "Disabled?;False;save_log_in_part;True" <br> 
                     <br> For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help. <br> 
                    
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetAttributeCustomizedFormulas
            (
                const char * formulaLines /** The formula lines of checker */
            );
            /** Gets child checker instance names in a profile checker.  @return  The instance names of child checkers in the profile checker 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetChildCheckerInstanceNames
            (
            );
            /** Gets child checker instance names and enable flags in a profile checker.  @return  The enable flags of child checkers in the profile checker 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<bool> GetChildCheckerEnabledFlags
            (
                std::vector<NXString> & childCheckerInstances /** The instance names of child checkers in the profile checker */
            );
            /** Sets child checker enable flags in a profile checker. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetChildCheckerEnabledFlags
            (
                std::vector<NXString> & childCheckerInstances /** The instance names of child checkers in the profile checker */,
                const std::vector<bool> & enableFlags /** The enable flags of child checkers in the profile checker */
            );
            /** Gets enable flag of child checker instance in a profile checker.  @return  The enable flag of child checker in the profile checker. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool GetChildCheckerEnabledFlag
            (
                const NXString & childCheckerInstance /** The instance name of child checker in the profile checker */
            );
            /** Gets enable flag of child checker instance in a profile checker.  @return  The enable flag of child checker in the profile checker. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            bool GetChildCheckerEnabledFlag
            (
                const char * childCheckerInstance /** The instance name of child checker in the profile checker */
            );
            /** Sets enable flag of child checker instance in a profile checker. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetChildCheckerEnabledFlag
            (
                const NXString & childCheckerInstance /** The instance name of child checker in the profile checker */,
                bool enableFlag /** The enable flag of child checker in the profile checker. */
            );
            /** Sets enable flag of child checker instance in a profile checker. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetChildCheckerEnabledFlag
            (
                const char * childCheckerInstance /** The instance name of child checker in the profile checker */,
                bool enableFlag /** The enable flag of child checker in the profile checker. */
            );
            /** Gets a @link Validate::Parameter Validate::Parameter@endlink  of specified title.<br/>
                    A parameter can be customized using methods like @link Validate::Parameter::SetBooleanValue Validate::Parameter::SetBooleanValue@endlink ,
                    @link Validate::Parameter::SetIntValue Validate::Parameter::SetIntValue@endlink , @link Validate::Parameter::SetDoubleValue Validate::Parameter::SetDoubleValue@endlink ,
                    @link Validate::Parameter::SetStringValue Validate::Parameter::SetStringValue@endlink , etc.
                    
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::Parameter * GetParameter
            (
                const NXString & parameterTitle /** parametertitle */ 
            );
            /** Gets a @link Validate::Parameter Validate::Parameter@endlink  of specified title.<br/>
                    A parameter can be customized using methods like @link Validate::Parameter::SetBooleanValue Validate::Parameter::SetBooleanValue@endlink ,
                    @link Validate::Parameter::SetIntValue Validate::Parameter::SetIntValue@endlink , @link Validate::Parameter::SetDoubleValue Validate::Parameter::SetDoubleValue@endlink ,
                    @link Validate::Parameter::SetStringValue Validate::Parameter::SetStringValue@endlink , etc.
                    
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Validate::Parameter * GetParameter
            (
                const char * parameterTitle /** parametertitle */ 
            );
            /** Gets all the @link Validate::Parameter Validate::Parameter@endlink . 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Validate::Parameter *> GetParameters
            (
            );
            /**  @brief 
                    Asks the @link Validate::Logger Validate::Logger@endlink  instance designated to the @link Validate::CheckerNode Validate::CheckerNode@endlink .
                     

             
                    
                    To obtain an instance of @link Validate::CheckerNode Validate::CheckerNode@endlink , refer to @link Validate::Validator::AppendCheckerNode Validate::Validator::AppendCheckerNode@endlink .
                    
                     @return  The logger to log result.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::Logger * AskLogger
            (
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