from dbinfo import app, api, db, render_template
from dotenv import load_dotenv

import os

from controls.salad import *

# load_dotenv()
# Load environment variables only in development
if os.environ.get('RENDER') is None:
    load_dotenv()

@app.errorhandler(404)
def page_not_found(err):
    return {"msg": "page not found"}

api.add_resource(HomePage, "/")
api.add_resource(Disease, "/disease/<did>")
api.add_resource(DiseaseList, "/diseaselist")
api.add_resource(SaladType, "/saladtype/<sid>")
api.add_resource(SaladList, "/saladlist")
api.add_resource(DiseaseImg, "/imagedata/<typeimg>")
api.add_resource(SaladKindImg, "/imagedata/salad/<typeimg>")
api.add_resource(DiseaseKindImg, "/imagedata/disease/<typeimg>")
api.add_resource(ImageUpload,"/imageupload" )

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    # db.init_app(app)
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host='0.0.0.0', port=port, debug=False)
