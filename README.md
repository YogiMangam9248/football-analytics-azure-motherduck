# football-analytics-azure-motherduck

## 📌 Overview  
This project demonstrates a modern data engineering pipeline using free and serverless tools.  
The base pipeline fetches live football match data from a public API (Football data org), ingests it into **MotherDuck** via an **Azure Function**

Transformations will be done using **dbt**, and I'm going to use **Power BI** for analytics.

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
- Python 3.9+  
- Azure Functions Core Tools  
- MotherDuck account (Free)  
- Power BI Desktop  
- Football data org (Free)  

---

## ⚙️ Setup Instructions  

### 1. Clone the repository
```bash  
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
```
### 2. Create and activate a virtual environment, then install dependencies:
```bash  
   python -m venv .venv
   .venv\Scripts\activate  # Windows
    source .venv/bin/activate  # Mac/Linux
    pip install -r requirements.txt
```
### 3. Configure environment variables in local.settings.json:
```json
 {
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "FOOTBALL_API_KEY": "<YOUR_API_KEY>",
    "MOTHERDUCK_TOKEN": "<YOUR_MOTHERDUCK_TOKEN>",
    "DB_NAME": "football_analytics"
  }
}
```
### 4. Run the Azure Function locally:
```bash
  func start
```

The pipeline will fetch live football match data and populate your MotherDuck tables.
You can then connect Power BI to visualize dashboards.

## 🚀 Features
- Live football match ingestion from API
- Incremental data loading with DLT
- Serverless, low-cost pipeline
- Fully extendable for analytics & dashboards

## 📝 Notes
- If pipeline runs fail or you need to reset, use `dev_mode=True` in the pipeline temporarily to reset pipeline state.
- MotherDuck dataset names are normalized automatically; avoid dots in dataset names or disable normalization via `enable_dataset_name_normalization`.
- This project demonstrates a real-time, incremental ingestion pipeline – data fetched is always the latest available from the API.
