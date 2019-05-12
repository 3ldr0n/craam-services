# craam-services

Microsserviços feitos para o CRAAM.

## GOES

* **URL**

`/goes/get_data`

* **Método:** `GET`

* **Parâmetros**

   **Obrigatórios:**
 
   `begin=[datetime]` <br />
   `end=[datetime]`

* **Resposta de sucesso:**
  
  * **Status:** 200 <br />
    **Conteúdo:**
	```json
	{
	  "xrsa" : {
	    "time_begin": "value",
	    "...": "...",
	    "time_end": "value",
	  },
	  "xrsb" : {
	    "time_begin": "value",
	    "...": "...",
	    "time_end": "value"
	  }
	}
	```
 
* **Resposta de erro:**

  * **Status:** 400 <br />
    **Conteúdo:**
	```json
	{ "message" : "Date error" }
	```

## NOAA

* **URL**

`/noaa_report/get_data`

* **Método:** `GET`

* **Parâmetros**

   **Obrigatórios:**
 
   `day=[int]` <br />
   `month=[int]` <br />
   `year=[int]` <br />
   `station=[string]`

* **Resposta de sucesso:**
  
  * **Status:** 200 <br />
    **Conteúdo:** 
	```json
	{
	  "event": {
	    "first_index": "value",
	    "...": "...",
	    "last_index": "value",
	  },
	  "begin": {"..."},
	  "max": {"..."},
	  "end": {"..."},
	  "obs": {"..."},
	  "Q": {"..."},
	  "type": {"..."},
	  "loc/frq": {"..."},
	  "particulars": {"..."},
	  "reg": {"..."}
	}
	```
 
* **Resposta de erro:**

  * **Status:** 500 <br />
    **Conteúdo:**
	```json
	{ "message" : "File not found" }
	```
	
  * **Status:** 500 <br />
    **Conteúdo:**
	```json
	{ "message" : "No event reports" }
	```
	
  * **Status:** 400 <br />
    **Conteúdo:**
	```json
	{ "message" : "Impossible date" }
	```

## RSTN

* **URL**

`/rstn/get_data`

* **Método:** `GET`

* **Parâmetros**

   **Obrigatórios:**
 
   `day=[int]` <br />
   `month=[int]`<br />
   `year=[int]` <br />
   `station=[str]`

* **Resposta de sucesso:**
  
  * **Status:** 200 <br />
    **Conteúdo:**
	```json	
	{
	  "245": {
	    "time": "value",
	    "...": "...",
	  },
	  "410": {"..."},
	  "610": {"..."},
	  "1415": {"..."},
	  "2695": {"..."},
	  "4995": {"..."},
	  "8800": {"..."},
	  "15400": {"..."}
	```
 
* **Resposta de erro:**

  * **Status:** 400 <br />
    **Conteúdo:** 
	```json
	{ "message" : "Impossible date" }
	```
	
  * **Status:** 500 <br />
    **Conteúdo:**
	```json
	{ "message" : "Internal error" }
	```
