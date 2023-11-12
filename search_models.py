import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
import tkinter.font as tkFont
import threading
from selenium.webdriver.chrome.options import Options



def InfiniteScrolling(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(4)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def Hotpoint_Web(driver,list_of_categories,data,Sharaf_DG):
        output_df = pd.DataFrame(columns=['Model','Hotpoint'])
        for cate in list_of_categories:
            df = data[data['Category'] == cate]
            # print(df)
            list_of_models = df["Models"]
            # We got the models of one category
            check_once = 0
            for models in list_of_models:
                if check_once == 0:
                    print("Model: ",models)
                    df_link = Sharaf_DG[Sharaf_DG['Category'] == cate]
                    keyword = models
                    # print(df_link["Links"])
                    dyno_link = df_link["Links"].iloc[0]
                    # print(dyno_link)
           
                    model_ids :list = []
                    driver.get(dyno_link)
                    # # Get scroll height
                    InfiniteScrolling(driver)
                    
                    # driver.get(dyno_link)
                    # time.sleep(5)
                    all_divs  = driver.find_elements(By.XPATH, "//h5[@class='card-title product-card-name']")
                    # print(len(all_divs))
                    # Compare product name with model name 
                    for div in all_divs:
                        model_id = div.text
                        print(model_id)
                        check_once = 1
                        # Save this model id in the list and use it later 
                        # 
                        model_ids.append(model_id)



                total_models = len(model_ids)
                counter = 0
                for each_model in model_ids: 
                    if each_model.lower().find(models.lower()) != -1:
                        output_df = output_df.append({
                                "Model":models,
                                "Hotpoint": "o",
                        },ignore_index=True)
                        print(models,"Found")
                        break
                    counter+=1

                if counter == total_models:
                    output_df = output_df.append({
                            "Model":models,
                            "Hotpoint": "x",
      
                    },ignore_index=True)
                    print(models,"Not Found")
                
                # Compare here now

        with pd.ExcelWriter("output.xlsx",mode="a",if_sheet_exists='replace') as writer:
            output_df.to_excel(writer,sheet_name="Hotpoint")
 

def Carrefour_Web(driver,list_of_categories,data,Sharaf_DG):
        output_df = pd.DataFrame(columns=['Model','Carrefour'])
        for cate in list_of_categories:
            df = data[data['Category'] == cate]
            # print(df)
            list_of_models = df["Models"]
            # We got the models of one category
            check_once = 0
            for models in list_of_models:
                if check_once == 0:
                    print("Model: ",models)
                    df_link = Sharaf_DG[Sharaf_DG['Category'] == cate]
                    keyword = models
                    # print(df_link["Links"])
                    dyno_link = df_link["Links"].iloc[0]
                    # print(dyno_link)
           
                    model_ids :list = []
                    driver.get(dyno_link)
                    # # Get scroll height
                    InfiniteScrolling(driver)
                    
                    # driver.get(dyno_link)
                    # time.sleep(5)
                    all_divs  = driver.find_elements(By.XPATH, "//a[@data-testid='product_name']")
                    # print(len(all_divs))
                    # Compare product name with model name 
                    for div in all_divs:
                        model_id = div.text
                        print(model_id)
                        check_once = 1
                        # Save this model id in the list and use it later 
                        # 
                        model_ids.append(model_id)



                total_models = len(model_ids)
                counter = 0
                for each_model in model_ids: 
                    if each_model.lower().find(models.lower()) != -1:
                        output_df = output_df.append({
                                "Model":models,
                                "Carrefour": "o",
                        },ignore_index=True)
                        print(models,"Found")
                        break
                    counter+=1

                if counter == total_models:
                    output_df = output_df.append({
                            "Model":models,
                            "Carrefour": "x",
      
                    },ignore_index=True)
                    print(models,"Not Found")
                
                # Compare here now

        with pd.ExcelWriter("output.xlsx",mode="a",if_sheet_exists='replace') as writer:
            output_df.to_excel(writer,sheet_name="Carrefour")
        
def Carrefour_WebT20(driver,list_of_categories,data,Sharaf_DG):
        output_df = pd.DataFrame(columns=['Model','CarrefourT20',"Old Models"])
        for cate in list_of_categories:
            df = data[data['Category'] == cate]
            # print(df)
            list_of_models = df["Models"]
            # We got the models of one category
            check_once = 0
            for models in list_of_models:
                if check_once == 0:
                    print("Model: ",models)
                    df_link = Sharaf_DG[Sharaf_DG['Category'] == cate]
                    keyword = models
                    # print(df_link["Links"])
                    dyno_link = df_link["Links"].iloc[0]
                    # print(dyno_link)
           
                    model_ids :list = []
                    driver.get(dyno_link)
                    # # Get scroll height
                    InfiniteScrolling(driver)
                    
                    # driver.get(dyno_link)
                    # time.sleep(5)
                    all_divs  = driver.find_elements(By.XPATH, "//a[@data-testid='product_name']")
                    # print(len(all_divs))
                    # Compare product name with model name 
                    x=0
                    for div in all_divs:
                        if div.text.find("LG") != -1:
                            model_id = div.text
                            print(model_id)
                            check_once = 1
                            # Save this model id in the list and use it later 
                            # 
                            model_ids.append(model_id)
                        x+=1
                        if x>20:
                            break


                total_models = len(model_ids)
                counter = 0
                for each_model in model_ids: 
                    if each_model.find(models) != -1:
                        output_df = output_df.append({
                                "Model":models,
                                "Carrefour": "o",
                                "Old Models": total_models
                        },ignore_index=True)
                        print(models,"Found")
                        break
                    counter+=1

                if counter == total_models:
                    output_df = output_df.append({
                            "Model":models,
                            "Carrefour": "x",
                            "Old Models": total_models
      
                    },ignore_index=True)
                    print(models,"Not Found")
                
                # Compare here now

        with pd.ExcelWriter("output.xlsx",mode="a",if_sheet_exists='replace') as writer:
            output_df.to_excel(writer,sheet_name="CarrefourTop20")
   

def KSP_Web(driver,list_of_categories,data,Sharaf_DG):
        output_df = pd.DataFrame(columns=['Model','KSP'])
        for cate in list_of_categories:
            df = data[data['Category'] == cate]
            # print(df)
            list_of_models = df["Models"]
            # We got the models of one category
            check_once = 0
            for models in list_of_models:
                if check_once == 0:
                    print("Model: ",models)
                    df_link = Sharaf_DG[Sharaf_DG['Category'] == cate]
                    keyword = models
                    # print(df_link["Links"])
                    dyno_link = df_link["Links"].iloc[0]
                    # print(dyno_link)
           
                    model_ids :list = []
                    driver.get(dyno_link)
                    # # Get scroll height
                    InfiniteScrolling(driver)
                    
                    # driver.get(dyno_link)
                    # time.sleep(5)
                    all_divs  = driver.find_elements(By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-subtitle1")
                    # print(len(all_divs))
                    # Compare product name with model name 
                    for div in all_divs:
                        model_id = div.text
                        print(model_id)
                        check_once = 1
                        # Save this model id in the list and use it later 
                        # 
                        model_ids.append(model_id)



                total_models = len(model_ids)
                counter = 0
                for each_model in model_ids: 
                    if each_model.find(models) != -1:
                        output_df = output_df.append({
                                "Model":models,
                                "KSP": "o",
                        },ignore_index=True)
                        print(models,"Found")
                        break
                    counter+=1

                if counter == total_models:
                    output_df = output_df.append({
                            "Model":models,
                            "KSP": "x",
      
                    },ignore_index=True)
                    print(models,"Not Found")
                
                # Compare here now

        with pd.ExcelWriter("output.xlsx",mode="a",if_sheet_exists='replace') as writer:
            output_df.to_excel(writer,sheet_name="KSP")
 

def Run_Carrefour():




    # 0------------------------------------------------------------------------------
    # df_sharaf_dg_categories_keywords = pd.read_excel("search_keywords.xlsx")
    # df_sharaf_dg_brands = pd.read_excel("input.xlsx")
    data = pd.read_excel("models.xlsx",sheet_name="Models")
    Sharaf_DG = pd.read_excel("models.xlsx",sheet_name="Carrefour")
    # LULU = pd.read_excel("models.xlsx",sheet_name="LULU")
    # Jumbo = pd.read_excel("models.xlsx",sheet_name="Jumbo")
    # output_df = pd.DataFrame(columns=['Model','Sharaf_DG'])
    # print(data["Model"])
    
    # print(data["Category"].unique())
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
    list_of_categories = data["Category"].unique()

    Carrefour_Web(driver,list_of_categories,data,Sharaf_DG)
    
def Run_CarrefourT20():




    # 0------------------------------------------------------------------------------
    # df_sharaf_dg_categories_keywords = pd.read_excel("search_keywords.xlsx")
    # df_sharaf_dg_brands = pd.read_excel("input.xlsx")
    data = pd.read_excel("models.xlsx",sheet_name="Models")
    Sharaf_DG = pd.read_excel("models.xlsx",sheet_name="CarrefourTop20")
    # LULU = pd.read_excel("models.xlsx",sheet_name="LULU")
    # Jumbo = pd.read_excel("models.xlsx",sheet_name="Jumbo")
    # output_df = pd.DataFrame(columns=['Model','Sharaf_DG'])
    # print(data["Model"])
    
    # print(data["Category"].unique())
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
    list_of_categories = data["Category"].unique()

    Carrefour_WebT20(driver,list_of_categories,data,Sharaf_DG)
     

def Run_KSP():




    # 0------------------------------------------------------------------------------
    # df_sharaf_dg_categories_keywords = pd.read_excel("search_keywords.xlsx")
    # df_sharaf_dg_brands = pd.read_excel("input.xlsx")
    data = pd.read_excel("models.xlsx",sheet_name="Models")
    Sharaf_DG = pd.read_excel("models.xlsx",sheet_name="KSP")
    # LULU = pd.read_excel("models.xlsx",sheet_name="LULU")
    # Jumbo = pd.read_excel("models.xlsx",sheet_name="Jumbo")
    # output_df = pd.DataFrame(columns=['Model','Sharaf_DG'])
    # print(data["Model"])
    
    # print(data["Category"].unique())
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
    list_of_categories = data["Category"].unique()

    KSP_Web(driver,list_of_categories,data,Sharaf_DG)
 

def Run_Hotpoint():




    # 0------------------------------------------------------------------------------
    # df_sharaf_dg_categories_keywords = pd.read_excel("search_keywords.xlsx")
    # df_sharaf_dg_brands = pd.read_excel("input.xlsx")
    data = pd.read_excel("models.xlsx",sheet_name="Models")
    Sharaf_DG = pd.read_excel("models.xlsx",sheet_name="Hotpoint")
    # LULU = pd.read_excel("models.xlsx",sheet_name="LULU")
    # Jumbo = pd.read_excel("models.xlsx",sheet_name="Jumbo")
    # output_df = pd.DataFrame(columns=['Model','Sharaf_DG'])
    # print(data["Model"])
    
    # print(data["Category"].unique())
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
    list_of_categories = data["Category"].unique()

    Hotpoint_Web(driver,list_of_categories,data,Sharaf_DG)
            


        
            
                    
         

# Main App 
class App:

    def __init__(self, root):
        #setting title
        root.title("Kenya Model Check")
        ft = tkFont.Font(family='Arial Narrow',size=13)
        #setting window size
        width=640
        height=480
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg='black')

        ClickBtnLabel=tk.Label(root)
       
      
        
        ClickBtnLabel["font"] = ft
        
        ClickBtnLabel["justify"] = "center"
        ClickBtnLabel["text"] = "Kenya Model Check"
        ClickBtnLabel["bg"] = "black"
        ClickBtnLabel["fg"] = "white"
        ClickBtnLabel.place(x=120,y=190,width=150,height=70)
    

        
        Lulu=tk.Button(root)
        Lulu["anchor"] = "center"
        Lulu["bg"] = "#009841"
        Lulu["borderwidth"] = "0px"
        
        Lulu["font"] = ft
        Lulu["fg"] = "#ffffff"
        Lulu["justify"] = "center"
        Lulu["text"] = "START"
        Lulu["relief"] = "raised"
        Lulu.place(x=375,y=190,width=150,height=70)
        Lulu["command"] = self.start_func




  

    def ClickRun(self):

        running_actions = [
            Run_Carrefour,          
            Run_Hotpoint,          
            # Run_CarrefourT20,          
            # Run_KSP,
            # Run_Jumbo
        ]

        thread_list = [threading.Thread(target=func) for func in running_actions]

        # start all the threads
        for thread in thread_list:
            thread.start()

        # wait for all the threads to complete
        for thread in thread_list:
            thread.join()
    
    def start_func(self):
        thread = threading.Thread(target=self.ClickRun)
        thread.start()

    
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


# Run()
