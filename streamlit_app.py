import streamlit as st
import subprocess
import importlib

# Nom du module à installer
module_name = 'langchain'

# Installer le module en utilisant pip
subprocess.check_call(['pip', 'install', module_name])

# Importer le module après l'installation
try:
    module = importlib.import_module(module_name)
    # Utiliser le module ici
    print(f"Le module {module_name} a été installé avec succès.")
except ImportError:
    print(f"Erreur : Impossible d'importer le module {module_name}. Assurez-vous que le module est correctement installé.")

st.title('🎈 App Name')

st.write('Hello world!')
