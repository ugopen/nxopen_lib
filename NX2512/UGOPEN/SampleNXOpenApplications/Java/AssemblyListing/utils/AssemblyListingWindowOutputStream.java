//
//          Copyright (c) 2005 UGS Corp.
//              All rights reserved
//               Written by V.A.L.

package utils;
import java.io.IOException;
import java.io.OutputStream;
import java.rmi.RemoteException;

import nxopen.ListingWindow;
import nxopen.NXException;

/** An OutputStream created out of an nxopen.ListingWindow */
public class AssemblyListingWindowOutputStream extends OutputStream
{
    private ListingWindow m_lw;
    private StringBuffer m_buf;
    
    public AssemblyListingWindowOutputStream(ListingWindow lw) throws NXException, RemoteException
    {
        m_lw = lw;
        m_buf = new StringBuffer();
        if ( !m_lw.isOpen() )
            m_lw.open();
    }

    /* (non-Javadoc)
     * @see java.io.OutputStream#write(int)
     */
    public void write(int b) throws IOException
    {
        char c = (char)b;
        try
        {
            if ( c == '\n' )
            {
                m_lw.writeLine(m_buf.toString());
                m_buf.delete(0, m_buf.length());
            }
            else
                m_buf.append(c);
        }
        catch (NXException ex)
        {
            throw new IOException(ex.toString());
        }

    }
    
    public void close() throws IOException
    {
        try
        {
            m_lw.close();
        }
        catch (NXException ex)
        {
            throw new IOException(ex.toString());
        }
    }

}
