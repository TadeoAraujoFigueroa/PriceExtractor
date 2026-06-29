import pdfplumber 
import pandas as pd 
import re 
import sys 
from pathlib import Path
from ...core.extractor_base import BaseExtractor

class AlpinaExtractor(BaseExtractor):
    
    NAME = "ALPINA";

    KEYWORDS = ["ALPINA", "Lista de Precios"];
    