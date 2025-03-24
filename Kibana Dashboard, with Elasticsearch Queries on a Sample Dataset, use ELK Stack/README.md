# Elasticsearch Beginner Commands

This document contains essential Elasticsearch commands for beginners. These commands can be executed using **Kibana's Dev Tools** 

---

## **1. Setup & Basic Commands**

### **Check if Elasticsearch is Running**
```json
GET /
```
<img width="1439" alt="Screenshot 2025-03-24 at 10 45 59 PM" src="https://github.com/user-attachments/assets/32ab9a28-a57c-448b-a8dc-7fcd6de648f7" />



### **Check Cluster Health**
```json
GET _cluster/health
```
<img width="1440" alt="Screenshot 2025-03-24 at 10 46 29 PM" src="https://github.com/user-attachments/assets/76706f2b-b1d7-4558-a689-4d9deb42ff6d" />

---

## **2. Index Management**

### **Create an Index**
```json
PUT my_index
```
<img width="1440" alt="Screenshot 2025-03-24 at 10 47 55 PM" src="https://github.com/user-attachments/assets/2ac8b5b0-3fac-405d-8ef9-c1460735253c" />


### **List All Indices**
```json
GET _cat/indices?v
```
<img width="1440" alt="Screenshot 2025-03-24 at 10 48 30 PM" src="https://github.com/user-attachments/assets/6d8fa0d5-7658-40aa-a9b5-dc16f1d4a6eb" />


### **Delete an Index**
```json
DELETE my_index
```
<img width="1436" alt="Screenshot 2025-03-24 at 10 48 57 PM" src="https://github.com/user-attachments/assets/ebecd6b0-d51a-4607-9d6b-82aa0bc19a84" />


### **Get Index Mapping**
```json
GET my_index/_mapping
```
<img width="1439" alt="Screenshot 2025-03-24 at 10 49 43 PM" src="https://github.com/user-attachments/assets/c7a93d76-14d8-42da-a85a-06369370dae1" />


---

## **3. Document Operations**

### **Insert a Document**
```json
POST my_index/_doc/1
{
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}
```
<img width="1436" alt="Screenshot 2025-03-24 at 10 50 16 PM" src="https://github.com/user-attachments/assets/a37e5439-2de8-44cb-9c39-0635411edf07" />


### **Retrieve a Document by ID**
```json
GET my_index/_doc/1
```
<img width="1440" alt="Screenshot 2025-03-24 at 10 50 48 PM" src="https://github.com/user-attachments/assets/448b6bc5-4ea4-4789-bc0e-a1221771e49a" />


### **Update a Document**
```json
POST my_index/_update/1
{
  "doc": {
    "age": 31
  }
}
```
<img width="1395" alt="Screenshot 2025-03-24 at 10 51 12 PM" src="https://github.com/user-attachments/assets/104fe7fd-bb57-4cb1-aed8-f9130670ff87" />


### **Delete a Document**
```json
DELETE my_index/_doc/1
```
<img width="1440" alt="Screenshot 2025-03-24 at 10 51 49 PM" src="https://github.com/user-attachments/assets/6459d8fe-4100-4b75-a450-cd2023d713b3" />


---

## **4. Searching Data**

### **Match All Documents**
```json
GET my_index/_search
{
  "query": {
    "match_all": {}
  }
}
```
<img width="1435" alt="Screenshot 2025-03-24 at 10 52 55 PM" src="https://github.com/user-attachments/assets/aabbc159-6404-4494-a268-967cb54d2a40" />


### **Search by Field**
```json
GET my_index/_search
{
  "query": {
    "match": {
      "name": "John"
    }
  }
}
```
<img width="1440" alt="Screenshot 2025-03-24 at 10 53 36 PM" src="https://github.com/user-attachments/assets/29ed7583-b1a7-434b-baff-d18dbbdb88e6" />


### **Search with Multiple Conditions**
```json
GET my_index/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "name": "John" }},
        { "range": { "age": { "gte": 25, "lte": 40 }}}
      ]
    }
  }
}
```
![Screenshot 2025-03-24 at 10 54 02 PM](https://github.com/user-attachments/assets/5e7b9344-5353-4b01-9499-f4c13a704f9d)


---

## **5. Bulk Operations**

### **Insert Multiple Documents**
```json
POST my_index/_bulk
{"index":{"_id":"1"}}
{"name": "Alice", "age": 28, "city": "Los Angeles"}
{"index":{"_id":"2"}}
{"name": "Bob", "age": 35, "city": "Chicago"}
```
<img width="1440" alt="Screenshot 2025-03-24 at 10 55 09 PM" src="https://github.com/user-attachments/assets/18942cf2-f86e-487b-8053-c3ca53b2d61d" />


---

## **6. Cluster & Node Information**

### **View Cluster Health**
```json
GET _cluster/health
```
<img width="1440" alt="Screenshot 2025-03-24 at 10 55 31 PM" src="https://github.com/user-attachments/assets/ba35e9e4-ed2e-4456-a578-193ece1aee96" />


### **View Node Stats**
```json
GET _nodes/stats
```
<img width="1440" alt="Screenshot 2025-03-24 at 10 56 02 PM" src="https://github.com/user-attachments/assets/2997e10e-58f1-4df2-9a31-f620866ab565" />


### **List All Running Tasks**
```json
GET _tasks
```
<img width="1438" alt="Screenshot 2025-03-24 at 10 56 32 PM" src="https://github.com/user-attachments/assets/f739751d-1ed6-47f2-963f-b662247d4c4c" />

---

## **7. Security (If Enabled)**

### **Authenticate User**
```json
GET /
```
<img width="1438" alt="Screenshot 2025-03-24 at 10 56 32 PM" src="https://github.com/user-attachments/assets/21cce023-6699-4169-a827-6aee685090d1" />

---

## **8. Kibana-Specific Commands**

### **Get Kibana Status**
```json
GET _cat/health?v
```
<img width="1437" alt="Screenshot 2025-03-24 at 10 58 16 PM" src="https://github.com/user-attachments/assets/17085ef6-8e90-4b72-89a3-1ab999219eee" />


### **List All Available API Endpoints**
```json
GET _cat
```
<img width="1439" alt="Screenshot 2025-03-24 at 10 58 39 PM" src="https://github.com/user-attachments/assets/567b0040-bb8a-475e-a0e0-03beb7c13842" />

---


