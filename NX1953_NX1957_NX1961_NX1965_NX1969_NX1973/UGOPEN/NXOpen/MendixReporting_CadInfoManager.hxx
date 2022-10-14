#ifndef NXOpen_MENDIXREPORTING_CADINFOMANAGER_HXX_INCLUDED
#define NXOpen_MENDIXREPORTING_CADINFOMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MendixReporting_CadInfoManager.ja
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
#include <NXOpen/libnxopencpp_mendixreporting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MendixReporting
    {
        class CadInfoManager;
    }
    class BasePart;
    class TaggedObject;
    namespace MendixReporting
    {
        class CadInfoManagerImpl;

        /// \cond NX_NO_DOC 
        /** For Internal NX Usage with specific projects only  <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_MENDIXREPORTINGEXPORT  CadInfoManager
        {

            /// \cond NX_NO_DOC 
             /** Contains flags for part information and part type */
            public:
            struct PartInformation
            {
                public: /** part has udf */ bool PartHasUdf;
                public: /** part has pos indep wave link */ bool PartHasPosIndepWaveLink;
                public: /** part has pos dep wave link */ bool PartHasPosDepWaveLink;
                public: /** part has interpart expression */ bool PartHasInterpartExpression;
                public: /** part has interpart references */ bool PartHasInterpartReferences;
                public: /** part has product interface */ bool PartHasProductInterface;
                public: /** part has broken links */ bool PartHasBrokenLinks;
                public: /** part has any components */ bool PartHasAnyComponents;
                public: /** part has geometry overrides */ bool PartHasGeometryOverrides;
                public: /** part has position overrides */ bool PartHasPositionOverrides;
                public: /** part has reference components */ bool PartHasReferenceComponents;
                public: /** part has supressed components */ bool PartHasSupressedComponents;
                public: /** part has restructured components */ bool PartHasRestructuredComponents;
                public: /** part has nonmaster component */ bool PartHasNonmasterComponent;
                public: /** part has multiple arrangements */ bool PartHasMultipleArrangements;
                public: /** part has altrep meta data */ bool PartHasAltrepMetaData;
                public: /** part has offcenter components */ bool PartHasOffcenterComponents;
                public: /** part has parts list */ bool PartHasPartsList;
                public: /** part has constraint */ bool PartHasConstraint;
                public: /** part is drawing */ bool PartIsDrawing;
                public: /** part has cae data */ bool PartHasCaeData;
                public: /** part has cam data */ bool PartHasCamData;
                public: /** part is part family member */ bool PartIsPartFamilyMember;
                public: /** part is part family template */ bool PartIsPartFamilyTemplate;
                public: /** part is part */ bool PartIsPart;
                public: /** part has measurable attribute */ bool PartHasMeasurableAttribute;
                public: /** part has body */ bool PartHasBody;
                public: /** part has suppression override */ bool PartHasSuppressionOverride;
                public: /** part has vis structure stream */ bool PartHasVisStructureStream;
                public: /** part has vis rm stream */ bool PartHasVisRmStream;
                public: /** part part units */ bool PartPartUnits;
                public: /** part has sheet metal data */ bool PartHasSheetMetalData;
                public: /** part is routing part */ bool PartIsRoutingPart;
                public: /** part is route system assembly */ bool PartIsRouteSystemAssembly;
                public: PartInformation() :
                    PartHasUdf(),
                    PartHasPosIndepWaveLink(),
                    PartHasPosDepWaveLink(),
                    PartHasInterpartExpression(),
                    PartHasInterpartReferences(),
                    PartHasProductInterface(),
                    PartHasBrokenLinks(),
                    PartHasAnyComponents(),
                    PartHasGeometryOverrides(),
                    PartHasPositionOverrides(),
                    PartHasReferenceComponents(),
                    PartHasSupressedComponents(),
                    PartHasRestructuredComponents(),
                    PartHasNonmasterComponent(),
                    PartHasMultipleArrangements(),
                    PartHasAltrepMetaData(),
                    PartHasOffcenterComponents(),
                    PartHasPartsList(),
                    PartHasConstraint(),
                    PartIsDrawing(),
                    PartHasCaeData(),
                    PartHasCamData(),
                    PartIsPartFamilyMember(),
                    PartIsPartFamilyTemplate(),
                    PartIsPart(),
                    PartHasMeasurableAttribute(),
                    PartHasBody(),
                    PartHasSuppressionOverride(),
                    PartHasVisStructureStream(),
                    PartHasVisRmStream(),
                    PartPartUnits(),
                    PartHasSheetMetalData(),
                    PartIsRoutingPart(),
                    PartIsRouteSystemAssembly()
                {
                }
                /** Constructor for the PartInformation struct. */ 
                public: PartInformation(bool partHasUdfInitial /** part has udf */ , 
                        bool partHasPosIndepWaveLinkInitial /** part has pos indep wave link */ , 
                        bool partHasPosDepWaveLinkInitial /** part has pos dep wave link */ , 
                        bool partHasInterpartExpressionInitial /** part has interpart expression */ , 
                        bool partHasInterpartReferencesInitial /** part has interpart references */ , 
                        bool partHasProductInterfaceInitial /** part has product interface */ , 
                        bool partHasBrokenLinksInitial /** part has broken links */ , 
                        bool partHasAnyComponentsInitial /** part has any components */ , 
                        bool partHasGeometryOverridesInitial /** part has geometry overrides */ , 
                        bool partHasPositionOverridesInitial /** part has position overrides */ , 
                        bool partHasReferenceComponentsInitial /** part has reference components */ , 
                        bool partHasSupressedComponentsInitial /** part has supressed components */ , 
                        bool partHasRestructuredComponentsInitial /** part has restructured components */ , 
                        bool partHasNonmasterComponentInitial /** part has nonmaster component */ , 
                        bool partHasMultipleArrangementsInitial /** part has multiple arrangements */ , 
                        bool partHasAltrepMetaDataInitial /** part has altrep meta data */ , 
                        bool partHasOffcenterComponentsInitial /** part has offcenter components */ , 
                        bool partHasPartsListInitial /** part has parts list */ , 
                        bool partHasConstraintInitial /** part has constraint */ , 
                        bool partIsDrawingInitial /** part is drawing */ , 
                        bool partHasCaeDataInitial /** part has cae data */ , 
                        bool partHasCamDataInitial /** part has cam data */ , 
                        bool partIsPartFamilyMemberInitial /** part is part family member */ , 
                        bool partIsPartFamilyTemplateInitial /** part is part family template */ , 
                        bool partIsPartInitial /** part is part */ , 
                        bool partHasMeasurableAttributeInitial /** part has measurable attribute */ , 
                        bool partHasBodyInitial /** part has body */ , 
                        bool partHasSuppressionOverrideInitial /** part has suppression override */ , 
                        bool partHasVisStructureStreamInitial /** part has vis structure stream */ , 
                        bool partHasVisRmStreamInitial /** part has vis rm stream */ , 
                        bool partPartUnitsInitial /** part part units */ , 
                        bool partHasSheetMetalDataInitial /** part has sheet metal data */ , 
                        bool partIsRoutingPartInitial /** part is routing part */ , 
                        bool partIsRouteSystemAssemblyInitial /** part is route system assembly */ ) :
                    PartHasUdf(partHasUdfInitial),
                    PartHasPosIndepWaveLink(partHasPosIndepWaveLinkInitial),
                    PartHasPosDepWaveLink(partHasPosDepWaveLinkInitial),
                    PartHasInterpartExpression(partHasInterpartExpressionInitial),
                    PartHasInterpartReferences(partHasInterpartReferencesInitial),
                    PartHasProductInterface(partHasProductInterfaceInitial),
                    PartHasBrokenLinks(partHasBrokenLinksInitial),
                    PartHasAnyComponents(partHasAnyComponentsInitial),
                    PartHasGeometryOverrides(partHasGeometryOverridesInitial),
                    PartHasPositionOverrides(partHasPositionOverridesInitial),
                    PartHasReferenceComponents(partHasReferenceComponentsInitial),
                    PartHasSupressedComponents(partHasSupressedComponentsInitial),
                    PartHasRestructuredComponents(partHasRestructuredComponentsInitial),
                    PartHasNonmasterComponent(partHasNonmasterComponentInitial),
                    PartHasMultipleArrangements(partHasMultipleArrangementsInitial),
                    PartHasAltrepMetaData(partHasAltrepMetaDataInitial),
                    PartHasOffcenterComponents(partHasOffcenterComponentsInitial),
                    PartHasPartsList(partHasPartsListInitial),
                    PartHasConstraint(partHasConstraintInitial),
                    PartIsDrawing(partIsDrawingInitial),
                    PartHasCaeData(partHasCaeDataInitial),
                    PartHasCamData(partHasCamDataInitial),
                    PartIsPartFamilyMember(partIsPartFamilyMemberInitial),
                    PartIsPartFamilyTemplate(partIsPartFamilyTemplateInitial),
                    PartIsPart(partIsPartInitial),
                    PartHasMeasurableAttribute(partHasMeasurableAttributeInitial),
                    PartHasBody(partHasBodyInitial),
                    PartHasSuppressionOverride(partHasSuppressionOverrideInitial),
                    PartHasVisStructureStream(partHasVisStructureStreamInitial),
                    PartHasVisRmStream(partHasVisRmStreamInitial),
                    PartPartUnits(partPartUnitsInitial),
                    PartHasSheetMetalData(partHasSheetMetalDataInitial),
                    PartIsRoutingPart(partIsRoutingPartInitial),
                    PartIsRouteSystemAssembly(partIsRouteSystemAssemblyInitial)
                {
                }
            };


            /// \endcond 
            private: CadInfoManagerImpl * m_cadinfomanager_impl;
            private: NXOpen::BasePart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CadInfoManager(NXOpen::BasePart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CadInfoManager();

            /// \cond NX_NO_DOC 
            /** Returns the creation date/time in UTC 
                    *   Date/time format example :  17-Mar-2020 12:34:54
                    
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetCreationDate
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the creation user name
                    
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetCreatedBy
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the last modification date/time in UTC
                    *   Date/time format example :  17-Mar-2020 12:34:54
                    
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetLastModificationDate
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the user name for last modification
                    
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetLastModifiedBy
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the partType with comma separated values
                     *  First value is part extension.
                     *  Following values may be appended if applicable to given part :
                     *  Drawing, PartFamilyTemplate, PartFamilyMember
                     
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetPartType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the Base64 ps and geometry cvf stream for the provided part 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void GetCvfForPart
            (
                bool bGenerateCvfFiles /** bgeneratecvffiles */ ,
                NXString* psCvfStream /** pscvfstream */ ,
                NXString* geometryCvfStream /** geometrycvfstream */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the PersistentIdentifier in form of jam id string and comma separated context ids string for the provided componentTag 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetPersistentIdForPart
            (
                NXOpen::TaggedObject * componentTag /** componenttag */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the pllink for the given part
                     *  This encrypted link will be used for opening the part in NX from Mendix App.
                     
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetPLLinkForPart
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Returns the PartInformation
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::MendixReporting::CadInfoManager::PartInformation GetPartInformation
            (
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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