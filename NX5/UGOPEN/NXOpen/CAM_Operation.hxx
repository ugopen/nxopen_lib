#ifndef NXOpen_CAM_OPERATION_HXX_INCLUDED
#define NXOpen_CAM_OPERATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_Operation.ja
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
#include <NXOpen/CAM_CAMObject.hxx>
#include <NXOpen/CAM_Move.hxx>
#include <NXOpen/CAM_Operation.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class Operation;
    }
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class Move;
    }
    namespace CAM
    {
        class MoveCollection;
    }
    namespace CAM
    {
        class _OperationBuilder;
        /** Represents an operation  <br> To obtain an instance of this class use @link CAM::OperationCollection CAM::OperationCollection@endlink  <br> */
        class NXOPENCPPEXPORT Operation : public CAM::CAMObject
        {
            private: friend class  _OperationBuilder;
            protected: Operation();
            /** append move  <br> License requirements : cam_base ("CAM BASE") */
            public: void AppendMove
            (
                NXOpen::CAM::Move * move /** move */ 
            );
            /** insert move  <br> License requirements : cam_base ("CAM BASE") */
            public: void InsertMove
            (
                NXOpen::CAM::Move * insert_after /** insert after */ ,
                NXOpen::CAM::Move * move /** move */ 
            );


            private: NXOpen::CAM::MoveCollection *cAMMoveCollection;
            /** Represents Move Collection */
            public: NXOpen::CAM::MoveCollection *CAMMoveCollection()
            {
                return cAMMoveCollection;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif