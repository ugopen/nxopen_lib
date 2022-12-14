#ifndef NXOpen_OMATTRIBUTE_HXX_INCLUDED
#define NXOpen_OMATTRIBUTE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     OMAttribute.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/IOMName.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    class OMAttribute;
    class IOMName;
    class OMClass;
    class OMSchema;
    class _OMAttributeBuilder;
    /**
    Represents a OMAttribute.  This is for internal testing only.
    */
    class NXOPENJAMTESTCPPEXPORT OMAttribute : public TaggedObject, public virtual IOMName
    {
        /** For internal testing */
        public: enum Type
        {
            TypeInt/** For internal testing */,
            TypeTag/** For internal testing */
        };

         /** For internal testing */
        public:
        struct Info
        {
            public: /** */NXString Name;
            public: /** */NXOpen::OMClass * DefiningClass;
            public: /** */NXOpen::OMSchema * DefiningSchema;
            public: /** */NXOpen::OMAttribute::Type Type;
            public: Info() :
                Name(),
                DefiningClass(),
                DefiningSchema(),
                Type((NXOpen::OMAttribute::Type)0)
            {
            }
            /** Constructor for the Info struct. */ 
            public: Info(NXString INIT_name /** */, NXOpen::OMClass * INIT_defining_class /** */, NXOpen::OMSchema * INIT_defining_schema /** */, NXOpen::OMAttribute::Type INIT_type /** */) :
                Name(INIT_name),
                DefiningClass(INIT_defining_class),
                DefiningSchema(INIT_defining_schema),
                Type(INIT_type)
            {
            }
        };

        private: friend class  _OMAttributeBuilder;
        protected: OMAttribute();
        /**  @return   <br> License requirements : None */
        public: NXOpen::OMAttribute::Info GetInfo
        (
        );
        /**  @return   */
        public: virtual NXString GetObjectName
        (
        );
        /**  @return   */
        public: virtual bool CompareWith
        (
            NXOpen::IOMName * other /** */
        );
    };
}
#undef EXPORTLIBRARY
#endif
