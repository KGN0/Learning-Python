'''A programming language uses objects in its programs to perfom operations. Objects include simple varibles, like strings, integers
or booleans. They also include more complex data structures like list, hashes, or classes.

    In early programming languages, most developers were responsible for all memory management in their programs. This meant before
creating a list or an object, we first needed to allocate the memory for a variable. After we are done with a variable, we then needed to deallocate
it to "free" that memeory for other users
This leads to two problems:
1. forgetting to free your memory
2. freeing memory too soon.'''

# Automatic garbage collection
'''With automatic memory management, programmers no longer needed to manage memory themselves. Rather the runtime handled this for them
There are two strategies
1. Reference counting
2. Garbage collection'''
# The gc module provides the following functions
'''
gc.enable()
gc.disable()
gc.isenabled()
gc.set_debug(flags)
gc.get_debug()
gc.get_objects(generation = None)
gc.get_stats()
gc.set_threshold(threshold0[, threshold1])
gc.get_count()
gc.get_threshold()
gc.get_referrers(*objs)
gc.get_referents(*objs)
gc.is_tracked(obj)
gc.is_finalized(obj)
gc.freeze()
gc.unfreeze()
gc.get_freeze_count()
gc.garbage
'''