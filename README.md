# Kafka CDC Setup


## Purpose

Test deduplication in Couchbase records using Kafka

## Prerequisites

<ul>
    <li> Java (11.0.17 preferred)
    <li> Python (3.10.9 preferred)
    <li> Couchbase Server 7.1.1
    <li> Zookeeper & Kafka
    <li> Couchbase Kafka Source Connector
</ul>


## Instructions for Running and Testing the project Locally

### Preparation

**a. Have Zookeeper and Kafka Server installed**
**b. Start Couchbase Server**
**c. Create a bucket called *Source* using Magma as the storage engine**
**d. Under the __default scope, create a collection called inputCollection**

### Running the script
**a. Clone the repository (Otherwise you can also download the zip file of the repository)**
```
> git clone https://github.com/jineshparakh/Kafka_CDC_Setup.git
```

**b. Change the directory. (You can also open this project on any IDE, preferably VSCode)**

```
> cd Kafka_CDC_Setup
```

**c. Update const.py with commands relevant to your machine**


**d. Setting Up Virtual Environment(Prerequisites: Your System should have Python3 installed)**

```
> pip install virtualenv    #Installing the virtual environment module
> virtualenv venv           #Create virtual environment venv
```

**e. Activating Virtual Environment:**
*On Windows (Tested on Windows 10)*
```
> venv\Scripts\activate    #Activate Virtual Environment 
```
*On macOS  and Linux (Tested on MacOs Monterey)*
```
> source venv/bin/activate   #Activate Virtual Environment
```

**f. Installing requirements**
```
> pip install -r requirements.txt    #Installing all the requirements for running the project
```

**g. Once all the requirements are installed, it's time to run the main process**
```
> python main.py    #Starts the process
```