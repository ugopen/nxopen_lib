#ifndef NXOpen_CAE_AEROSTRUCTURES_AUTHOR_METHODLIBRARY_HXX_INCLUDED
#define NXOpen_CAE_AEROSTRUCTURES_AUTHOR_METHODLIBRARY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroStructures_Author_MethodLibrary.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class MethodLibrary;
            }
        }
    }
    class Session;
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class CalculationContext;
            }
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class MethodLibraryImpl;
                /** Represents a @link NXOpen::CAE::AeroStructures::Author::MethodLibrary NXOpen::CAE::AeroStructures::Author::MethodLibrary@endlink  object.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
                 <br>  Created in NX12.0.0.  <br>  
                */
                class NXOPENCPP_CAEEXPORT  MethodLibrary
                {
                    public: /** Callback type 
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : None */
                    typedef NXOpen::Callback1<bool, NXOpen::CAE::AeroStructures::Author::CalculationContext *> Callback;
                    private: MethodLibraryImpl * m_methodlibrary_impl;
                    private: NXOpen::Session* m_owner;
                    /// \cond NX_NO_DOC 
                    public: explicit MethodLibrary(NXOpen::Session *owner);


                    /// \endcond 
                    public: 
                    /**Returns the tag of this object.  */
                    tag_t Tag() const; 
                    private: static MethodLibrary* theMethodLibrary;
                    /** Returns the MethodLibrary object for the running session which serves as the 'gateway' class for the application API.  
                        References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                        Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
                    */
                    public: static MethodLibrary* GetMethodLibrary(NXOpen::Session *owner);
                    public: ~MethodLibrary();
                    /** Routine to register an evaluate callback 
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : None */
                    public: void RegisterEvaluate
                    (
                        const NXString & methodID /** must match 'id' field in method descriptor */,
                        int version /** version number - currently must be 1 */,
                        const NXOpen::CAE::AeroStructures::Author::MethodLibrary::Callback&  cb /** routine to register */
                    );
                    /** Routine to register an evaluate callback 
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : None */
                    void RegisterEvaluate
                    (
                        const char * methodID /** must match 'id' field in method descriptor */,
                        int version /** version number - currently must be 1 */,
                        const NXOpen::CAE::AeroStructures::Author::MethodLibrary::Callback&  cb /** routine to register */
                    );
                    /** Routine to register a validate callback 
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : None */
                    public: void RegisterValidate
                    (
                        const NXString & methodID /** must match 'id' field in method descriptor */,
                        int version /** version number - currently must be 1 */,
                        const NXOpen::CAE::AeroStructures::Author::MethodLibrary::Callback&  cb /** routine to register */
                    );
                    /** Routine to register a validate callback 
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : None */
                    void RegisterValidate
                    (
                        const char * methodID /** must match 'id' field in method descriptor */,
                        int version /** version number - currently must be 1 */,
                        const NXOpen::CAE::AeroStructures::Author::MethodLibrary::Callback&  cb /** routine to register */
                    );
                }; //lint !e1712 default constructor not defined for class  

            }
        }
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif