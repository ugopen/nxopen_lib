#ifndef NXOpen_FEATURES_MOVEOBJECTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_MOVEOBJECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MoveObjectBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Features_MoveObjectBuilder.hxx>
#include <NXOpen/GeometricUtilities_ModlMotion.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class MoveObjectBuilder;
    }
    class Builder;
    namespace GeometricUtilities
    {
        class ModlMotion;
    }
    class SelectNXObjectList;
    namespace Features
    {
        class _MoveObjectBuilderBuilder;
        /** Represents a @link MoveObjectBuilder MoveObjectBuilder@endlink   <br> To create a new instance of this class, use @link Features::BaseFeatureCollection::CreateMoveObjectBuilder Features::BaseFeatureCollection::CreateMoveObjectBuilder@endlink  <br> 
        Default values:
        CreateTraceLines: 0
        Divisions: 1
        MoveObjectResult: MoveOriginal
        MoveParents: 1
        NumberOfCopies: 1
        TransformMotion.Option: Dynamic
        */
        class NXOPENCPPEXPORT MoveObjectBuilder : public Builder
        {
            /** Indicates whether to move or copy objects */
            public: enum MoveObjectResultOptions
            {
                MoveObjectResultOptionsMoveOriginal/** move objects */,
                MoveObjectResultOptionsCopyOriginal/** copy objects*/
            };

            private: friend class  _MoveObjectBuilderBuilder;
            protected: MoveObjectBuilder();
            /**Returns  the objects to move-rotate  <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * ObjectToMoveObject
            (
            );
            /**Returns  the transform  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ModlMotion * TransformMotion
            (
            );
            /**Returns  the move rotate result  <br> License requirements : None */
            public: NXOpen::Features::MoveObjectBuilder::MoveObjectResultOptions MoveObjectResult
            (
            );
            /**Sets  the move rotate result  <br> License requirements : None */
            public: void SetMoveObjectResult
            (
                NXOpen::Features::MoveObjectBuilder::MoveObjectResultOptions moveObjectResult /** moveobjectresult */ 
            );
            /**Returns  the distance or angle divisions  <br> License requirements : None */
            public: int Divisions
            (
            );
            /**Sets  the distance or angle divisions  <br> License requirements : None */
            public: void SetDivisions
            (
                int distanceOrAngleDivisions /** distanceorangledivisions */ 
            );
            /**Returns  the number of copies  <br> License requirements : None */
            public: int NumberOfCopies
            (
            );
            /**Sets  the number of copies  <br> License requirements : None */
            public: void SetNumberOfCopies
            (
                int numCopies /** numcopies */ 
            );
            /**Returns  the move parents flag  <br> License requirements : None */
            public: bool MoveParents
            (
            );
            /**Sets  the move parents flag  <br> License requirements : None */
            public: void SetMoveParents
            (
                bool moveParents /** moveparents */ 
            );
            /**Returns  the create trace lines flag  <br> License requirements : None */
            public: bool CreateTraceLines
            (
            );
            /**Sets  the create trace lines flag  <br> License requirements : None */
            public: void SetCreateTraceLines
            (
                bool createTraceLines /** createtracelines */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif