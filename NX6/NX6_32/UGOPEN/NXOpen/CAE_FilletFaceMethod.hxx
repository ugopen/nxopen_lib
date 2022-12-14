#ifndef NXOpen_CAE_FILLETFACEMETHOD_HXX_INCLUDED
#define NXOpen_CAE_FILLETFACEMETHOD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FilletFaceMethod.ja
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
#include <NXOpen/SelectionMethod.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class FilletFaceMethod;
    }
    class SelectionMethod;
    namespace CAE
    {
    }
    namespace CAE
    {
        /** Represents the output from the fillet face smart selector method
             <br> To obtain an instance of this class use CAE::SmartSelectionManager <br> */
        class NXOPENCPPEXPORT FilletFaceMethod : public SelectionMethod
        {
            public: explicit FilletFaceMethod(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~FilletFaceMethod();
        };
    }
}
#undef EXPORTLIBRARY
#endif
