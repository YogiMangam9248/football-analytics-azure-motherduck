# football-analytics-azure-motherduck

## 📌 Overview  
This project demonstrates a modern data engineering pipeline using free and serverless tools.  
The pipeline fetches live football match data from a public API, ingests it into **MotherDuck** via an **Azure Function**, transforms it using **dbt**, and finally visualizes insights in **Power BI**.

The goal is to showcase how to build a **low-cost, cloud-native, end-to-end analytics solution** that can be extended for real-world use cases such as sports analytics, real-time dashboards, and data reporting.

---

## 🏗️ Architecture  
The data flow is as follows:  
1. **Fetch data from API** – Football matches data from a public API  
2. **Store data** – Azure Function loads data into MotherDuck tables  
3. **Transform data** – dbt models transform raw data  
4. **Visualize data** – Power BI dashboards show analytics  

---

## 🛠️ Prerequisites  
- Python 3.10+  
- Azure Functions Core Tools  
- MotherDuck account (Free)  
- Power BI Desktop  
- API key (Football API, etc.)  

---

## ⚙️ Setup Instructions  

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
 

## ⚙️ Setup Instructions  
1. Clone the repository  
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
