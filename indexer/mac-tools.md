# Indexing, mac specific

You can utilize a mac's spotlight indexing to great effect.

    mdfind      # to find files with specific metadata
    mdls        # to see metadata about a specific file
    mdimport -X # gives you a full list of available schemas

To find all jpegs in your home directory

    mdfind -onlyin ~ 'kMDItemContentType == "public.jpeg"'

To grab the initial index data I care about and dump it into a csv

    kMDItemContentCreationDate
    kMDItemDisplayName (also kMDItemFSName what's the difference?)
    kMDItemPixelHeight
    kMDItemPixelWidth

The following should work to push everything into a file for import

    ./mac.sh > out/jpegs.json
