#ifndef NXOpen_GEOMETRICUTILITIES_ROTATIONSETBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_ROTATIONSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_RotationSetBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/GeometricUtilities_RotationSetBuilder.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class RotationSetBuilder;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class INXObject;
    namespace GeometricUtilities
    {
        class _RotationSetBuilderBuilder;
        class RotationSetBuilderImpl;
        /**
            Represents a  @link GeometricUtilities::RotationSetBuilder GeometricUtilities::RotationSetBuilder@endlink  
            */
        class NXOPENCPPEXPORT  RotationSetBuilder : public TaggedObject, public virtual INXObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: RotationSetBuilderImpl * m_rotationsetbuilder_impl;
            private: friend class  _RotationSetBuilderBuilder;
            protected: RotationSetBuilder();
            public: ~RotationSetBuilder();
            /**Returns  the location on path  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * Location
            (
            );
            /**Returns  the value expression  <br> License requirements : None */
            public: NXOpen::Expression * Value
            (
            );
            /** Resets rotation extra data. 
                    For legacy reason, Rotation has to contain some extra data.
                    When you try to reset the rotation, you not only need to reset the angular dimension 
                    but also need to simultaneously call this API to reset the extra data.  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void ResetExtraData
            (
            );
            /** Finds the @link  NXObject   NXObject @endlink  with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.

                An exception will be thrown if no object can be found with the given journal identifier.  @return   <br> License requirements : None */
            public: virtual NXOpen::INXObject * FindObject
            (
                const NXString & journalIdentifier /** Journal identifier of the object */
            );
            /**Returns  the identifier that would be recorded in a journal for this object. 
                This may not be the same across different releases of the software.  <br> License requirements : None */
            public: virtual NXString JournalIdentifier
            (
            );
            /**Returns  whether this object is an occurrence or not.  <br> License requirements : None */
            public: virtual bool IsOccurrence
            (
            );
            /**Returns  the prototype of this object if it is an occurrence.  <br> License requirements : None */
            public: virtual NXOpen::INXObject * Prototype
            (
            );
            /**Returns  the owning component, if this object is an occurrence.  <br> License requirements : None */
            public: virtual NXOpen::Assemblies::Component * OwningComponent
            (
            );
            /**Returns  the owning part of this object  <br> License requirements : None */
            public: virtual NXOpen::BasePart * OwningPart
            (
            );
            /** Prints a representation of this object to the system log file.
                  <br> License requirements : None */
            public: virtual void Print
            (
            );
            /**Returns  the custom name of the object.   <br> License requirements : None */
            public: virtual NXString Name
            (
            );
            /** Sets the custom name of the object.  <br> License requirements : None */
            public: virtual void SetName
            (
                const NXString & name /** name */ 
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
