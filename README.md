<div align="center">
  
  <div id="user-content-toc">
    <ul>
      <summary><h1 style="display: inline-block;"> Analyzing Sales of AdventureWorks </h1></summary>
    </ul>
  </div>
  
  <p>On-prem Microsoft SQL server to Azure Cloud Pipeline with Data Factory, Data Lake Storage, Databricks, Synapse and PowerBI</p>
  
  <a href="#">
    <img src="https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/AWSaleReport.png">
  </a>
 
</div>
<br>

## 📝 Table of Contents
1. [Introduction](#introduction)
2. [Key Insights](#key-insights)
3. [Project Architecture](#project-architecture)  
  3.1. [Data Ingestion](#data-ingestion)  
  3.2. [Data Transformation](#data-transformation)  
  3.3. [Data Loading](#data-loading)  
  3.4. [Data Reporting](#data-reporting)
  3.5. [Pipeline Testing](#pipeline-testing)
4. [Technologies Used](#technology)
5. [Contact](#contact)

<a name="introduction"></a>
## 🔬 Project Overview 

This is a comprehensive data engineering project on the Azure Cloud encompassing data ingestion, transformation, loading, reporting, as well as pipeline testing and data security and governance. Data were uploaded from an on-premise SQL server to Azure Data Lake Storage Gen 2 using Azure Data Factory, and then transformed using Azure Databricks. Subsequently, the data were loaded into Azure Synapse Analytics Serverless SQL pool as views and linked to PowerBI for reporting. Finally, the pipeline in Data Factory was tested with a scheduled trigger, incorporating new rows input into the on-premise database. The successful execution of the pipeline was confirmed through the PowerBI report.


### 💾 Dataset

**AdventureWorks** is a free database provided by Microsoft on online platforms. Initially published to showcase the design of a SQL Server database using SQL Server 2008, it serves as a product sample database.

Key aspects of AdventureWorks include:

- The database supports a manufacturing multinational corporation named Adventure Works Cycles.
- It is a sample Online Transaction Processing (OLTP) database, which handles multiple concurrent transactions and is included with all Microsoft SQL Server products.

> For this project, I used the **AdventureWorksLT2017** dataset. Lightweight (LT) data refers to a streamlined version of the OLTP sample. [Download here](https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks)


### 🎯 Project Goals

- Establish a connection between the on-premise SQL Server and the Azure Cloud.
- Ingest tables into Azure Data Lake Storage Gen 2.
- Perform data cleaning and transformation using Azure Databricks.
- Load the cleaned data into Azure Synapse Analytics.
- Create interactive data visualizations and reports with Microsoft Power BI.
- Implement Azure Active Directory (Microsoft Entra ID) and Azure Key Vault for data sercurity and governance.

<a name="key-insights"></a>
## 🕵️ Key Insights

- 💸 **Total Revenue and Products sold**
  - On 2008-06-01, a total of 32 sales orders generated revenue of $708.69K, with approximately 2000 products sold.
 
- 🌍 **Popular products**
  - **Top1:** Products with IDs between 850 and 875 were the most popular on 2008-06-01, with more than 50 units sold for each ID.
  - **Top2:** Products with IDs between 710 and 725 were the second most popular, with around 50 units sold for each ID.

- 🚻 **Customer by gender**
  - There are 847 customers in total
  - 41% of the customer are Female
  - 59% of the customers are Male

> This can be explained by males have more interest in doing outdoor activites with the different categories of Bikes than females.

<a name="project-architecture"></a>
## 📝 Project Architecture

You can find the detailed information on the diagram below:

![AW_Architecture](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/ProjectArchitecture.png)

<a name="data-ingestion"></a>
### 📤 Data Ingestion
- Connected the on-premise SQL Server with Azure using Microsoft Integration Runtime.

![SHIR](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/SHIR.PNG)

- Setup the **Resource group** with Azure services (Key Vault, Storage Account, Data Factory, Databricks, Synapse Analytics)

![ressource-group](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/ResourceGroup.PNG)

- Migrated the tables from on-premise SQL Server to Azure Data Lake Storage Gen2.
- Containers in storage account: **bronze** for raw data migrated from on premise SQL server, **silver** for data after level 1 transformation, **gold** for data after level 2 transformation (clean format)
- Folder structure in containers: container_name/schema_name/table_name/table_name.parquet. e.g. bronze/SalesLT/Customer/Customer.parquet.
![containers](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/containers.PNG)
![ADFpipeline1](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/ADFpipeline1.png)

<a name="data-transformation"></a>
### ⚙️ Data Transformation

- Mount Azure Blob Storage to Databricks to retrieve raw data from the Data Lake.
- Create Spark Cluster in Azure Databricks to clean and refine the raw data.
- Level 1 transformation: Change the date format in all the tables to YYYY-MM-DD.
- Level 2 transformation: Change the column names in all the tables from CamelCase to snake_case.
- Save the cleaned data in a Delta format; optimized for further analysis.
- Build a complete pipeline in Azure Data Factory to include the Data Bricks Transfromation

![DB_storagemount](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/db_storagemount.png)
![level1transform1](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/level1T1.png)
![level1transform2](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/level1T2.png)
![level2transform](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/level2T.png)
![ADFpipeline2](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/ADFpipeline.png)


<a name="data-loading"></a>
### 📥 Data Loading

- Create a Serverless SQL Pool to load transformed data using Azure Synapse Analytics.
- Create Views for all tables using Stored Procedure Activity in Azure Synapse Analytics.

![synapse-pipeline](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/synapse_pipeline.png)
![stored_procedure](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/SP-createViews.png)
![views](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/views.png)

<a name="data-reporting"></a>
### 📊 Data Reporting
- Connected Microsoft Power BI to Azure Synapse, and used the Views of the DB to create interactive and insightful data visualizations.
- Use slicing to get report for states (for example Califonia)

![AWsalesreport](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/AWSaleReport.png)
![AWsalesreport_california](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/AWSaleReport_Califonia.png)

<a name="pipeline-testing"></a>
### ⚙️ Pipeline Testing
- Add two more customer details to the on premise AdventureWorks database.
- Set a Schedule trigger for the Azure Data Factory pipeline.
- Check the PowerBI for change in the Customer Number.

![trigger](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/trigger.png)
![addrows](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/addrows.png)
![powerbi3](https://github.com/IrisWangAU/Azure_Data_Engineer_Project/blob/main/asset/powerbi3.png)


<a name="technology"></a>
## 🛠️ Technologies Used

- **Data Source**: Microsoft SQL Server
- **Data Storage**: Azure Data Lake Gen2
- **Data Ingestion**: Azure Data Factory
- **Data Transformation**: Azure Databricks
- **Data Loading**: Azure Synapse Analytics
- **Data Visualization**: PowerBI
- **Authentication and Secrets Management**: Azure Active Directory and Azure Key Vault


### 📋 Credits

- This Project is inspired by the video of the [YouTube Channel "Mr. K Talks Tech"](https://www.youtube.com/watch?v=iQ41WqhHglk)  

<a name="contact"></a>
## 📨 Contact Me

[LinkedIn](https://www.linkedin.com/in/iriswangau/) •
[Gmail](iriswang.mel@gmail.com)
