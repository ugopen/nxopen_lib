#ifndef NXOpen_TOOLDESIGNER_ASSIGNWELDSBUILDER_HXX_INCLUDED
#define NXOpen_TOOLDESIGNER_ASSIGNWELDSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ToolDesigner_AssignWeldsBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libtooldesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace ToolDesigner
    {
        class AssignWeldsBuilder;
    }
    class Builder;
    class SelectTaggedObjectList;
    class TaggedObject;
    namespace ToolDesigner
    {
        class _AssignWeldsBuilderBuilder;
        class AssignWeldsBuilderImpl;

        /// \cond NX_NO_DOC 
        /** AssignWeldsBuilder   <br> To create a new instance of this class, use @link NXOpen::ToolDesigner::ToolDesignerManager::CreateAssignWeldsBuilder  NXOpen::ToolDesigner::ToolDesignerManager::CreateAssignWeldsBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class TOOLDESIGNEROPENCPPEXPORT  AssignWeldsBuilder : public NXOpen::Builder
        {
            /** Represents the weld's objects types */
            public: enum Menu
            {
                MenuAllWeldsinScope/** all weldsin scope */ ,
                MenuVolumeScope/** volume scope */ 
            };

            private: AssignWeldsBuilderImpl * m_assignweldsbuilder_impl;
            private: friend class  _AssignWeldsBuilderBuilder;
            protected: AssignWeldsBuilder();
            public: ~AssignWeldsBuilder();
            /** Fetch Weld Points In Scope 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void FetchWeldPointsInScope
            (
                std::vector<NXOpen::TaggedObject *> & weldPoints /** weldpoints */ 
            );
            /** Search for all the welds inside a certain box
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void VolumeSearch
            (
                const NXOpen::Point3d & bottomVertex /** bottomvertex */ ,
                const NXOpen::Point3d & upperVertex /** uppervertex */ ,
                std::vector<NXOpen::TaggedObject *> & objects /** the datums that were found*/
            );
            /** Assign weld
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void Assign
            (
                const std::vector<NXOpen::TaggedObject *> & welds /** welds */ 
            );
            /** UnAssign weld
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void UnAssign
            (
                const std::vector<NXOpen::TaggedObject *> & welds /** welds */ 
            );
            /**Returns  the weld selection getter 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: NXOpen::SelectTaggedObjectList * InvisibleSelection
            (
            );
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