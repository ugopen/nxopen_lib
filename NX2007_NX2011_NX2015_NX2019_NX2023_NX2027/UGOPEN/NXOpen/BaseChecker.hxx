/*==================================================================================================

               Copyright (c) 2021 Siemens Product Lifecycle Management Software Inc.

                                Unpublished - All Rights Reserved.

====================================================================================================
File description:

    This file defines the base class for Check-Mate checker classes based on the NX Open for C++ API.

====================================================================================================*/

#ifndef BASECHECKER_HXX_INCLUDE
#define BASECHECKER_HXX_INCLUDE

#include <uf_defs.h>
#include <unordered_map>
#include <NXOpen/Validate_CheckerNode.hxx>

#pragma warning(disable: 4251)

namespace NXOpen
{
    namespace Validate
    {
        /*
            The abstract class BaseChecker provides the following methods and fields to simplify
            a Check-Mate checker definition. A concrete checker class can be derived from the
            abstract class BaseChecker by inheriting these methods and fields.

            Class Scope:

                Fields:

                    ResultTypes : std::unordered_map<std::string, NXOpen::Validation::Result>

            Instance Scope:

                Constructors:

                    BaseChecker()

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
                    GetLogger() : NXOpen::Validate::Logger *
                    DoCheck() = 0 : virtual void
                    DoCustomize() : virtual void
                    DoHelp() : virtual void
                    SetRegistered(bool isRegistered) : virtual void
                    Register(bool hasCustomization = true, bool hasHelp = true) : void
                    PrintChecker() : void

                    GetClassId() : const char *
                    SetClassId(const char * classId) : void
                    GetCategory() : const char *
                    SetCategory(const char * category) : void
                    GetDisplayName() : const char *
                    SetDisplayName(const char * displayName) : void

                    CanRegister() : virtual bool

                    _DoCheck(NXOpen::Validate::CheckerNode * checkerNode) : void
                    _DoCustomize(NXOpen::Validate::CheckerNode * checkerNode) : void
                    _DoHelp(NXOpen::Validate::CheckerNode * checkerNode) : void
                    _AddParameter(NXOpen::Validate::Parameter * parameter) : void

                Fields:

                    m_classId : char []
                    m_category : char []
                    m_displayName : char []
                    m_parameters : std::vector<NXOpen::Validate::Parameter *>
                    m_checkerNode : NXOpen::Validate::CheckerNode *

            A concrete checker class needs to provide its own unique class id, a category, a display
            name, a checking method DoCheck(), an optional checker customization method DoCustomize(),
            and an optional display method DoHelp() of the checker document. The concrete checker class
            can be registered into the Check-Mate by using the method Register().
        */
        class DllExport BaseChecker
        {
        public:

            // Purpose: A constructor method of the checker. Sets the class id, the category,
            //          and the display name of the checker to an empty string. Adds the
            //          following common parameters for checkers derived from this base class.
            //          -----------------------------------------------------------------------
            //               Label                         Title         Default Value
            //          -----------------------------------------------------------------------
            //            "Save Log in Part"            "SaveInPart",       true
            //            "Log Option"                  "LogOption",       "LOG_INFO"
            //            "Log Additional Message"      "LogMessage",      ""
            //          -----------------------------------------------------------------------
            // Version: It has been released in NX 2007.
            BaseChecker();

            virtual ~BaseChecker() = default;

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, int parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, int parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<int> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<int> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, bool parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, bool parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<bool> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<bool> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, double parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, double parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<double> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<double> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const NXOpen::NXString & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const char * parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, std::vector<NXOpen::NXString> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, std::vector<NXOpen::NXString> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const NXOpen::Point3d & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const NXOpen::Point3d & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<NXOpen::Point3d> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const NXOpen::Vector3d & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const NXOpen::Vector3d & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddParameter(const char * label, const char * parameterTitle, const std::vector<NXOpen::Vector3d> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddNXObjectParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, NXOpen::NXObject * parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddNXObjectParameter(const char * label, const char * parameterTitle, NXOpen::NXObject * parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddNXObjectParameter(const NXOpen::NXString & label, const NXOpen::NXString & parameterTitle, const std::vector<NXOpen::NXObject *> & parameterValue);

            // Purpose: Adds a parameter to the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  label           - Specifies a label of the parameter.
            //  parameterTitle  - Specifies a unique title of the parameter.
            //  parameterValue  - Specifies a value of the parameter.
            void AddNXObjectParameter(const char * label, const char * parameterTitle, const std::vector<NXOpen::NXObject *> & parameterValue);

            // Purpose: Gets the unique titles of all parameters of the checker.
            // Version: It has been released in NX 2007.
            // Returns: Returns the unique titles of all parameters of the checker.
            std::vector<std::string> GetParameterTitles();

            // Purpose: Gets the parameter object with the specified title.
            // Version: It has been released in NX 2007.
            // Params:
            //  title - Specifies a unique title of the parameter.
            // Returns: Returns the parameter object that has the specified unique title in the checker. If it is not found, returns nullptr.
            NXOpen::Validate::Parameter * GetParameter(const std::string & title);

            // Purpose: Gets all parameter objects from the checker.
            // Version: It has been released in NX 2007.
            // Returns: Returns all parameter objects from the checker.
            std::vector<NXOpen::Validate::Parameter *> GetParameters();

            // Purpose: Gets a logger object from the checker.
            // Version: It has been released in NX 2007.
            // Returns: Returns a logger object from the checker.
            NXOpen::Validate::Logger * GetLogger();

            // Purpose: A derived class of the BaseChecker class should override this method to provide a concrete checking logic.
            // Version: It has been released in NX 2007.
            virtual void DoCheck() = 0;

            // Purpose: A derived class of the BaseChecker class should override this method to provide a concrete checker customization logic.
            // Version: It has been released in NX 2007.
            virtual void DoCustomize();

            // Purpose: A derived class of the BaseChecker class should override this method to display the help document of the concrete checker.
            // Version: It has been released in NX 2007.
            virtual void DoHelp();

            // Purpose: Specifies if the checker class has been registered.
            // Version: It has been released in NX 2007.
            // Params:
            //  isRegistered - Specifies if the checker class has been registered.
            virtual void SetRegistered(bool isRegistered);

            // Purpose: Registers the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  hasCustomization    - Specifies if a DoCustomize method will be registered. The default value is true.
            //  hasHelp             - Specifies if a DoHelp method will be registered. The default value is true.
            void Register(bool hasCustomization = true, bool hasHelp = true);

            // Purpose: Prints the category, the display name, the class id, and the parameters of the checker.
            // Version: It has been released in NX 2007.
            void PrintChecker();

            // Purpose: Gets the class id of the checker.
            // Version: It has been released in NX 2007.
            // Returns: Returns the class id of the checker.
            const char * GetClassId() const;

            // Purpose: Sets the class id of the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  classId - Specifies the class id of the checker.
            void SetClassId(const char * classId);

            // Purpose: Gets the category of the checker.
            // Version: It has been released in NX 2007.
            // Returns: Returns the category of the checker.
            const char * GetCategory() const;

            // Purpose: Sets the category of the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  category - Specifies the category of the checker.
            void SetCategory(const char * category);

            // Purpose: Gets the display name of the checker.
            // Version: It has been released in NX 2007.
            // Returns: Returns the display name of the checker.
            const char * GetDisplayName() const;

            // Purpose: Sets the display name of the checker.
            // Version: It has been released in NX 2007.
            // Params:
            //  displayName - Specifies the display name of the checker.
            void SetDisplayName(const char * displayName);

            // Purpose: Dictionary of the checker result types.
            // Version: It has been released in NX 2007.
            static std::unordered_map<std::string, NXOpen::Validation::Result> ResultTypes;

        protected:

            // Purpose: Checks if the checker class can be registered.
            // Version: It has been released in NX 2007.
            // Returns: Returns true if the checker class can be registered. Else, returns false.
            virtual bool CanRegister();

            static std::string Join(const std::string delimiter, const std::vector<std::string> & vals);
            static std::string Join(const std::string delimiter, const std::vector<tag_t> & vals);

        private:

            // Purpose: This method will be registered as a callback for the checking logic of the checker.
            //          When this method is called during the execution of the checker in Check-Mate,
            //          a CheckerNode object will be inputted by the checker, and then the method DoCheck()
            //          will be invoked.
            // Version: It has been released in NX 2007.
            // Params:
            //  checkerNode - A CheckerNode object that the checker provides when this method is invoked.
            void _DoCheck(NXOpen::Validate::CheckerNode * checkerNode);

            // Purpose: This method will be registered as a callback for the customization of the checker parameters.
            //          When this method is called by the Check-Mate, a CheckerNode object will be inputted by the checker,
            //          and then the method DoCustomize() will be invoked.
            // Version: It has been released in NX 2007.
            // Params:
            //  checkerNode - A CheckerNode object that the checker provides when this method is invoked.
            void _DoCustomize(NXOpen::Validate::CheckerNode * checkerNode);

            // Purpose: This method will be registered as a callback for the display of the checker help document.
            //          When this method is called by the Check-Mate to display the help document, the CheckerNode
            //          object will be inputted by the checker, and then the method DoHelp() will be invoked.
            // Version: It has been released in NX 2007.
            // Params:
            //  checkerNode - A CheckerNode object that the checker provides when this method is invoked.
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

            // Purpose: The class id, the category, and the display name of the checker.
            // Version: It has been released in NX 2007.
            char m_classId[MAX_LINE_BUFSIZE];
            char m_category[MAX_LINE_BUFSIZE];
            char m_displayName[MAX_LINE_BUFSIZE];

            // Purpose: The parameter list of the checker.
            // Version: It has been released in NX 2007.
            std::vector<NXOpen::Validate::Parameter *> m_parameters;

            // Purpose: The CheckerNode object of the checker.
            // Version: It has been released in NX 2007.
            NXOpen::Validate::CheckerNode * m_checkerNode;

        };
    }
}

#endif // BASECHECKER_HXX_INCLUDE

