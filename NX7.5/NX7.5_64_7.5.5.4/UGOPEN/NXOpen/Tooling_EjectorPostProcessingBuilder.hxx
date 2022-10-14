#ifndef NXOpen_TOOLING_EJECTORPOSTPROCESSINGBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_EJECTORPOSTPROCESSINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_EjectorPostProcessingBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_EjectorPostProcessingBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class EjectorPostProcessingBuilder;
    }
    class Builder;
    class Expression;
    class NXObject;
    class ScCollector;
    class SelectBody;
    class SelectNXObjectList;
    namespace Tooling
    {
        class _EjectorPostProcessingBuilderBuilder;
        class EjectorPostProcessingBuilderImpl;
        /** Represents a builder to be used to create Mold Wizard ejector post processing.  <br> To create a new instance of this class, use @link Tooling::EjectorPostProcessingCollection::CreateEjectorPostProcessingBuilder Tooling::EjectorPostProcessingCollection::CreateEjectorPostProcessingBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ActionType </td> <td> 
         
        AdjustLength </td> </tr> 

        <tr><td> 
         
        TrimPart </td> <td> 
         
        Notrimpart </td> </tr> 

        <tr><td> 
         
        TrimSurface </td> <td> 
         
        Face </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  EjectorPostProcessingBuilder : public Builder
        {
            /** The processing type: Trim, Adjust length and Untrim. */
            public: enum TrimMethod
            {
                TrimMethodAdjustLength/** Adjust Length */,
                TrimMethodSheetTrim/** Sheet Trim */,
                TrimMethodUntrim/** Untrim */
            };

            /** The trim part where to find a trim surface as tool to trim ejector pins. */
            public: enum TrimPartName
            {
                TrimPartNameNotrimpart/** No trim part */
            };

            /** The trim surface types. */
            public: enum TrimSufaceName
            {
                TrimSufaceNameFace/** Select faces */,
                TrimSufaceNameSheetBody/** Select sheet body */
            };

            private: EjectorPostProcessingBuilderImpl * m_ejectorpostprocessingbuilder_impl;
            private: friend class  _EjectorPostProcessingBuilderBuilder;
            protected: EjectorPostProcessingBuilder();
            public: ~EjectorPostProcessingBuilder();
            /**Returns  the trim method of ejector pin post processing.  <br> License requirements : None */
            public: NXOpen::Tooling::EjectorPostProcessingBuilder::TrimMethod ActionType
            (
            );
            /**Sets  the trim method of ejector pin post processing.  <br> License requirements : None */
            public: void SetActionType
            (
                NXOpen::Tooling::EjectorPostProcessingBuilder::TrimMethod actionType /** actiontype */ 
            );
            /**Returns  the target components which contains the target ejector pins to be trimmed.  <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * TargetComponents
            (
            );
            /**Returns  the trim part in which trim surface features are cycled.  <br> License requirements : None */
            public: NXOpen::Tooling::EjectorPostProcessingBuilder::TrimPartName TrimPart
            (
            );
            /**Sets  the trim part in which trim surface features are cycled.  <br> License requirements : None */
            public: void SetTrimPart
            (
                NXOpen::Tooling::EjectorPostProcessingBuilder::TrimPartName trimPart /** trimpart */ 
            );
            /**Returns  the trim surface used to trim an ejector pin.  <br> License requirements : None */
            public: NXOpen::Tooling::EjectorPostProcessingBuilder::TrimSufaceName TrimSurface
            (
            );
            /**Sets  the trim surface used to trim an ejector pin.  <br> License requirements : None */
            public: void SetTrimSurface
            (
                NXOpen::Tooling::EjectorPostProcessingBuilder::TrimSufaceName trimSurface /** trimsurface */ 
            );
            /**Returns  the sheet body used to trim an ejector pin.  <br> License requirements : None */
            public: NXOpen::SelectBody * ToolSheetBody
            (
            );
            /**Returns  the faces used to trim an ejector pin.  <br> License requirements : None */
            public: NXOpen::ScCollector * ToolFace
            (
            );
            /**Returns  the distance used to adjust the length of an ejector pin for the false body   <br> License requirements : None */
            public: NXOpen::Expression * FitDistance
            (
            );
            /**Returns  the offset value is used to create offset feature on the trimmed ejector pin true body.  <br> License requirements : None */
            public: NXOpen::Expression * OffsetValue
            (
            );
            /** Set details of the trim data.  <br> License requirements : None */
            public: void SetTrimDataDetails
            (
                int surfaceType /** the surface type. */,
                const std::vector<NXOpen::NXObject *> & targets /** array of target ejector pins. */,
                const std::vector<NXOpen::NXObject *> & tools /** array of tool objects. */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif