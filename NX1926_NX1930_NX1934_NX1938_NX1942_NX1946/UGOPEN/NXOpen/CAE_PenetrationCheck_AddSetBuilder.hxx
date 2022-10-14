#ifndef NXOpen_CAE_PENETRATIONCHECK_ADDSETBUILDER_HXX_INCLUDED
#define NXOpen_CAE_PENETRATIONCHECK_ADDSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PenetrationCheck_AddSetBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace PenetrationCheck
        {
            class AddSetBuilder;
        }
    }
    class Builder;
    class Expression;
    class SelectNXObjectList;
    namespace CAE
    {
        namespace PenetrationCheck
        {
            class _AddSetBuilderBuilder;
            class AddSetBuilderImpl;
            /** Represents a @link CAE::PenetrationCheck::AddSet CAE::PenetrationCheck::AddSet@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::CaePart::CreatePenetrationCheckAddSetBuilder  NXOpen::CAE::CaePart::CreatePenetrationCheckAddSetBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            ElemThickness.Value </term> <description> 
             
            10 (millimeters part), 2.5 (inches part) </description> </item> 

            <item><term> 
             
            InterferenceBetween </term> <description> 
             
            MeshCollectorContainers </description> </item> 

            <item><term> 
             
            InterferenceOption </term> <description> 
             
            All </description> </item> 

            <item><term> 
             
            SelectionType </term> <description> 
             
            MeshObjects </description> </item> 

            <item><term> 
             
            ThicknessFactor.Value </term> <description> 
             
            1.0 </description> </item> 

            <item><term> 
             
            ThicknessSource </term> <description> 
             
            ElementAssociatedData </description> </item> 

            </list> 

             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  AddSetBuilder : public NXOpen::Builder
            {
                /** The selection types */
                public: enum SelectionTypeOptions
                {
                    SelectionTypeOptionsMeshObjects/** mesh objects */ ,
                    SelectionTypeOptionsContactDefinitions/** contact definitions */ 
                };

                /** the interference between types */
                public: enum InterferenceBetweenType
                {
                    InterferenceBetweenTypeMeshCollectorContainers/** mesh collector containers */ ,
                    InterferenceBetweenTypeMeshes/** meshes */ ,
                    InterferenceBetweenTypeComponentFEMs/** component fems */ 
                };

                /** the intereference types */
                public: enum InterferenceType
                {
                    InterferenceTypeAll/** all */ ,
                    InterferenceTypeIntersections/** intersections */ ,
                    InterferenceTypePenetrations/** penetrations */ 
                };

                /** the thickness definition types */
                public: enum ThicknessSourceType
                {
                    ThicknessSourceTypeElementAssociatedData/** element associated data */ ,
                    ThicknessSourceTypeUserDefined/** user defined */ 
                };

                private: AddSetBuilderImpl * m_addsetbuilder_impl;
                private: friend class  _AddSetBuilderBuilder;
                protected: AddSetBuilder();
                public: ~AddSetBuilder();
                /**Returns  the clearance set name. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString PenetrationSetName
                (
                );
                /**Sets  the clearance set name. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetPenetrationSetName
                (
                    const NXString & clearanceSetName /** clearancesetname */ 
                );
                /**Sets  the clearance set name. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                void SetPenetrationSetName
                (
                    const char * clearanceSetName /** clearancesetname */ 
                );
                /**Returns  the selection type 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::PenetrationCheck::AddSetBuilder::SelectionTypeOptions SelectionType
                (
                );
                /**Sets  the selection type 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetSelectionType
                (
                    NXOpen::CAE::PenetrationCheck::AddSetBuilder::SelectionTypeOptions selectionType /** selectiontype */ 
                );
                /**Returns  the selection 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * Selection
                (
                );
                /**Returns  the interference between 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::PenetrationCheck::AddSetBuilder::InterferenceBetweenType InterferenceBetween
                (
                );
                /**Sets  the interference between 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetInterferenceBetween
                (
                    NXOpen::CAE::PenetrationCheck::AddSetBuilder::InterferenceBetweenType interferenceBetween /** interferencebetween */ 
                );
                /**Returns  the interference option 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::PenetrationCheck::AddSetBuilder::InterferenceType InterferenceOption
                (
                );
                /**Sets  the interference option 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetInterferenceOption
                (
                    NXOpen::CAE::PenetrationCheck::AddSetBuilder::InterferenceType interferenceOption /** interferenceoption */ 
                );
                /**Returns  the thickness source 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::PenetrationCheck::AddSetBuilder::ThicknessSourceType ThicknessSource
                (
                );
                /**Sets  the thickness source 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetThicknessSource
                (
                    NXOpen::CAE::PenetrationCheck::AddSetBuilder::ThicknessSourceType thicknessSource /** thicknesssource */ 
                );
                /**Returns  the elem thickness 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ElemThickness
                (
                );
                /**Returns  the scaling factor 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ThicknessFactor
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