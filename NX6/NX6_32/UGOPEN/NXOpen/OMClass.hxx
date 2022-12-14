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
#include <NXOpen/Callback.hxx>
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
     <br> This is a test classs. <br> */
    class NXOPENJAMTESTCPPEXPORT OMClass : public TaggedObject, public virtual IOMName
    {
        private: friend class  _OMClassBuilder;
        protected: OMClass();
        /**Returns   <br> License requirements : None */
        public: NXOpen::OMClass * Superclass
        (
        );
        /**  @return   <br> License requirements : None */
        public: std::vector<NXOpen::OMAttribute *> GetAttributes
        (
        );
        /**  @return   <br> License requirements : None */
        public: bool IsDefiningClassFor
        (
            NXOpen::OMAttribute * attribute /** attribute */ 
        );
        /**  @return   <br> License requirements : None */
        public: std::vector<NXOpen::OMAttribute::Info> GetAllAttributeInfo
        (
        );
        /**  @return   <br> License requirements : None */
        public: virtual NXString GetObjectName
        (
        );
        /**  @return   <br> License requirements : None */
        public: virtual bool CompareWith
        (
            NXOpen::IOMName * other /** other */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif
