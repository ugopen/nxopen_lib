#ifndef NXOpen_TOOLING_DESIGNEJECTORPINBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_DESIGNEJECTORPINBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_DesignEjectorPinBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_ConceptStandardPartRecord.hxx>
#include <NXOpen/Tooling_EjectorDesignData.hxx>
#include <NXOpen/Tooling_EjectorRecords.hxx>
#include <NXOpen/Tooling_SpreadsheetData.hxx>
#include <NXOpen/Tooling_StandardPartData.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class DesignEjectorPinBuilder;
    }
    namespace Annotations
    {
        class PmiCustomSymbol;
    }
    class Builder;
    class NXObject;
    class Point;
    class SelectNXObjectList;
    class TaggedObject;
    namespace Tooling
    {
        class ConceptStandardPartRecord;
    }
    namespace Tooling
    {
        class EjectorDesignData;
    }
    namespace Tooling
    {
        class EjectorRecords;
    }
    namespace Tooling
    {
        class SpreadsheetData;
    }
    namespace Tooling
    {
        class StandardPartData;
    }
    namespace Tooling
    {
        class _DesignEjectorPinBuilderBuilder;
        class DesignEjectorPinBuilderImpl;
        /** Represents a builder to be used to design ejector pin.  <br> To create a new instance of this class, use @link NXOpen::Tooling::MoldwizardManager::CreateDesignEjectorPinBuilder  NXOpen::Tooling::MoldwizardManager::CreateDesignEjectorPinBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  DesignEjectorPinBuilder : public NXOpen::Builder
        {
            /** Represents the type to define an ejector pin part. */
            public: enum DefineType
            {
                DefineTypeInsert/** Insert type */,
                DefineTypeEdit/** Edit type */
            };

            /** Represents the type to create ejector pin component. */
            public: enum ComponentType
            {
                ComponentTypeInstance/** Add Instance type */,
                ComponentTypeNewPart/** Add new part type */
            };

            /** Represents the type to ejector pin part.  */
            public: enum EjectorPinType
            {
                EjectorPinTypeStraight/** Straight ejector type */,
                EjectorPinTypeShoulder/** Shoulder ejector type */,
                EjectorPinTypeBlade/** Blade ejector type */,
                EjectorPinTypeSleeve/** Sleeve ejector type */
            };

            private: DesignEjectorPinBuilderImpl * m_designejectorpinbuilder_impl;
            private: friend class  _DesignEjectorPinBuilderBuilder;
            protected: DesignEjectorPinBuilder();
            public: ~DesignEjectorPinBuilder();
            /**Returns  the ejector part definition type. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::DesignEjectorPinBuilder::DefineType DefinitionType
            (
            );
            /**Sets  the ejector part definition type. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetDefinitionType
            (
                NXOpen::Tooling::DesignEjectorPinBuilder::DefineType definitionType /** definitiontype */ 
            );
            /**Returns  the point tag to install an ejector part. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * InsertPoint
            (
            );
            /**Sets  the point tag to install an ejector part. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetInsertPoint
            (
                NXOpen::TaggedObject * insertPointTag /** insertpointtag */ 
            );
            /**Returns  the selected ejector points. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * EjectorPoints
            (
            );
            /**Returns  the creation type of ejector pin component. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::DesignEjectorPinBuilder::ComponentType CreateComponentType
            (
            );
            /**Sets  the creation type of ejector pin component. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCreateComponentType
            (
                NXOpen::Tooling::DesignEjectorPinBuilder::ComponentType createComponentType /** createcomponenttype */ 
            );
            /**Returns  the flag to indicate whether to display rename dialog box or not. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool Rename
            (
            );
            /**Sets  the flag to indicate whether to display rename dialog box or not. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetRename
            (
                bool rename /** rename */ 
            );
            /**Returns  the flag to indicate whether to design concept symbol for ejector pin or not. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseSymbol
            (
            );
            /**Sets  the flag to indicate whether to design concept symbol for ejector pin or not. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetUseSymbol
            (
                bool useSymbol /** usesymbol */ 
            );
            /**Returns  the flag to indicate whether to calculate length of ejector pin or not. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool CalculateLength
            (
            );
            /**Sets  the flag to indicate whether to calculate length of ejector pin or not. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCalculateLength
            (
                bool calculateLength /** calculatelength */ 
            );
            /**Returns  the reference point to position ejector parts. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * ReferencePoint
            (
            );
            /**Sets  the reference point to position ejector parts. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetReferencePoint
            (
                NXOpen::TaggedObject * referencePointTag /** referencepointtag */ 
            );
            /** Gets ejector pin record data.  @return  A @link NXOpen::Tooling::EjectorRecords NXOpen::Tooling::EjectorRecords@endlink  instance 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::EjectorRecords * GetEjectorRecords
            (
            );
            /** Sets ejector pin record data. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetEjectorRecords
            (
                NXOpen::Tooling::EjectorRecords * ejectorRecords /** A @link NXOpen::Tooling::EjectorRecords NXOpen::Tooling::EjectorRecords@endlink  instance */
            );
            /**Returns  the parent part index. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: int ParentIndex
            (
            );
            /**Sets  the parent part index. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetParentIndex
            (
                int parentIndex /** parentindex */ 
            );
            /**Returns  the selected sleeve ejector points. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SleevePoints
            (
            );
            /**Returns  the ejector part type. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::DesignEjectorPinBuilder::EjectorPinType EjectorType
            (
            );
            /**Sets  the ejector part type. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetEjectorType
            (
                NXOpen::Tooling::DesignEjectorPinBuilder::EjectorPinType ejectorType /** ejectortype */ 
            );
            /**Gets the reference set of the ejector pin. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetReferenceSet
            (
            );
            /**Sets the reference set of the ejector pin. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetReferenceSet
            (
                const NXString & referenceSet /** referenceset */ 
            );
            /**Sets the reference set of the ejector pin. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            void SetReferenceSet
            (
                const char * referenceSet /** referenceset */ 
            );
            /** Gets ejector client data.  @return  A @link NXOpen::Tooling::StandardPartData NXOpen::Tooling::StandardPartData@endlink  instance 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::StandardPartData * GetEjectorClientData
            (
            );
            /** Sets ejector client data. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetEjectorClientData
            (
                NXOpen::Tooling::StandardPartData * standardClientData /** A @link NXOpen::Tooling::StandardPartData NXOpen::Tooling::StandardPartData@endlink  instance */
            );
            /** Gets spreadsheet data.   @return  A @link NXOpen::Tooling::SpreadsheetData NXOpen::Tooling::SpreadsheetData@endlink  instance 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpreadsheetData * GetParameterTreeData
            (
            );
            /** Sets spreadsheet data.  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetParameterTreeData
            (
                NXOpen::Tooling::SpreadsheetData * sheetData /** A @link NXOpen::Tooling::SpreadsheetData NXOpen::Tooling::SpreadsheetData@endlink  instance */
            );
            /** Gets the selected ejector component. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::NXObject * GetSelectedEjectorComponent
            (
            );
            /** Aligns selected ejectors in horizontal direction with same X value. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void XAlignment
            (
            );
            /** Aligns selected ejectors in vertical direction with same Y value. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void YAlignment
            (
            );
            /** Searches sleeve positions in parting part. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SearchSleeve
            (
                const NXString & maxPinDia /** the maximum diameter in the ejector pin template */
            );
            /** Searches sleeve positions in parting part. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            void SearchSleeve
            (
                const char * maxPinDia /** the maximum diameter in the ejector pin template */
            );
            /** Gets angle of the selected symbol.  @return  the angle of symbol 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: double GetSymbolAngle
            (
                NXOpen::Annotations::PmiCustomSymbol * symbolTag /** the selected symbol */
            );
            /** Deletes concept ejector. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void DeleteConceptEjector
            (
                NXOpen::Tooling::EjectorDesignData * singleRecord /** A @link NXOpen::Tooling::EjectorDesignData NXOpen::Tooling::EjectorDesignData@endlink  instance */
            );
            /** Deletes selected ejectors. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void DeleteEjector
            (
            );
            /** Deletes dumb design points. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void DeleteDumbDesignPoints
            (
            );
            /** Reads data from the library with given name and path. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void ReadEjectorClientDataFromLibrary
            (
                bool isFromMemberView /** True if an item is dragged from reuse library */,
                int dataType /** The data type of the library */,
                const NXString & libName /** Library name */,
                const NXString & libPath /** Library path */
            );
            /** Reads data from the library with given name and path. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            void ReadEjectorClientDataFromLibrary
            (
                bool isFromMemberView /** True if an item is dragged from reuse library */,
                int dataType /** The data type of the library */,
                const char * libName /** Library name */,
                const char * libPath /** Library path */
            );
            /** Resets standard client data. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void ResetStandardClientData
            (
                NXOpen::Tooling::EjectorDesignData * singleRecord /** A @link NXOpen::Tooling::EjectorDesignData NXOpen::Tooling::EjectorDesignData@endlink  instance */
            );
            /** Repositions the ejector instance. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RepositionEjector
            (
                NXOpen::Tooling::EjectorDesignData * singleRecord /** A @link NXOpen::Tooling::EjectorDesignData NXOpen::Tooling::EjectorDesignData@endlink  instance */,
                const NXString & fileName /** The part file name */,
                const NXString & refsetName /** The reference set name */
            );
            /** Repositions the ejector instance. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            void RepositionEjector
            (
                NXOpen::Tooling::EjectorDesignData * singleRecord /** A @link NXOpen::Tooling::EjectorDesignData NXOpen::Tooling::EjectorDesignData@endlink  instance */,
                const char * fileName /** The part file name */,
                const char * refsetName /** The reference set name */
            );
            /** Gets the information of add instance to determine whether to add new object or existed object.  @return  The type to add instance 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: bool GetAddInstanceInformation
            (
                NXString* pinLength /** The length of the ejector pin */,
                NXString* sleeveLength /** The length of the sleeve */,
                int* pinType /** The ejector type id */,
                bool* beyondRange /** The calculated length beyond the length list */,
                bool* isSleeve /** The searched sleeve pin */,
                bool* updateTemplateData /** Update the parameter tree */
            );
            /** Adds a new ejector pin.  @return  The inserted symbol tag 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Annotations::PmiCustomSymbol * AddEjectorPart
            (
                NXOpen::Tooling::ConceptStandardPartRecord * conceptRecord /** Concept standard part record */,
                const std::vector<double> & destinationCsys /** destinationcsys */ ,
                int pinType /** The ejector type id */,
                const NXString & pinLength /** The length of the ejector pin */,
                const NXString & sleeveLength /** The length of the sleeve */,
                bool isRecommended /** The recommended length status of the ejector pin */,
                const std::vector<double> & ejectorCsys /** The ejector pin csys */
            );
            /** Adds a new ejector pin.  @return  The inserted symbol tag 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            NXOpen::Annotations::PmiCustomSymbol * AddEjectorPart
            (
                NXOpen::Tooling::ConceptStandardPartRecord * conceptRecord /** Concept standard part record */,
                const std::vector<double> & destinationCsys /** destinationcsys */ ,
                int pinType /** The ejector type id */,
                const char * pinLength /** The length of the ejector pin */,
                const char * sleeveLength /** The length of the sleeve */,
                bool isRecommended /** The recommended length status of the ejector pin */,
                const std::vector<double> & ejectorCsys /** The ejector pin csys */
            );
            /** Adds an existing ejector pin.  @return  The inserted symbol tag 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Annotations::PmiCustomSymbol * AddInstanceOfExistingEjector
            (
                const std::vector<double> & destinationCsys /** destinationcsys */ ,
                int pinType /** The ejector type id */,
                const NXString & pinLength /** The length of the ejector pin */,
                const NXString & sleeveLength /** The length of the sleeve */,
                bool isRecommended /** The recommended length status of the ejector pin */,
                const std::vector<double> & ejectorCsys /** The ejector pin csys */,
                bool* isPointDeleted /** The deleted status of point */
            );
            /** Adds an existing ejector pin.  @return  The inserted symbol tag 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            NXOpen::Annotations::PmiCustomSymbol * AddInstanceOfExistingEjector
            (
                const std::vector<double> & destinationCsys /** destinationcsys */ ,
                int pinType /** The ejector type id */,
                const char * pinLength /** The length of the ejector pin */,
                const char * sleeveLength /** The length of the sleeve */,
                bool isRecommended /** The recommended length status of the ejector pin */,
                const std::vector<double> & ejectorCsys /** The ejector pin csys */,
                bool* isPointDeleted /** The deleted status of point */
            );
            /** Updates parameter data of existing instance components. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void UpdateDataOfInstance
            (
            );
            /** Finds the maximum diameter in the pin template list. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXString FindPinMaxDiameter
            (
            );
            /** Analyzes the parent parts. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetParentParts
            (
                bool bAnalyze /** banalyze */ 
            );
            /** Restores parameter data of selected instance components. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RestoreParameterOfInstance
            (
            );
            /** Edits concept symbols for ejectors. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void EditConceptEjector
            (
            );
            /** Sets the edit records data. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Annotations::PmiCustomSymbol * SetEditRecords
            (
            );
            /** Creates point in current RM part.  @return  The point tag 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Point * CreatePoint
            (
                bool createNewPoint /** Determine whether to create a new point */,
                const std::vector<double> & coordinates /** The point coordinates */,
                int conceptObjectLayer /** The layer index */
            );
            /** Gets install point csys matrix value.  @return  The origin of point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Point3d GetInstallPointMatrix
            (
                NXOpen::NXObject * pointTag /** The point tag */,
                NXOpen::Matrix3x3* matrix /** The csys matrix value */
            );
            /** Update longest recommended length for concept ejector. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void UpdateLengthForConceptEjector
            (
            );
            /** Gets the moving vector of the moving point.  @return  The point movement vector 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Vector3d GetMoveVector
            (
                NXOpen::NXObject * pointTag /** The point tag */,
                const NXOpen::Point3d & origin /** The origin of point */
            );
            /** Resets the coordinates of point after it's moved.  @return  The coordinates after the point has moved 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Point3d ResetPointsCoordinates
            (
                NXOpen::NXObject * pointTag /** The moving point tag */,
                const NXOpen::Matrix3x3 & matrix /** The matrix of the point */,
                const NXOpen::Vector3d & moveVector /** The point movement vector */,
                int currentHandle /** The handle type */,
                int gesture /** The user gesture */,
                int moveType /** The move type of the point */,
                double snapDistance /** The snip distance */,
                double angle /** The value of rotation angle */
            );
            /** Updates standard part spread sheet data by reading parameter values from a part, point or symbol. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void UpdateSpreadsheetDataWithObject
            (
                NXOpen::NXObject * objectWithParameters /** The object where parameter values to be read */,
                bool isConcpetObject /** True if the object is a concept one( a point or symbol with special attributes) */,
                NXOpen::Tooling::EjectorDesignData * designData /** the EjectorDesignData data */,
                NXOpen::Tooling::SpreadsheetData * sheetData /** Spreadsheet data */
            );
            /** Updates component data for select component. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void UpdateComponentData
            (
                const NXString & nativeDataPath /** The file path in native */,
                NXOpen::NXObject * partOcc /** partocc */ ,
                NXOpen::Tooling::SpreadsheetData * sheetData /** Spreadsheet data */
            );
            /** Updates component data for select component. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            void UpdateComponentData
            (
                const char * nativeDataPath /** The file path in native */,
                NXOpen::NXObject * partOcc /** partocc */ ,
                NXOpen::Tooling::SpreadsheetData * sheetData /** Spreadsheet data */
            );
        };
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
