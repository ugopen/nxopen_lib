/*==================================================================================================

               Copyright (c) 2021 Siemens Product Lifecycle Management Software Inc.

                                Unpublished - All Rights Reserved.

====================================================================================================
File description:

    This file defines the class to simplify the checker execution script.

====================================================================================================*/

#ifndef CHECKEREXECUTOR_HPP_INCLUDE
#define CHECKEREXECUTOR_HPP_INCLUDE

#include <uf_defs.h>
#include <NXOpen/NXException.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/PartLoadStatus.hxx>
#include <NXOpen/Validate_Parameter.hxx>
#include <NXOpen/Validate_ValidationManager.hxx>
#include <NXOpen/Validate_Validator.hxx>
#include <NXOpen/Validate_ValidatorOptions.hxx>

#pragma warning(disable: 4251)

namespace NXOpen
{
    namespace Validate
    {
        /*
            The class CheckerExecutor provides the following methods and fields to simplify
            the checker execution script.
   
            Class Scope:
   
                Methods:
                    GetValidatorOptions() : NXOpen::Validate::ValidatorOptions
                    InitValidatorOptions() : void
   
                    OpenPartDisplay(const char * filePath) : void
   
            Instance Scope:
   
                Fields:
                    m_validator : NXOpen::Validate::Validator
                    m_nCheckerNodes : int
   
                Constructors:
                    CheckerExecutor()
   
                Methods:
                    AddPart(string partPath, bool asDisplayPart = false) : CheckerExecutor
                    AddChecker(string checkerId) : CheckerExecutor
                    SetParameter(string parameterTitle, Object parameterValue) : CheckerExecutor
                    SetParameter(string parameterTitle, Object parameterValue, int checkerIndex) : CheckerExecutor
                    Commit() : void
   
                    Init() : void
        */
        class DllExport CheckerExecutor
        {
        public:

            // Purpose: A constructor method.
            // Version: It has been released in NX 2007.
            CheckerExecutor();

            // Purpose: Gets the ValidatorOptions object from the Check-Mate Validator object.
            // Version: It has been released in NX 2007.
            // Returns: Returns the ValidatorOptions object of the Check-Mate Validator object.
            static NXOpen::Validate::ValidatorOptions * GetValidatorOptions();

            // Purpose: Sets the default values for the ValidatorOptions object of the Check-Mate Validator object.
            // Version: It has been released in NX 2007.
            static void InitValidatorOptions();

            // Purpose: Adds an NX part to be checked.
            // Version: It has been released in NX 2007.
            // Params:
            //  partPath      - Specifies the full path of an NX part file.
            //  asDisplayPart - Specifies if the NX part is opened as a display part.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & AddPart(const NXOpen::NXString & partPath, bool asDisplayPart = false);

            // Purpose: Adds an NX part to be checked.
            // Version: It has been released in NX 2007.
            // Params:
            //  partPath      - Specifies the full path of an NX part file.
            //  asDisplayPart - Specifies if the NX part is opened as a display part.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & AddPart(const char * partPath, bool asDisplayPart = false);

            // Purpose: Adds the checker specified by its unique class id.
            // Version: It has been released in NX 2007.
            // Params:
            //  checkerId - Specifies a unique class id of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & AddChecker(const NXOpen::NXString & checkerId);

            // Purpose: Adds the checker specified by its unique class id.
            // Version: It has been released in NX 2007.
            // Params:
            //  checkerId - Specifies a unique class id of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & AddChecker(const char * checkerId);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, int parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, int parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, int parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, int parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<int> & parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<int> & parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<int> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<int> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, bool parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, bool parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, bool parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, bool parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<bool> & parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<bool> & parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<bool> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<bool> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, double parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, double parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, double parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, double parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<double> & parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<double> & parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<double> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<double> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const char * parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const NXOpen::NXString & parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const char * parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const NXOpen::NXString & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, std::vector<NXOpen::NXString> & parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, std::vector<NXOpen::NXString> & parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, std::vector<NXOpen::NXString> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, std::vector<NXOpen::NXString> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const NXOpen::Point3d & parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const NXOpen::Point3d & parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const NXOpen::Point3d & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const NXOpen::Point3d & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const NXOpen::Vector3d & parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const NXOpen::Vector3d & parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const NXOpen::Vector3d & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const NXOpen::Vector3d & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const char * parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetParameter(const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue, int checkerIndex);
    
            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetNXObjectParameter(const char * parameterTitle, NXOpen::NXObject * parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetNXObjectParameter(const NXOpen::NXString & parameterTitle, NXOpen::NXObject * parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetNXObjectParameter(const char * parameterTitle, NXOpen::NXObject * parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetNXObjectParameter(const NXOpen::NXString & parameterTitle, NXOpen::NXObject * parameterValue, int checkerIndex);
    
            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetNXObjectParameter(const char * parameterTitle, const std::vector<NXOpen::NXObject *> parameterValue);

            // Purpose: Sets a parameter for the latest CheckerNode.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetNXObjectParameter(const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::NXObject *> parameterValue);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetNXObjectParameter(const char * parameterTitle, const std::vector<NXOpen::NXObject *> parameterValue, int checkerIndex);

            // Purpose: Sets a parameter for the CheckerNode with the specified checkerIndex.
            // Version: It has been released in NX 2007.
            // Params:
            //  parameterTitle - Specifies a unique title of the parameter.
            //  parameterValue - Specifies a value of the parameter.
            //  checkerIndex   - Specifies an index of the checker.
            // Returns: Returns the current CheckerExecutor object.
            CheckerExecutor & SetNXObjectParameter(const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::NXObject *> parameterValue, int checkerIndex);

            // Purpose: Commits the validator to execute the selected checkers against the selected parts.
            // Version: It has been released in NX 2007.
            void Commit();

        private:

            // Purpose: Initializes a CheckerExecutor object.
            // Version: It has been released in NX 2007.
            void Init();

            // Purpose: Opens an NX part file as a display part.
            // Version: It has been released in NX 2007.
            // Params:
            //  filePath - Specifies the full path of an NX part file.
            static void OpenPartDisplay(const NXOpen::NXString & filePath);

            // Purpose: Opens an NX part file as a display part.
            // Version: It has been released in NX 2007.
            // Params:
            //  filePath - Specifies the full path of an NX part file.
            static void OpenPartDisplay(const char * filePath);

            // Check-Mate Validator object.
            NXOpen::Validate::Validator * m_validator;

            // Count of the checker nodes added into the Validator object.
            int m_nCheckerNodes;
        };
    }
}

#endif // CHECKEREXECUTOR_HPP_INCLUDE

