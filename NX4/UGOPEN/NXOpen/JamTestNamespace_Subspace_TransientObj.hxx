#ifndef NXOpen_JAMTESTNAMESPACE_SUBSPACE_TRANSIENTOBJ_HXX_INCLUDED
#define NXOpen_JAMTESTNAMESPACE_SUBSPACE_TRANSIENTOBJ_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestNamespace_Subspace_TransientObj.ja
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
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            class TransientObj;
        }
    }
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            /** Test class for testing a class inside a nested namespace  <br> not done yet <br> */
            class NXOPENJAMTESTCPPEXPORT TransientObj : public TransientObject
            {
                 /** The struct */
                public:
                struct Struct1
                {
                    public: /** */int I;
                    public: /** */double D;
                    public: Struct1() :
                        I(),
                        D()
                    {
                    }
                    /** Constructor for the Struct1 struct. */ 
                    public: Struct1(int INIT_i /** */, double INIT_d /** */) :
                        I(INIT_i),
                        D(INIT_d)
                    {
                    }
                };

                /** The type */
                public: enum ObjType
                {
                    ObjTypeZero/** */,
                    ObjTypeOne/** */
                };

                public: explicit TransientObj(void *ptr);
                /** Disposes of object  <br> License requirements : None */
                public: virtual ~TransientObj();
                /**Returns  the type  <br> License requirements : None */
                public: NXOpen::JamTestNamespace::Subspace::TransientObj::ObjType Type
                (
                );
                /**Returns  the int id  <br> License requirements : None */
                public: int IntId
                (
                );
                /**Sets  the int id  <br> License requirements : None */
                public: void SetIntId
                (
                    int id /** */
                );
                /** Sets the struct  <br> License requirements : None */
                public: void SetStruct
                (
                    const NXOpen::JamTestNamespace::Subspace::TransientObj::Struct1 & input /** */
                );
                /** Gets the struct  @return   <br> License requirements : None */
                public: NXOpen::JamTestNamespace::Subspace::TransientObj::Struct1 GetStruct
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif