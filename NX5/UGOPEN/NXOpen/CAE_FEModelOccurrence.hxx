#ifndef NXOpen_CAE_FEMODELOCCURRENCE_HXX_INCLUDED
#define NXOpen_CAE_FEMODELOCCURRENCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FEModelOccurrence.ja
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
#include <NXOpen/CAE_IFEModel.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class FEModelOccurrence;
    }
    namespace CAE
    {
        class IFEModel;
    }
    namespace CAE
    {
        class MeshCollectorOccurrenceCollection;
    }
    namespace CAE
    {
        class _FEModelOccurrenceBuilder;
        /**  @brief  This class represents a Finite Element Model Occurrence.
                          Only one instance of this class will exist in each sim part file 

           <br> To obtain an instance of this class, use @link CAE::SimSimulation::Femodel CAE::SimSimulation::Femodel@endlink  <br> */
        class NXOPENCPPEXPORT FEModelOccurrence : public CAE::IFEModel
        {
            private: friend class  _FEModelOccurrenceBuilder;
            protected: FEModelOccurrence();
            /** Finds the object within the @link CAE::FEModelOccurrence CAE::FEModelOccurrence@endlink  context,
                        with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with the given journal identifier.  @return Object with the journal identifier  <br> License requirements : None */
            public: NXOpen::TaggedObject * Find
            (
                const NXString & journal_identifier /** Journal identifier of the object   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );


            private: NXOpen::CAE::MeshCollectorOccurrenceCollection *meshCollectorOccurrences;
            /** Returns the mesh collector collection occurrence belonging to the part */
            public: NXOpen::CAE::MeshCollectorOccurrenceCollection *MeshCollectorOccurrences()
            {
                return meshCollectorOccurrences;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
