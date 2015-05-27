#!/bin/bash

function image_metadata() {
    fn="$@"
    echo "{"
    mdls -name kMDItemContentCreationDate -name kMDItemDisplayName -name kMDItemPixelHeight -name kMDItemPixelWidth "$fn" | sed -E s/\(.+\)=\(.+\)/\\1:\\2/
    echo "},"
}

echo "["
while read fn
do
    image_metadata $fn
done < <(mdfind -onlyin ~ 'kMDItemContentType == "public.jpeg"')
echo "{}]"
