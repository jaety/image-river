import logging as log
import time

log.basicConfig(level=log.INFO)

warning = log.warning
info = log.info

def timed(show_args = True):
    def timed_decorator(f):
        def _timed(*args, **kw):
            ts = time.time()
            result = f(*args, **kw)
            te = time.time()
            if show_args:
                log.info('func:%r args: [%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
            else:
                log.info('func:%r took: %2.4f sec' % (f.__name__, te-ts))
            return result

        return _timed
    return timed_decorator
