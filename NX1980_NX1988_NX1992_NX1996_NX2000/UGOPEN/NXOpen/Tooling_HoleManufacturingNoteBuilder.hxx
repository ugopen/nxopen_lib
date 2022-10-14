#ifndef NXOpen_TOOLING_HOLEMANUFACTURINGNOTEBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_HOLEMANUFACTURINGNOTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_HoleManufacturingNoteBuilder.ja
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
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Annotations_StyleBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class HoleManufacturingNoteBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    class Builder;
    class NXColor;
    class NXObject;
    class SelectNXObject;
    class SelectNXObjectList;
    namespace Tooling
    {
        class _HoleManufacturingNoteBuilderBuilder;
        class HoleManufacturingNoteBuilderImpl;
        /** Tooling builder for HoleManufacturingNote  <br> To create a new instance of this class, use @link NXOpen::Tooling::HoleManufacturingNoteCollection::CreateHoleManufacturingNoteBuilder  NXOpen::Tooling::HoleManufacturingNoteCollection::CreateHoleManufacturingNoteBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        DefineByViewOrHolesEnum </term> <description> 
         
        View </description> </item> 

        <item><term> 
         
        HoleIndexSize </term> <description> 
         
        3.5 </description> </item> 

        <item><term> 
         
        HoleIndexTypeEnum </term> <description> 
         
        UserDefinedAndNumber </description> </item> 

        <item><term> 
         
        HoleManufacturingNoteSize </term> <description> 
         
        3.5 </description> </item> 

        <item><term> 
         
        UseDifferentSubIndexForSameDiameterHoles </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  HoleManufacturingNoteBuilder : public NXOpen::Builder
        {
            /** the view selection or window selection type */
            public: enum DefineByViewOrHoles
            {
                DefineByViewOrHolesView/** view */ ,
                DefineByViewOrHolesHoles/** holes */ 
            };

            /** the hole index type */
            public: enum HoleIndexType
            {
                HoleIndexTypeUserDefinedAndNumber/** user defined and number */ ,
                HoleIndexTypeAlphabetic/** alphabetic */ ,
                HoleIndexTypeNumeric/** numeric */ 
            };

            private: HoleManufacturingNoteBuilderImpl * m_holemanufacturingnotebuilder_impl;
            private: friend class  _HoleManufacturingNoteBuilderBuilder;
            protected: HoleManufacturingNoteBuilder();
            public: ~HoleManufacturingNoteBuilder();
            /**Returns  the selection type enumeration 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::HoleManufacturingNoteBuilder::DefineByViewOrHoles DefineByViewOrHolesEnum
            (
            );
            /**Sets  the selection type enumeration 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetDefineByViewOrHolesEnum
            (
                NXOpen::Tooling::HoleManufacturingNoteBuilder::DefineByViewOrHoles defineByViewOrHoles /** definebyvieworholes */ 
            );
            /**Returns  the selected view 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectView
            (
            );
            /**Returns  the hole index type enumeration 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::HoleManufacturingNoteBuilder::HoleIndexType HoleIndexTypeEnum
            (
            );
            /**Sets  the hole index type enumeration 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetHoleIndexTypeEnum
            (
                NXOpen::Tooling::HoleManufacturingNoteBuilder::HoleIndexType holeIndexTypeEnum /** holeindextypeenum */ 
            );
            /**Returns  the selected holes 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectHoles
            (
            );
            /**Returns  the manufacturing information origin 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::OriginBuilder * HoleManufacturingNoteOrigin
            (
            );
            /**Returns  the use different sub index for same diameter holes 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseDifferentSubIndexForSameDiameterHoles
            (
            );
            /**Sets  the use different sub index for same diameter holes 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetUseDifferentSubIndexForSameDiameterHoles
            (
                bool useDifferentSubIndexForSameDiameterHoles /** usedifferentsubindexforsamediameterholes */ 
            );
            /**Returns  the hole index character size 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double HoleIndexSize
            (
            );
            /**Sets  the hole index character size 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetHoleIndexSize
            (
                double holeIndexSize /** holeindexsize */ 
            );
            /**Returns  the hole index character color 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * HoleIndexColor
            (
            );
            /**Sets  the hole index character color 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetHoleIndexColor
            (
                NXOpen::NXColor * holeIndexColor /** holeindexcolor */ 
            );
            /**Returns  the manufaturing information character size 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double HoleManufacturingNoteSize
            (
            );
            /**Sets  the manufaturing information character size 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetHoleManufacturingNoteSize
            (
                double holeManufacturingNoteSize /** holemanufacturingnotesize */ 
            );
            /**Returns  the manufaturing information character color 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * HoleManufacturingNoteColor
            (
            );
            /**Sets  the manufaturing information character color 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetHoleManufacturingNoteColor
            (
                NXOpen::NXColor * holeManufacturingNoteColor /** holemanufacturingnotecolor */ 
            );
            /**Returns  the hole manufacturing note style 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * HoleManufacturingNoteStyle
            (
            );
            /**Returns  the wizard type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int WizardType
            (
            );
            /**Sets  the wizard type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetWizardType
            (
                int wizardType /** wizardtype */ 
            );
            /**Returns  the created hole manufacturing note 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * CreatedHoleManufacturingNote
            (
            );
            /**Sets  the created hole manufacturing note 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetCreatedHoleManufacturingNote
            (
                NXOpen::NXObject * createdHoleManufacturingNote /** createdholemanufacturingnote */ 
            );
            /** The method to create hole index  @return  The hole index label tag 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::NXObject * CreateHoleIndexLabel
            (
                NXOpen::NXObject * viewTag /** The view to create hole index label */,
                const NXString & holeTypeIndex /** The hole hole index label string */,
                NXOpen::NXObject * faceTag /** The hole face data */,
                double holeDiameter /** The hole diameter */,
                const NXOpen::Point3d & holePos /** The hole position */,
                const NXString & holetype /** The hole type string */,
                bool reverseFlag /** The hole reversed flag */
            );
            /** The method to create hole index  @return  The hole index label tag 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            NXOpen::NXObject * CreateHoleIndexLabel
            (
                NXOpen::NXObject * viewTag /** The view to create hole index label */,
                const char * holeTypeIndex /** The hole hole index label string */,
                NXOpen::NXObject * faceTag /** The hole face data */,
                double holeDiameter /** The hole diameter */,
                const NXOpen::Point3d & holePos /** The hole position */,
                const char * holetype /** The hole type string */,
                bool reverseFlag /** The hole reversed flag */
            );
            /** The method to create manufaturing information as note  @return  The manufaturing information note tag 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::NXObject * CreateHoleManufacturingNoteAsNote
            (
                NXOpen::NXObject * viewTag /** The view to create hole index label */,
                std::vector<NXString> & holeManufacturingNoteVector /** The hole index label string */,
                const NXOpen::Point3d & point /** The location point data */
            );
            /** The method to cycle objects in view  @return  Output object 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::NXObject * CycleObjectsInView
            (
                NXOpen::NXObject * viewTag /** The view to cycle */,
                int vseqNumber /** The View Sequence Number of the View must NOT be DSS_ALL_VIEWS or DSS_NO_VIEWS */,
                bool isDrawing /** Is this view a drawing */,
                NXOpen::NXObject * inObject /** Input object */
            );
            /** The method to modify the style of the previewed note 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void ModifyStyle
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