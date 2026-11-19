//
//      Copyright (c) 2005 UGS Corp.
//         All rights reserved
//          Written by V.A.L.
//
//====================================================================================================
//
//====================================================================================================
//
package nxexamples.createnote;

import java.awt.Component;
import java.awt.Container;
import java.awt.Frame;
import java.beans.PropertyChangeEvent;
import java.text.NumberFormat;

import javax.swing.*;
import javax.swing.filechooser.*;

import nxopen.*;
import nxopen.annotations.*;
import nxopen.uf.UFConstants;

/*
 *  A dialog for the user to input data for creating a note
 *  either by copying an existing note or from a user defined symbol
 */
public class UserSymbolDialog extends JDialog
{
    public UserSymbolDialog(Session session, UI ui) 
    {
        super((java.awt.Frame)null, true /* modal */);
        initialize();
        m_session = session;
        m_ui = ui;
    }
    
    /**
     * Show the modal dialog.
     * @return Indicates whether the user pressed the 'Create' button or cancelled the dialog.
     *         The return value is either JOptionPane.OK_OPTION or JOption.CANCEL_OPTION.
     */
    public int showDialog()
    {
        setVisible(true);
        return m_status;
    }
    
    /**
     * Disposes the dialog
     */
    public void doDispose()
    {
        Container parent = this.getParent();
        if ( parent instanceof Frame )
            ((Frame)parent).dispose();
        dispose();
    }

    public static class NoteCreationData
    {
        LetteringPreferences letteringPrefs;
        UserSymbolPreferences userSymPrefs;
        String [] noteText;
    }
    
    /**
     * Returns the data for note creation selected on the dialog.
     * This function should only be called after this dialog has been
     * shown to the user and only if the user did not cancel the dialog.
     * @return  The note creation data
     * @throws Exception
     */
    public NoteCreationData getNoteCreationData() throws Exception
    {
        if ( m_status != JOptionPane.OK_OPTION )
            throw new Exception("Illegal to call getNoteCreationData if the dialog was canceled");
        if ( this.m_copyExistingRadioButton.isSelected() )
        {
            // User selected Copy Existing Note
            
            // Prompt user to select a note to copy
            final Selection.MaskTriple [] mask = new Selection.MaskTriple[] {
                    new Selection.MaskTriple(
                    UFConstants.UF_drafting_entity_type, 
                    UFConstants.UF_draft_note_subtype, 0),
                    new Selection.MaskTriple(
                    UFConstants.UF_drafting_entity_type,
                    UFConstants.UF_draft_label_subtype, 0)
            };
            Selection.SelectTaggedObjectData selection = 
                m_ui.selectionManager().selectTaggedObject("Select note to clone", "Select note to clone", Selection.SelectionScope.WORK_PART,
                    Selection.SelectionAction.CLEAR_AND_ENABLE_SPECIFIC, false, false, mask);
            if ( selection.object == null ) return null;
            
            // Send back the note's data
            NoteBase note = (NoteBase)selection.object;
            NoteCreationData result = new NoteCreationData();
            result.letteringPrefs = note.getLetteringPreferences();
            result.userSymPrefs = note.getUserSymbolPreferences();
            result.noteText = note.getText();
            return result;
        }
        else
        {
            // User selected Create From User Defined Symbol
            Part workPart = m_session.parts().work();
            String selectedSymbol = (String)this.m_symbolCombobox.getSelectedItem();
            // The symbol font must be loaded before it can be used
            workPart.annotations().loadSymbolFontFromSbfFile(selectedSymbol);
            NoteCreationData result = new NoteCreationData();
            result.letteringPrefs = null;
            result.userSymPrefs = workPart.annotations().newUserSymbolPreferences(
                    UserSymbolPreferences.SizeType.SCALE_ASPECT_RATIO, 
                    this.m_scaleTextField.value(), this.m_aspectRatioTextField.value());
            result.noteText = new String[] { "<%" + selectedSymbol.trim() + ">" };
            return result;
        }
    }
    
    /**
     * A text field that only accepts floating point numbers greater than 1.0e-5
     */
    static class PositiveDoubleTextField extends JFormattedTextField
    {
        public PositiveDoubleTextField()
        {
            super(getFormat());
            setValue(new Double(1.0));
            addPropertyChangeListener("value", new java.beans.PropertyChangeListener() {
                public void propertyChange(PropertyChangeEvent e) {
                    double newValue = ((Number)e.getNewValue()).doubleValue();
                    if ( newValue < 1.0e-5 )
                    {
                        ((JFormattedTextField)e.getSource()).setValue(e.getOldValue());
                    }
                }
            });
            java.awt.Dimension maxSize = getPreferredSize();
            maxSize.width = Integer.MAX_VALUE;
            setMaximumSize(maxSize);
        }
        
        /**
         * Returns the numeric value in the text field
         */
        public double value()
        {
            return ((Number)this.getValue()).doubleValue();
        }
        
        private static NumberFormat getFormat()
        {
            NumberFormat format = NumberFormat.getNumberInstance();
            format.setMaximumFractionDigits(20);
            return format;           
        }
        
    }

    /**
     * This method initializes m_copyExistingRadioButton 
     *  
     * @return javax.swing.JRadioButton 
     */
    private JRadioButton getCopyExistingRadioButton() {
        if (m_copyExistingRadioButton == null) {
            m_copyExistingRadioButton = new JRadioButton();
            m_copyExistingRadioButton.setText("Copy existing symbol");
            m_copyExistingRadioButton.setSelected(true);
        }
        return m_copyExistingRadioButton;
    }

    /**
     * This method initializes m_createFromUserDefinedRadioButton   
     *  
     * @return javax.swing.JRadioButton 
     */
    private JRadioButton getCreateFromUserDefinedRadioButton() {
        if (m_createFromUserDefinedRadioButton == null) {
            m_createFromUserDefinedRadioButton = new JRadioButton();
            m_createFromUserDefinedRadioButton.setText("Create from user defined symbol");
        }
        return m_createFromUserDefinedRadioButton;
    }
    
    /**
     * This class is called when the user leaves the SbfFileNamePanel.
     * It verifies that the SbfFileName is valid.
     */
    private class SbfFileNamePanelVerifier extends java.awt.event.FocusAdapter
    {
        private UserSymbolDialog f;
        public SbfFileNamePanelVerifier(UserSymbolDialog f) { this.f = f; }
        public void focusLost(java.awt.event.FocusEvent e ) 
        {
            Component opp = e.getOppositeComponent();
            if ( opp != null && 
                    opp != f.m_sbfFileNameTextField && opp != f.m_sbfFileNameBrowse &&
                    opp != f.m_cancelButton )
            {
                if ( verifySbfFileName() == false )
                    f.m_sbfFileNameTextField.grabFocus();
            }
        }
    }

    /**
     * This method initializes m_sbfFilePanel   
     *  
     * @return javax.swing.JPanel   
     */
    private JPanel getSbfFilePanel() {
        if (m_sbfFilePanel == null) {
            m_sbfFilePanel = new JPanel();
            m_sbfFilePanel.setLayout(new BoxLayout(getSbfFilePanel(), BoxLayout.X_AXIS));
            m_sbfFilePanel.setAlignmentX(0.0F);
            m_sbfFilePanel.add(getSbfFileNameTextField(), null);
            m_sbfFilePanel.add(getSbfFileNameBrowse(), null);
            SbfFileNamePanelVerifier verifier = new SbfFileNamePanelVerifier(this);
            getSbfFileNameBrowse().addFocusListener(verifier);
            getSbfFileNameTextField().addFocusListener(verifier);
        }
        return m_sbfFilePanel;
    }
    
    /**
     * This method initializes m_sbfFileNameTextField   
     *  
     * @return javax.swing.JTextField   
     */
    private JTextField getSbfFileNameTextField() {
        if (m_sbfFileNameTextField == null) {
            m_sbfFileNameTextField = new JTextField();
            java.awt.Dimension maxSize = m_sbfFileNameTextField.getPreferredSize();
            maxSize.width = Integer.MAX_VALUE;
            m_sbfFileNameTextField.setMaximumSize(maxSize);
        }
        return m_sbfFileNameTextField;
    }
    
    /**
     * This method initializes m_sbfFileNameBrowse  
     *  
     * @return javax.swing.JButton  
     */
    private JButton getSbfFileNameBrowse() {
        if (m_sbfFileNameBrowse == null) {
            m_sbfFileNameBrowse = new JButton();
            m_sbfFileNameBrowse.setText("Browse");
            m_sbfFileNameBrowse.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent e) {
                    JFileChooser fileDialog = new JFileChooser();
                    fileDialog.setFileFilter( new FileFilter() {
                        public String getDescription() { return "sbf files (*.sbf)"; }
                        public boolean accept(java.io.File f) { return f.isDirectory() || f.getName().endsWith(".sbf"); }
                    });
                    if ( fileDialog.showOpenDialog(null) == JFileChooser.APPROVE_OPTION )
                    {
                        m_sbfFileNameTextField.setText(fileDialog.getSelectedFile().getPath());
                        verifySbfFileName();
                    }
                }
            });
        }
        return m_sbfFileNameBrowse;
    }

    /**
     * This method initializes jPanel   
     *  
     * @return javax.swing.JPanel   
     */
    private JPanel getJPanel() {
        if (jPanel == null) {
            jPanel = new JPanel();
            jPanel.setLayout(new BoxLayout(getJPanel(), BoxLayout.X_AXIS));
            jPanel.setAlignmentX(0.0F);
            jPanel.add(getJPanel1(), null);
            jPanel.add(getJPanel2(), null);
        }
        return jPanel;
    }

    /**
     * This method initializes jPanel1  
     *  
     * @return javax.swing.JPanel   
     */
    private JPanel getJPanel1() {
        if (jPanel1 == null) {
            jLabel1 = new JLabel();
            jLabel1.setText("Select symbol");
            jPanel1 = new JPanel();
            jPanel1.setLayout(new BoxLayout(getJPanel1(), BoxLayout.Y_AXIS));
            jPanel1.add(jLabel1, null);
            jPanel1.add(getSymbolCombobox(), null);
        }
        return jPanel1;
    }

    /**
     * This method initializes jPanel2  
     *  
     * @return javax.swing.JPanel   
     */
    private JPanel getJPanel2() {
        if (jPanel2 == null) {
            jLabel3 = new JLabel();
            jLabel3.setText("Aspect ratio");
            jLabel2 = new JLabel();
            jLabel2.setText("Scale");
            jPanel2 = new JPanel();
            jPanel2.setLayout(new BoxLayout(getJPanel2(), BoxLayout.Y_AXIS));
            jPanel2.add(jLabel2, null);
            jPanel2.add(getScaleTextField(), null);
            jPanel2.add(jLabel3, null);
            jPanel2.add(getAspectRatioTextField(), null);
        }
        return jPanel2;
    }

    /**
     * This method initializes m_symbolCombobox 
     *  
     * @return javax.swing.JComboBox    
     */
    private JComboBox getSymbolCombobox() {
        if (m_symbolCombobox == null) {
            m_symbolCombobox = new JComboBox();
        }
        return m_symbolCombobox;
    }
    
    /**
     * This method initializes m_scaleTextField 
     *  
     * @return javax.swing.JTextField   
     */
    private JTextField getScaleTextField() {
        if (m_scaleTextField == null) {
            m_scaleTextField = new PositiveDoubleTextField();
        }
        return m_scaleTextField;
    }

    /**
     * This method initializes m_aspectRatioTextField   
     *  
     * @return javax.swing.JTextField   
     */
    private JTextField getAspectRatioTextField() {
        if (m_aspectRatioTextField == null) {
            m_aspectRatioTextField = new PositiveDoubleTextField();
        }
        return m_aspectRatioTextField;
    }

    /**
     * This method initializes jPanel3  
     *  
     * @return javax.swing.JPanel   
     */
    private JPanel getJPanel3() {
        if (jPanel3 == null) {
            jPanel3 = new JPanel();
            jPanel3.setAlignmentX(0.0F);
            jPanel3.add(getCreateButton(), null);
            jPanel3.add(getCancelButton(), null);
        }
        return jPanel3;
    }

    /**
     * This method initializes m_createButton   
     *  
     * @return javax.swing.JButton  
     */
    private JButton getCreateButton() {
        if (m_createButton == null) {
            m_createButton = new JButton();
            m_createButton.setText("Create");
            m_createButton.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent e) {
                    m_status = JOptionPane.OK_OPTION;
                    setVisible(false);
                }
            });
        }
        return m_createButton;
    }
    
    /**
     * This method initializes m_cancelButton   
     *  
     * @return javax.swing.JButton  
     */
    private JButton getCancelButton() {
        if (m_cancelButton == null) {
            m_cancelButton = new JButton();
            m_cancelButton.setText("Cancel");
            m_cancelButton.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent e) {
                    m_status = JOptionPane.CANCEL_OPTION;
                    setVisible(false);
                }
            });
        }
        return m_cancelButton;
    }

    /*
     * This method initializes jContentPane
     * 
     * @return javax.swing.JPanel
     */
    private JPanel getJContentPane() {
        if (jContentPane == null) {
            jLabel = new JLabel();
            jLabel.setText("Location of symbol font file");
            jLabel.setBorder(javax.swing.BorderFactory.createEmptyBorder(5,5,5,5));
            jContentPane = new JPanel();
            jContentPane.setLayout(new BoxLayout(getJContentPane(), BoxLayout.Y_AXIS));
            jContentPane.add(getCopyExistingRadioButton(), null);
            jContentPane.add(getCreateFromUserDefinedRadioButton(), null);
            jContentPane.add(jLabel, null);
            jContentPane.add(getSbfFilePanel(), null);
            jContentPane.add(getJPanel(), null);
            jContentPane.add(getJPanel3(), null);
            
            m_copyExistingRadioButton.addItemListener(
                    new java.awt.event.ItemListener() {
                        public void itemStateChanged(java.awt.event.ItemEvent e) {
                            updateAfterCopyExistingRadioButtonChanged();
                        }
                    });
          
            ButtonGroup radioButtons = new ButtonGroup();
            radioButtons.add(this.m_copyExistingRadioButton);
            radioButtons.add(this.m_createFromUserDefinedRadioButton);
        }
        return jContentPane;
    }
    
    /**
     * This method initializes this
     * 
     * @return void
     */
    private void initialize() 
    {
        this.setSize(302, 247);
        this.setTitle("Create note");
        this.setContentPane(getJContentPane());
        this.updateAfterCopyExistingRadioButtonChanged();
    }

    /**
     * Loads the symbol font names from the file named in the sbf file name text box
     * @throws Exception  If the sbf file was not successfully loaded
     */
    private void loadSymbolNames() throws Exception
    {
        java.io.File f = new java.io.File(this.m_sbfFileNameTextField.getText());
        if ( !f.exists() || f.isDirectory() )
            throw new Exception("File not found");
        String [] symbolNames;
        try
        {
            m_session.parts().work().annotations().setCurrentSbfFile(f.getPath());
            symbolNames = m_session.parts().work().annotations().readAllSymbolNamesFromSbfFile();
        }
        catch ( Exception e )
        {
            throw new Exception("Error opening sbf file\n" + e.getMessage());
        }
        if ( symbolNames.length == 0 )
            throw new Exception("No symbols in the sbf file");
        this.m_symbolCombobox.removeAllItems();
        for (int ii = 0; ii < symbolNames.length; ii++) 
            this.m_symbolCombobox.addItem(symbolNames[ii]);
    }
    
    /**
     * Verifies the sbf file name input.  
     * If the file is valid, the symbol names are placed in the symbol name combobox.
     * If the file is not valid, the sbf file name text box is reverted to the name
     * of the last valid sbf file (or NO_VALID_SBF_FILE_MSG if no valid sbf file has
     * ever been entered) and an error message is displayed.
     * @return  true iff the user entered a valid sbf file or NO_VALID_SBF_FILE_MSG
     */
    private boolean verifySbfFileName()
    {
        if ( this.m_sbfFileNameTextField.getText().equals(NO_VALID_SBF_FILE_MSG) )
        {
            this.m_createButton.setEnabled(false);
            return true;
        }
        if ( this.m_sbfFileNameTextField.getText().equals(m_sbfFileName) )
            return true;
        try
        {
            loadSymbolNames();
        }
        catch (Exception e )
        {
            JOptionPane.showMessageDialog(null, e.getMessage()); 
            m_sbfFileNameTextField.setText(m_sbfFileName);            
            return false;
        }
        m_sbfFileName = m_sbfFileNameTextField.getText();
        this.m_createButton.setEnabled(isFormInputValid());
        return true;
    }
    
    /**
     * Called after the "Copy Existing" radio button has changed
     * in order to update the GUI.
     */
    private void updateAfterCopyExistingRadioButtonChanged()
    {
        this.m_createButton.setEnabled(isFormInputValid());
        boolean enable = !m_copyExistingRadioButton.isSelected();
        m_sbfFileNameTextField.setEnabled(enable);
        m_sbfFileNameBrowse.setEnabled(enable);
        m_symbolCombobox.setEnabled(enable);
        m_scaleTextField.setEnabled(enable);
        m_aspectRatioTextField.setEnabled(enable);
        jLabel.setEnabled(enable);
        jLabel1.setEnabled(enable);
        jLabel2.setEnabled(enable);
        jLabel3.setEnabled(enable);
        // The first time that Create From User Defined is selected,
        // try to initialize m_sbfFileNameTextField with $UGII_BASE_DIR/ugii/ug_default.sbf.
        // m_sbfFileNameTextField.getText() will be "" only if this is the first
        // time that Create From User Defined is selected.  Otherwise,
        // m_sbfFileNameTextField.getText() will be either a valid SBF file name or
        // NO_VALID_SBF_FILE_MSG.
        if ( enable && m_sbfFileNameTextField.getText().equals("") )
        {
            String ugii_dir = System.getProperty("UGII_BASE_DIR") + java.io.File.separator + "ugii";
            if ( ugii_dir == null ) { ugii_dir = "."; }
            m_sbfFileNameTextField.setText(
                    ugii_dir + java.io.File.separator + "ug_default.sbf"
                    );
            m_sbfFileName = NO_VALID_SBF_FILE_MSG;
            if ( !verifySbfFileName() )
                m_sbfFileNameTextField.grabFocus();
        }
    }
    
    /**
     * Returns true if all the user's input is valid
     * The "Create" button should be enabled iff this returns true.
     */
    private boolean isFormInputValid()
    {
        // Because this dialog's components do verification to forbid invalid input,
        // very little needs to be done here
        return ( this.m_copyExistingRadioButton.isSelected() ||
                (m_sbfFileName != null && !this.m_sbfFileName.equals("") && !this.m_sbfFileName.equals(NO_VALID_SBF_FILE_MSG) )
            );
    }
    
    private int m_status = JOptionPane.CANCEL_OPTION;
    private Session m_session;
    private UI m_ui;
    private JPanel jContentPane = null;
    private JRadioButton m_copyExistingRadioButton = null;
    private JRadioButton m_createFromUserDefinedRadioButton = null;
    private JLabel jLabel = null;
    private JPanel m_sbfFilePanel = null;
    private JTextField m_sbfFileNameTextField = null;
    private JButton m_sbfFileNameBrowse = null;
    private JPanel jPanel = null;
    private JPanel jPanel1 = null;
    private JPanel jPanel2 = null;
    private JLabel jLabel1 = null;
    private JComboBox m_symbolCombobox = null;
    private PositiveDoubleTextField m_scaleTextField = null;
    private JLabel jLabel2 = null;
    private JLabel jLabel3 = null;
    private PositiveDoubleTextField m_aspectRatioTextField = null;
    private JPanel jPanel3 = null;
    private JButton m_createButton = null;
    private JButton m_cancelButton = null;
    private final String NO_VALID_SBF_FILE_MSG = "(enter sbf file location)";
    private String m_sbfFileName = null;
    
}
