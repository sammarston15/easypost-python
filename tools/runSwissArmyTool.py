""" This file will do the necessary terminal commands
    to run the swiss army knife tool.
"""
import os

def main():
    os.chdir('/Users/smarston/Documents/dev/support_tools/swiss_army_knife')
    os.system("pipenv run streamlit run app.py")

if __name__ == "__main__":
    main()
