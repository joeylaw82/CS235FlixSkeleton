# CS235FlixSkeleton
The skeleton python project for the 2020 S2 CompSci 235 practical assignment CS235Flix.

For assignment 2. I have only done the repository part , hope to get some mark from it.



## Testing for repository

Testing requires that file *CS235FlixSkeleton/adapters/test_memory_repository.py* be edited to set the value of `TEST_DATA_PATH`. You should set this to the absolute path of the *CS235FlixSkeleton/datafiles* directory. 

E.g. 

`TEST_DATA_PATH = os.path.join('Macintosh HD', os.sep, 'Users', 'joeylaw', 'CS235FlixSkeleton',
                              'datafiles')`

assigns TEST_DATA_PATH with the following value (the use of os.path.join and os.sep ensures use of the correct platform path separator):

`Macintosh HD\Users\joeylaw\CS235FlixSkeleton\python-dev\datafiles`

You can then run tests from within PyCharm.
