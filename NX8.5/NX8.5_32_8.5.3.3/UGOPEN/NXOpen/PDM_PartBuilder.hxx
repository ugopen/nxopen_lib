#ifndef NXOpen_PDM_PARTBUILDER_HXX_INCLUDED
#define NXOpen_PDM_PARTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_PartBuilder.ja
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
#include <NXOpen/PDM_AlternateIdManager.hxx>
#include <NXOpen/PDM_DatabaseAttributeManager.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_pdm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PDM
    {
        class PartBuilder;
    }
    namespace PDM
    {
        class AlternateIdManager;
    }
    namespace PDM
    {
        class DatabaseAttributeManager;
    }
    namespace PDM
    {
        class PartCreationObject;
    }
    namespace PDM
    {
        class PartBuilderImpl;
        /** This class serves as the base class for NX Manager part builders. The
                NX Manager part builders are used to create new parts in NX Manager mode.
             <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  PartBuilder : public TransientObject
        {
             /** Contains part number information.*/
            public:
            struct  PartNumberData
            {
                public: /** The part name*/NXString PartName;
                public: /** Modifiable flag for part name.*/bool PartNameModifiable;
                public: /** The part description*/NXString PartDescription;
                public: /** Modifiable flag for part description.*/bool PartDescriptionModifiable;
                public: /** The part number*/NXString PartNumber;
                public: /** Modifiable flag for part number.*/bool PartNumberModifiable;
                public: PartNumberData() :
                    PartName(),
                    PartNameModifiable(),
                    PartDescription(),
                    PartDescriptionModifiable(),
                    PartNumber(),
                    PartNumberModifiable()
                {
                }
                /** Constructor for the PartNumberData struct. */ 
                public: PartNumberData(const NXString &partNameInitial /** The part name*/, 
                        bool partNameModifiableInitial /** Modifiable flag for part name.*/, 
                        const NXString &partDescriptionInitial /** The part description*/, 
                        bool partDescriptionModifiableInitial /** Modifiable flag for part description.*/, 
                        const NXString &partNumberInitial /** The part number*/, 
                        bool partNumberModifiableInitial /** Modifiable flag for part number.*/) :
                    PartName(partNameInitial),
                    PartNameModifiable(partNameModifiableInitial),
                    PartDescription(partDescriptionInitial),
                    PartDescriptionModifiable(partDescriptionModifiableInitial),
                    PartNumber(partNumberInitial),
                    PartNumberModifiable(partNumberModifiableInitial)
                {
                }
            };

             /** Contains part revision information */
            public:
            struct  PartRevisionData
            {
                public: /**Part revision*/NXString PartRevision;
                public: /** Revision Modifiable flag. False if part revision is not modifiable*/bool PartRevisionModifiable;
                public: PartRevisionData() :
                    PartRevision(),
                    PartRevisionModifiable()
                {
                }
                /** Constructor for the PartRevisionData struct. */ 
                public: PartRevisionData(const NXString &partRevisionInitial /**Part revision*/, 
                        bool partRevisionModifiableInitial /** Revision Modifiable flag. False if part revision is not modifiable*/) :
                    PartRevision(partRevisionInitial),
                    PartRevisionModifiable(partRevisionModifiableInitial)
                {
                }
            };

             /** Contains part file name information */
            public:
            struct  PartFileNameData
            {
                public: /**Part file name*/NXString PartFileName;
                public: /** False if part file name is not modifiable*/bool PartFileNameModifiable;
                public: PartFileNameData() :
                    PartFileName(),
                    PartFileNameModifiable()
                {
                }
                /** Constructor for the PartFileNameData struct. */ 
                public: PartFileNameData(const NXString &partFileNameInitial /**Part file name*/, 
                        bool partFileNameModifiableInitial /** False if part file name is not modifiable*/) :
                    PartFileName(partFileNameInitial),
                    PartFileNameModifiable(partFileNameModifiableInitial)
                {
                }
            };

            /** Tokens identifying every possible UG/Manager part selection dialog. */
            public: enum Operation
            {
                OperationExportPartNew/** File-\>Export-\>Part:New radio button*/,
                OperationAssemblyDiagram/** Assembly-\>Report-\>Assembly Diagram... */,
                OperationAssemblyCreateNewComponent/** Assembly-\>Component-\>Create New... */,
                OperationDefault/** Default UG/Manager part selection dialog*/
            };

            private: PartBuilderImpl * m_partbuilder_impl;
            /// \cond NX_NO_DOC 
            public: explicit PartBuilder(void *ptr);
            /// \endcond 
            /** Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PartBuilder();
            /** Create the specification for the new part that will be created. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void CreatePartSpec
            (
                const NXString & partType /** the part type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & partNumber /** the part number   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & partRevision /** the part revision   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & partFileType /** the part file type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & partFileName /** the part file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Create the specification for the new part that will be created. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            void CreatePartSpec
            (
                const char * partType /** the part type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * partNumber /** the part number   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * partRevision /** the part revision   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * partFileType /** the part file type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * partFileName /** the part file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Create an instance of a @link PDM::DatabaseAttributeManager PDM::DatabaseAttributeManager@endlink 
                    class that will be used to modify database attributes while creating the new part.  @return  the new @link PDM::DatabaseAttributeManager PDM::DatabaseAttributeManager@endlink  instance 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::DatabaseAttributeManager * NewDatabaseAttributeManager
            (
            );
            /** Create an instance of a @link PDM::PartCreationObject PDM::PartCreationObject@endlink 
                    class that acts as a proxy for a part in NX Manager mode prior to that part
                    being created.  @return  the new @link PDM::PartCreationObject PDM::PartCreationObject@endlink  instance 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::PartCreationObject * CreatePartCreationObject
            (
            );
            /** Create an instance of a @link PDM::AlternateIdManager PDM::AlternateIdManager@endlink 
                    class that will be used to create alternate ID information while creating the new part.  @return  the new @link PDM::AlternateIdManager PDM::AlternateIdManager@endlink  instance 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::AlternateIdManager * NewAlternateIdManager
            (
            );
            /** This method generates a part number given an input part type and
                    assigns this part number to the builder.
                    
                     <br> The input part type will also be assigned to the builder. If the
                    input part type is NULL then this method will fail unless the part
                    type has already been set on the builder via a previous call to this method
                    or to @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink .
                     <br> 

                     <br> 
                    If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    (as will typically be the case) then the <b>part_type</b> and
                    <b>part_number</b> parameters of
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the values assigned
                    by this method. Otherwise, CreatePartSpec will override the values assigned
                    here and assign the values of the <b>part_type</b> and <b>part_number</b>
                    parameters to the builder.
                     <br> 
                     @return  the assigned part number 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString AssignPartNumber
            (
                const NXString & partType /** the part type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** This method generates a part number given an input part type and
                    assigns this part number to the builder.
                    
                     <br> The input part type will also be assigned to the builder. If the
                    input part type is NULL then this method will fail unless the part
                    type has already been set on the builder via a previous call to this method
                    or to @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink .
                     <br> 

                     <br> 
                    If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    (as will typically be the case) then the <b>part_type</b> and
                    <b>part_number</b> parameters of
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the values assigned
                    by this method. Otherwise, CreatePartSpec will override the values assigned
                    here and assign the values of the <b>part_type</b> and <b>part_number</b>
                    parameters to the builder.
                     <br> 
                     @return  the assigned part number 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            NXString AssignPartNumber
            (
                const char * partType /** the part type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**This method generates a part revision and assigns this part revision
                    to the builder.

                     <br> 
                    This method depends on the part type and part number already being
                    set on the builder. Therefore, a call to
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
                    more likely, to @link AssignPartNumber AssignPartNumber@endlink  must be made
                    before calling this method.
                     <br> 

                     <br> 
                    If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    (as will typically be the case) then the <b>part_revision</b> parameter of
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the value assigned
                    by this method. Otherwise, CreatePartSpec will override the value assigned
                    here and assign the value of the <b>part_revision</b>
                    parameters to the builder.
                     <br> 
                     @return  the assigned part revision 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString AssignPartRevision
            (
            );
            /**This method generates a part file name given an input part file type and
                    assigns this part file name to the builder.

                     <br> 
                    This method depends on the part type, part number, and part revision
                    already being set on the builder. Therefore, a call to
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
                    more likely, calls to @link PDM::PartBuilder::AssignPartNumber PDM::PartBuilder::AssignPartNumber@endlink  and
                    @link PDM::PartBuilder::AssignPartRevision PDM::PartBuilder::AssignPartRevision@endlink  must be made
                    before calling this method.
                     <br> 

                     <br> 
                    If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    (as will typically be the case) then the <b>part_file_type</b> and
                    <b>part_file_name</b> parameters of
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the values assigned
                    by this method. Otherwise, CreatePartSpec will override the values assigned
                    here and assign the values of the <b>part_file_type</b> and <b>part_file_name</b>
                    parameters to the builder.
                     <br> 

                     @return  the assigned part file name 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString AssignPartFileName
            (
                const NXString & partFileType /** the part file type. Note that if the
                               part file type is "master", then this method will return NULL but
                               will still set the part file type in the builder.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**This method generates a part file name given an input part file type and
                    assigns this part file name to the builder.

                     <br> 
                    This method depends on the part type, part number, and part revision
                    already being set on the builder. Therefore, a call to
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
                    more likely, calls to @link PDM::PartBuilder::AssignPartNumber PDM::PartBuilder::AssignPartNumber@endlink  and
                    @link PDM::PartBuilder::AssignPartRevision PDM::PartBuilder::AssignPartRevision@endlink  must be made
                    before calling this method.
                     <br> 

                     <br> 
                    If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    (as will typically be the case) then the <b>part_file_type</b> and
                    <b>part_file_name</b> parameters of
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the values assigned
                    by this method. Otherwise, CreatePartSpec will override the values assigned
                    here and assign the values of the <b>part_file_type</b> and <b>part_file_name</b>
                    parameters to the builder.
                     <br> 

                     @return  the assigned part file name 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            NXString AssignPartFileName
            (
                const char * partFileType /** the part file type. Note that if the
                               part file type is "master", then this method will return NULL but
                               will still set the part file type in the builder.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** This method generates a part number given an input part type and
                    sets this part number to the builder.
                    
                     <br> The input part type will also be assigned to the builder. If the
                    input part type is NULL then this method will fail unless the part
                    type has already been set on the builder via a previous call to this method
                    or to @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink .
                     <br> 

                     <br> 
                    If this overloaded method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    then the <b>part_number</b> parameter of
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the value assigned
                    by this method. Otherwise, CreatePartSpec will override the value assigned
                    here and assign the value of <b>part_number</b>
                    parameter to the builder.
                     <br> 
                     @return  Contains part number information.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::PartBuilder::PartNumberData AssignPartNumber
            (
                const NXString & oldPartNumber /** Old part number   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & partType /** Part type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** This method generates a part number given an input part type and
                    sets this part number to the builder.
                    
                     <br> The input part type will also be assigned to the builder. If the
                    input part type is NULL then this method will fail unless the part
                    type has already been set on the builder via a previous call to this method
                    or to @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink .
                     <br> 

                     <br> 
                    If this overloaded method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    then the <b>part_number</b> parameter of
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the value assigned
                    by this method. Otherwise, CreatePartSpec will override the value assigned
                    here and assign the value of <b>part_number</b>
                    parameter to the builder.
                     <br> 
                     @return  Contains part number information.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::PDM::PartBuilder::PartNumberData AssignPartNumber
            (
                const char * oldPartNumber /** Old part number   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * partType /** Part type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** This method generates a part revision and sets this part number to the builder.

                     <br> 
                    This method depends on the part type and part number already being
                    set on the builder. Therefore, a call to
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
                    more likely, to @link AssignPartNumber AssignPartNumber@endlink  must be made
                    before calling this method.
                     <br> 

                     <br> If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    then the <b>part_revision</b> parameter of
                    @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the value assigned
                    by this method. Otherwise, CreatePartSpec will override the value assigned
                    here and assign the value of the <b>part_revision</b>
                    parameters to the builder.
                     <br> 
                     @return  Contains part revision information 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::PartBuilder::PartRevisionData AssignPartRevision
            (
                int overload /** Dummy parameter to call this overloaded method*/
            );
            /**This method generates a part file name and assigns this part 
                    file name to the builder.

                     <br> 
                    If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    then the <b>part_file_name</b> parameter of @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the value assigned
                    by this method. Otherwise, CreatePartSpec will override the value assigned
                    here and assign the values of the <b>part_file_type</b> and <b>part_file_name</b>
                    parameters to the builder.
                     <br> 

                     @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::PartBuilder::PartFileNameData AssignPartFileName
            (
                const NXString & partNumber /**Part Number  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & partRevision /** part revision  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & partFileNameType /**Part file name type.
                                Note that if the part file type is "master", then this method will set the 
                                field <b>PartFileName</b> of @link PDM::PartBuilder::PartFileNameData PDM::PartBuilder::PartFileNameData@endlink 
                                with NULL  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & oldPartFileName /**Old part file name  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**This method generates a part file name and assigns this part 
                    file name to the builder.

                     <br> 
                    If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    then the <b>part_file_name</b> parameter of @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                    should be set to NULL so that the builder will use the value assigned
                    by this method. Otherwise, CreatePartSpec will override the value assigned
                    here and assign the values of the <b>part_file_type</b> and <b>part_file_name</b>
                    parameters to the builder.
                     <br> 

                     @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::PDM::PartBuilder::PartFileNameData AssignPartFileName
            (
                const char * partNumber /**Part Number  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * partRevision /** part revision  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * partFileNameType /**Part file name type.
                                Note that if the part file type is "master", then this method will set the 
                                field <b>PartFileName</b> of @link PDM::PartBuilder::PartFileNameData PDM::PartBuilder::PartFileNameData@endlink 
                                with NULL  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * oldPartFileName /**Old part file name  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**
                    Sets the part number explicitly into builder.   <br> 
                    This method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink         
                     <br> 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAssignPartNumber
            (
                const NXString & partNumber /** the part number   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**
                    Sets the part number explicitly into builder.   <br> 
                    This method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink         
                     <br> 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetAssignPartNumber
            (
                const char * partNumber /** the part number   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**
                    Sets the part type explicitly into builder.   <br> 
                    This method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink        
                     <br> 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAssignPartType
            (
                const NXString & partType /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**
                    Sets the part type explicitly into builder.   <br> 
                    This method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink        
                     <br> 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetAssignPartType
            (
                const char * partType /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
                    Sets explicitly the place from where part selection dialog invoked into builder.
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetContextOperation
            (
                NXOpen::PDM::PartBuilder::Operation operation /** Token identifying place from where UG/Manager part selection dialog invoked */
            );
        }; //lint !e1712 default constructor not defined for class  

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
