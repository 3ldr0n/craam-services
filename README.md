# craam-services

Microsserviços feitos para o CRAAM.

## GOES

* **URL**

`/goes/get_data`

* **Método:** `GET`

*  **Parâmetros**

   **Required:**
 
   `begin=[]`
   `end=[]`
   

* **Resposta de sucesso:**
  
  * **Status:** 200 <br />
    **Conteúdo:** `{ "" : "" }`
 
* **Resposta de erro:**

  * **Status:** 400 <br />
    **Conteúdo:** `{ message : "Date error" }`

## NOAA

```
GET:
/noaa_report/get_data
```

## RSTN

```
GET:
/rstn/get_data
```
