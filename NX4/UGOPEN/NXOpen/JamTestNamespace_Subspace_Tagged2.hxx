#ifndef NXOpen_JAMTESTNAMESPACE_SUBSPACE_TAGGED2_HXX_INCLUDED
#define NXOpen_JAMTESTNAMESPACE_SUBSPACE_TAGGED2_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestNamespace_Subspace_Tagged2.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/JamTestNamespace_Subspace_Tagged2.hxx>
#include <NXOpen/JamTestNamespace_Tagged.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            class Tagged2;
        }
    }
    namespace JamTestNamespace
    {
        class Tagged;
    }
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            class _Tagged2Builder;
            /** Test class for testing a class inside a nested namespace  <br> not done yet <br> */
            class NXOPENJAMTESTCPPEXPORT Tagged2 : public JamTestNamespace::Tagged
            {
                /** Object type */
                public: enum ObjType
                {
                    ObjTypeTypeTwo/** */,
                    ObjTypeTypeTwoB/** */
                };

                 /** Data struct */
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

                private: friend class  _Tagged2Builder;
                protected: Tagged2();
                /** Test method  @return   <br> License requirements : None */
                public: int NegateAndAddId
                (
                    int input /** */
                );
                /**Returns  the type  <br> License requirements : None */
                public: NXOpen::JamTestNamespace::Subspace::Tagged2::ObjType Type
                (
                );
                /** Test method  @return   <br> License requirements : None */
                public: int AddToId
                (
                    int x /** */
                );
                /** Sets the struct  <br> License requirements : None */
                public: void SetStruct
                (
                    const NXOpen::JamTestNamespace::Subspace::Tagged2::Struct1 & input /** */
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif