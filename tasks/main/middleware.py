class XForwardedPortMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_port = request.META.get("HTTP_X_FORWARDED_PORT")
        if x_forwarded_port:
            # Save the original get_host method so we can restore it later
            original_get_host = request.get_host

            # Define a new get_host method that includes the X-Forwarded-Port
            def get_host_with_port():
                host = original_get_host()
                return f"{host}:{x_forwarded_port}"

            # Replace the request's get_host method with our new method
            request.get_host = get_host_with_port

        response = self.get_response(request)

        if x_forwarded_port:
            # Restore the original get_host method
            request.get_host = original_get_host

        return response
