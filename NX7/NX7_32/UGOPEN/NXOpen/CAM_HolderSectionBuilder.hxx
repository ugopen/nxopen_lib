#ifndef NXOpen_CAM_HOLDERSECTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAM_HOLDERSECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_HolderSectionBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class HolderSectionBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    class NXObject;
    namespace CAM
    {
        class _HolderSectionBuilderBuilder;
        /** Represents a Holder Section Builder */
        class NXOPENCPPEXPORT HolderSectionBuilder : public TaggedObject
        {
            private: friend class  _HolderSectionBuilderBuilder;
            protected: HolderSectionBuilder();
            /**Returns  the Offset (inheritable double)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * TlHolderOffsetBuilder
            (
            );
            /** Create a new holder section item @return  input the current selected item pointer and return new created item pointer.
                                                                                       if list is empty, should input NULL  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * Create
            (
                double diameter /** the diameter */,
                double length /** the length */,
                double taperAngle /** the taper angle */,
                double cornerRadius /** the corner radius */
            );
            /** Modify an existing holder section item <br> License requirements : cam_base ("CAM BASE") */
            public: void Modify
            (
                NXOpen::NXObject * section /** the pointer of modified holder section */,
                double diameter /** the diameter */,
                double length /** the length */,
                double taperAngle /** the taper angle */,
                double cornerRadius /** the corner radius */
            );
            /** Modify an existing holder section item by index  <br> License requirements : cam_base ("CAM BASE") */
            public: void Modify
            (
                int index /** the index of modified holder section */,
                double diameter /** the diameter */,
                double length /** the length */,
                double taperAngle /** the taper angle */,
                double cornerRadius /** the corner radius */
            );
            /** Delete an existing holder section item <br> License requirements : cam_base ("CAM BASE") */
            public: void Delete
            (
                NXOpen::NXObject * section /** the pointer of deleted holder section */
            );
            /** Delete an existing holder section item by index  <br> License requirements : cam_base ("CAM BASE") */
            public: void Delete
            (
                int index /** the index of deleted holder section */
            );
            /** Move up a holder section item  <br> License requirements : None */
            public: void MoveUp
            (
                int index /** the index of item which should be moved up*/
            );
            /** Move down a holder section item  <br> License requirements : None */
            public: void MoveDown
            (
                int index /** the index of item which should be moved down*/
            );
            /** Get the values of an existing holder section item  <br> License requirements : cam_base ("CAM BASE") */
            public: void Get
            (
                NXOpen::NXObject * section /** the section */,
                double* diameter /** the diameter */,
                double* length /** the length */,
                double* taperAngle /** the taper angle */,
                double* cornerRadius /** the corner radius */
            );
            /**Returns  the number of holder sections  <br> License requirements : cam_base ("CAM BASE") */
            public: int NumberOfSections
            (
            );
            /** Get a specific holder section  @return  the section  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * GetSection
            (
                int position /** index in array */
            );
            /** Add a new holder section item @return  output the new created item actual index,if error happens, output will be -1  <br> License requirements : cam_base ("CAM BASE") */
            public: int Add
            (
                int inputIndex /** input the new created item index */,
                double diameter /** the diameter */,
                double length /** the length */,
                double taperAngle /** the taper angle */,
                double cornerRadius /** the corner radius */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
