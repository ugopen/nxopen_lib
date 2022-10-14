#ifndef NXOpen_GATEWAY_MASSPROPERTYOPTIONSBUILDER_HXX_INCLUDED
#define NXOpen_GATEWAY_MASSPROPERTYOPTIONSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Gateway_MassPropertyOptionsBuilder.ja
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
#include <NXOpen/libnxopencpp_gateway_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Gateway
    {
        class MassPropertyOptionsBuilder;
    }
    class Builder;
    namespace Gateway
    {
        class _MassPropertyOptionsBuilderBuilder;
        class MassPropertyOptionsBuilderImpl;
        /** Represents a @link NXOpen::Gateway::MassPropertyOptionsBuilder NXOpen::Gateway::MassPropertyOptionsBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Gateway::MassCollection::CreatePropertyOptionsBuilder  NXOpen::Gateway::MassCollection::CreatePropertyOptionsBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_GATEWAYEXPORT  MassPropertyOptionsBuilder : public NXOpen::Builder
        {
            /**the accuracy type */
            public: enum AccuracyTypes
            {
                AccuracyTypesValue1/** value1 */ ,
                AccuracyTypesValue2/** value2 */ ,
                AccuracyTypesValue3/** value3 */ ,
                AccuracyTypesValue4/** value4 */ ,
                AccuracyTypesValue5/** value5 */ ,
                AccuracyTypesValue6/** value6 */ 
            };

            private: MassPropertyOptionsBuilderImpl * m_masspropertyoptionsbuilder_impl;
            private: friend class  _MassPropertyOptionsBuilderBuilder;
            protected: MassPropertyOptionsBuilder();
            public: ~MassPropertyOptionsBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the accuracy 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Gateway::MassPropertyOptionsBuilder::AccuracyTypes AccuracyType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the accuracy 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetAccuracyType
            (
                NXOpen::Gateway::MassPropertyOptionsBuilder::AccuracyTypes accuracy /** accuracy */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the name of component group 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ComponentGroupName
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the name of component group 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetComponentGroupName
            (
                const NXString & componentGroupName /** componentgroupname */ 
            );
            /**Sets  the name of component group 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            void SetComponentGroupName
            (
                const char * componentGroupName /** componentgroupname */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the value of using source hierarchy 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseSourceHierarchy
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the value of using source hierarchy 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetUseSourceHierarchy
            (
                bool enabled /** enabled */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get Source Hierarchy  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void GetSourceHierarchy
            (
                std::vector<int> & variableSources /** variablesources */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set Source Hierarchy  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetSourceHierarchy
            (
                const std::vector<int> & variableSources /** variablesources */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the value of using selected component set 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseSelectedComponentSet
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the value of using selected component set 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetUseSelectedComponentSet
            (
                bool enabled /** enabled */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the value of using displayed part 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseDisplayedPart
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the value of using displayed part 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetUseDisplayedPart
            (
                bool enabled /** enabled */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the value of using selected components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseSelectedComponents
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the value of using selected components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetUseSelectedComponents
            (
                bool enabled /** enabled */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the value of using all components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseAllComponents
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the value of using all components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetUseAllComponents
            (
                bool enabled /** enabled */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mark color of display part 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: int MarkerColorOfDisplayedPart
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the mark color of display part 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetMarkerColorOfDisplayedPart
            (
                int color /** color */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mark color of selected component set 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: int MarkerColorOfSelectedComponentSet
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the mark color of selected component set 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetMarkerColorOfSelectedComponentSet
            (
                int color /** color */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mark color of selected components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: int MarkerColorOfSelectedComponents
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the mark color of selected components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetMarkerColorOfSelectedComponents
            (
                int color /** color */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mark color of all components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: int MarkerColorOfAllComponents
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the mark color of all components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetMarkerColorOfAllComponents
            (
                int color /** color */ 
            );

            /// \endcond 
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