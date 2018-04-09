fab --set DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH setup:query=queries/articles_containing_words.py,datafile=query_args/interesting_gender_words.txt,number_oid=5 test

or in results:
pyspark < newsrods/local_runner.py

#GalenP examples: https://www.ft.com/content/514f00a0-a0fe-3b2c-99e0-3be8201f9e8c

