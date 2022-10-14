#ifndef NXOpen_FORMBOARD_UPDATEDISCREPANCY_HXX_INCLUDED
#define NXOpen_FORMBOARD_UPDATEDISCREPANCY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Formboard_UpdateDiscrepancy.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Formboard
    {
        class UpdateDiscrepancy;
    }
    class NXObject;
    namespace Formboard
    {
    }
    namespace Formboard
    {
        class UpdateDiscrepancyImpl;
        /**
                Defines a discrepancy object which contains information about a specific
                difference between the formboard drawing and the 3D harness model.
            */
        class NXOPENCPPEXPORT  UpdateDiscrepancy : public TransientObject
        {
            /** The general type of the discrepancy. */
            public: enum Type
            {
                TypeUnknown/** Unknown type, not valid. */,
                TypeMissing/** Object exits in the 3D harness but is 
                                                                missing from the formboard. */,
                TypeExtra/** Object is in the formboard but not in
                                                                the 3D harness. */,
                TypeModified/** Object exists in both 3D and the formboard but
                                                                is modified in some way. */
            };

            /** Specifies the type of objects involved in the discrepancy. */
            public: enum ObjectType
            {
                ObjectTypeUnknown/** Unknown type. */,
                ObjectTypeRcp/** Routing Control Point. */,
                ObjectTypeSegment/** Routing Segment. */,
                ObjectTypeClip/** A component not assigned as a
                                                                        electrical connector. */,
                ObjectTypeComponent/** A component assigned as a
                                                                        electrical connector or device. */,
                ObjectTypeHarness/** Harness. */,
                ObjectTypeWire/** Wire connection. */,
                ObjectTypeCable/** Cable connection. */,
                ObjectTypeShield/** Shield connection. */,
                ObjectTypeConnector/** ConnectorDevice object which 
                                                                       has a type of connector. */,
                ObjectTypeDevice/** ConnectorDevice object which 
                                                                       has a type of device. */,
                ObjectTypeOverstock/** Overstock. */,
                ObjectTypeFillerstock/** Filler stock. */,
                ObjectTypeFittingOverstock/** Overstock applied to fittings. */
            };

            private: UpdateDiscrepancyImpl * m_updatediscrepancy_impl;
            public: explicit UpdateDiscrepancy(void *ptr);
            /** Frees the memory associated with this object.  <br> License requirements : None */
            public: virtual ~UpdateDiscrepancy();
            /**Returns  the general type of the discrepancy.  <br> License requirements : None */
            public: NXOpen::Formboard::UpdateDiscrepancy::Type DiscrepancyType
            (
            );
            /**Returns  the type of object referenced by the discrepancy.  <br> License requirements : None */
            public: NXOpen::Formboard::UpdateDiscrepancy::ObjectType DiscrepancyObjectType
            (
            );
            /**Returns  the object in the 3D harness referenced by the discrepancy.  This may
                      be NULL depending on the type of the discrepancy. <br> License requirements : None */
            public: NXOpen::NXObject * HarnessObject
            (
            );
            /**Returns  the object in the 2D formboard referenced by the discrepancy. This may
                      be NULL depending on the type of the discrepancy. <br> License requirements : None */
            public: NXOpen::NXObject * FormboardObject
            (
            );
            /**Returns  the description string of the discrepancy.  <br> License requirements : None */
            public: NXString Description
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif