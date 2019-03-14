# craam-services

Microsserviços feitos para o CRAAM.

## GOES

* **URL**

`/goes/get_data`

* **Método:** `GET`

*  **Parâmetros**

   **Required:**
 
   `begin=[datetime]`
   `end=[datetime]`

* **Resposta de sucesso:**
  
  * **Status:** 200 <br />
    **Conteúdo:**
	```json
	{
	  "xrsa" : {
	    "time_begin": "value",
		.
		.
		.
	    "time_end": "value",
	  },
	  "xrsb" : {
	    "time_begin": "value",
		.
		.
		.
		"time_end": value
	  }
	}
	```
 
* **Resposta de erro:**

  * **Status:** 400 <br />
    **Conteúdo:** `{ message : "Date error" }`

## NOAA

* **URL**

`/noaa_report/get_data`

* **Método:** `GET`

*  **Parâmetros**

   **Required:**
 
   `day=[int]`
   `month=[int]`
   `year=[int]`

* **Resposta de sucesso:**
  
  * **Status:** 200 <br />
    **Conteúdo:** `{ "" : "" }`
 
* **Resposta de erro:**

  * **Status:** 500 <br />
    **Conteúdo:** `{ message : "File not found" }`
	
  * **Status:** 500 <br />
    **Conteúdo:** `{ message : "No event reports" }`
	
  * **Status:** 400 <br />
    **Conteúdo:** `{ message : "Impossible date" }`

## RSTN

* **URL**

`/rstn/get_data`

* **Método:** `GET`

*  **Parâmetros**

   **Required:**
 
   `begin=[datetime]`
   `end=[datetime]`

* **Resposta de sucesso:**
  
  * **Status:** 200 <br />
    **Conteúdo:** `{ "" : "" }`
 
* **Resposta de erro:**

  * **Status:** 400 <br />
    **Conteúdo:** `{ message : "Date error" }`
