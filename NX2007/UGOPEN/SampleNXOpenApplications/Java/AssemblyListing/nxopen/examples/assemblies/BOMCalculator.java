/*
 * Created on Mar 2, 2005
 * 
 * Copyright 2005 UGS Corp. All Rights Reserved.
 * 
 */
package nxopen.examples.assemblies;

import java.rmi.RemoteException;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

import nxopen.NXException;
import nxopen.assemblies.Component;

/**
 * @author pesumner
 * An implementation of IComponentFunctor that creates a BOM for the assembly
 */
public class BOMCalculator implements IComponentFunctor {

    private Map bomMap;
    
    public BOMCalculator() {
        bomMap = new HashMap();
    }
    
    public void execute(Component c) {
        try {
            String name = c.name();
            int count = 0;
            if (bomMap.containsKey(name)) {
                BOMPair bomEntry = (BOMPair) bomMap.get(name);
                bomEntry.incrementCount();
            }
            else {
                count = 1;
                BOMPair bomEntry = new BOMPair(c, count);
                bomMap.put(name, bomEntry);
            }
        } catch (NXException nxEx) {
            nxEx.printStackTrace();
        } catch (RemoteException ex) {
            ex.printStackTrace();
        }
    }

    public Collection getBOMTable() {
        return bomMap.values();
    }
}
