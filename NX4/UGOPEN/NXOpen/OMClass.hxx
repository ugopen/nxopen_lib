#ifndef NXOpen_OMCLASS_HXX_INCLUDED
#define NXOpen_OMCLASS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     OMClass.ja
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
#include <NXOpen/OMAttribute.hxx>
#include <NXOpen/OMClass.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    class OMClass;
    class IOMName;
    class OMAttribute;
    class OMSchema;
    class _OMClassBuilder;
    /**
    Represents a OMClass.  This is for internal testing only.
    */
    class NXOPENJAMTESTCPPEXPORT OMClass : public TaggedObject, public virtual IOMName
    {
        private: friend class  _OMClassBuilder;
        protected: OMClass();
        /**Returns   <br> License requirements : None */
        public: NXOpen::OMClass * Superclass
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Superclass() Superclass@endlink instead.
        @deprecated
        */
        public: NXOpen::OMClass * GetSuperclass
        (
        ) { return this->Superclass(); }
        /**  @return   <br> License requirements : None */
        public: std::vector<NXOpen::OMAttribute *> GetAttributes
        (
        );
        /**  @return   <br> License requirements : None */
        public: bool IsDefiningClassFor
        (
            NXOpen::OMAttribute * attribute /** */
        );
        /**  @return   <br> License requirements : None */
        public: std::vector<NXOpen::OMAttribute::Info> GetAllAttributeInfo
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