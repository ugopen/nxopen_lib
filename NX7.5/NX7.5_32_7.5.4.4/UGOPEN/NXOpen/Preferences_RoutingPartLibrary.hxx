#ifndef NXOpen_PREFERENCES_ROUTINGPARTLIBRARY_HXX_INCLUDED
#define NXOpen_PREFERENCES_ROUTINGPARTLIBRARY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_RoutingPartLibrary.ja
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
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class RoutingPartLibrary;
    }
    namespace Preferences
    {
        class RoutingPart;
    }
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Preferences
    {
        class RoutingPartLibraryImpl;
        /**Represents a Routing Part library.   <br> To obtain an instance of this class, refer to @link Preferences::RoutingPart Preferences::RoutingPart@endlink  <br> */
        class NXOPENCPPEXPORT  RoutingPartLibrary
        {
            /** Type of nodes in the part library. */
            public: enum NodeType
            {
                NodeTypeNormal/** Normal node, may contain part table children.  
                                                                Doesn't have any part table information.  */,
                NodeTypeTable/** Part table node.  Contains columns/rows that
                                                                specify parts. */,
                NodeTypePart/** Part node, contains information necessary
                                                                for loading/using a routing part. */
            };

            /** Type of column values. */
            public: enum ColumnType
            {
                ColumnTypeInteger/** Integer values. */,
                ColumnTypeReal/** Floating-point values. */,
                ColumnTypeString = 4/** String values. */
            };

            /** Type of root nodes. */
            public: enum RootType
            {
                RootTypeTop/** Top of entire part table. */,
                RootTypeStock/** Top node for selecting stocks.*/,
                RootTypeWire/** Top node for selecting wires. */,
                RootTypePart/** Top node for selecting parts. */
            };

            /** Hidden status of a column. */
            public: enum ColumnStatus
            {
                ColumnStatusNotHidden/** Column is displayed in Specify Item. */,
                ColumnStatusHidden/** Column is not displayed in Specify Item. */
            };

             /** Part table column type. */
            public:
            struct  Column
            {
                public: /** Column name.  PART_NUMBER is the index column for
                                                                    all part tables.  */NXString Name;
                public: /** Whether or not the column is used for selection
                                                                    in the specify item dialog. */NXOpen::Preferences::RoutingPartLibrary::ColumnStatus Hidden;
                public: /** The value type the column stores. */NXOpen::Preferences::RoutingPartLibrary::ColumnType Type;
                public: Column() :
                    Name(),
                    Hidden((NXOpen::Preferences::RoutingPartLibrary::ColumnStatus)0),
                    Type((NXOpen::Preferences::RoutingPartLibrary::ColumnType)0)
                {
                }
                /** Constructor for the Column struct. */ 
                public: Column(const NXString &nameInitial /** Column name.  PART_NUMBER is the index column for
                                                                            all part tables.  */, 
                        NXOpen::Preferences::RoutingPartLibrary::ColumnStatus hiddenInitial /** Whether or not the column is used for selection
                                                                            in the specify item dialog. */, 
                        NXOpen::Preferences::RoutingPartLibrary::ColumnType typeInitial /** The value type the column stores. */) :
                    Name(nameInitial),
                    Hidden(hiddenInitial),
                    Type(typeInitial)
                {
                }
            };

            private: RoutingPartLibraryImpl * m_routingpartlibrary_impl;
            private: NXOpen::Preferences::RoutingPart* m_owner;
            /** Constructor */
            public: explicit RoutingPartLibrary(NXOpen::Preferences::RoutingPart *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~RoutingPartLibrary();
            /** Returns the root node of the part library. Returns NULL if there
                       is no root node.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetRoot
            (
            );
            /** Returns the root node of the part library using the current active
                       discipline.  Returns NULL if there is no root node.   @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetFilteredRoot
            (
                NXOpen::Preferences::RoutingPartLibrary::RootType rootType /** Which root node to find. */
            );
            /** Returns the children nodes of the input node.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXString> GetChildrenNodes
            (
                const NXString & parent /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Returns the node type.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPartLibrary::NodeType GetNodeType
            (
                const NXString & node /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Returns the table information for a given 
                        @link NXOpen::Preferences::RoutingPartLibrary::NodeTypeTable NXOpen::Preferences::RoutingPartLibrary::NodeTypeTable@endlink  node.   @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Preferences::RoutingPartLibrary::Column> GetTableDefinition
            (
                const NXString & node /** Must be a @link NXOpen::Preferences::RoutingPartLibrary::NodeTypeTable NXOpen::Preferences::RoutingPartLibrary::NodeTypeTable@endlink  
                                                    type node, any other node type causes an exception.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Returns the part information for a given 
                        @link NXOpen::Preferences::RoutingPartLibrary::NodeTypePart NXOpen::Preferences::RoutingPartLibrary::NodeTypePart@endlink  node.   @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::CharacteristicList * GetPartDefinition
            (
                const NXString & node /** Must be a @link NXOpen::Preferences::RoutingPartLibrary::NodeTypePart NXOpen::Preferences::RoutingPartLibrary::NodeTypePart@endlink  
                                                    type node, any other node type causes an exception.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a new empty @link Routing::CharacteristicList Routing::CharacteristicList@endlink  object that can be used
                     as input to @link Preferences::RoutingPartLibrary::MatchCriteria Preferences::RoutingPartLibrary::MatchCriteria@endlink  and
                     @link Preferences::RoutingPartLibrary::MatchCriteriaWithFilter Preferences::RoutingPartLibrary::MatchCriteriaWithFilter@endlink .   @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::CharacteristicList * CreateCriteria
            (
            );
            /** Search for entries in the part library table nodes that match the given set of 
                      criteria.  Returns an array of @link Routing::CharacteristicList Routing::CharacteristicList@endlink  objects that
                      can be used for assigning stock or placing parts. Searches all nodes at or below
                      the input node for matches.
                       <br>  
                        Performs matches on the name/value pairs in the input critiera, to the column name
                        column values in the part tables below the input node.  Ignores names in the input 
                        critiera that don't have a corresonding column in the part for matching.
                       <br>  
                       @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::CharacteristicList *> MatchCriteria
            (
                const NXString & startNode /** Must not be a @link NXOpen::Preferences::RoutingPartLibrary::NodeTypePart NXOpen::Preferences::RoutingPartLibrary::NodeTypePart@endlink  
                                                    node.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Routing::CharacteristicList * criteria /** criteria */ 
            );
            /** Similar to @link Preferences::RoutingPartLibrary::MatchCriteria Preferences::RoutingPartLibrary::MatchCriteria@endlink , however it also
                     filters out any parts that don't match the critiera specified by the current specification.   @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::CharacteristicList *> MatchCriteriaWithFilter
            (
                const NXString & startNode /** Must not be a @link NXOpen::Preferences::RoutingPartLibrary::NodeTypePart NXOpen::Preferences::RoutingPartLibrary::NodeTypePart@endlink  
                                                    node.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Routing::CharacteristicList * criteria /** criteria */ 
            );
            /** Does a characteristic list match the current discipline and specifications?  @return  Is the characteristic list valid under the current discipline and specifications?  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool FilterOnCurrentSpecifications
            (
                NXOpen::Routing::CharacteristicList * match /** The matching part's Characteristic List to check against the
                                                            current discipline and specifications. */,
                std::vector<NXString> & partClasses /** The part class hierarchy list that contains the matching part. 
                                                            The first item in the list is the top node name. The last 
                                                            item in the list is the lowest node that contains the matching part.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif