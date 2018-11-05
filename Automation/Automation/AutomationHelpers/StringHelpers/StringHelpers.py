import string
import random
class StringHelpers:
    """String generation helpers class"""
    
    def UserIdGenerator(size=10, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


