#ifndef NXOpen_CAE_SIMLOADRECIPEMAPENTRYTARGETTYPES_HXX_INCLUDED
#define NXOpen_CAE_SIMLOADRECIPEMAPENTRYTARGETTYPES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimLoadRecipeMapEntryTargetTypes.ja
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
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class SimLoadRecipeMapEntryTargetTypes;
    }
    namespace CAE
    {
        class SimLoadRecipeMapEntryTargetTypesImpl;
        /**  @brief  The class handles the enum definitions needed by load recipe map entries  

           <br> No Creator this holds an enum  shared by other classes  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimLoadRecipeMapEntryTargetTypes
        {
            /** This enum defines the target type options of a @link NXOpen::CAE::SimLoadRecipeMapEntry NXOpen::CAE::SimLoadRecipeMapEntry@endlink  */
            public: enum TargetTypes
            {
                TargetTypesUnknown/** Unkown target type */,
                TargetTypesNode/** Node */,
                TargetTypesNodeGroup/** Nodes in a group. */,
                TargetTypesNodeMesh/** Nodes in a mesh. */,
                TargetTypesFace/** Element face */,
                TargetTypesFaceGroup/** Element faces in a group. */,
                TargetTypesFaceMesh/** Element faces in a mesh. */,
                TargetTypesNodeFem/** Nodes in a fem model. */,
                TargetTypesFaceFem/** Element faces in a fem model. */
            };

            private: SimLoadRecipeMapEntryTargetTypesImpl * m_simloadrecipemapentrytargettypes_impl;
            public: ~SimLoadRecipeMapEntryTargetTypes();
        }; //lint !e1712 default constructor not defined for class  

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
