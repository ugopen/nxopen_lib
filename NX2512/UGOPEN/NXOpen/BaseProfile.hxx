/*==================================================================================================

               Copyright (c) 2022 Siemens Digital Industries Software

                        Unpublished - All Rights Reserved.

====================================================================================================
File description:

    This file defines the base class for Check-Mate profile classes based on the NX Open for C++ API.


====================================================================================================*/

#ifndef BASEPROFILE_HXX_INCLUDE
#define BASEPROFILE_HXX_INCLUDE

#ifdef _MSC_VER
#pragma once
#endif

#include <uf_defs.h>
#include <unordered_map>

#include <NXOpen/Validate_CheckerNode.hxx>

#ifdef _MSC_VER
#pragma warning(disable: 4251)
#endif

namespace NXOpen
{
    namespace Validate
    {
        /*
            The abstract class BaseProfile provides the following methods and fields to simplify
            a Check-Mate profile definition. A concrete profile class can be derived from the
            abstract class BaseProfile by inheriting these methods and fields.

            Instance Scope:

                Constructors:

                    BaseProfile()

                Methods:

                    AddParameter(const NXString & label, const NXString & parameterTitle, int parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, int parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, const std::vector<int> & parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, const std::vector<int> & parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, bool parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, bool parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, const std::vector<bool> & parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, const std::vector<bool> & parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, double parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, double parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, const std::vector<double> & parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, const std::vector<double> & parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, const NXString & parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, const char * parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, std::vector<NXString> & parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, std::vector<NXString> & parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, const NXOpen::Point3d & parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, const NXOpen::Point3d & parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, const NXOpen::Vector3d & parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, const NXOpen::Vector3d & parameterValue) : void
                    AddParameter(const NXString & label, const NXString & parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue) : void
                    AddParameter(const char * label, const char * parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue) : void
                    AddNXObjectParameter(const NXString & label, const NXString & parameterTitle, NXOpen::NXObject * parameterValue) : void
                    AddNXObjectParameter(const char * label, const char * parameterTitle, NXOpen::NXObject * parameterValue) : void
                    AddNXObjectParameters(const NXString & label, const NXString & parameterTitle, const std::vector<NXOpen::NXObject *> & parameterValue) : void
                    AddNXObjectParameters(const char * label, const char * parameterTitle, const std::vector<NXOpen::NXObject *> & parameterValue) : void

                    GetParameterTitles() : std::vector<std::string>
                    GetParameter(const char * title) : NXOpen::Validate::Parameter *
                    GetParameters() : std::vector<NXOpen::Validate::Parameter *>
                    DoCustomize() : virtual void
                    DoHelp() : virtual void
                    SetRegistered(bool isRegistered) : virtual void
                    Register(bool hasCustomization = true, bool hasHelp = true) : void
                    PrintProfile() : void

                    GetClassId() : const char *
                    SetClassId(const char * classId) : void
                    GetCategory() : const char *
                    SetCategory(const char * category) : void
                    GetDisplayName() : const char *
                    SetDisplayName(const char * displayName) : void
                    GetAllowUserCustomize() : bool
                    SetAllowUserCustomize(bool allowUserCustomize) : void

                    CanRegister() : virtual bool

                    SetParm(const char* parmID, int parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, const std::vector<int>& parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, bool parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, const std::vector<bool>& parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, double parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, const std::vector<double>& parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, const char* parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, std::vector<NXOpen::NXString>& parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, const NXOpen::Point3d& parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, const std::vector<NXOpen::Point3d>& parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, const NXOpen::Vector3d& parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, const std::vector<NXOpen::Vector3d>& parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, NXOpen::NXObject* parameterValue) : NXOpen::Validate::Parameter*
                    SetParm(const char* parmID, const std::vector<NXOpen::NXObject*>& parameterValue) : NXOpen::Validate::Parameter*
                    RefParm(const char* parmID, const char* refParmID) : NXOpen::Validate::Parameter*
                    AddChecker(const char* checkerId) : void
                    AddChecker(const char* checkerId, std::vector<NXOpen::Validate::Parameter*> checkerParms) : void

                    _DoCustomize(NXOpen::Validate::CheckerNode * checkerNode) : void
                    _DoHelp(NXOpen::Validate::CheckerNode * checkerNode) : void
                    _AddParameter(NXOpen::Validate::Parameter * parameter) : void

                Fields:

                    m_classId : char []
                    m_category : char []
                    m_displayName : char []
                    m_allowUserCustomize : bool
                    m_parameters : std::vector<NXOpen::Validate::Parameter *>
                    m_checkerNode : NXOpen::Validate::CheckerNode *

            A concrete profile class needs to provide its own unique class id, a category, a display
            name, a set of child checkers via method AddChecker(), an optional profile customization
            method DoCustomize(), and an optional display method DoHelp() of the checker document.
            The concrete checker class can be registered into the Check-Mate by using method Register().
        */
        class DllExport BaseProfile
        {
        public:

            // Purpose: A constructor method of the profile. Sets the class id, the category,
            //          and the display name of the profile to an empty string. Adds the
            //          following common parameters for profiles derived from this base class.
            //          -----------------------------------------------------------------------
            //               Label                         Title         Default Value
            //          -----------------------------------------------------------------------
            //            "disabled?"                   "Disabled",         false
            //            "Save Log in Part"            "SaveInPart",       true
            //          -----------------------------------------------------------------------
            // Version: It has been released in NX 2306.
            BaseProfile();

            virtual ~BaseProfile() = default;

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, int parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, int parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<int> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<int> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, bool parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, bool parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<bool> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<bool> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, double parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, double parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<double> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<double> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const NXOpen::NXString & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const char * parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<const char*> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, std::vector<NXOpen::NXString> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const NXOpen::Point3d & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const NXOpen::Point3d & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const NXOpen::Vector3d & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const NXOpen::Vector3d & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddNXObjectParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, NXOpen::NXObject * parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddNXObjectParameter(const char * label, const char * parameterTitle, NXOpen::NXObject * parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddNXObjectParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::NXObject *> & parameterValue);

            // Purpose: Adds a parameter to the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddNXObjectParameter(const char * label, const char * parameterTitle, const std::vector<NXOpen::NXObject *> & parameterValue);

            // Purpose: Gets the unique titles of all parameters of the profile.
            // Version: It has been released in NX 2306.
            // Returns: Returns the unique titles of all parameters of the profile.
            std::vector<std::string> GetParameterTitles();

            // Purpose: Gets the parameter object with the specified title.
            // Version: It has been released in NX 2306.
            // Params:
            //  title - Specifies a unique title of the parameter.
            // Returns: Returns the parameter object that has the specified unique title in the checker. If it is not found, returns nullptr.
            NXOpen::Validate::Parameter * GetParameter(const std::string & title);

            // Purpose: Gets all parameter objects from the profile.
            // Version: It has been released in NX 2306.
            // Returns: Returns all parameter objects from the profile.
            std::vector<NXOpen::Validate::Parameter *> GetParameters();

            // Purpose: A derived class of the BaseProfile class should override this method to provide a concrete profile customization logic.
            // Version: It has been released in NX 2306.
            virtual void DoCustomize();

            // Purpose: A derived class of the BaseProfile class should override this method to display the help document of the concrete profile.
            // Version: It has been released in NX 2306.
            virtual void DoHelp();

            // Purpose: Specifies if the profile class has been registered.
            // Version: It has been released in NX 2306.
            // Params:
            //  isRegistered - Specifies if the profile class has been registered.
            virtual void SetRegistered(bool isRegistered);

            // Purpose: Registers the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  hasCustomization    - Specifies if a DoCustomize method will be registered. The default value is true.
            //  hasHelp             - Specifies if a DoHelp method will be registered. The default value is true.
            void Register(bool hasCustomization = true, bool hasHelp = true);

            // Purpose: Prints the category, the display name, the class id, and the parameters of the profile.
            // Version: It has been released in NX 2306.
            void PrintProfile();

            // Purpose: Gets the class id of the profile.
            // Version: It has been released in NX 2306.
            // Returns: Returns the class id of the profile.
            const char * GetClassId() const;

            // Purpose: Sets the class id of the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  classId - Specifies the class id of the profile.
            void SetClassId(const char * classId);

            // Purpose: Gets the category of the profile.
            // Version: It has been released in NX 2306.
            // Returns: Returns the category of the profile.
            const char * GetCategory() const;

            // Purpose: Sets the category of the profile.
            // Version: It has been released in NX 2306.
            // Params:
            //  category - Specifies the category of the profile.
            void SetCategory(const char * category);

            // Purpose: Gets the display name of the profile.
            // Version: It has been released in NX 2306.
            // Returns: Returns the display name of the profile.
            const char * GetDisplayName() const;

            // Purpose: Sets the display name of the profile.
            // Version: It has been released in NX profile.
            // Params:
            //  displayName - Specifies the display name of the profile.
            void SetDisplayName(const char * displayName);

            // Purpose: Gets the statues whether the profile can be customized or not.
            // Version: It has been released in NX 2306.
            // Returns: Returns the statues whether the profile can be customized or not.
            const bool GetAllowUserCustomize() const;

            // Purpose: Sets the statues whether the profile can be customized or not.
            // Version: It has been released in NX profile.
            // Params:
            //  allowUserCustomize - Specifies the statues whether the profile can be customized or not.
            void SetAllowUserCustomize(bool allowUserCustomize);

            std::vector<NXOpen::NXString> GetCheckerNames();
            std::vector<bool> GetCheckerEnableFlags(std::vector<NXOpen::NXString> checkerNames);
            void SetCheckerEnableFlag(NXOpen::NXString checkerName, bool enableFlag);

        protected:

            // Purpose: Checks if the profile class can be registered.
            // Version: It has been released in NX 2306.
            // Returns: Returns true if the profile class can be registered. Else, returns false.
            virtual bool CanRegister();

            static std::string Join(const std::string delimiter, const std::vector<std::string> & vals);
            static std::string Join(const std::string delimiter, const std::vector<tag_t> & vals);

            // checkers to hold checker id, parameter set
            struct CheckerInstance
            {
                std::string ID;
                std::vector<NXOpen::Validate::Parameter*> Parms;
            };
            std::vector<CheckerInstance>  m_childCheckers;
    
            // Purpose: A set of APIs that are used in AddChecker()
            //          to set value to the parameter in checker instance
            // Version: They have been released in NX 2306.
            // Returns: Returns the parameter that has the specified value
            NXOpen::Validate::Parameter* SetParm(const char* parmID, int parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const std::vector<int>& parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, bool parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const std::vector<bool>& parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, double parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const std::vector<double>& parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const char* parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const std::vector<const char*>& parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const NXOpen::Point3d& parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const std::vector<NXOpen::Point3d>& parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const NXOpen::Vector3d& parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const std::vector<NXOpen::Vector3d>& parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, NXOpen::NXObject* parameterValue);
            NXOpen::Validate::Parameter* SetParm(const char* parmID, const std::vector<NXOpen::NXObject*>& parameterValue);

            // Purpose: An API that is used in AddChecker() to set the parameter value
            //          in checker instance by referencing the parameter in the profile 
            // Version: It has been released in NX 2306.
            // Returns: Returns the parameter that has the specified value
            NXOpen::Validate::Parameter* RefParm(const char* parmID, const char* refParmID);

            // Purpose: APIs to add a set of checker instances into the profile 
            // Version: It has been released in NX 2306.
            void AddChecker(const char* checkerId);
            void AddChecker(const char* checkerId, std::vector<NXOpen::Validate::Parameter*> checkerParms);

        private:

            // Purpose: This method will be registered as a callback for the customization of the profile parameters.
            //          When this method is called by the Check-Mate, a CheckerNode object will be inputted by the profile,
            //          and then the method DoCustomize() will be invoked.
            // Version: It has been released in NX 2306.
            // Params:
            //  checkerNode - A CheckerNode object that the profile provides when this method is invoked.
            void _DoCustomize(NXOpen::Validate::CheckerNode * checkerNode);

            // Purpose: This method will be registered as a callback for the display of the profile help document.
            //          When this method is called by the Check-Mate to display the help document, the CheckerNode
            //          object will be inputted by the profile, and then the method DoHelp() will be invoked.
            // Version: It has been released in NX 2306.
            // Params:
            //  checkerNode - A CheckerNode object that the profile provides when this method is invoked.
            void _DoHelp(NXOpen::Validate::CheckerNode * checkerNode);

            void _AddParameter(NXOpen::Validate::Parameter * parameter);

            static std::string Format(bool val);
            static std::string Format(int val);
            static std::string Format(double val);
            static std::string Format(const NXOpen::Point3d & val);
            static std::string Format(const NXOpen::Vector3d & val);
            static std::string Format(const NXOpen::NXObject * val);
            static std::string Format(const NXOpen::NXString & val);
            static std::string Format(const std::vector<bool> & vals);
            static std::string Format(const std::vector<std::string> & vals);
            static std::string Format(const std::vector<NXOpen::NXString> & vals);
            static std::string Format(const std::vector<int> & vals);
            static std::string Format(const std::vector<double> & vals);
            static std::string Format(const std::vector<NXOpen::Point3d> & vals);
            static std::string Format(const std::vector<NXOpen::Vector3d> & vals);
            static std::string Format(const std::vector <NXOpen::NXObject *> & vals);

            // Purpose: The class id, the category, and the display name of the profile.
            // Version: It has been released in NX 2306.
            char m_classId[MAX_LINE_BUFSIZE];
            char m_category[MAX_LINE_BUFSIZE];
            char m_displayName[MAX_LINE_BUFSIZE];
            bool m_allowUserCustomize = true;

            // Purpose: The parameter list of the profile.
            // Version: It has been released in NX 2306.
            std::vector<NXOpen::Validate::Parameter *> m_parameters;

            // Purpose: The CheckerNode object of the profile.
            // Version: It has been released in NX 2306.
            NXOpen::Validate::CheckerNode * m_checkerNode;
        };
    }
}

#endif // BASEPROFILE_HXX_INCLUDE

