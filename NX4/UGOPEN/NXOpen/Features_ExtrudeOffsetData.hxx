#ifndef NXOpen_FEATURES_EXTRUDEOFFSETDATA_HXX_INCLUDED
#define NXOpen_FEATURES_EXTRUDEOFFSETDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ExtrudeOffsetData.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ExtrudeOffsetData;
    }
    namespace Features
    {
    }
    namespace Features
    {
        /** Represents offset data of an extrude feature. */
        class NXOPENCPPEXPORT ExtrudeOffsetData : public TransientObject
        {
            /** This enum represents the type of offset */
            public: enum OffsetType
            {
                OffsetTypeNone/** No offset */,
                OffsetTypeNormalOffset/** Offset with two different distances */,
                OffsetTypeSymmetricOffset/** Offset with same distance in both directions */,
                OffsetTypeSingleOffset/** Offset with single distance in one direction */
            };

            public: explicit ExtrudeOffsetData(void *ptr);
            /** Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual ~ExtrudeOffsetData();
            /**Returns  the extrude offset type 
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::ExtrudeOffsetData::OffsetType ExtrudeOffsetType
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link ExtrudeOffsetType() ExtrudeOffsetType@endlink instead.
            @deprecated
            */
            public: NXOpen::Features::ExtrudeOffsetData::OffsetType GetExtrudeOffsetType
            (
            ) { return this->ExtrudeOffsetType(); }
            /**Returns  the extrude start offset
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXString StartOffset
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link StartOffset() StartOffset@endlink instead.
            @deprecated
            */
            public: NXString GetStartOffset
            (
            ) { return this->StartOffset(); }
            /**Returns  the extrude end offset
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXString EndOffset
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link EndOffset() EndOffset@endlink instead.
            @deprecated
            */
            public: NXString GetEndOffset
            (
            ) { return this->EndOffset(); }
        };
    }
}
#undef EXPORTLIBRARY
#endif