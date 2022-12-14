#ifndef NXOpen_GATEWAY_MASSASSIGNMENTBUILDER_HXX_INCLUDED
#define NXOpen_GATEWAY_MASSASSIGNMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Gateway_MassAssignmentBuilder.ja
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
        class MassAssignmentBuilder;
    }
    class Builder;
    class Expression;
    class SelectNXObjectList;
    namespace Gateway
    {
        class _MassAssignmentBuilderBuilder;
        class MassAssignmentBuilderImpl;
        /** Represents a @link NXOpen::Gateway::MassAssignmentBuilder NXOpen::Gateway::MassAssignmentBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Gateway::MassCollection::CreateAssignmentBuilder  NXOpen::Gateway::MassCollection::CreateAssignmentBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Area.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        AreaStatus </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        AssignmentStatus </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        Density.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        GravityCenterStatus </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        GravityCenterX.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        GravityCenterY.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        GravityCenterZ.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        InertiaStatus </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Mass.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        MassType </term> <description> 
         
        MassOnly </description> </item> 

        <item><term> 
         
        MomentsInertiaXX.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        MomentsInertiaYY.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        MomentsInertiaZZ.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        ProductsInertiaXY.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        ProductsInertiaXZ.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        ProductsInertiaYZ.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        ValueType </term> <description> 
         
        Asserted </description> </item> 

        <item><term> 
         
        Volume.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_GATEWAYEXPORT  MassAssignmentBuilder : public NXOpen::Builder
        {
            /** the value type*/
            public: enum ValueTypes
            {
                ValueTypesAsserted/** asserted */ ,
                ValueTypesUserDefined1/** user defined1 */ ,
                ValueTypesUserDefined2/** user defined2 */ ,
                ValueTypesUserDefined3/** user defined3 */ ,
                ValueTypesUserDefined4/** user defined4 */ 
            };

            /** the mass definition type*/
            public: enum MassTypes
            {
                MassTypesMassOnly/** mass only */ ,
                MassTypesDensityMass/** density mass */ ,
                MassTypesDensityVolume/** density volume */ ,
                MassTypesMassVolume/** mass volume */ 
            };

            private: MassAssignmentBuilderImpl * m_massassignmentbuilder_impl;
            private: friend class  _MassAssignmentBuilderBuilder;
            protected: MassAssignmentBuilder();
            public: ~MassAssignmentBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the objects 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * Objects
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the assignment status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool AssignmentStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the assignment status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetAssignmentStatus
            (
                bool assignmentStatus /** assignmentstatus */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the value type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Gateway::MassAssignmentBuilder::ValueTypes ValueType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the value type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetValueType
            (
                NXOpen::Gateway::MassAssignmentBuilder::ValueTypes valueType /** valuetype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mass type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Gateway::MassAssignmentBuilder::MassTypes MassType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the mass type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetMassType
            (
                NXOpen::Gateway::MassAssignmentBuilder::MassTypes massType /** masstype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mass 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Mass
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the density 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Density
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the volume 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Volume
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mass status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool MassStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the mass status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetMassStatus
            (
                bool massStatus /** massstatus */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the density status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool DensityStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the density status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetDensityStatus
            (
                bool densityStatus /** densitystatus */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the volume status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool VolumeStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the volume status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetVolumeStatus
            (
                bool volumeStatus /** volumestatus */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the area status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool AreaStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the area status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetAreaStatus
            (
                bool areaStatus /** areastatus */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the area 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Area
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mass center status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool GravityCenterStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the mass center status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetGravityCenterStatus
            (
                bool gravityCenterStatus /** gravitycenterstatus */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mass center x 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * GravityCenterX
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mass center y 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * GravityCenterY
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the mass center z 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * GravityCenterZ
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the inertia status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool InertiaStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the inertia status 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetInertiaStatus
            (
                bool inertiaStatus /** inertiastatus */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the moments of inertia xx 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MomentsInertiaXX
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the moments of inertia yy 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MomentsInertiaYY
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the moments of inertia zz 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MomentsInertiaZZ
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the products of inertia XY 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ProductsInertiaXY
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the products of inertia XZ 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ProductsInertiaXZ
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the products of inertia YZ 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ProductsInertiaYZ
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get the assignment values of the root part or user selected object, and save to the builder . 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void GetAssignmentValues
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the deriveOption 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: int DeriveOption
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the deriveOption 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void SetDeriveOption
            (
                int deriveOption /** deriveoption */ 
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
