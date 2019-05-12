# RSTN

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
    }
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
