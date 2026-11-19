-------------------------------------------------------------------------------
		UIStyler Selection Example
-------------------------------------------------------------------------------


Description:
------------
This example demonstrates the Selection capability of NXOpen UIStyler.
Running this example will launch a dialog which creates Edge Blend on the selected edges.


There is more than one way to compile this program (command prompt vs visual studio) 
and compilation instructions may vary slightly depending on the current release and 
your operating system.  For the most current compile and link instructions view the 
NXOpen documentation.


Once this program has been compiled and linked you need to place the dialog file
(UIStylerSelectionExample.dlg) in an application directory so that NX knows where
to find it.  Please see the NXOpen Programmer's Guide for details on how NX
locates custom applications at startup and how you must define the startup and
application directories.

You may also place the compiled/linked program (UIStylerSelectionExample.dll) with
the dialog file in the application directory, but it is not required to live in 
the application folder.

Now you're ready to start NX and use this example.

	1. Start NX.
	2. Open Block.prt file
	2. Go to File -> Execute ->NX Open.
	3. You will lead to window called "Execute User Function". 
	4. Navigate to the location of the dll file.  
	5. Select UistylerselectionExample.dll file and Click ok. 
	   This will launch the UIStylerSelectionExample.dlg file. 
	6. Select any edge/s (One of the edge of the Block is not selectable),
	   enter appropriate blend radius value and Ok the dialog, 
	   this will blend the selected edges.
