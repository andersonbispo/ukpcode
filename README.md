# ukpcode
UK post code library

Basically, there are two functions: format and is_valid. Call the format function to format a UK post code following the patterns described [here](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting). 

If the format function is called with an invalid post code, the function will raise an exception. On the other hand, the is_valid function returns True or False if the UK post code is valid or not. 

The ukpcode accepts, in both functions, the code in lower case and with extra blank spaces.


```
import ukpcode

ukpcode.format("EC1A1BB")
ukpcode.format(" M1  1AE  ")
ukpcode.format("ec1a1bb")

ukpcode.is_valid("EC1A 1BB")
ukpcode.is_valid("EC1A1BB")
ukpcode.is_valid("EC1ABBB")
```
