import os
import json

def load_signature(path):
     with open(path) as f:
          return json.load(f)