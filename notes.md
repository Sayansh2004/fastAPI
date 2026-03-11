## FastAPI (Fast to run/code)

made up of two things
1.Startlette(recieves and send HTTP requests)
2.Pydantic (data validation library)


## FastAPI


web server -----> SGI ------> API code
                  (Server 
                  Gateway
                  Interface
                  )

SGI is required as to get convert request data as python cannot validate it so we need a SGI and which is starlette in case of fastAPI and webserver used is uvicorn. The biggest advantage over other framework such as flask is that it is asynchronus.
