# GOES

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
