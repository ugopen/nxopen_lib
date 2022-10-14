/*==================================================================================================

            Copyright (c) 2004 UGS PLM Solutions.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example explains show how to create an Arc using Swing.
@<DEL>@ TEXT ENCLOSED within delete markers will be REMOVED
====================================================================================================
   Date      Name                    Description of Change
04-Jul-2005  Abhishek Mishra         Fix for PR# 5187197
$HISTORY$
====================================================================================================
TEXT ENCLOSED within delete markers will be REMOVED @<DEL>@ 
*/
import java.awt.*;
import java.awt.event.*; 
import javax.swing.*;
import javax.swing.event.*;
import nxopen.*;
import nxopen.uf.*;
import javax.swing.JOptionPane;
import java.io.PrintWriter;
import java.io.StringWriter;
import javax.swing.BorderFactory;
import javax.swing.border.Border;
import java.io.*;
public class CreateImage extends JDialog  implements ActionListener, Runnable,FocusListener
{ 
    JPanel				snagPanel; 
	JTextField			fileName;
    JLabel				enterFileName;
    JButton				btnCreate,btnCancel;
    JButton				btnBrowse;
    JRadioButton		rdBMP,rdJPG,rdCMPRSD,rdORIGINAL,rdWHITE,rdGIF,rdPNG,rdTIFF;
	ButtonGroup			myButtonGroup ;
	int					fileTypeflag;
	int					fileBGflag;
    public	Session		theSession	=null ;
	public 	UFSession	theUFSession=null ;
	public	String		strDefaultFile;
	public	UFDisp.ImageFormat imageFormat			= UFDisp.ImageFormat.BMP;
	public	UFDisp.BackgroundColor backgroundColor	= UFDisp.BackgroundColor.WHITE;
	public	File fileMaster;
	public  String fileExt;
	public  String Dir;
	public 	CreateImage() 
    { 
        //Create and set up the window.
        super((Frame)null, "Snag", false);
        snagPanel = new JPanel(new GridLayout(0,2));
        addWidgets();
        pack();
        setParent(this); 
    } 
	/** Create and add the widgets. */ 
    private static CreateImage theDialog;
    private void addWidgets() 
    { 
        //Create widgets. 
		fileName		= new JTextField(2);
		rdBMP			= new JRadioButton("BMP",true);
		rdJPG			= new JRadioButton("JPEG");
		rdCMPRSD		= new JRadioButton("COMPRESSED TIFF",true);
		rdORIGINAL		= new JRadioButton("ORIGINAL");
		rdWHITE			= new JRadioButton("WHITE",true);
		rdGIF			= new JRadioButton("GIF");
		rdPNG 			= new JRadioButton("PNG",true);
		rdTIFF			= new JRadioButton("TIFF");
		btnBrowse		= new JButton("BROWSE");
		strDefaultFile	=new String("MyImage");
		fileExt	=new String(".bmp");
		//fileMaster = new File(strDefaultFile+fileExt);
		//fileMaster = new File(strDefaultFile+fileExt);
		File dir1 = new File (".");
		try 
		{
		   System.out.println ("Current dir : " + dir1.getCanonicalPath());
		   Dir			=new String(dir1.getCanonicalPath());
		}
		catch(Exception e)
		{
		   e.printStackTrace();
		}
		//JOptionPane.showMessageDialog(null,Dir,"Invalid file name",JOptionPane.INFORMATION_MESSAGE);
		fileName.setText(Dir+"\\"+strDefaultFile+fileExt);
		myButtonGroup	= new ButtonGroup();
		myButtonGroup.add(rdBMP);
		myButtonGroup.add(rdJPG);
		myButtonGroup.add(rdCMPRSD);
		myButtonGroup.add(rdTIFF);
		myButtonGroup.add(rdPNG);
		myButtonGroup.add(rdGIF);
		ButtonGroup colorButtonGroup = new ButtonGroup();
		colorButtonGroup.add(rdWHITE);
		colorButtonGroup.add(rdORIGINAL);
		fileTypeflag=1;
		fileBGflag=6;
		enterFileName          = new JLabel("Enter file name", SwingConstants.LEFT);
		btnCreate       = new JButton("Create");
        btnCancel       = new JButton("Cancel"); 
		rdBMP.addActionListener(this);
		rdJPG.addActionListener(this);
		rdCMPRSD.addActionListener(this);
        rdORIGINAL.addActionListener(this);
		rdWHITE.addActionListener(this);
        rdGIF.addActionListener(this);
		rdPNG.addActionListener(this);
        rdTIFF.addActionListener(this);
		btnBrowse.addActionListener(this);
		
        btnCreate.addActionListener(this);
		btnCancel.addActionListener(this);
		Border border = BorderFactory.createTitledBorder("File Extension");
		snagPanel.setBorder(border);
		snagPanel.add (rdGIF);
        snagPanel.add(rdBMP);
        snagPanel.add(rdPNG);
        snagPanel.add(rdJPG);
        snagPanel.add(rdTIFF);
        snagPanel.add(rdCMPRSD);
		Container contentPane = getContentPane();
		contentPane.add(snagPanel, BorderLayout.EAST);
		snagPanel= new JPanel(new GridLayout(0, 2));
		border = BorderFactory.createTitledBorder("Choose Color");
		snagPanel.setBorder(border);
        snagPanel.add(rdWHITE);
        snagPanel.add(rdORIGINAL);
		contentPane.add(snagPanel, BorderLayout.WEST);
		snagPanel= new JPanel(new GridLayout(0, 3));
		snagPanel.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
		snagPanel.add(enterFileName);
		snagPanel.add(fileName);
		snagPanel.add(btnBrowse);
		snagPanel.add(btnCreate);
		snagPanel.add(btnCancel);
		contentPane.add(snagPanel, BorderLayout.SOUTH);
		
		fileName.addFocusListener(this);

 
    } 
	public void focusGained(FocusEvent event)
	{	
		fileName.setText(Dir+"\\"+strDefaultFile+fileExt);
		return;
	}
	public void checkFileName()
	{
		
		String []strArrChechExt=fileName.getText().split("\\.");
		System.out.println(strDefaultFile);
		System.out.println(fileName.getText());
		System.out.println(strDefaultFile=strArrChechExt[0]);
		if(strArrChechExt.length!=2)
		{
			JOptionPane.showMessageDialog(null,"Re-Enter the file name","Invalid file name",JOptionPane.INFORMATION_MESSAGE);
			fileName.setText(Dir+"\\"+strDefaultFile+fileExt);
			return;
		}
		else 
		{
			strDefaultFile=strArrChechExt[0];
			String []strArrFileName=strDefaultFile.split("\\\\");
			System.out.println(strArrFileName.length);
			if(strArrFileName.length>2)
			{
				System.out.println(strArrFileName[strArrFileName.length-1]);
				strDefaultFile=strArrFileName[strArrFileName.length-1];
			}
			
			if(!(strArrChechExt[1].compareToIgnoreCase("bmp")==0||
			strArrChechExt[1].compareToIgnoreCase("png")==0||
			strArrChechExt[1].compareToIgnoreCase("tif")==0||
			strArrChechExt[1].compareToIgnoreCase("jpg")==0||
			strArrChechExt[1].compareToIgnoreCase("gif")==0))
			{
				JOptionPane.showMessageDialog(null,"Please select any of above mentioned file extention","Invalid file name",JOptionPane.INFORMATION_MESSAGE);
				fileName.setText(Dir+"\\"+strDefaultFile+fileExt);
				return;
			}
			else
			{
				if(!(fileExt.compareToIgnoreCase("."+strArrChechExt[1])==0))
				{
					ButtonModel model=null;
					if(strArrChechExt[1].compareToIgnoreCase("gif")==0)
						model = rdGIF.getModel(); 
					if(strArrChechExt[1].compareToIgnoreCase("bmp")==0)
						model = rdBMP.getModel();  
					if(strArrChechExt[1].compareToIgnoreCase("jpg")==0)
						model = rdJPG.getModel();
					if(strArrChechExt[1].compareToIgnoreCase("tif")==0)
						model = rdTIFF.getModel(); 
					if(strArrChechExt[1].compareToIgnoreCase("png")==0)
						model = rdPNG.getModel();
					JOptionPane.showMessageDialog(null,strArrChechExt[1],"Invalid file name",JOptionPane.INFORMATION_MESSAGE);
					myButtonGroup.setSelected(model,true);
				}
			}
		}
	}
	public void focusLost(FocusEvent event)
	{	
		
		checkFileName();
		return;
	}
	public void actionPerformed(ActionEvent event) 
    { 
		try
		{
			
			if(event.getActionCommand().equals("GIF" ) )
			{
				imageFormat= UFDisp.ImageFormat.GIF;
				fileExt=".gif";
				
      		}
			if(event.getActionCommand().equals("BMP" ) )
			{
				imageFormat= UFDisp.ImageFormat.BMP;
				fileExt=".bmp";
      		}
			if(event.getActionCommand().equals("PNG" ) )
			{
				imageFormat= UFDisp.ImageFormat.PNG;
				fileExt=".png";
      		}
			if(event.getActionCommand().equals("JPEG" ) )
			{
				imageFormat= UFDisp.ImageFormat.JPEG;
				fileExt=".jpg";
      		}
			if(event.getActionCommand().equals("TIFF" ) )
			{
				imageFormat= UFDisp.ImageFormat.TIFF;
				fileExt=".tif";
      		}
			if(event.getActionCommand().equals("COMPRESSED TIFF" ) )
			{
				imageFormat= UFDisp.ImageFormat.COMPRESSED_TIFF;
				fileExt=".tif";
      		}
			if(event.getActionCommand().equals("WHITE" ) )
			{
				backgroundColor= UFDisp.BackgroundColor.WHITE;
      		}
			if(event.getActionCommand().equals("BROWSE" ) )
			{
				JFileChooser c = new JFileChooser();
				c.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES);
				int rVal = c.showOpenDialog(this);
	  			if (rVal == JFileChooser.APPROVE_OPTION) 
	  			{
					if(strDefaultFile.trim().compareTo("")!=0)
					{
						String [] tempStrArray= c.getSelectedFile().getName().split("\\.");
						if(tempStrArray.length==2)
						{
							strDefaultFile=tempStrArray[0];
							fileExt="."+tempStrArray[1];
							Dir=c.getCurrentDirectory().toString().trim();
						}						
					}
					else
					{
						Dir=fileMaster.getPath().trim();
						strDefaultFile="MyImage";
					}
					
					checkFileName();
	  			}
			fileName.setText(Dir+"\\"+strDefaultFile+fileExt);
			}
			if(event.getActionCommand().equals("ORIGINAL" ) )
			{
				backgroundColor= UFDisp.BackgroundColor.ORIGINAL;
      		}
			if(event.getActionCommand().equals("Cancel" ) )
			{	
				int exit = JOptionPane.showConfirmDialog(this, "Do you want to quit?","Cancal Operation",JOptionPane.YES_NO_OPTION );
				if (exit == JOptionPane.YES_OPTION) 
				{
					cancelDialog();
					setVisible(false);
					dispose();
				}
			}
			else if(event.getActionCommand().equals("Create" ) )
			{
				sngGUI();
			}
			fileName.setText(Dir+"\\"+strDefaultFile+fileExt);
		}
		catch(Exception ex)
		{
			System.out.println("Failed");
		}
        return;
    } 
    public void sngGUI() throws Exception
    {
       try
        {
            theSession      = (Session)SessionFactory.get("Session");
            theUFSession  = (UFSession)SessionFactory.get("UFSession");
            theUFSession.ui().openListingWindow();
            theUFSession.ui().writeListingWindow("Session and UFSession are created");
			if(!(fileName.getText().equals("")))
			{
				//strDefaultFile=fileName.getText();
				fileMaster = new File(strDefaultFile+fileExt);
				if(fileMaster.exists())
				{
					int exit = JOptionPane.showConfirmDialog(this, "File already exists.Do you want to replace it","File Exists",JOptionPane.YES_NO_OPTION );
					if (exit == JOptionPane.YES_OPTION) 
					{
						fileMaster.delete();
					}
					else
					{
						return;
					}
				}
				checkFileName();
				
				theUFSession.disp().createImage(strDefaultFile,imageFormat,backgroundColor);
				theUFSession.ui().writeListingWindow("\nFile "+fileMaster.getAbsolutePath()+ " created successfully ");
				int exit = JOptionPane.showConfirmDialog(this, "Image is Created.Do you want to quit now?","Cancal Operation",JOptionPane.YES_NO_OPTION );
				if (exit == JOptionPane.YES_OPTION) 
				{
					cancelDialog();
					setVisible(false);
					dispose();
				}
			}
        }
        catch (Exception ex)
        {
			StringWriter s = new StringWriter();
			PrintWriter p = new PrintWriter(s);
			p.println("Caught exception " + ex );
			ex.printStackTrace(p);
			theUFSession.ui().writeListingWindow("\nFailed");
			theUFSession.ui().writeListingWindow("\n"+s.getBuffer().toString());
        } 
    }
    /**  Create the GUI and show it. For thread safety, * this method should be invoked from the * event-dispatching thread. */ 
    public void valueChanged(ListSelectionEvent e)  {}
    private void deselect(int object) {}
    private void cancelDialog() {}
    private void setParent(Component comp) {}
    public void run() 
    { 
        createAndShowGUI(); 
    } 
    private static void createAndShowGUI() 
    { 
		CreateImage converter = new CreateImage(); 
    } 
    public static void showDialog()  
    {
        theDialog = new CreateImage();
        theDialog.setVisible(true);
	}
    public static void main(String[] args) 
    { 
    	showDialog();
    } 
    public static int getUnloadOption() 
	{ 
        return BaseSession.LibraryUnloadOption.IMMEDIATELY; 
    }
	protected void processWindowEvent(WindowEvent e) 
	{
        if (e.getID() == WindowEvent.WINDOW_CLOSING) 
		{
            int exit = JOptionPane.showConfirmDialog(this, "Do you want to continue?","CONTINUE?",JOptionPane.YES_NO_OPTION );
            if (exit == JOptionPane.YES_OPTION) 
			{
				cancelDialog();
				setVisible(false);
				dispose();
            }
        } 
		else 
		{
		    super.processWindowEvent(e);
        }
    }
}
