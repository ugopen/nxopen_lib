#ifndef NXOpen_ROUTING_ELECTRICAL_CONNECTION_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_CONNECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_Connection.ja
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
#include <NXOpen/Routing_LogicalConnection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class Connection;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class CableDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class ConnectorDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class HarnessDevice;
        }
    }
    namespace Routing
    {
        class LogicalConnection;
    }
    namespace Routing
    {
        class LogicalTerminal;
    }
    namespace Routing
    {
        class SingleDevice;
    }
    namespace Routing
    {
        namespace Electrical
        {
            class _ConnectionBuilder;
            /**  @brief 
                        The electrical usage of a @link Routing::LogicalConnection Routing::LogicalConnection@endlink , restricted to
                        one From and one To terminal.
                         

             
                         <br> 
                        See NX Open Routing help for detailed information on the Connection data model.
                         <br> 
                     <br> Creator not available in KF. <br> */
            class NXOPENCPPEXPORT Connection : public Routing::LogicalConnection
            {
                private: friend class  _ConnectionBuilder;
                protected: Connection();
                /**Returns  the From terminal. The From terminal is one end of an electrical connection.  From does not imply an ordering. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::LogicalTerminal * FromTerminal
                (
                );
                /**Returns  the To terminal. The To terminal is one end of an electrical connection.  To does not imply an ordering <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::LogicalTerminal * ToTerminal
                (
                );
                /**Sets  the From terminal. The From terminal is one end of an electrical connection.  From does not imply an ordering. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetFromTerminal
                (
                    NXOpen::Routing::LogicalTerminal * fromTerminal /** May not be NULL */
                );
                /**Sets  the To terminal. The To terminal is one end of an electrical connection.  To does not imply an ordering <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetToTerminal
                (
                    NXOpen::Routing::LogicalTerminal * toTerminal /**May not be NULL*/
                );
                /** Get the intermediate terminals associated with this connection. Intermediate Terminals are
                                optional and need not exist for a @link Routing::Electrical::Connection Routing::Electrical::Connection@endlink  to be valid in NX. @return  Collection of intermediate @link Routing::LogicalTerminal Routing::LogicalTerminal@endlink  - May be NULL <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: std::vector<NXOpen::Routing::LogicalTerminal *> GetIntermediateTerminals
                (
                );
                /** Replaces the intermediate terminals associated with this connection.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void ReplaceIntermediateTerminals
                (
                    const std::vector<NXOpen::Routing::LogicalTerminal *> & intermediateTerminals /** Collection of intermediate @link Routing::LogicalTerminal Routing::LogicalTerminal@endlink  - Use NULL to remove all intermdiate terminals */
                );
                /** Add an intermediate terminal to this connection @return  @link Routing::LogicalTerminal Routing::LogicalTerminal@endlink  added?   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: bool AddIntermediateTerminal
                (
                    NXOpen::Routing::LogicalTerminal * intermediateTerminal /** may be NULL */
                );
                /** Remove an intermediate terminal from this connection @return  @link Routing::LogicalTerminal Routing::LogicalTerminal@endlink  removed?   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: bool RemoveIntermediateTerminal
                (
                    NXOpen::Routing::LogicalTerminal * intermediateTerminal /** may be NULL */
                );
                /**Returns  the minimum path length for this connection.  Minimum path length is the shortest allowable length
                                of all segments referred to by this connection. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: double MinimumPathLength
                (
                );
                /**Sets  the minimum path length for this connection.  Minimum path length is the shortest allowable length
                                of all segments referred to by this connection. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetMinimumPathLength
                (
                    double pathLength /** May be zero */
                );
                /**Returns  the maximum path length for this connection.  Maximum path length is the longest allowable length
                                of all segments referred to by this connection. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: double MaximumPathLength
                (
                );
                /**Sets  the maximum path length for this connection.  Maximum path length is the longest allowable length
                                of all segments referred to by this connection. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetMaximumPathLength
                (
                    double pathLength /** May be zero */
                );
                /**Returns  the path length multiplier.  Used to calculate cut length.  
                                Cut length = length * multiplier + offset  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXString PathLengthMultiplier
                (
                );
                /**Sets  the path length multiplier.  Used to calculate cut length.  
                                Cut length = length * multiplier + offset  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetPathLengthMultiplier
                (
                    const NXString & pathLengthMultiplier /** May be zero (cut length will be zero)  */
                );
                /**Returns  the path length offset.  Used to calculate cut length.  
                                Cut length = length * multiplier + offset  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXString PathLengthOffset
                (
                );
                /**Sets  the path length offset.  Used to calculate cut length.  
                                Cut length = length * multiplier + offset  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetPathLengthOffset
                (
                    const NXString & pathLengthOffset /** May be zero */
                );
                /** Gets the method used to route this connection.  @return  <ul>
                                                                                       <li>"A" Connection is auto routed</li>
                                                                                       <li>"M" Connection is manual routed</li>
                                                                                       <li>"N" Connection is not routed</li>
                                                                                       </ul>  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXString GetRoutingMethod
                (
                );
                /** Gets the level used to route this connection.  @return  <ul>
                                                                                       <li>"C" Connection routed at component level</li>
                                                                                       <li>"P" Connection routed at pin level</li>
                                                                                       <li>"M" Connection routed at mixed level</li>
                                                                                       </ul>  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXString GetRoutedLevel
                (
                );
                /** Is this connection routed?  @return  Is connection routed?  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: bool IsRouted
                (
                );
                /** Queries this connection for the nearest parent device.  The nearest parent device is either
                                a cable, shield, or harness   @return  May be NULL if connection is not in a harness, cable, or shield <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::SingleDevice * FindNearestParentDevice
                (
                );
                /** Query this connection to find the nearest harness.
                                Only finds a harness that is a parent to this connection at some level up the connection heirarchy.  @return  May be NULL if connection is not in a harness  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::HarnessDevice * FindNearestHarnessDevice
                (
                );
                /** Query this connection to find the nearest harness.
                                Only finds a cable that is a parent to this connection at some level up the connection heirarchy. @return  May be NULL if connection is not in a cable  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::CableDevice * FindNearestCableDevice
                (
                );
                /** Get the From Connector for this connection.  From does not imply an ordering.  @return  May be NULL   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::ConnectorDevice * FindFromConnector
                (
                );
                /** Get the To Connector for this connection.  To does not imply an ordering  @return  May be NULL  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::ConnectorDevice * FindToConnector
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
