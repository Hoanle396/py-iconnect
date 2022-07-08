from app import app
import app.settings as settings
from TiktokRoute import TiktokRoute
from ImageRoute import ImageRoute
if __name__ == "__main__":
    TiktokRoute(app)
    ImageRoute(app)
    app.run(host=settings.BE_HOST, port=settings.BE_PORT, debug=settings.ENV != "PROD")
