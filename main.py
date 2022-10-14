import pandas as pd
import os
import numpy as np
import shutil


def validate(path):
    return os.path.exists(path)

def leer_xlsx():
    name_base="Saarbruecken"    
    df = pd.read_excel(name_base + '_metadata.xlsx', sheet_name=name_base)
    dict_info_signal = {}
    pathology=[]
    for ind, row in df.iterrows():        
        p= "PATH" if df['PATHOLOGY'][ind]=='p' else "NORM"
        g= "hombres" if df['GENDER'][ind]=='m' else "mujeres"
        path=  "data/audio/"+str(name_base)+"/"+p+"/"+g+"/"+str(row[0])            
        patho= row[13]
        spk= row[0]
        dict_info_signal[row[0]] = {'spk': row[0], 'Path': path, 'age': row[5], 'gender': row[4], 'tipo': row[7], 'pathology': row[13], 'group': row[14]}
        
        if not patho in pathology:          
            camino ="data/pathology"
            pathology.append(patho)
            if not os.path.exists(camino+'/'+patho):                                    
                os.makedirs(camino+'/'+patho)
                
        if validate(path+"-a_h.wav"):
            shutil.copy(path+"-a_h.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-a_h.wav")
        if validate(path+"-a_l.wav"):
            shutil.copy(path+"-a_l.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-a_l.wav")
        if validate(path+"-a_lhl.wav"):
            shutil.copy(path+"-a_lhl.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-a_lhl.wav")
        if validate(path+"-a_n.wav"):
            shutil.copy(path+"-a_n.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-a_n.wav")
        if validate(path+"-i_h.wav"):
            shutil.copy(path+"-i_h.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-i_h.wav")
        if validate(path+"-i_l.wav"):
            shutil.copy(path+"-i_l.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-i_l.wav")            
        if validate(path+"-i_lhl.wav"):
            shutil.copy(path+"-i_lhl.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-i_lhl.wav")
        if validate(path+"-i_n.wav"):
            shutil.copy(path+"-i_n.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-i_n.wav")
        if validate(path+"-u_h.wav"):
            shutil.copy(path+"-u_h.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-u_h.wav")
        if validate(path+"-u_l.wav"):
            shutil.copy(path+"-u_l.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-u_l.wav")            
        if validate(path+"-u_lhl.wav"):
            shutil.copy(path+"-u_lhl.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-u_lhl.wav")
        if validate(path+"-u_n.wav"):
            shutil.copy(path+"-u_n.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-u_n.wav")
        if validate(path+"-phrase.wav"):
            shutil.copy(path+"-phrase.wav", camino+'/'+patho+"/"+p+"_"+g+"_"+str(spk)+"-phrase.wav")


    return dict_info_signal


leer_xlsx()