# Debug slow website

## possible problems 

- ## Front End Performance
    Monitor web performance with Monitoring tools

    ### we need to optimize two things
    
    - The time from the request till the first byte received from the server
    - Time from the first to reach the browser till when it's loaded and processed by the browser
    
    ### External HTTPS requests
    
    need to reduce any external request the browser needs to make to get the data, any javascript-enabled content is like plugins take more time to request and download. remove any non-essential plugins

    ### reduce internal HTTP requests
    
    multiple files mean multiple requests which take more time. one request for one big fils is faster than multiple for smaller files 

    ### reduce files size with gzip compression

    it takes time to decompress but it saves time when download files and decompression happens on the user side

    ### Load Critical files first

    load only what is needed and when it is needed


    consider splitting big files into multiple files and request files needed to load the website first

    ### Un-Bloat your CSS

    front-end developers should remove repetitive CSS code as it results in a large CSS file which slows downtime of load for the website

    ### Image Optimization

    remove images option and details and consider reducing the resolution when possible or using smaller images

    ### Cache Optimization

    considering response depending on regions cashing some static files on servers in regions which have reduced loading performance
    
- ## Back End Performance
    
    Investigating back-end request time on server-side
    
    ### Profiling backend
    
    profiling back end application to measure the performance of everything
    , you can use it on a local machine

    #### Slow database 
    
    - the average number of requests per page: needs to be reduced
    - slow queries: needs to be optimized
    - multiple queries on the same table: need to group multiple requests into one big request
    
    #### Slow External requests 

    - caching files to reduce external request
    - some requests can be handled asynchronously as writing servers

    #### Slow Back-end Code

    - check slow functions in code and rewrite them
    - upgrade to newer versions if possible

    
    ### Optimize your Server

    ### Network problems

    #### check Latency

    The time it takes TCP packet between the server and database server. 

    #### check Bandwidth

    The amount of data that a server can receive in an amount of time .

    ### check processor and memory usage
    
    simply using top and htop if you are in dedicated server, add more ram or better CPU machine or more cores, servers with SSD help in reading and write process
    
    #### Consider using CDN

    #### Analyzing your server’s access logs
    
    #### Fix any 404 error found in log





