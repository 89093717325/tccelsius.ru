import os, sys
from app import app

if os.environ.get('APP_LOCATION') == 'heroku':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    app.run(debug=True)

sys.path.append('/home/v/vlad/.local/lib/python3.6/site-packages/PIL')
