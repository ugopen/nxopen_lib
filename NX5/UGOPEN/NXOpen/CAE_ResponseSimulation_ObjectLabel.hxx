#ifndef NXOpen_CAE_RESPONSESIMULATION_OBJECTLABEL_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_OBJECTLABEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_ObjectLabel.ja
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
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ObjectLabel;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _ObjectLabelBuilder;
            /** Represents the setting to label an object. Includes name and description */
            class NXOPENCPPEXPORT ObjectLabel : public TaggedObject
            {
                private: friend class  _ObjectLabelBuilder;
                protected: ObjectLabel();
                /**Returns  the object name  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXString Name
                (
                );
                /**Sets  the object name  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetName
                (
                    const NXString & name /** name */ 
                );
                /**Returns  the description for the object  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXString Description
                (
                );
                /**Sets  the description for the object  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDescription
                (
                    const NXString & description /** description */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif