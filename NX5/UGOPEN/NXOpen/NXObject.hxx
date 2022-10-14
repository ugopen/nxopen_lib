#ifndef NXOpen_NXOBJECT_HXX_INCLUDED
#define NXOpen_NXOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     NXObject.ja
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
#include <NXOpen/INXObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class NXObject;
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    class _NXObjectBuilder;
    /** A base class providing low-level services for most NXOpen classes.
         <br> For more information on NX rules for Names and Attributes, see 
        the Properties section of the Gateway Help. <br>   <br> This is an abstract class, and cannot be instantiated. <br> */
    class NXOPENCPPEXPORT NXObject : public TaggedObject, public virtual INXObject
    {
        /** Specifies attribute type. */
        public: enum AttributeType
        {
            AttributeTypeInteger/** Integer */,
            AttributeTypeReal/** Real */,
            AttributeTypeString/** String */,
            AttributeTypeNull/** Null */,
            AttributeTypeTime/** Time and Date */,
            AttributeTypeReference/** Reference */,
            AttributeTypeAny/** All types */
        };

        /** Specifies the format of the date and time attribute. */
        public: enum DateAndTimeFormat
        {
            DateAndTimeFormatNumeric/** 2004/04/28 22:06:15  */,
            DateAndTimeFormatTextual/** 28-Apr-2004 22:06:15 */
        };

         /** Contains attribute information.  This structure is used by
                @link NXObject::GetAttributeTitlesByType NXObject::GetAttributeTitlesByType@endlink . */
        public:
        struct AttributeInformation
        {
            public: /** Attribute type  */NXOpen::NXObject::AttributeType Type;
            public: /** Attribute title */NXString Title;
            public: AttributeInformation() :
                Type((NXOpen::NXObject::AttributeType)0),
                Title()
            {
            }
            /** Constructor for the AttributeInformation struct. */ 
            public: AttributeInformation(NXOpen::NXObject::AttributeType INIT_type /** Attribute type  */, NXString INIT_title /** Attribute title */) :
                Type(INIT_type),
                Title(INIT_title)
            {
            }
        };

        private: friend class  _NXObjectBuilder;
        protected: NXObject();
        /** Creates or modifies an integer attribute.  <br> License requirements : None */
        public: void SetAttribute
        (
            const NXString & title /** title */ ,
            int value /** value */ 
        );
        /** Creates or modifies a real attribute.  <br> License requirements : None */
        public: void SetAttribute
        (
            const NXString & title /** title */ ,
            double value /** value */ 
        );
        /** Creates or modifies a string attribute.  <br> License requirements : None */
        public: void SetAttribute
        (
            const NXString & title /** title */ ,
            const NXString & value /** value */ 
        );
        /** Creates or modifies a null attribute.
                Attribute with a title and no value.  <br> License requirements : None */
        public: void SetAttribute
        (
            const NXString & title /** title */ 
        );
        /** Creates or modifies a time attribute.  <br> License requirements : None */
        public: void SetTimeAttribute
        (
            const NXString & title /** title */ ,
            const NXString & value /** The current date and time is used if
                                               the value is NULL.  See
                                               @link NXObject::DateAndTimeFormat NXObject::DateAndTimeFormat@endlink 
                                               for valid formats.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Creates or modifies a reference attribute.  <br> License requirements : None */
        public: void SetReferenceAttribute
        (
            const NXString & title /** title */ ,
            const NXString & value /** value */ 
        );
        /** Gets the integer attribute by title.  @return    <br> License requirements : None */
        public: int GetIntegerAttribute
        (
            const NXString & title /** title */ 
        );
        /** Gets the real attribute by title.  @return    <br> License requirements : None */
        public: double GetRealAttribute
        (
            const NXString & title /** title */ 
        );
        /** Gets the string attribute by title.  @return    <br> License requirements : None */
        public: NXString GetStringAttribute
        (
            const NXString & title /** title */ 
        );
        /** Gets the time attribute by title.  @return    <br> License requirements : None */
        public: NXString GetTimeAttribute
        (
            NXOpen::NXObject::DateAndTimeFormat format /** format */ ,
            const NXString & title /** title */ 
        );
        /** Gets the reference attribute by title.  @return    <br> License requirements : None */
        public: NXString GetReferenceAttribute
        (
            const NXString & title /** title */ 
        );
        /** Gets all the attribute titles of a specific type.  An array
                of @link NXObject::AttributeInformation NXObject::AttributeInformation@endlink  is returned in no
                specific order.  The respective GetAttribute(type) methods are
                then required to get the actual attribute value.  @return    <br> License requirements : None */
        public: std::vector<NXOpen::NXObject::AttributeInformation> GetAttributeTitlesByType
        (
            NXOpen::NXObject::AttributeType type /** type */ 
        );
        /** Deletes an attribute by type and title.  <br> License requirements : None */
        public: void DeleteAttributeByTypeAndTitle
        (
            NXOpen::NXObject::AttributeType type /** type */ ,
            const NXString & title /** title */ 
        );
        /** Deletes all attributes of a specific type.  <br> License requirements : None */
        public: void DeleteAllAttributesByType
        (
            NXOpen::NXObject::AttributeType type /** type */ 
        );
        /** Finds the @link  NXObject   NXObject @endlink  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.

            An exception will be thrown if no object can be found with the given journal identifier.  @return   <br> License requirements : None */
        public: virtual NXOpen::INXObject * FindObject
        (
            const NXString & journal_identifier /** Journal identifier of the object   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**Returns  the identifier that would be recorded in a journal for this object. 
            This may not be the same across different releases of the software.  <br> License requirements : None */
        public: virtual NXString JournalIdentifier
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link JournalIdentifier() JournalIdentifier@endlink instead.
        @deprecated
        */
        public: NXString GetJournalIdentifier
        (
        ) { return this->JournalIdentifier(); }
        /**Returns  whether this object is an occurrence or not.  <br> License requirements : None */
        public: virtual bool IsOccurrence
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link IsOccurrence() IsOccurrence@endlink instead.
        @deprecated
        */
        public: bool GetIsOccurrence
        (
        ) { return this->IsOccurrence(); }
        /**Returns  the prototype of this object if it is an occurrence.  <br> License requirements : None */
        public: virtual NXOpen::INXObject * Prototype
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Prototype() Prototype@endlink instead.
        @deprecated
        */
        public: NXOpen::INXObject * GetPrototype
        (
        ) { return this->Prototype(); }
        /**Returns  the owning component, if this object is an occurrence.  <br> License requirements : None */
        public: virtual NXOpen::Assemblies::Component * OwningComponent
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link OwningComponent() OwningComponent@endlink instead.
        @deprecated
        */
        public: NXOpen::Assemblies::Component * GetOwningComponent
        (
        ) { return this->OwningComponent(); }
        /**Returns  the owning part of this object  <br> License requirements : None */
        public: virtual NXOpen::BasePart * OwningPart
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link OwningPart() OwningPart@endlink instead.
        @deprecated
        */
        public: NXOpen::BasePart * GetOwningPart
        (
        ) { return this->OwningPart(); }
        /** Prints a representation of this object to the system log file.
              <br> License requirements : None */
        public: virtual void Print
        (
        );
        /**Returns  the custom name of the object.   <br> License requirements : None */
        public: virtual NXString Name
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Name() Name@endlink instead.
        @deprecated
        */
        public: NXString GetName
        (
        ) { return this->Name(); }
        /** Sets the custom name of the object.  <br> License requirements : None */
        public: virtual void SetName
        (
            const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
    };
}
#undef EXPORTLIBRARY
#endif