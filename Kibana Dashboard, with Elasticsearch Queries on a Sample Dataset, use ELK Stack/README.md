# Elasticsearch Commands

This document contains essential Elasticsearch commands for beginners. These commands can be executed using **Kibana's Dev Tools** or via **cURL**.

---

## **1. Setup & Basic Commands**

### **Check if Elasticsearch is Running**
```json
GET /
```

### **Check Cluster Health**
```json
GET _cluster/health
```

### **View Elasticsearch Version**
```json
GET /
```

---

## **2. Index Management**

### **Create an Index**
```json
PUT my_index
```

### **List All Indices**
```json
GET _cat/indices?v
```

### **Delete an Index**
```json
DELETE my_index
```

### **Get Index Mapping**
```json
GET my_index/_mapping
```

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

### **Retrieve a Document by ID**
```json
GET my_index/_doc/1
```

### **Update a Document**
```json
POST my_index/_update/1
{
  "doc": {
    "age": 31
  }
}
```

### **Delete a Document**
```json
DELETE my_index/_doc/1
```

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

---

## **6. Cluster & Node Information**

### **View Cluster Health**
```json
GET _cluster/health
```

### **View Node Stats**
```json
GET _nodes/stats
```

### **List All Running Tasks**
```json
GET _tasks
```

---

## **7. Security (If Enabled)**

### **Authenticate User**
```json
GET /
```
(If security is enabled, credentials may be required.)

---

## **8. Kibana-Specific Commands**

### **Get Kibana Status**
```json
GET _cat/health?v
```

### **List All Available API Endpoints**
```json
GET _cat
```

---

These commands are helpful for basic operations in Elasticsearch. Run them using Kibana's **Dev Tools** or **cURL**. 🚀

