#ifndef NXOpen_ASSEMBLIES_COMPONENTPATTERN_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_COMPONENTPATTERN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ComponentPattern.ja
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
#include <NXOpen/Assemblies_ComponentPattern.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/PartLoadStatus.hxx>
#include <NXOpen/libnxopencpp_assemblies_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Assemblies
    {
        class ComponentPattern;
    }
    namespace Assemblies
    {
        class Component;
    }
    namespace Assemblies
    {
        class PatternMember;
    }
    class NXObject;
    class PartLoadStatus;
    namespace Assemblies
    {
        class _ComponentPatternBuilder;
        class ComponentPatternImpl;
        /** 
               Represents the component pattern class.
             <br> To create or edit an instance of this class, use @link NXOpen::Assemblies::ComponentPatternBuilder  NXOpen::Assemblies::ComponentPatternBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  ComponentPattern : public NXOpen::NXObject
        {
            private: ComponentPatternImpl * m_componentpattern_impl;
            private: friend class  _ComponentPatternBuilder;
            protected: ComponentPattern();
            public: ~ComponentPattern();
            /** Deletes the component pattern object.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void Delete
            (
                bool deleteComponents /** deletecomponents */ 
            );
            /** Suppresses the component pattern object.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void Suppress
            (
            );
            /** Unsuppresses the component pattern object.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void Unsuppress
            (
            );
            /** Displays the information of the component pattern.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void DisplayInformation
            (
            );
            /** Loads the parts containing data referenced by this pattern, 
                        including the parts that are patterned and parts containing 
                        the objects that define the pattern parameters.
                     @return  Error information for any part that could not be loaded. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: NXOpen::PartLoadStatus * LoadRelatedGeometry
            (
            );
            /** Gets the component pattern name.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetPatternName
            (
            );
            /** Gets the suppressed status of the component pattern. 
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetPatternSuppressedStatus
            (
            );
            /**  Gets the deferred status of the component pattern.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetPatternDeferredStatus
            (
            );
            /** Returns all the pattern members.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Assemblies::PatternMember *> GetAllPatternMembers
            (
            );
            /** Gets all the @link Assemblies::Component Assemblies::Component@endlink  that are selected for component pattern.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Assemblies::Component *> GetComponentsToPattern
            (
            );
            /** Changes the template component of a reference pattern to a pattern member at indices (firstBaseInstanceIndex, secondBaseInstanceIndex).
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void ChangeReferencePatternTemplate
            (
                int firstBaseInstanceIndex /** firstbaseinstanceindex */ ,
                int secondBaseInstanceIndex /** secondbaseinstanceindex */ 
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
