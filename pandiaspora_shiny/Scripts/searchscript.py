import os
import re
import time
import csv 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import glob


options = Options();
prefs = {"download.default_directory" : os.path.abspath("pandiaspora_shiny\Rawdata")};
#example: prefs = {"download.default_directory" : "C:\Tutorial\down"};
options.add_experimental_option("prefs",prefs);


def getXPATH(boolean):
    if boolean == 'AND': return "/html/body/main/form/div/div/div[6]/div[3]/div/ul/li[1]"
    if boolean == 'OR': return "/html/body/main/form/div/div/div[6]/div[3]/div/ul/li[2]"
    if boolean == 'NOT': return "/html/body/main/form/div/div/div[6]/div[3]/div/ul/li[3]"
def wait_for_downloads(download_directory):
    while any(file.endswith(".crdownload") for file in os.listdir(download_directory)):
        time.sleep(1)
def createrepository(queries, booleans):
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=options);
    driver.get("https://pubmed.ncbi.nlm.nih.gov/advanced/")
    for index, term in enumerate(queries):
        driver.find_element(By.ID, "id_term").send_keys(term)
        try:
            xpath = getXPATH(booleans[index]) 
        except:
            break
        driver.find_element(By.XPATH,  '/html/body/main/form/div/div/div[6]/div[3]/div/button').click()
        time.sleep(1)
        errorcatch = False
        while errorcatch == False:
            try:   
                driver.find_element(By.XPATH,  '/html/body/main/form/div/div/div[6]/div[3]/div/button').click()
                driver.find_element(By.XPATH, xpath).click()
                errorcatch = True
            except:
                errorcatch = False
        
        
    #Search
    driver.find_element(By.CLASS_NAME, "search-btn").click()
    #Open Save Panel
    driver.find_element(By.ID, "save-results-panel-trigger").click()
    #Wait for save panel
    time.sleep(1)
    #All Results
    driver.find_element(By.CLASS_NAME, 'action-panel-selector').click()
    driver.find_element(By.XPATH, '/html/body/main/div[1]/div/form/div[1]/div[1]/select/option[2]').click()
    #CSV
    driver.find_element(By.XPATH, '/html/body/main/div[1]/div/form/div[2]/select').click()
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/form/div[2]/select/option[5]").click()
    driver.find_element(By.XPATH, '/html/body/main/div[1]/div/form/div[3]/button[1]').click()
    #Open Save Panel
    driver.find_element(By.ID, "save-results-panel-trigger").click()
    #Wait for save panel
    time.sleep(1)
    #Abstract
    driver.find_element(By.XPATH, '/html/body/main/div[1]/div/form/div[2]/select').click()
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/form/div[2]/select/option[4]").click()
    driver.find_element(By.XPATH, '/html/body/main/div[1]/div/form/div[3]/button[1]').click()
    #Open Save Panel
    driver.find_element(By.ID, "save-results-panel-trigger").click()
    #Wait for save panel
    time.sleep(1)
    #Mesh
    driver.find_element(By.XPATH, '/html/body/main/div[1]/div/form/div[2]/select').click()
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/form/div[2]/select/option[2]").click()
    driver.find_element(By.XPATH, '/html/body/main/div[1]/div/form/div[3]/button[1]').click()
    wait_for_downloads(r"pandiaspora_shiny\Rawdata")

def list_to_string(lst):
    if not isinstance(lst, list):
        raise ValueError("Input is not a list")
    
    # Convert each element of the list to a string
    stringified_elements = [repr(element) for element in lst]
    
    # Join the elements with commas and surround them with square brackets
    result = '[' + ', '.join(stringified_elements) + ']'
    return result

def format_abstracts(filename):
    output, current, latest = [], "", ""
    with open(filename, encoding="utf8") as f:
        for line in f:
            if re.match("^\d+[.]\s.*", line.strip()) and re.match("^\s*$", latest):
                output.append(current)
                current = ""
            current = current + line.strip()
            latest = line.strip()
    output.append(current)

    return output[1:]

def format_mesh(filename):
    aux, ouput, current, latest = [], [] , [], ""
    with open(filename, encoding="utf8") as f:
        for line in f:
            if re.match("^PMID.*", line.strip()):
                aux.append(list_to_string(current))
                current = []
            if re.match("^MH.*", line.strip()):
                current.append(line.strip()[6:])
    aux.append(list_to_string(current))

    return aux[1:]

def combine_abs(csvfile, columnname, columndata):
    data_new = pd.read_csv(csvfile)
    data_new[columnname] = columndata
    data_new.to_csv(r'pandiaspora_shiny\Rawdata\abs.csv')             
def combine_mesh(csvfile, columnname, columndata):
    data_new = pd.read_csv(csvfile)
    data_new[columnname] = columndata
    data_new.to_csv(r'pandiaspora_shiny\Rawdata\data_new.csv')     

queries = [
    r'(Human[MeSH Terms] OR human population[MeSH Terms] )', 
    r'("race"[Title/Abstract] OR "ethnic"[All Fields] OR "ethnical"[All Fields] OR "ethnically"[All Fields] OR "ethnicities"[All Fields] OR "ethnics"[All Fields] OR "ethnology"[MeSH Subheading] OR "ethnology"[All Fields] OR "ethnicity"[All Fields] OR "ethnology"[MeSH Terms] OR "ethnicity"[MeSH Terms] OR "racial*"[Title/Abstract] OR "racism"[Title/Abstract] OR "ethnic*"[Title/Abstract] OR "racial inequalities"[Title/Abstract] OR "racial groups"[MeSH Terms] OR "race-based"[Title/Abstract] OR "ethnic based"[All Fields] OR "Ethnic groups"[All Fields] OR "Risk factors"[All Fields] OR "Systemic Racism"[All Fields] OR "Ethnic Origin"[All Fields] OR "Ethnic groups"[All Fields] OR "Racial minorities"[All Fields] OR "Black"[All Fields] OR "Afro-descendant"[All Fields] OR "afro*"[All Fields] OR "afric*"[All Fields])',
    r'("ineq*"[All Fields] OR "dispar*"[All Fields] OR ("healthcare disparities"[MeSH Terms] OR "health status disparities"[MeSH Terms] OR (("disparate"[All Fields] OR "disparately"[All Fields] OR "disparities"[All Fields] OR "disparity"[All Fields]) AND "health status"[MeSH Terms]) OR "healthcare disparities"[MeSH Terms]))',
    r'Latin America [mesh] OR Belize OR Costa Rica OR Cuba OR Dominican Republic OR El Salvador OR Guatemala OR Haiti OR Honduras OR Mexico OR Nicaragua, Panama, Saint Lucia OR Argentina OR Bolivia OR Brazil OR Chile OR Colombia OR Ecuador OR Paraguay OR Peru OR Uruguay OR Venezuela',
    r'(y_10[Filter])'
    ]
booleans = ['AND', 'AND', 'AND', 'AND']
files = glob.glob(r'pandiaspora_shiny\Rawdata\*')
for f in files:
    os.remove(f)

files = glob.glob(r'pandiaspora_shiny\Data\*')
for f in files:
    os.remove(f)

errorcatch = False
while errorcatch == False:
    try:   
        createrepository(queries, booleans)
        errorcatch = True
    except:
        errorcatch = False
inp = r"pandiaspora_shiny\Rawdata\abstract-HumanMeSHT-set.txt"
abstract = format_abstracts(inp)
combine_abs(r"pandiaspora_shiny\Rawdata\csv-HumanMeSHT-set.csv", "Abstracts", abstract)
meshterms = format_mesh(r"pandiaspora_shiny\Rawdata\pubmed-HumanMeSHT-set.txt")
combine_mesh(r"pandiaspora_shiny\Rawdata\abs.csv", "Mesh Terms", meshterms)
    
import barByCountry 
import barByYear
import barByMesh
import lineByCountry

