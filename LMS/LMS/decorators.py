from functools import wraps
import time
import threading
from rest_framework.response import Response
from rest_framework import status

class RateLimiter:
    def __init__(self):
        self.requests = {}
        self.lock = threading.Lock()

    def add_request(self, key, window):
        current_time = time.time()
        with self.lock:
            timestamps = self.requests.get(key, [])
            timestamps = [t for t in timestamps if current_time - t < window]
            timestamps.append(current_time)
            self.requests[key] = timestamps
            return len(timestamps)

rate_limiter = RateLimiter()

def rate_limit(requests=5, window=60):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(view_instance, request, *args, **kwargs):
            client_ip = request.META.get('REMOTE_ADDR')
            key = f'rate_limit:{client_ip}:{view_func.__name__}'
            request_count = rate_limiter.add_request(key, window)

            if request_count > requests:
                # Create a Response object with fallback for renderer attributes
                response = Response({
                    'error': 'Too many requests',
                    'detail': f'Please wait {window} seconds before trying again.',
                    'retry_after': window
                }, status=status.HTTP_429_TOO_MANY_REQUESTS)

                # Set renderer attributes only if they exist on the request
                if hasattr(request, 'accepted_renderer'):
                    response.accepted_renderer = request.accepted_renderer
                if hasattr(request, 'accepted_media_type'):
                    response.accepted_media_type = request.accepted_media_type
                if hasattr(request, 'renderer_context'):
                    response.renderer_context = request.renderer_context

                return response

            return view_func(view_instance, request, *args, **kwargs)
        return wrapped_view
    return decorator