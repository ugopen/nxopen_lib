#ifndef NXOpen_GROUPBUILDER_HXX_INCLUDED
#define NXOpen_GROUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GroupBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/GroupBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class GroupBuilder;
    class Builder;
    class NXObject;
    class SelectGroup;
    class SelectObjectList;
    class _GroupBuilderBuilder;
    /**
    Represents a @link GroupBuilder GroupBuilder@endlink 
     <br> To create a new instance of this class, use @link BasePart::CreateGatewayGroupBuilder BasePart::CreateGatewayGroupBuilder@endlink  <br> */
    class NXOPENCPPEXPORT GroupBuilder : public Builder
    {
        /** Represents the type of action for this builder to perform. */
        public: enum Action
        {
            ActionNewGroup/** new group */ ,
            ActionAddToGroup/** add to group */ ,
            ActionRemoveFromGroup/** remove from group */ ,
            ActionUngroup/** ungroup */ ,
            ActionEditGroup/** edit group */ 
        };

        /** Represents the option to control the behavior when deleting a group. */
        public: enum UngroupOption
        {
            UngroupOptionTop/** top */ ,
            UngroupOptionFull/** full */ 
        };

        private: friend class  _GroupBuilderBuilder;
        protected: GroupBuilder();
        /**Returns  the action type  <br> License requirements : None */
        public: int ActionType
        (
        );
        /**Sets  the action type  <br> License requirements : None */
        public: void SetActionType
        (
            int actionType /** actiontype */ 
        );
        /**Returns  the group in action  <br> License requirements : None */
        public: NXOpen::SelectGroup * GroupInAction
        (
        );
        /**Returns  the objects in group  <br> License requirements : None */
        public: NXOpen::SelectObjectList * ObjectsInGroup
        (
        );
        /**Returns  the group name  <br> License requirements : None */
        public: NXString GroupName
        (
        );
        /**Sets  the group name  <br> License requirements : None */
        public: void SetGroupName
        (
            const NXString & groupName /** groupname */ 
        );
        /**Returns  the umg option  <br> License requirements : None */
        public: bool UniqueMembershipOption
        (
        );
        /**Sets  the umg option  <br> License requirements : None */
        public: void SetUniqueMembershipOption
        (
            bool umgOption /** umgoption */ 
        );
        /**Returns  the activegroup option  <br> License requirements : None */
        public: bool ActivegroupOption
        (
        );
        /**Sets  the activegroup option  <br> License requirements : None */
        public: void SetActivegroupOption
        (
            bool activegroupOption /** activegroupoption */ 
        );
        /**Returns  the ungroup level  <br> License requirements : None */
        public: NXOpen::GroupBuilder::UngroupOption UngroupLevel
        (
        );
        /**Sets  the ungroup level  <br> License requirements : None */
        public: void SetUngroupLevel
        (
            NXOpen::GroupBuilder::UngroupOption ungroupLevel /** ungrouplevel */ 
        );
        /**Returns  the owning object which currently has to be a sketch  <br> License requirements : None */
        public: NXOpen::NXObject * OwningObject
        (
        );
        /**Sets  the owning object which currently has to be a sketch  <br> License requirements : None */
        public: void SetOwningObject
        (
            NXOpen::NXObject * owningObject /** owningobject */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif