# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:27:13 2021

@author: juan.ramirezp
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:43:41 2021

@author: juan.ramirezp
"""
import pathlib
from PIL import Image
from PIL import UnidentifiedImageError
for path in pathlib.Path(r"C:\Users\juan.ramirezp\Documents\imaterialist-furniture-2018\tmp\train").iterdir():
    if path.is_file():
        try:
            x=Image.open(path)
            try:
                x=x.convert("RGB")
            except OSError as e:
                print("conversion error")
                print(path)
                print(e)
                x.close()
                path.unlink()
        except UnidentifiedImageError as e2:
            print("unidentified")
            print(e2)
            print(path)
            path.unlink()
        except OSError as e:
            print("truncd")
            print(path)
            print(e)
            path.unlink()
        x.close()

