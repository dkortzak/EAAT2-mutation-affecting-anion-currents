import sys
import struct
import numpy as np
import PULimport
import PGFimport
import DATimport

#from PyQt4 import QtGui
#from PyQt4.QtCore import SIGNAL, SLOT
#from HEKATree import Ui_Dialog as Dlg

import matplotlib
import matplotlib.gridspec as gridspec
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import scalebars as sb

def loadPatchmasterFile(filename):
        
        if filename is "":
            return      
                
        patchmaster_file = open(filename, 'rb')
        patchmaster_data = patchmaster_file.read()      
        if "DAT2" not in str(struct.unpack("8s", patchmaster_data[0:8])[0]):
            print("Sorry, but this does not appear to be a properly bundled HEKA Patchmaster file.")
            quit()
        number_of_items = struct.unpack('i', patchmaster_data[48:52])[0]
        start_dict = {}
        stop_dict = {}
        for i in np.arange(0, number_of_items):
            data_type = b"".join(struct.unpack("4c", patchmaster_data[72+(i*16):76+(i*16)]))
            start_dict[data_type] = int(struct.unpack("i", patchmaster_data[64+(i*16):68+(i*16)])[0])
            stop_dict[data_type] = int(struct.unpack("i", patchmaster_data[68+(i*16):72+(i*16)])[0])   
        
        pulfile = PULimport.PULfile(patchmaster_data, int(start_dict[b".pul"]))
        pgffile = PGFimport.PGFfile(patchmaster_data, int(start_dict[b".pgf"]))
        #model = QtGui.QStandardItemModel()
        #model.setHorizontalHeaderLabels([filename])
        #treeView.setUniformRowHeights(True)
        #treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # The TreeView should not be editable

        #for group in pulfile.Groups:
        #    #parent_group = QtGui.QStandardItem(group.Label.decode())
        #    parent_group.setSelectable(False)
        #    for series in group.Series:
        #        parent_group.appendRow(QtGui.QStandardItem(series.Label.decode()))
        #    model.appendRow(parent_group)

        selected_group=0
	tmp=[]
	for i in range(0,len(pulfile.Groups[selected_group].Series)):
	   
            for sweep in pulfile.Groups[selected_group].Series[i].Sweeps:
                tr_plot = 0 # Cm Trace
                ########
                print sweep.Traces[tr_plot].RsValue
                trace_data = DATimport.DATload(patchmaster_data, sweep.Traces[tr_plot].Data, sweep.Traces[tr_plot].DataPoints, sweep.Traces[tr_plot].DataFormat, (sweep.Traces[tr_plot].DataScaler*10**12), False)    
		tmp.append(trace_data)
	return tmp
                
def loadPatchmasterFile2(filename):
        
        if filename is "":
            return      
                
        patchmaster_file = open(filename, 'rb')
        patchmaster_data = patchmaster_file.read()      
        if "DAT2" not in str(struct.unpack("8s", patchmaster_data[0:8])[0]):
            print("Sorry, but this does not appear to be a properly bundled HEKA Patchmaster file.")
            quit()
        number_of_items = struct.unpack('i', patchmaster_data[48:52])[0]
        start_dict = {}
        stop_dict = {}
        for i in np.arange(0, number_of_items):
            data_type = b"".join(struct.unpack("4c", patchmaster_data[72+(i*16):76+(i*16)]))
            start_dict[data_type] = int(struct.unpack("i", patchmaster_data[64+(i*16):68+(i*16)])[0])
            stop_dict[data_type] = int(struct.unpack("i", patchmaster_data[68+(i*16):72+(i*16)])[0])   
        
        pulfile = PULimport.PULfile(patchmaster_data, int(start_dict[b".pul"]))
        pgffile = PGFimport.PGFfile(patchmaster_data, int(start_dict[b".pgf"]))
        #model = QtGui.QStandardItemModel()
        #model.setHorizontalHeaderLabels([filename])
        #treeView.setUniformRowHeights(True)
        #treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # The TreeView should not be editable

        #for group in pulfile.Groups:
            #parent_group = QtGui.QStandardItem(group.Label.decode())
            #parent_group.setSelectable(False)
            #for series in group.Series:
                #parent_group.appendRow(QtGui.QStandardItem(series.Label.decode()))
            #model.appendRow(parent_group)

        selected_group=0
	tmp=[]
	for i in range(0,len(pulfile.Groups[selected_group].Series)):
	    tmp.append([])
	    
            for sweep in pulfile.Groups[selected_group].Series[i].Sweeps:
                tr_plot = 0 # Cm Trace
                ########
                
                trace_data = DATimport.DATload(patchmaster_data, sweep.Traces[tr_plot].Data, sweep.Traces[tr_plot].DataPoints, sweep.Traces[tr_plot].DataFormat, (sweep.Traces[tr_plot].DataScaler*10**12), False)    
		tmp[i].append(trace_data)
	return tmp               

def loadPatchmasterFile_LockInCtrace(filename):
        
        if filename is "":
            return      
                
        patchmaster_file = open(filename, 'rb')
        patchmaster_data = patchmaster_file.read()      
        if "DAT2" not in str(struct.unpack("8s", patchmaster_data[0:8])[0]):
            print("Sorry, but this does not appear to be a properly bundled HEKA Patchmaster file.")
            quit()
        number_of_items = struct.unpack('i', patchmaster_data[48:52])[0]
        start_dict = {}
        stop_dict = {}
        for i in np.arange(0, number_of_items):
            data_type = b"".join(struct.unpack("4c", patchmaster_data[72+(i*16):76+(i*16)]))
            start_dict[data_type] = int(struct.unpack("i", patchmaster_data[64+(i*16):68+(i*16)])[0])
            stop_dict[data_type] = int(struct.unpack("i", patchmaster_data[68+(i*16):72+(i*16)])[0])   
        
        pulfile = PULimport.PULfile(patchmaster_data, int(start_dict[b".pul"]))
        pgffile = PGFimport.PGFfile(patchmaster_data, int(start_dict[b".pgf"]))
        #model = QtGui.QStandardItemModel()
        #model.setHorizontalHeaderLabels([filename])
        #treeView.setUniformRowHeights(True)
        #treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # The TreeView should not be editable

        #for group in pulfile.Groups:
        #    parent_group = QtGui.QStandardItem(group.Label.decode())
        #    parent_group.setSelectable(False)
        #    for series in group.Series:
        #        parent_group.appendRow(QtGui.QStandardItem(series.Label.decode()))
        #    model.appendRow(parent_group)

        selected_group=0
	tmp=[]
	for i in range(0,len(pulfile.Groups[selected_group].Series)):
	    tmp.append([])
	    
            for sweep in pulfile.Groups[selected_group].Series[i].Sweeps:
                tr_plot = 0 # Cm Trace
                ########
                
                trace_data = DATimport.DATload(patchmaster_data, sweep.Traces[tr_plot].Data, sweep.Traces[tr_plot].DataPoints, sweep.Traces[tr_plot].DataFormat, (sweep.Traces[tr_plot].DataScaler*10**12), False)    
		tmp[i].append(trace_data)
	return tmp               


def loadPatchmasterFile_Rs(filename):
        
        if filename is "":
            return      
                
        patchmaster_file = open(filename, 'rb')
        patchmaster_data = patchmaster_file.read()      
        if "DAT2" not in str(struct.unpack("8s", patchmaster_data[0:8])[0]):
            print("Sorry, but this does not appear to be a properly bundled HEKA Patchmaster file.")
            quit()
        number_of_items = struct.unpack('i', patchmaster_data[48:52])[0]
        start_dict = {}
        stop_dict = {}
        for i in np.arange(0, number_of_items):
            data_type = b"".join(struct.unpack("4c", patchmaster_data[72+(i*16):76+(i*16)]))
            start_dict[data_type] = int(struct.unpack("i", patchmaster_data[64+(i*16):68+(i*16)])[0])
            stop_dict[data_type] = int(struct.unpack("i", patchmaster_data[68+(i*16):72+(i*16)])[0])   
        
        pulfile = PULimport.PULfile(patchmaster_data, int(start_dict[b".pul"]))
        pgffile = PGFimport.PGFfile(patchmaster_data, int(start_dict[b".pgf"]))
        #model = QtGui.QStandardItemModel()
        #model.setHorizontalHeaderLabels([filename])
        #treeView.setUniformRowHeights(True)
        #treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # The TreeView should not be editable

        #for group in pulfile.Groups:
        #    parent_group = QtGui.QStandardItem(group.Label.decode())
        #    parent_group.setSelectable(False)
        #    for series in group.Series:
        #        parent_group.appendRow(QtGui.QStandardItem(series.Label.decode()))
        #    model.appendRow(parent_group)

        selected_group=0
	tmp=[]
	for i in range(0,len(pulfile.Groups[selected_group].Series)):
	    tmp.append([])
	   
            for sweep in pulfile.Groups[selected_group].Series[i].Sweeps:
                tr_plot = 0 # Cm Trace
                ########
                trace_data=sweep.Traces[tr_plot].RsValue
                
		tmp[i].append(trace_data)
	return tmp
      
def loadPatchmasterFile_Time(filename):
        
        if filename is "":
            return      
                
        patchmaster_file = open(filename, 'rb')
        patchmaster_data = patchmaster_file.read()      
        if "DAT2" not in str(struct.unpack("8s", patchmaster_data[0:8])[0]):
            print("Sorry, but this does not appear to be a properly bundled HEKA Patchmaster file.")
            quit()
        number_of_items = struct.unpack('i', patchmaster_data[48:52])[0]
        start_dict = {}
        stop_dict = {}
        for i in np.arange(0, number_of_items):
            data_type = b"".join(struct.unpack("4c", patchmaster_data[72+(i*16):76+(i*16)]))
            start_dict[data_type] = int(struct.unpack("i", patchmaster_data[64+(i*16):68+(i*16)])[0])
            stop_dict[data_type] = int(struct.unpack("i", patchmaster_data[68+(i*16):72+(i*16)])[0])   
        
        pulfile = PULimport.PULfile(patchmaster_data, int(start_dict[b".pul"]))
        pgffile = PGFimport.PGFfile(patchmaster_data, int(start_dict[b".pgf"]))
        #model = QtGui.QStandardItemModel()
        #model.setHorizontalHeaderLabels([filename])
        #treeView.setUniformRowHeights(True)
        #treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # The TreeView should not be editable

        #for group in pulfile.Groups:
        #    parent_group = QtGui.QStandardItem(group.Label.decode())
        #    parent_group.setSelectable(False)
        #    for series in group.Series:
        #        parent_group.appendRow(QtGui.QStandardItem(series.Label.decode()))
        #    model.appendRow(parent_group)

        selected_group=0
	tmp=[]
	for i in range(0,len(pulfile.Groups[selected_group].Series)):
	    tmp.append([])
	   
            for sweep in pulfile.Groups[selected_group].Series[i].Sweeps:
                tr_plot = 0 # Cm Trace
                ########
                trace_data=sweep.Timer
                
		tmp[i].append(trace_data)
	return tmp   
      
def loadPatchmasterFile_CS(filename):
        
        if filename is "":
            return      
                
        patchmaster_file = open(filename, 'rb')
        patchmaster_data = patchmaster_file.read()      
        if "DAT2" not in str(struct.unpack("8s", patchmaster_data[0:8])[0]):
            print("Sorry, but this does not appear to be a properly bundled HEKA Patchmaster file.")
            quit()
        number_of_items = struct.unpack('i', patchmaster_data[48:52])[0]
        start_dict = {}
        stop_dict = {}
        for i in np.arange(0, number_of_items):
            data_type = b"".join(struct.unpack("4c", patchmaster_data[72+(i*16):76+(i*16)]))
            start_dict[data_type] = int(struct.unpack("i", patchmaster_data[64+(i*16):68+(i*16)])[0])
            stop_dict[data_type] = int(struct.unpack("i", patchmaster_data[68+(i*16):72+(i*16)])[0])   
        
        pulfile = PULimport.PULfile(patchmaster_data, int(start_dict[b".pul"]))
        pgffile = PGFimport.PGFfile(patchmaster_data, int(start_dict[b".pgf"]))
        #model = QtGui.QStandardItemModel()
        #model.setHorizontalHeaderLabels([filename])
        #treeView.setUniformRowHeights(True)
        #treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # The TreeView should not be editable

        #for group in pulfile.Groups:
        #    parent_group = QtGui.QStandardItem(group.Label.decode())
        #    parent_group.setSelectable(False)
        #    for series in group.Series:
        #        parent_group.appendRow(QtGui.QStandardItem(series.Label.decode()))
        #    model.appendRow(parent_group)

        selected_group=0
	tmp=[]
	for i in range(0,len(pulfile.Groups[selected_group].Series)):
	    tmp.append([])
	   
            for sweep in pulfile.Groups[selected_group].Series[i].Sweeps:
                tr_plot = 0 # Cm Trace
                ########
                trace_data=sweep.Traces[tr_plot].CSlow
                
		tmp[i].append(trace_data)
	return tmp
      
def loadPatchmasterFile_intervalls(filename):
        
        if filename is "":
            return      
                
        patchmaster_file = open(filename, 'rb')
        patchmaster_data = patchmaster_file.read()      
        if "DAT2" not in str(struct.unpack("8s", patchmaster_data[0:8])[0]):
            print("Sorry, but this does not appear to be a properly bundled HEKA Patchmaster file.")
            quit()
        number_of_items = struct.unpack('i', patchmaster_data[48:52])[0]
        start_dict = {}
        stop_dict = {}
        for i in np.arange(0, number_of_items):
            data_type = b"".join(struct.unpack("4c", patchmaster_data[72+(i*16):76+(i*16)]))
            start_dict[data_type] = int(struct.unpack("i", patchmaster_data[64+(i*16):68+(i*16)])[0])
            stop_dict[data_type] = int(struct.unpack("i", patchmaster_data[68+(i*16):72+(i*16)])[0])   
        
        pulfile = PULimport.PULfile(patchmaster_data, int(start_dict[b".pul"]))
        pgffile = PGFimport.PGFfile(patchmaster_data, int(start_dict[b".pgf"]))
        #model = QtGui.QStandardItemModel()
        #model.setHorizontalHeaderLabels([filename])
        #treeView.setUniformRowHeights(True)
        #treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # The TreeView should not be editable

        #for group in pulfile.Groups:
        #    parent_group = QtGui.QStandardItem(group.Label.decode())
        ##    parent_group.setSelectable(False)
        #    for series in group.Series:
        #        parent_group.appendRow(QtGui.QStandardItem(series.Label.decode()))
        #    model.appendRow(parent_group)

        selected_group=0
	tmp=[]
	for i in range(0,len(pulfile.Groups[selected_group].Series)):
	    tmp.append(pgffile.StimulationRecords.SweepInterval)
	   
            #for sweep in pulfile.Groups[selected_group].Series[i].Sweeps:
            #    tr_plot = 0 # Cm Trace
            #    ########
            #    trace_data=sweep.Traces[tr_plot].CSlow
            #    
		#tmp[i].append(trace_data)
	return tmp