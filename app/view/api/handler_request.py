from app.app import app

with app.app_context():
    class HandlerRequest():
        
        def handle_get_request(self):
            pass