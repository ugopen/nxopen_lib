#ifndef NXOpen_JAMTESTNAMESPACE_SUBSPACE_OMPPTAGGED2_HXX_INCLUDED
#define NXOpen_JAMTESTNAMESPACE_SUBSPACE_OMPPTAGGED2_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestNamespace_Subspace_OMPPTagged2.ja
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
#include <NXOpen/JamTestNamespace_Subspace_OMPPTagged2.hxx>
#include <NXOpen/JamTestNamespace_OMPPTagged.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            class OMPPTagged2;
        }
    }
    namespace JamTestNamespace
    {
        class OMPPTagged;
    }
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            class _OMPPTagged2Builder;
            /** Test class for testing a class inside a nested namespace  <br> not done yet <br> */
            class NXOPENJAMTESTCPPEXPORT OMPPTagged2 : public JamTestNamespace::OMPPTagged
            {
                /** Object type */
                public: enum ObjType
                {
                    ObjTypeTypeTwo/** type two */ ,
                    ObjTypeTypeTwoB/** type two b */ ,
                    ObjTypeTypeTwoC/** type two c */ 
                };

                 /** Data struct */
                public:
                struct Struct1
                {
                    public: /** i */ int I;
                    public: /** d */ double D;
                    public: Struct1() :
                        I(),
                        D()
                    {
                    }
                    /** Constructor for the Struct1 struct. */ 
                    public: Struct1(int INIT_i /** i */ , 
                            double INIT_d /** d */ ) :
                        I(INIT_i),
                        D(INIT_d)
                    {
                    }
                };

                private: friend class  _OMPPTagged2Builder;
                protected: OMPPTagged2();
                /** Test method  @return   <br> License requirements : None */
                public: int NegateAndAddId
                (
                    int input /** input */ 
                );
                /**Returns  the type  <br> License requirements : None */
                public: NXOpen::JamTestNamespace::Subspace::OMPPTagged2::ObjType Type
                (
                );
                /** Test method  @return   <br> License requirements : None */
                public: int AddToId
                (
                    int x /** x */ 
                );
                /** Sets the struct  <br> License requirements : None */
                public: void SetStruct
                (
                    const NXOpen::JamTestNamespace::Subspace::OMPPTagged2::Struct1 & input /** input */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
