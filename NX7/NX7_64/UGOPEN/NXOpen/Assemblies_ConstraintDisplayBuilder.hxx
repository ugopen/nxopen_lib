#ifndef NXOpen_ASSEMBLIES_CONSTRAINTDISPLAYBUILDER_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_CONSTRAINTDISPLAYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ConstraintDisplayBuilder.ja
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
#include <NXOpen/Assemblies_ConstraintDisplayBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Assemblies
    {
        class ConstraintDisplayBuilder;
    }
    class Builder;
    class SelectDisplayableObjectList;
    namespace Assemblies
    {
        class _ConstraintDisplayBuilderBuilder;
        /** The @link Assemblies::ConstraintDisplayBuilder Assemblies::ConstraintDisplayBuilder@endlink  can be used to control visibility
                of constraints and optionally components.  Any selected constraint is shown, and any
                constraint that refers to geometry in selected components is shown (subject to the
                setting of the VisibleConstraintsRule).  All other constraints are hidden.
         <br> 
                If ChangeComponentVisibility is on, then selected components and components positioned by
                selected constraints are shown, and all other components are hidden.  If
                ChangeComponentVisibility is off, then component visibility is not affected.
         <br> 
         <br> 
                This builder operates on displayed constraints.  A displayed constraint represents a single
                assembly constraint in a given assembly, and need not be in the same part as the assembly
                constraint it represents.  An assembly may contain more than one displayed constraint for a
                given assembly constraint.
         <br> 
             <br> To create a new instance of this class, use @link Assemblies::AssemblyManager::CreateConstraintDisplayBuilder Assemblies::AssemblyManager::CreateConstraintDisplayBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ChangeComponentVisibility </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        FilterNavigator </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        VisibleConstraintsRule </td> <td> 
         
        BetweenComponents </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT ConstraintDisplayBuilder : public Builder
        {
            /** This enum is used to control which constraints are treated as connected to the selected
                        components. */
            public: enum VisibleConstraintsRuleOptions
            {
                VisibleConstraintsRuleOptionsBetweenComponents/** Show only constraints that refer only to selected components */,
                VisibleConstraintsRuleOptionsConnectedToComponents/** Show only constraints that refer at least once to a selected component */
            };

            private: friend class  _ConstraintDisplayBuilderBuilder;
            protected: ConstraintDisplayBuilder();
            /**Returns  the selected constraints and components.  All selected constraints and components are shown
                        when the builder is committed, and so are constraints and components connected to them.  <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * ObjectSelection
            (
            );
            /**Returns  the rule determining which constraints are treated as connected to the selected components.  <br> License requirements : None */
            public: NXOpen::Assemblies::ConstraintDisplayBuilder::VisibleConstraintsRuleOptions VisibleConstraintsRule
            (
            );
            /**Sets  the rule determining which constraints are treated as connected to the selected components.  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetVisibleConstraintsRule
            (
                NXOpen::Assemblies::ConstraintDisplayBuilder::VisibleConstraintsRuleOptions visibleConstraintsRule /** visibleconstraintsrule */ 
            );
            /**Returns  the flag indicating whether or not a Show Only operation should be done on the connecting
                        components.  <br> License requirements : None */
            public: bool ChangeComponentVisibility
            (
            );
            /**Sets  the flag indicating whether or not a Show Only operation should be done on the connecting
                        components.  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetChangeComponentVisibility
            (
                bool changeComponentVisibility /** changecomponentvisibility */ 
            );
            /**Returns  the flag indicating whether the assembly navigator should filter hidden constraints.  <br> License requirements : None */
            public: bool FilterNavigator
            (
            );
            /**Sets  the flag indicating whether the assembly navigator should filter hidden constraints.  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetFilterNavigator
            (
                bool filterNavigator /** filternavigator */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif