# NOAA

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
