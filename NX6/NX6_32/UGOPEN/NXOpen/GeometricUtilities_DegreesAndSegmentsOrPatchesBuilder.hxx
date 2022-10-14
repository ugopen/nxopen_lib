#ifndef NXOpen_GEOMETRICUTILITIES_DEGREESANDSEGMENTSORPATCHESBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_DEGREESANDSEGMENTSORPATCHESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_DegreesAndSegmentsOrPatchesBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_DegreesAndSegmentsOrPatchesBuilder.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class DegreesAndSegmentsOrPatchesBuilder;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class INXObject;
    namespace GeometricUtilities
    {
        class _DegreesAndSegmentsOrPatchesBuilderBuilder;
        /** the DegreesAndSegmentsOrPatches builder */
        class NXOPENCPPEXPORT DegreesAndSegmentsOrPatchesBuilder : public TaggedObject, public virtual INXObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _DegreesAndSegmentsOrPatchesBuilderBuilder;
            protected: DegreesAndSegmentsOrPatchesBuilder();
            /**Returns  the degree  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: int Degree
            (
            );
            /**Sets  the degree  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetDegree
            (
                int degree /** degree */ 
            );
            /**Returns  the patches  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: int SegmentsOrPatches
            (
            );
            /**Sets  the patches  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetSegmentsOrPatches
            (
                int segmentsOrPatches /** segmentsorpatches */ 
            );
            /**Returns  the u degree  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: int UDegree
            (
            );
            /**Sets  the u degree  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetUDegree
            (
                int uDegree /** udegree */ 
            );
            /**Returns  the v degree  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: int VDegree
            (
            );
            /**Sets  the v degree  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetVDegree
            (
                int vDegree /** vdegree */ 
            );
            /**Returns  the u patches  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: int UPatches
            (
            );
            /**Sets  the u patches  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetUPatches
            (
                int uPatches /** upatches */ 
            );
            /**Returns  the v patches  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: int VPatches
            (
            );
            /**Sets  the v patches  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetVPatches
            (
                int vPatches /** vpatches */ 
            );
            /** Finds the @link  NXObject   NXObject @endlink  with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.

                An exception will be thrown if no object can be found with the given journal identifier.  @return   <br> License requirements : None */
            public: virtual NXOpen::INXObject * FindObject
            (
                const NXString & journalIdentifier /** Journal identifier of the object   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
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
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif