# image-river
Tools for processing images en masse

## Next steps

[This link](https://aws.amazon.com/articles/PHP/1602) points to an example of setting everything up in AWS. The architecture here.

* Local image database
* Synchronization tool to wake up AWS, synchronize the databases, and close itself down.
* Ability to kick off a job that will look for new uploads, process them, return them to the database.
* Tool for browsing the image database
