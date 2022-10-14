#ifndef NXOpen_ROUTING_PLACEPARTBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_PLACEPARTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_PlacePartBuilder.ja
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
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/Routing_PlacePartBuilder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class PlacePartBuilder;
    }
    class Builder;
    namespace Routing
    {
        class CharacteristicList;
    }
    class TaggedObject;
    namespace Routing
    {
        class _PlacePartBuilderBuilder;
        class PlacePartBuilderImpl;
        /** 
             <br> To create a new instance of this class, use @link Routing::RouteManager::CreatePlacePartBuilderPTS Routing::RouteManager::CreatePlacePartBuilderPTS@endlink  <br> */
        class NXOPENCPPEXPORT  PlacePartBuilder : public Builder
        {
            private: PlacePartBuilderImpl * m_placepartbuilder_impl;
            private: friend class  _PlacePartBuilderBuilder;
            protected: PlacePartBuilder();
            public: ~PlacePartBuilder();
            /** Load a part given the input part number.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void LoadPart
            (
                const NXString & partNumber /** Part number */
            );
            /** Set the reference set to use for the loaded part.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetActiveRefSet
            (
                const NXString & refSet /** Reference Set Name */
            );
            /** Set the layer for the loaded part.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetActiveLayer
            (
                int layerOption /** Layer Option  */,
                int layer /** Layer Number */
            );
            /** Complete the placement operation.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void FinalizePlacement
            (
                NXOpen::Routing::CharacteristicList * optionalCharx /** Optional Charx to apply. */,
                NXOpen::Routing::CharacteristicList * requiredCharx /** Required Charx to apply. */,
                const NXString & name /** The component name to apply to the part. */,
                int layerOption /** The layer option. */,
                int layer /** The layer to apply. */,
                bool dfaultOStock /** Assign overstock to a fitting when a default is defined.*/
            );
            /** Update the loaded part with a new placement location and object.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void UpdatePlacementObj
            (
                NXOpen::TaggedObject * placementObj /** New object to attach to. Can bee NULL. */,
                const NXOpen::Point3d & placementPos /** The new location for the part. */
            );
            /** Update the loaded part with a new placement location and object.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void UnloadPart
            (
            );
            /** Get information about the parts being placed.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void GetLoadedPartInfo
            (
                NXOpen::TaggedObject ** loadedPart /** The PART_part tag of the loaded part. */,
                NXOpen::TaggedObject ** loadedInst /** The Instance tag of the loaded part. */
            );
            /** Replace the builder's part instance with a new instance.
                        This is used when the assemblies absolute positioning method is used. It will create
                        it's own part instance and we need make sure the builder has the new one.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void ReplaceLoadedInstance
            (
                NXOpen::TaggedObject * partInst /** The instance tag of the loaded part. */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif