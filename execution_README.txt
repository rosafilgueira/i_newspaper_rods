fab --set DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH setup:query=queries/articles_containing_words.py,datafile=query_args/interesting_gender_words.txt,number_oid=5 test

or in results:
pyspark < newsrods/local_runner.py
