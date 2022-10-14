#ifndef NXOpen_JAMTESTNAMESPACE_OMPPTAGGED_HXX_INCLUDED
#define NXOpen_JAMTESTNAMESPACE_OMPPTAGGED_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestNamespace_OMPPTagged.ja
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
#include <NXOpen/JamTestNamespace_OMPPSubobject.hxx>
#include <NXOpen/JamTestNamespace_OMPPTagged.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    namespace JamTestNamespace
    {
        class OMPPTagged;
    }
    namespace JamTestNamespace
    {
        class OMPPSubobject;
    }
    class TaggedObject;
    namespace JamTestNamespace
    {
        class _OMPPTaggedBuilder;
        class OMPPTaggedImpl;
        /**
            Represents a OM++ Schema.  This is for internal testing only.
             <br> TEST CLASS <br> */
        class NXOPENJAMTESTCPPEXPORT  OMPPTagged : public TaggedObject
        {
            private: OMPPTaggedImpl * m_ompptagged_impl;
            private: friend class  _OMPPTaggedBuilder;
            protected: OMPPTagged();
            public: ~OMPPTagged();
            /** Test for input of subobject array  @return   <br> License requirements : None */
            public: int OwnsOneOf
            (
                const std::vector<NXOpen::JamTestNamespace::OMPPSubobject *> & objects /** this is the one we want */
            );
            /** Test for input of subobject array  @return   <br> License requirements : None */
            public: int OwnsOneOf2
            (
                const std::vector<NXOpen::TaggedObject *> & objects /** this is the one we want */
            );
            /**Returns  the test for returning a single subobject  <br> License requirements : None */
            public: NXOpen::JamTestNamespace::OMPPSubobject * Subobject
            (
            );
            /** Returns the Test for returning a subobject array (contents will all be the same object )  @return   <br> License requirements : None */
            public: std::vector<NXOpen::JamTestNamespace::OMPPSubobject *> GetSubobjects
            (
                int n /** n */ 
            );
            /** Test for input of single subobject  @return   <br> License requirements : None */
            public: bool OwnsSubobject
            (
                NXOpen::JamTestNamespace::OMPPSubobject * obj /** obj */ 
            );
            /**Returns  the Id of this Tagged object  <br> License requirements : None */
            public: int Id
            (
            );
            /**Returns  the Id of the Tagged object's subobject  <br> License requirements : None */
            public: int SubobjectId
            (
            );
            /** Destroy the current subobject of this object and create a new one  <br> License requirements : None */
            public: void NewSubobject
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif