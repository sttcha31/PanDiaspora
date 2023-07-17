import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def getXPATH(boolean):
    if boolean == 'AND': return "/html/body/main/form/div/div/div[5]/div[3]/div/ul/li[1]/a"
    if boolean == 'OR': return "/html/body/main/form/div/div/div[5]/div[3]/div/ul/li[2]/a"
    if boolean == 'NOT': return "/html/body/main/form/div/div/div[5]/div[3]/div/ul/li[3]/a"

def createrepository(queries, booleans):
    driver = webdriver.Chrome()
    driver.get("https://pubmed.ncbi.nlm.nih.gov/advanced/")
    for index, term in enumerate(queries):
        driver.find_element(By.ID, "id_term").send_keys(term)
        try:
            xpath = getXPATH(booleans[index]) 
        except:
            break
        driver.find_element(By.XPATH,  '/html/body/main/form/div/div/div[5]/div[3]/div/button').click()
        driver.find_element(By.XPATH, xpath).click()
        

    driver.find_element(By.CLASS_NAME, "search-btn").click()
    time.sleep(3)
    
    #download csv here

    #compine csv with abstaract here


queries = [
    r'(Human[MeSH Terms] OR human population[MeSH Terms] )', 
    r'("race"[Title/Abstract] OR "ethnic"[All Fields] OR "ethnical"[All Fields] OR "ethnically"[All Fields] OR "ethnicities"[All Fields] OR "ethnics"[All Fields] OR "ethnology"[MeSH Subheading] OR "ethnology"[All Fields] OR "ethnicity"[All Fields] OR "ethnology"[MeSH Terms] OR "ethnicity"[MeSH Terms] OR "racial*"[Title/Abstract] OR "racism"[Title/Abstract] OR "ethnic*"[Title/Abstract] OR "racial inequalities"[Title/Abstract] OR "racial groups"[MeSH Terms] OR "race-based"[Title/Abstract] OR "ethnic based"[All Fields] OR "Ethnic groups"[All Fields] OR "Risk factors"[All Fields] OR "Systemic Racism"[All Fields] OR "Ethnic Origin"[All Fields] OR "Ethnic groups"[All Fields] OR "Racial minorities"[All Fields] OR "Black"[All Fields] OR "Afro-descendant"[All Fields] OR "afro*"[All Fields] OR "afric*"[All Fields])',
    r'("ineq*"[All Fields] OR "dispar*"[All Fields] OR ("healthcare disparities"[MeSH Terms] OR "health status disparities"[MeSH Terms] OR (("disparate"[All Fields] OR "disparately"[All Fields] OR "disparities"[All Fields] OR "disparity"[All Fields]) AND "health status"[MeSH Terms]) OR "healthcare disparities"[MeSH Terms]))',
    r'Latin America [mesh] OR Belize OR Costa Rica OR Cuba OR Dominican Republic OR El Salvador OR Guatemala OR Haiti OR Honduras OR Mexico OR Nicaragua, Panama, Saint Lucia OR Argentina OR Bolivia OR Brazil OR Chile OR Colombia OR Ecuador OR Paraguay OR Peru OR Uruguay OR Venezuela',
    r'(y_10[Filter])'
    ]
booleans = ['AND', 'AND', 'AND', 'AND']
createrepository(queries, booleans)




