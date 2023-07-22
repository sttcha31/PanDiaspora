
import re
import time
import csv 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


options = Options() ;
prefs = {"download.default_directory" : "D:\PanDiaspora\metadata"};
#example: prefs = {"download.default_directory" : "C:\Tutorial\down"};
options.add_experimental_option("prefs",prefs);

def getXPATH(boolean):
    if boolean == 'AND': return "/html/body/main/form/div/div/div[5]/div[3]/div/ul/li[1]/a"
    if boolean == 'OR': return "/html/body/main/form/div/div/div[5]/div[3]/div/ul/li[2]/a"
    if boolean == 'NOT': return "/html/body/main/form/div/div/div[5]/div[3]/div/ul/li[3]/a"

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
        driver.find_element(By.XPATH,  '/html/body/main/form/div/div/div[5]/div[3]/div/button').click()
        driver.find_element(By.XPATH, xpath).click()
        
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
    time.sleep(15)

    #download csv here

    #compine csv with abstaract here
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
            
    return output
def combine_files(csvfile, abstract):
    with open(csvfile, 'r') as read_obj, \
        open('output_1.csv', 'w', newline='') as write_obj:
        csv_reader = csv.reader(read_obj)
        
        
        row0 = next(r)
        row0.append('Abstract')
        for index, article in enumerate(r):
            article.append(abstract[index])
    
                
                
                
    return

queries = [
    r'(Human[MeSH Terms] OR human population[MeSH Terms] )', 
    r'("race"[Title/Abstract] OR "ethnic"[All Fields] OR "ethnical"[All Fields] OR "ethnically"[All Fields] OR "ethnicities"[All Fields] OR "ethnics"[All Fields] OR "ethnology"[MeSH Subheading] OR "ethnology"[All Fields] OR "ethnicity"[All Fields] OR "ethnology"[MeSH Terms] OR "ethnicity"[MeSH Terms] OR "racial*"[Title/Abstract] OR "racism"[Title/Abstract] OR "ethnic*"[Title/Abstract] OR "racial inequalities"[Title/Abstract] OR "racial groups"[MeSH Terms] OR "race-based"[Title/Abstract] OR "ethnic based"[All Fields] OR "Ethnic groups"[All Fields] OR "Risk factors"[All Fields] OR "Systemic Racism"[All Fields] OR "Ethnic Origin"[All Fields] OR "Ethnic groups"[All Fields] OR "Racial minorities"[All Fields] OR "Black"[All Fields] OR "Afro-descendant"[All Fields] OR "afro*"[All Fields] OR "afric*"[All Fields])',
    r'("ineq*"[All Fields] OR "dispar*"[All Fields] OR ("healthcare disparities"[MeSH Terms] OR "health status disparities"[MeSH Terms] OR (("disparate"[All Fields] OR "disparately"[All Fields] OR "disparities"[All Fields] OR "disparity"[All Fields]) AND "health status"[MeSH Terms]) OR "healthcare disparities"[MeSH Terms]))',
    r'Latin America [mesh] OR Belize OR Costa Rica OR Cuba OR Dominican Republic OR El Salvador OR Guatemala OR Haiti OR Honduras OR Mexico OR Nicaragua, Panama, Saint Lucia OR Argentina OR Bolivia OR Brazil OR Chile OR Colombia OR Ecuador OR Paraguay OR Peru OR Uruguay OR Venezuela',
    r'(y_10[Filter])'
    ]
booleans = ['AND', 'AND', 'AND', 'AND']
r"metadata\abstract-HumanMeSHT-set.txt"
# createrepository(queries, booleans)
inp = r"metadata\abstract-HumanMeSHT-set.txt"
abstract = format_abstracts(inp)

combine_files("metadata\csv-HumanMeSHT-set.csv", abstract)



