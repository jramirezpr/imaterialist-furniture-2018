# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:43:41 2021

@author: juan.ramirezp
"""
import pathlib

for path in pathlib.Path(r"C:\Users\juan.ramirezp\Documents\imaterialist-furniture-2018\tmp\validation").iterdir():
    if path.is_file():
        old_name = path.stem

        old_extension = path.suffix

        directory = path.parent
        
        removed_suffix = old_name.split("_")[0]

        new_name = removed_suffix + old_extension
        path.rename(pathlib.Path(directory, new_name))
#conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c conda-forge
