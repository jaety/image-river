import subprocess
import logutil as log
import itertools
import re
import csv

def group(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

@log.timed()
def list_images(subdir):
    cmd = [
        "/bin/sh", "-c",
        "mdfind -onlyin %s 'kMDItemContentType == public.jpeg'" % subdir
    ]
    result = subprocess.check_output(cmd).split("\n")
    log.info("found %d images in %s" % (len(result), subdir))
    return result

@log.timed(show_args = False)
def image_info(image_paths):
    keys = [
        "kMDItemContentCreationDate", "kMDItemDisplayName", "kMDItemPixelHeight", "kMDItemPixelWidth"
    ]

    images = " ".join(['"%s"' % s for s in image_paths if s is not None and len(s) > 0])
    cmd = [
        "/bin/sh", "-c",
        "mdls %s %s" % (" ".join(["-name %s" % s for s in keys]), images)
    ]
    result = [s for s in subprocess.check_output(cmd).split("\n") if len(s) > 0]

    matcher = re.compile(r"^(.+)\s+=\s+(.+)$")
    out = []
    for (fn, items) in itertools.izip(image_paths, group(result, len(keys))):
        cleaned_items = [matcher.match(item).group(2) for item in items]
        out.append([fn] + cleaned_items)

    return {
       "keys": ["filename"] + keys,
       "values": out
    }

# data: { keys: Seq[String], values: Seq[Seq[Any]]}
def write_csv(fn, data, write_header=True, append=False):
    flags = 'ab' if append else 'wb'
    with open(fn, flags) as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(data["keys"])
        for line in data["values"]:
            if line is not None:
                writer.writerow(line)

if __name__ == "__main__":
    lines = list_images("/Users/jaety/Pictures")
    fn = '/Users/jaety/projects/image-river/indexer/out/image_info.csv'
    info = image_info(lines[:1000])
    write_csv(fn, info)
    for grp in group(lines[1000:], 1000):
        info = image_info(grp)
        write_csv(fn, info, False, True)

    # with open(fn) as f:
    #     for lin in f:
    #         print lin

#    for line in lines[:5]:
#        print line
