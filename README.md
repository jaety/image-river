# image-river
Tools for processing images en masse

## Next steps

[This link](https://aws.amazon.com/articles/PHP/1602) points to an example of setting everything up in AWS. The architecture here.

* Local image database
* Synchronization tool to wake up AWS, synchronize the databases, and close itself down.
* Ability to kick off a job that will look for new uploads, process them, return them to the database.
* Tool for browsing the image database

## Local Image database

* Deal with aperture. Do I need to get all the images out?
* Very simple image database. I just want to start by being able to collect all the images I have available on a given disk drive.


# Change log

## 5/31/15 - Wrote python mac inspector

* inspector.py
* logutil.py  # Should get lifted out, and be a standard module for all my projects


Still some hard coding in inspector, so watch for that.
The indexer, when run, will query my Pictures directory, and return metadata in a
csv file for all images in my home Pictures directory

    cd indexer
    python inspector.py
    # will output into out/image_info.csv
