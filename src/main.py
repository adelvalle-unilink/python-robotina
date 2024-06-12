from flask import Flask, request

from repositories.lane import Lane
from utils.functions import copy_excel_template
from config import config, db_connection

app = Flask(__name__)

@app.route("/", methods=["POST"])
def create_excel():
    config = config.load_config(section='postgresql')
    conn = db_connection.connect(config)

    # GET LANE REPOSITORY METHODS WITH CONNECTION.
    lane = Lane(conn)
    
    # GET IDS FROM BODY.
    ids = request.json["ids"]
    
    lanes = lane.get_all(ids)

    copy_excel_template(lanes)
    
    conn.close()
    
    response = {
        "success": True,
    }
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5001)