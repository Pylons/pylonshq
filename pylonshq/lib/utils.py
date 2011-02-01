import re
import unicodedata

def natural(key):
    """natural(key)
    usage:
    >>> sorted(unsorted, key=natural)
    >>> unsorted.sort(key=natural)

    if key is unicode, it simplifies key to ascii using unicodedata.normalize.
    
    by Timo Reunanen
    """

    if isinstance(key, basestring):
        if isinstance(key, unicode):
            key=unicodedata.normalize('NFKD', key.lower()).encode('ascii', 'ignore')
        else:
            key=key.lower()

        return [int(n) if n else s for n,s in re.findall(r'(\d+)|(\D+)', key)]
    else:
        return key
