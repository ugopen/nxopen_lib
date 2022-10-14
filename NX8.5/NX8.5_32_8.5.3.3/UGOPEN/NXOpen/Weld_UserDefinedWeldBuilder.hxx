#ifndef NXOpen_WELD_USERDEFINEDWELDBUILDER_HXX_INCLUDED
#define NXOpen_WELD_USERDEFINEDWELDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_UserDefinedWeldBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Weld_CharacteristicsBuilder.hxx>
#include <NXOpen/Weld_UserDefinedWeldBuilder.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class UserDefinedWeldBuilder;
    }
    class Builder;
    class ScCollector;
    class SelectDisplayableObjectList;
    namespace Weld
    {
        class CharacteristicsBuilder;
    }
    namespace Weld
    {
        class _UserDefinedWeldBuilderBuilder;
        class UserDefinedWeldBuilderImpl;
        /** Represents a @link Weld::UserDefinedWeldBuilder Weld::UserDefinedWeldBuilder@endlink  builder  <br> To create a new instance of this class, use @link Weld::WeldManager::CreateUserDefinedWeldBuilder  Weld::WeldManager::CreateUserDefinedWeldBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AssignWeldPMI </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  UserDefinedWeldBuilder : public Builder
        {
            private: UserDefinedWeldBuilderImpl * m_userdefinedweldbuilder_impl;
            private: friend class  _UserDefinedWeldBuilderBuilder;
            protected: UserDefinedWeldBuilder();
            public: ~UserDefinedWeldBuilder();
            /**Returns  the select body 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectBody
            (
            );
            /**Returns  the select edge 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectEdge
            (
            );
            /**Returns  the select connect parts 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * SelectConnectParts
            (
            );
            /**Returns  the characteristics 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::CharacteristicsBuilder * Characteristics
            (
            );
            /**Returns  the assign weld pmi 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool AssignWeldPMI
            (
            );
            /**Sets  the assign weld pmi 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetAssignWeldPMI
            (
                bool assignWeldPMI /** assignweldpmi */ 
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