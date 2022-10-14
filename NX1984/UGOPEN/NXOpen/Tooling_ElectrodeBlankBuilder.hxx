#ifndef NXOpen_TOOLING_ELECTRODEBLANKBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_ELECTRODEBLANKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_ElectrodeBlankBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_CloneObject.hxx>
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
        class ElectrodeBlankBuilder;
    }
    namespace Assemblies
    {
        class SelectComponent;
    }
    class Builder;
    class Expression;
    class SelectBodyList;
    class SelectFace;
    class TaggedObject;
    namespace Tooling
    {
        class CloneObject;
    }
    namespace Tooling
    {
        class _ElectrodeBlankBuilderBuilder;
        class ElectrodeBlankBuilderImpl;
        /** Design electrode blank builder to create an electrode blank for the selected body.  <br> To create a new instance of this class, use @link NXOpen::Tooling::ElectrodeDesignCollection::CreateBlankBuilder  NXOpen::Tooling::ElectrodeDesignCollection::CreateBlankBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Angle.Value </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        BlendRadius.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        ExtensionHeight.Value </term> <description> 
         
        5 (millimeters part), 0.2 (inches part) </description> </item> 

        <item><term> 
         
        JointMethod </term> <description> 
         
        Extrude </description> </item> 

        <item><term> 
         
        KeepSize </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        KeepZValueInSameMSet </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Material </term> <description> 
         
        Copper </description> </item> 

        <item><term> 
         
        ReferencePointPrecision </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        Rename </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RotationAngle.Value </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RoundCrossLinesPosition </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Shape </term> <description> 
         
        Block </description> </item> 

        <item><term> 
         
        UniteBodies </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        XRefValue.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        YRefValue.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        ZRefValue.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  ElectrodeBlankBuilder : public NXOpen::Builder
        {
            /** Represents the electrode blank shape option. */
            public: enum BlankShape
            {
                BlankShapeBlock/** the shape of the blank is block */,
                BlankShapeCylinder/** the shape of the blank is cylinder */,
                BlankShapeUndercut/** the shape of the blank is block to spark undercut area */
            };

            /** Represents the blank material option. */
            public: enum BlankMaterial
            {
                BlankMaterialCopper/** the material of the blank is copper */,
                BlankMaterialGraphite/** the material of the blank is graphite */
            };

            /** Represents the transition type between head bodies and the blank. */
            public: enum JointObject
            {
                JointObjectExtrude/** extrude body from joint face to blank */,
                JointObjectOffset/** create offset feature from joint face to blank */,
                JointObjectNone/** nothing to do */
            };

            private: ElectrodeBlankBuilderImpl * m_electrodeblankbuilder_impl;
            private: friend class  _ElectrodeBlankBuilderBuilder;
            protected: ElectrodeBlankBuilder();
            public: ~ElectrodeBlankBuilder();
            /**Returns  the head bodies to be used to create a blank. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * HeadBodies
            (
            );
            /**Returns  the blank to be edited. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponent * Blank
            (
            );
            /**Returns  the shape of the blank. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::ElectrodeBlankBuilder::BlankShape Shape
            (
            );
            /**Sets  the shape of the blank. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetShape
            (
                NXOpen::Tooling::ElectrodeBlankBuilder::BlankShape shape /** shape */ 
            );
            /**Returns  the material of the blank. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::ElectrodeBlankBuilder::BlankMaterial Material
            (
            );
            /**Sets  the material of the blank. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetMaterial
            (
                NXOpen::Tooling::ElectrodeBlankBuilder::BlankMaterial material /** material */ 
            );
            /**Returns  the face to create a joint object between the blank and head bodies. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * JointFace
            (
            );
            /**Returns  the joint object type. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::ElectrodeBlankBuilder::JointObject JointMethod
            (
            );
            /**Sets  the joint object type. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetJointMethod
            (
                NXOpen::Tooling::ElectrodeBlankBuilder::JointObject jointMethod /** jointmethod */ 
            );
            /**Returns  the default extension height between head bodies and the blank. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ExtensionHeight
            (
            );
            /**Returns  the angle of the joint object. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );
            /**Returns  the default blend radius of blended edges. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BlendRadius
            (
            );
            /**Returns  the X value of the blank origin in the current machine set coordinator. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * XRefValue
            (
            );
            /**Returns  the Y value of the blank origin in the current machine set coordinator. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * YRefValue
            (
            );
            /**Returns  the Z value of the blank origin in the current machine set coordinator. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ZRefValue
            (
            );
            /**Returns  the rotation angle of blank. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RotationAngle
            (
            );
            /**Returns  the option to use the part name management dialog box or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool Rename
            (
            );
            /**Sets  the option to use the part name management dialog box or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetRename
            (
                bool rename /** rename */ 
            );
            /**Returns  the option to keep size of the blank or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool KeepSize
            (
            );
            /**Sets  the option to keep size of the blank or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetKeepSize
            (
                bool keepSize /** keepsize */ 
            );
            /**Returns  the current machine set under which a blank is added. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * MsetPart
            (
            );
            /**Sets  the current machine set under which a blank is added. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetMsetPart
            (
                NXOpen::TaggedObject * mset /** the machine set part */
            );
            /**Returns  the precision of the reference coordinates in the machine set csys. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double ReferencePointPrecision
            (
            );
            /**Sets  the precision of the reference coordinates in the machine set csys. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetReferencePointPrecision
            (
                double precision /** precision value */
            );
            /**Returns  the ratio of cross center lines. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double CrossLinesRatio
            (
            );
            /**Sets  the ratio of cross center lines. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetCrossLinesRatio
            (
                double ratio /** ratio */
            );
            /**Returns  the option to specify whether to keep the Z values of all blanks in the current machine set CSYS. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool KeepZValueInSameMSet
            (
            );
            /**Sets  the option to specify whether to keep the Z values of all blanks in the current machine set CSYS. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetKeepZValueInSameMSet
            (
                bool keepValue /** keep z value in machine set or not */
            );
            /**Returns  the option to round the position of cross lines or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool RoundCrossLinesPosition
            (
            );
            /**Sets  the option to round the position of cross lines or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetRoundCrossLinesPosition
            (
                bool round /** round cross lines or not */
            );
            /**Returns  the option to unite head bodies, the extension and the blank or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool UniteBodies
            (
            );
            /**Sets  the option to unite head bodies, the extension and the blank or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetUniteBodies
            (
                bool unite /** unite head, extension and blank together or not */
            );
            /**Returns  the reusable part builder. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * ReusablePartBuilder
            (
            );
            /**Sets  the reusable part builder. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetReusablePartBuilder
            (
                NXOpen::TaggedObject * builderTag /** reusable part builder tag */
            );
            /**Returns  the multi position builder. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * MultiPositionBuilder
            (
            );
            /**Sets  the multi position builder. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetMultiPositionBuilder
            (
                NXOpen::TaggedObject * builderTag /** multi position builder tag */
            );
            /**Returns  the blank matrix. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Matrix3x3 BlankMatrix
            (
            );
            /**Sets  the blank matrix. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetBlankMatrix
            (
                const NXOpen::Matrix3x3 & matrix /** blank matrix */
            );
            /**Returns  the blank reference point. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d ReferenceCenter
            (
            );
            /**Sets  the blank reference point. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void SetReferenceCenter
            (
                const NXOpen::Point3d & point /** blank position */
            );
            /** Update the data of the blank. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void UpdateBlankData
            (
                const NXString & registerPath /** register path of the blank part */,
                const NXString & dataPath /** data path of the blank part */,
                const NXString & modelPath /** model path of the blank part */,
                const NXString & bitmapPath /** bitmap path of the blank part */,
                const NXString & material /** material of the blank part */,
                std::vector<NXString> & paraNames /** parameter name the blank part */,
                std::vector<NXString> & paraValues /** parameter value the blank part */
            );
            /** Update the data of the blank. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            void UpdateBlankData
            (
                const char * registerPath /** register path of the blank part */,
                const char * dataPath /** data path of the blank part */,
                const char * modelPath /** model path of the blank part */,
                const char * bitmapPath /** bitmap path of the blank part */,
                const char * material /** material of the blank part */,
                std::vector<NXString> & paraNames /** parameter name the blank part */,
                std::vector<NXString> & paraValues /** parameter value the blank part */
            );
            /** Creates clone object. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::CloneObject * CreateCloneObject
            (
                int applicationType /** applicationtype */ ,
                int installationMethod /** installationmethod */ ,
                const NXString & partToBeInstalled /** parttobeinstalled */ ,
                const NXString & folderToSaveParts /** foldertosaveparts */ ,
                const NXString & projectName /** projectname */ 
            );
            /** Creates clone object. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Tooling::CloneObject * CreateCloneObject
            (
                int applicationType /** applicationtype */ ,
                int installationMethod /** installationmethod */ ,
                const char * partToBeInstalled /** parttobeinstalled */ ,
                const char * folderToSaveParts /** foldertosaveparts */ ,
                const char * projectName /** projectname */ 
            );
            /** Update display name of the blank. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            public: void UpdateDisplayName
            (
                const NXString & displayName /** display name of the blank part */
            );
            /** Update display name of the blank. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_electrode_wizard ("NX Electrode Wizard") */
            void UpdateDisplayName
            (
                const char * displayName /** display name of the blank part */
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