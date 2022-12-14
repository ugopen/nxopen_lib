#ifndef NXOpen_JAMTESTNAMESPACE_SUBSPACE_TRANSIENTOBJB_HXX_INCLUDED
#define NXOpen_JAMTESTNAMESPACE_SUBSPACE_TRANSIENTOBJB_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestNamespace_Subspace_TransientObjB.ja
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
#include <NXOpen/JamTestNamespace_Subspace_TransientObj.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            class TransientObjB;
        }
    }
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
            class NXOPENJAMTESTCPPEXPORT TransientObjB : public JamTestNamespace::Subspace::TransientObj
            {
                 /** The struct */
                public:
                struct Struct2
                {
                    public: /** b */ bool B;
                    public: /** s */ NXString S;
                    public: Struct2() :
                        B(),
                        S()
                    {
                    }
                    /** Constructor for the Struct2 struct. */ 
                    public: Struct2(bool INIT_b /** b */ , NXString INIT_s /** s */ ) :
                        B(INIT_b),
                        S(INIT_s)
                    {
                    }
                };

                public: explicit TransientObjB(void *ptr);
                /** Sets the struct  <br> License requirements : None */
                public: void SetStructB
                (
                    const NXOpen::JamTestNamespace::Subspace::TransientObjB::Struct2 & input /** input */ 
                );
                /** Gets the struct  @return   <br> License requirements : None */
                public: NXOpen::JamTestNamespace::Subspace::TransientObjB::Struct2 GetStructB
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
