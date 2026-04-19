Test Ideas

1) Test the health endpoint and check response
2) Test Basic Upload
   1) We need to check via AWS to see if the object exists after a single upload
3) Test Overwrite Upload
   1) Upload 2 different objects for the same key, and check at each step to make sure overwrite occurred
4) Test File Too Large
   1) Attempt to upload a file larger than 1 MB
5) Test Missing filename Field
6) Test Missing content Field