#ifndef NXOpen_SIM_KINEMATICCOMPONENTBUILDER_HXX_INCLUDED
#define NXOpen_SIM_KINEMATICCOMPONENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_KinematicComponentBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace SIM
    {
        class KinematicComponentBuilder;
    }
    class Builder;
    class NXObject;
    namespace SIM
    {
        class KinematicJunctionBuilderList;
    }
    namespace SIM
    {
        class _KinematicComponentBuilderBuilder;
        class KinematicComponentBuilderImpl;
        /**  @brief  Represents the KinamaticComponentBuilder class object  

            <br> To create a new instance of this class, use @link SIM::KinematicComponentCollection::CreateToolBaseComponentBuilder SIM::KinematicComponentCollection::CreateToolBaseComponentBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  KinematicComponentBuilder : public Builder
        {
            /** The register types */
            public: enum RegisterTypes
            {
                RegisterTypesSameAsPocketId/** the pocket id defined the register */,
                RegisterTypesSpecify/** the register is specified */
            };

            /** The Working Position Angle type */
            public: enum WorkPositionAngleTypes
            {
                WorkPositionAngleTypesNone/** no angle specified */,
                WorkPositionAngleTypesSpecifyAngle/** angle is specified */
            };

            /** The SIM KIM system classes */
            public: enum SystemClass
            {
                SystemClassMachine/** Machine Base class */,
                SystemClassTool/** tool class */,
                SystemClassTurret/** turret class */,
                SystemClassPocket/** Pocket class */,
                SystemClassTemporary/** temporary class */,
                SystemClassPart/** Design part setup class */,
                SystemClassWorkpiece/** Blank setup class */,
                SystemClassSetupElement/** Any setup element */,
                SystemClassBasic/** On available in a BASIC machine.
                                                                                                If this bit is set, then the machine part
                                                                                                can be used for simulation when only
                                                                                                UG_ISV_BASIC license is available
                                                                                            */,
                SystemClassLatheSpindle/** lathe spindle class */,
                SystemClassPocketOnHead/** Pocket on a machine head class */,
                SystemClassToolCutting/** Cutting portion of a tool */,
                SystemClassSpinning/** Component defines spinning geometry */
            };

            private: KinematicComponentBuilderImpl * m_kinematiccomponentbuilder_impl;
            private: friend class  _KinematicComponentBuilderBuilder;
            protected: KinematicComponentBuilder();
            public: ~KinematicComponentBuilder();
            /**Returns  the kim component's name  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXString Name
            (
            );
            /**Sets  the kim component's name  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetName
            (
                const NXString & name /** the component's new name */
            );
            /**Returns  the device id  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXString DeviceId
            (
            );
            /**Sets  the device id  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetDeviceId
            (
                const NXString & deviceId /** the new device id */
            );
            /**Returns  the holder id  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: int HolderId
            (
            );
            /**Sets  the holder id  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetHolderId
            (
                int holderId /** the holder id */
            );
            /**Returns  the adjust register type  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXOpen::SIM::KinematicComponentBuilder::RegisterTypes AdjustRegisterType
            (
            );
            /**Sets  the adjust register type  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetAdjustRegisterType
            (
                NXOpen::SIM::KinematicComponentBuilder::RegisterTypes regType /** the adjust register type */
            );
            /**Returns  the cutcom register type  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXOpen::SIM::KinematicComponentBuilder::RegisterTypes CutcomRegisterType
            (
            );
            /**Sets  the cutcom register type  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetCutcomRegisterType
            (
                NXOpen::SIM::KinematicComponentBuilder::RegisterTypes regType /** the cutcom register type */
            );
            /**Returns  the working position angle type  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXOpen::SIM::KinematicComponentBuilder::WorkPositionAngleTypes WorkPositionAngleType
            (
            );
            /**Sets  the working position angle type  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetWorkPositionAngleType
            (
                NXOpen::SIM::KinematicComponentBuilder::WorkPositionAngleTypes type /** The working position angle type */
            );
            /**Returns  the adjust register  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: int AdjustRegister
            (
            );
            /**Sets  the adjust register  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetAdjustRegister
            (
                int adjustReg /** the adjust regsiter */
            );
            /**Returns  the cutcom register  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: int CutcomRegister
            (
            );
            /**Sets  the cutcom register  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetCutcomRegister
            (
                int cutcomReg /** the cutcom regsiter */
            );
            /**Returns  the working position angle  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: double WorkPositionAngle
            (
            );
            /**Sets  the working position angle  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetWorkPositionAngle
            (
                double angle /** the working position angle */
            );
            /** Sets geometry elements for the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetGeometries
            (
                const std::vector<NXOpen::NXObject *> & geos /** the geometry elements */
            );
            /** Returns the geometry elements assigned to this component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void GetGeometries
            (
                std::vector<NXOpen::NXObject *> & geos /** The geometry elements */
            );
            /** Deletes all geometry elements from the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void DeleteAllGeometries
            (
            );
            /** Adds a single geometry element  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void AddGeometry
            (
                NXOpen::NXObject * geo /** The geometry element to add */
            );
            /** Deletes a single geometry element from the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void DeleteGeometry
            (
                NXOpen::NXObject * geo /** The geometry to remove */
            );
            /** Add a system class  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void AddSystemClass
            (
                NXOpen::SIM::KinematicComponentBuilder::SystemClass sysClass /** the system class to add */
            );
            /** Delete a system class  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void DeleteSystemClass
            (
                NXOpen::SIM::KinematicComponentBuilder::SystemClass sysClasses /** the system class to delete */
            );
            /** Returns the component's system classes  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void GetSystemClasses
            (
                std::vector<NXOpen::SIM::KinematicComponentBuilder::SystemClass> & sysClasses /** the component's system classes */
            );
            /** Delete all system classes of the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void DeleteAllSystemClasses
            (
            );
            /** Test if the compomnent is a member of the given system class  @return  TRUE if component is of the system class  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: bool IsOfSystemClass
            (
                NXOpen::SIM::KinematicComponentBuilder::SystemClass sysClass /** the system class to test */
            );
            /** Adds a user class to the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void AddUserClassName
            (
                const NXString & uclass /** The user cass to add   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Deletes a user class from the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void DeleteUserClassName
            (
                const NXString & uclass /** The user cass to remove   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Get a list of user classes of the component  @return  The user classes of the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: std::vector<NXString> GetUserClassNames
            (
            );
            /** Adds a channel name to the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void AddChannelName
            (
                const NXString & channel /** The channel name to add   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Deletes a channel name from the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void DeleteChannelName
            (
                const NXString & channel /** The channel name to remove   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Get a list of channel names of the component  @return  The channel names of the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: std::vector<NXString> GetChannelNames
            (
            );
            /** Adds a holding system to the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void AddHoldingSystem
            (
                const NXString & holdSys /** The holding system to add   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Deletes a holding system from the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void DeleteHoldingSystem
            (
                const NXString & holdSys /** The holding system to remove   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Get a list of holding systems of the component  @return  The channel names of the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: std::vector<NXString> GetHoldingSystems
            (
            );
            /**Returns  the junction list  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXOpen::SIM::KinematicJunctionBuilderList * JunctionList
            (
            );
            /** Renames a user class from the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void RenameUserClass
            (
                const NXString & oldName /** The old user class   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & newName /** The new user class   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Renames a holding system from the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void RenameHoldingSystem
            (
                const NXString & oldName /** The old holding system   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & newName /** The new holding system   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Renames a channel name from the component  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void RenameChannelName
            (
                const NXString & oldName /** The old channel name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & newName /** The new channel name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif