#ifndef NXOpen_VALIDATE_CHECKTHERMALDISTORTIONBUILDER_HXX_INCLUDED
#define NXOpen_VALIDATE_CHECKTHERMALDISTORTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_CheckThermalDistortionBuilder.ja
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
#include <NXOpen/GeometricUtilities_DisplayResolutionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Validate_SelectionAndPlacementBuilder.hxx>
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
        class CheckThermalDistortionBuilder;
    }
    class Builder;
    class Expression;
    namespace GeometricUtilities
    {
        class DisplayResolutionBuilder;
    }
    namespace Validate
    {
        class SelectionAndPlacementBuilder;
    }
    namespace Validate
    {
        class _CheckThermalDistortionBuilderBuilder;
        class CheckThermalDistortionBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents a Check Thermal Distortion builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckThermalDistortionBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckThermalDistortionBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BuildPlateTemperature.Value </term> <description> 
         
        353.15 </description> </item> 

        <item><term> 
         
        BuildPlateThickness.Value </term> <description> 
         
        3 (millimeters part), 0.2 (inches part) </description> </item> 

        <item><term> 
         
        CriticalAngle.Value </term> <description> 
         
        40 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.AngleTolerance </term> <description> 
         
        15.0 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.EdgeTolerance </term> <description> 
         
        0.005 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.FaceTolerance </term> <description> 
         
        0.005 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.Resolution </term> <description> 
         
        Standard </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.WidthTolerance </term> <description> 
         
        0.3 </description> </item> 

        <item><term> 
         
        ElementSize.Value </term> <description> 
         
        2 (millimeters part), 0.08 (inches part) </description> </item> 

        <item><term> 
         
        LayerThickness.Value </term> <description> 
         
        0.03 (millimeters part), 0.040 (inches part) </description> </item> 

        <item><term> 
         
        NumberOfLasers.Value </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        PrinterDiameter.Value </term> <description> 
         
        300.0 (millimeters part), 8.0 (inches part) </description> </item> 

        <item><term> 
         
        PrinterHeight.Value </term> <description> 
         
        300.0 (millimeters part), 8.0 (inches part) </description> </item> 

        <item><term> 
         
        PrinterLength.Value </term> <description> 
         
        300.0 (millimeters part), 8.0 (inches part) </description> </item> 

        <item><term> 
         
        PrinterWidth.Value </term> <description> 
         
        300.0 (millimeters part), 8.0 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  CheckThermalDistortionBuilder : public NXOpen::Builder
        {
            /** Represents the printer shape type */

            /// \cond NX_NO_DOC 
            public: enum PrinterShapeTypes
            {
                PrinterShapeTypesBlock/** printer volume shape is block */,
                PrinterShapeTypesCylinder/** cylinder */ 
            };


            /// \endcond 
            /** Represents the printer shape type */

            /// \cond NX_NO_DOC 
            public: enum JobStatusType
            {
                JobStatusTypeQueued/** Job is Queued */,
                JobStatusTypeProcessing/** Job Under Processing */,
                JobStatusTypeCompleted/** Job Completed Successfully */,
                JobStatusTypeError/** Error in Computation */,
                JobStatusTypeUnknown/** Job Status Unknown or Job Missing */
            };


            /// \endcond 
            private: CheckThermalDistortionBuilderImpl * m_checkthermaldistortionbuilder_impl;
            private: friend class  _CheckThermalDistortionBuilderBuilder;
            protected: CheckThermalDistortionBuilder();
            public: ~CheckThermalDistortionBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the selection and placement builder
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::SelectionAndPlacementBuilder * SelectionAndPlacement
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the printer material 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString PartMaterial
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the printer material 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPartMaterial
            (
                const NXString & partMaterial /** partmaterial */ 
            );
            /**Sets  the printer material 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            void SetPartMaterial
            (
                const char * partMaterial /** partmaterial */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the material enum 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: int MaterialEnum
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the material enum 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMaterialEnum
            (
                int materialEnum /** materialenum */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the printer name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString PrinterName
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the printer name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPrinterName
            (
                const NXString & printerName /** printername */ 
            );
            /**Sets  the printer name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            void SetPrinterName
            (
                const char * printerName /** printername */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the shape type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::CheckThermalDistortionBuilder::PrinterShapeTypes PrinterShape
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the shape type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPrinterShape
            (
                NXOpen::Validate::CheckThermalDistortionBuilder::PrinterShapeTypes printerShapeType /** printershapetype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the printer length 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PrinterLength
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the printer width 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PrinterWidth
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the printer height 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PrinterHeight
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the printer diameter 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PrinterDiameter
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the number of lasers 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * NumberOfLasers
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the element Size 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ElementSize
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the Layer thickness or slice thickness.
                    Specify the thickness of material to be added on each layer. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * LayerThickness
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the critical Angle  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * CriticalAngle
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the build plate temperature 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BuildPlateTemperature
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the build plate thickness 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BuildPlateThickness
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Update the checker 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void Update
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the display resolution 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DisplayResolutionBuilder * DisplayResolutionBuilder
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the stress relief option 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool StressRelief
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the stress relief option 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStressRelief
            (
                bool stressRelief /** stressrelief */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the User ID 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString UserID
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the User ID 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetUserID
            (
                const NXString & userID /** userid */ 
            );
            /**Sets  the User ID 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            void SetUserID
            (
                const char * userID /** userid */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the AM Build Optimizer Job ID 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString JobID
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the AM Build Optimizer Job ID 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetJobID
            (
                const NXString & jobID /** jobid */ 
            );
            /**Sets  the AM Build Optimizer Job ID 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            void SetJobID
            (
                const char * jobID /** jobid */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the File Path Key
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FilePathKey
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the File Path Key
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFilePathKey
            (
                const NXString & filePathKey /** filepathkey */ 
            );
            /**Sets  the File Path Key
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            void SetFilePathKey
            (
                const char * filePathKey /** filepathkey */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the Job Status 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::CheckThermalDistortionBuilder::JobStatusType JobStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the Job Status 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetJobStatus
            (
                NXOpen::Validate::CheckThermalDistortionBuilder::JobStatusType jobStatus /** jobstatus */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** The api to check the job status 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void CheckJobStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** The api to create and print the csys
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void CreatePrintCsys
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** The api to orient the part to minimum thermal distortion
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void OrientPartToMinimumThermalDistortion
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the thermal distortion checker creation time
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString CheckerCreationTime
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the thermal distortion checker creation time
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCheckerCreationTime
            (
                const NXString & creationTime /** creationtime */ 
            );
            /**Sets  the thermal distortion checker creation time
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            void SetCheckerCreationTime
            (
                const char * creationTime /** creationtime */ 
            );

            /// \endcond 
        };

        /// \endcond 
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