import os
import certifi
from dotenv import load_dotenv
from flask import Flask
from flask_graphql import GraphQLView
from mongoengine import connect
from .schema import schema

load_dotenv()
mongo_user = os.getenv('MONGO_USER')
mongo_pass = os.getenv('MONGO_PASSWORD')
mongo_connection = os.getenv('MONGO_CONNECTION_STRING').format(mongo_user=mongo_user, mongo_password=mongo_pass)
connect('per_season_stats', host=mongo_connection, alias='default', tls=True, tlsCAFile=certifi.where())
app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('CONTAINER_PORT'))