#ifndef NXOpen_CAM_INSPECTIONCMMCOMMANDBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONCMMCOMMANDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionCmmCommandBuilder.ja
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
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/CAM_InspectionCmmCommandBuilder.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class InspectionCmmCommandBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class Point;
    namespace CAM
    {
        class _InspectionCmmCommandBuilderBuilder;
        class InspectionCmmCommandBuilderImpl;
        /** Represents a CMM Inspection miscellaneous command builder.   <br> To create a new instance of this class, use @link CAM::InspectionOperationCollection::CreateInspectionCmmCommandBuilder  CAM::InspectionOperationCollection::CreateInspectionCmmCommandBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionCmmCommandBuilder : public CAM::OperationBuilder
        {
            /** The type of CMM command to be entered */
            public: enum CommandTypes
            {
                CommandTypesEnterStatement/** Enter any CMM statement */,
                CommandTypesMeasurementMode/** Enter a statement to set the measurement mode */,
                CommandTypesDefineHomePoint/** Enter a statement defining the home point */,
                CommandTypesMoveMachine/** Enter a statement to move the machine */,
                CommandTypesOutputDecimalPlaces/** Enter a statement defining the number of decimal places for output */,
                CommandTypesDeclareVariable/** Enter a statement declaring a variable */,
                CommandTypesQISVariable/** Enter a statement declaring a QIS variable */,
                CommandTypesPromptforInput/** Enter a statement prompting the user for input */,
                CommandTypesProgramLabel/** Enter a program label statement */,
                CommandTypesJumptoLabel/** Enter a jump to label statement */,
                CommandTypesProgramHeader/** Enter a program header statement */,
                CommandTypesSensorSelect/** Enter a statement defining a sensor selection statement */
            };

            /** The method used to specify the home point */
            public: enum HomePtMethods
            {
                HomePtMethodsMachineZero/** Use the Machine zero point as the home point */,
                HomePtMethodsUserSpecifiedPoint/** Use a user specified point as the home point */
            };

            /** The type of move */
            public: enum MoveTypes
            {
                MoveTypesLinearMove/** Specifies a linear move */,
                MoveTypesArcMove/** Specifies an arc move */,
                MoveTypesHomeLocation/** Specifies a move to the home location */,
                MoveTypesLinear5axis/** Specifies a linear 5 axis move */
            };

            /** Sets variable scope */
            public: enum VarScopes
            {
                VarScopesGlobal/** Variable has global scope */,
                VarScopesCommon/** Variable has common scope */,
                VarScopesLocal/** Variable has local scope */
            };

            /** Variable type */
            public: enum VarTypes
            {
                VarTypesBoolean/** Specifies a boolean variable */,
                VarTypesInteger/** Specifies an integer variable */,
                VarTypesLong/** Specifies a long integer variable */,
                VarTypesReal/** Specifies a real variable */,
                VarTypesDouble/** Specifies a double variable */,
                VarTypesCharacter/** Specifies a character variable */,
                VarTypesVector/** Specifies a vector variable */
            };

            /** QIS variable type */
            public: enum QisvarTypes
            {
                QisvarTypesNull/** Specifies a NULL QIS variable */
            };

            /** User prompt variable */
            public: enum PromptVars
            {
                PromptVarsNull/** Specifies a NULL prompt */
            };

            /** Naming method */
            public: enum IdnameMethods
            {
                IdnameMethodsCurrentPartName/** Use current part name for ID */,
                IdnameMethodsUserSpecified/** Use user specified name for ID */
            };

            /** Revision method */
            public: enum RevMethods
            {
                RevMethodsCurrentPartRevision/** Use current part revision */,
                RevMethodsUserSpecified/** Use user specified revision */
            };

            /** Program name */
            public: enum ProgramNameMethods
            {
                ProgramNameMethodsCurrentPartName/** Use current part name for program name */,
                ProgramNameMethodsUserSpecified/** Use user specified name for program name */
            };

            /** Linear units specifications */
            public: enum LinearUnitsOptions
            {
                LinearUnitsOptionsPartUnits/** Use part units */,
                LinearUnitsOptionsMillimeters/** Use millimeters */,
                LinearUnitsOptionsCentimeters/** Use centimeters */,
                LinearUnitsOptionsMeters/** Use meters */,
                LinearUnitsOptionsInches/** Use inches */,
                LinearUnitsOptionsFeet/** Use feat */
            };

            /** Angular units specifications */
            public: enum AngularUnitsOptions
            {
                AngularUnitsOptionsDecimalDegrees/** Use decimal degrees */,
                AngularUnitsOptionsRadians/** Use radians */,
                AngularUnitsOptionsDegreesMinutesSeconds/** Use Degrees:Minutes:Seconds */
            };

            /** Temperature units specifications */
            public: enum TemperatureUnitsOptions
            {
                TemperatureUnitsOptionsFahrenheit/** Use fahrenheit */,
                TemperatureUnitsOptionsCentigrade/** Use Centigrade */
            };

            private: InspectionCmmCommandBuilderImpl * m_inspectioncmmcommandbuilder_impl;
            private: friend class  _InspectionCmmCommandBuilderBuilder;
            protected: InspectionCmmCommandBuilder();
            public: ~InspectionCmmCommandBuilder();
            /**Returns  the command type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::CommandTypes CommandType
            (
            );
            /**Sets  the command type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCommandType
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::CommandTypes commandType /** commandtype */ 
            );
            /**Returns  the auto mode toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool AutoToggle
            (
            );
            /**Sets  the auto mode toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAutoToggle
            (
                bool autoToggle /** autotoggle */ 
            );
            /**Returns  the program mode toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProgramToggle
            (
            );
            /**Sets  the program mode toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetProgramToggle
            (
                bool programToggle /** programtoggle */ 
            );
            /**Returns  the manual mode toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool ManualToggle
            (
            );
            /**Sets  the manual mode toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetManualToggle
            (
                bool manualToggle /** manualtoggle */ 
            );
            /**Returns  the home point method 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::HomePtMethods HomePtMethod
            (
            );
            /**Sets  the home point method 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetHomePtMethod
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::HomePtMethods homePtMethod /** homeptmethod */ 
            );
            /**Returns  the home point location 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * HomePtPoint
            (
            );
            /**Sets  the home point location 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetHomePtPoint
            (
                NXOpen::Point * homePtPoint /** homeptpoint */ 
            );
            /**Returns  the move type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::MoveTypes MoveType
            (
            );
            /**Sets  the move type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMoveType
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::MoveTypes moveType /** movetype */ 
            );
            /**Returns  the target point 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * TargetPoint
            (
            );
            /**Sets  the target point 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTargetPoint
            (
                NXOpen::Point * targetPoint /** targetpoint */ 
            );
            /**Returns  the intermediate point 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * IntermediatePoint
            (
            );
            /**Sets  the intermediate point 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetIntermediatePoint
            (
                NXOpen::Point * intermediatePoint /** intermediatepoint */ 
            );
            /**Returns  the linear decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: int LinearPlaces
            (
            );
            /**Sets  the linear decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLinearPlaces
            (
                int linearPlaces /** linearplaces */ 
            );
            /**Returns  the angular decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: int AngularPlaces
            (
            );
            /**Sets  the angular decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngularPlaces
            (
                int angularPlaces /** angularplaces */ 
            );
            /**Returns  the deviation and tolerance decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: int DevTolPlaces
            (
            );
            /**Sets  the deviation and tolerance decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDevTolPlaces
            (
                int devTolPlaces /** devtolplaces */ 
            );
            /**Returns  the vector decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: int VectorPlaces
            (
            );
            /**Sets  the vector decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVectorPlaces
            (
                int vectorPlaces /** vectorplaces */ 
            );
            /**Returns  the temperature decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: int TemperaturePlaces
            (
            );
            /**Sets  the temperature decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTemperaturePlaces
            (
                int temperaturePlaces /** temperatureplaces */ 
            );
            /**Returns  the humidity decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: int HumidityPlaces
            (
            );
            /**Sets  the humidity decimal places 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetHumidityPlaces
            (
                int humidityPlaces /** humidityplaces */ 
            );
            /**Returns  the variable name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString VarName
            (
            );
            /**Sets  the variable name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVarName
            (
                const NXString & varName /** varname */ 
            );
            /**Sets  the variable name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetVarName
            (
                const char * varName /** varname */ 
            );
            /**Returns  the variable scope 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::VarScopes VarScope
            (
            );
            /**Sets  the variable scope 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVarScope
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::VarScopes varScope /** varscope */ 
            );
            /**Returns  the variable type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::VarTypes VarType
            (
            );
            /**Sets  the variable type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVarType
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::VarTypes varType /** vartype */ 
            );
            /**Returns  the number of characters 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: int NumChar
            (
            );
            /**Sets  the number of characters 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNumChar
            (
                int numChar /** numchar */ 
            );
            /**Returns  the index size 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: int IndexSize
            (
            );
            /**Sets  the index size 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetIndexSize
            (
                int indexSize /** indexsize */ 
            );
            /**Returns  the qis variable type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::QisvarTypes QisvarType
            (
            );
            /**Sets  the qis variable type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetQisvarType
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::QisvarTypes qisvarType /** qisvartype */ 
            );
            /**Returns  the qis variable value 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString QisvarValue
            (
            );
            /**Sets  the qis variable value 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetQisvarValue
            (
                const NXString & qisvarValue /** qisvarvalue */ 
            );
            /**Sets  the qis variable value 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetQisvarValue
            (
                const char * qisvarValue /** qisvarvalue */ 
            );
            /**Returns  the prompt variable 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::PromptVars PromptVar
            (
            );
            /**Sets  the prompt variable 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetPromptVar
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::PromptVars promptVar /** promptvar */ 
            );
            /**Returns  the user prompt 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString UserPrompt
            (
            );
            /**Sets  the user prompt 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetUserPrompt
            (
                const NXString & userPrompt /** userprompt */ 
            );
            /**Sets  the user prompt 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetUserPrompt
            (
                const char * userPrompt /** userprompt */ 
            );
            /**Returns  the max toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool MaxToggle
            (
            );
            /**Sets  the max toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMaxToggle
            (
                bool maxToggle /** maxtoggle */ 
            );
            /**Returns  the max value 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double MaxValue
            (
            );
            /**Sets  the max value 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMaxValue
            (
                double maxValue /** maxvalue */ 
            );
            /**Returns  the min toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool MinToggle
            (
            );
            /**Sets  the min toggle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMinToggle
            (
                bool minToggle /** mintoggle */ 
            );
            /**Returns  the min value 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double MinValue
            (
            );
            /**Sets  the min value 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMinValue
            (
                double minValue /** minvalue */ 
            );
            /**Returns  the program jump label 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString JumpLabel
            (
            );
            /**Sets  the program jump label 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetJumpLabel
            (
                const NXString & jumpLabel /** jumplabel */ 
            );
            /**Sets  the program jump label 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetJumpLabel
            (
                const char * jumpLabel /** jumplabel */ 
            );
            /** Returns the program statements  @return  
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetProgStatements
            (
            );
            /** Sets the program statements 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetProgStatements
            (
                std::vector<NXString> & progStatements /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the ID name method 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::IdnameMethods IdnameMethod
            (
            );
            /**Sets  the ID name method 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetIdnameMethod
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::IdnameMethods idnameMethod /** idnamemethod */ 
            );
            /**Returns  the ID name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString IdName
            (
            );
            /**Sets  the ID name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetIdName
            (
                const NXString & idName /** idname */ 
            );
            /**Sets  the ID name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetIdName
            (
                const char * idName /** idname */ 
            );
            /**Returns  the revision method 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::RevMethods RevMethod
            (
            );
            /**Sets  the revision method 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetRevMethod
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::RevMethods revMethod /** revmethod */ 
            );
            /**Returns  the revision name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString RevName
            (
            );
            /**Sets  the revision name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetRevName
            (
                const NXString & revName /** revname */ 
            );
            /**Sets  the revision name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetRevName
            (
                const char * revName /** revname */ 
            );
            /**Returns  the program name method 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::ProgramNameMethods ProgramNameMethod
            (
            );
            /**Sets  the program name method 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetProgramNameMethod
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::ProgramNameMethods programNameMethod /** programnamemethod */ 
            );
            /**Returns  the program name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ProgramName
            (
            );
            /**Sets  the program name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetProgramName
            (
                const NXString & programName /** programname */ 
            );
            /**Sets  the program name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetProgramName
            (
                const char * programName /** programname */ 
            );
            /**Returns  the linear units 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::LinearUnitsOptions LinearUnits
            (
            );
            /**Sets  the linear units 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLinearUnits
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::LinearUnitsOptions linearUnits /** linearunits */ 
            );
            /**Returns  the angular units 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::AngularUnitsOptions AngularUnits
            (
            );
            /**Sets  the angular units 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngularUnits
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::AngularUnitsOptions angularUnits /** angularunits */ 
            );
            /**Returns  the temperature units 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCmmCommandBuilder::TemperatureUnitsOptions TemperatureUnits
            (
            );
            /**Sets  the temperature units 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTemperatureUnits
            (
                NXOpen::CAM::InspectionCmmCommandBuilder::TemperatureUnitsOptions temperatureUnits /** temperatureunits */ 
            );
            /**Returns  the command operation name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString OpName
            (
            );
            /**Sets  the command operation name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetOpName
            (
                const NXString & opName /** opname */ 
            );
            /**Sets  the command operation name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetOpName
            (
                const char * opName /** opname */ 
            );
            /**Returns  the goto A angle 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: double GotoAangle
            (
            );
            /**Sets  the goto A angle 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetGotoAangle
            (
                double gotoAangle /** gotoaangle */ 
            );
            /**Returns  the goto B angle 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: double GotoBangle
            (
            );
            /**Sets  the goto B angle 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetGotoBangle
            (
                double gotoBangle /** gotobangle */ 
            );
            /**Returns  the tool name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString ToolName
            (
            );
            /**Sets  the tool name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetToolName
            (
                const NXString & toolName /** toolname */ 
            );
            /**Sets  the tool name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetToolName
            (
                const char * toolName /** toolname */ 
            );
            /**Returns  the sensor name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString SensorName
            (
            );
            /**Sets  the sensor name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetSensorName
            (
                const NXString & sensorName /** sensorname */ 
            );
            /**Sets  the sensor name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetSensorName
            (
                const char * sensorName /** sensorname */ 
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