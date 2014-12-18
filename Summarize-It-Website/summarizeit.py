from flask import Flask
from flask import g
from flask import Markup 
from flask import session, redirect, url_for, escape, request, render_template

from bson.json_util import dumps
from queryDAO import QueryDAO
import summarizer_util

app = Flask(__name__, static_url_path = "", static_folder = "static")
#Allows the use of Access-Control-Allow-Origin
#from flask.ext.cors import CORS
#CORS(app, resources="/Query", headers='Content-Type')


@app.route('/', methods=['GET'])
def Index():	

	past_query_sources = QueryDAO.GetQuerySources()

	return render_template('summarizeit.html', past_queries = past_query_sources)


@app.route("/Query", methods=['POST'])
def PostQuery():
	query_uri = request.form["query_uri"].strip()
	query_text = request.form["query_text"].strip()

	print query_uri
	print query_text

	#QueryDAO.SaveQuerySource(query_uri)

	summary = summarizer_util.get_summary(query_text)
	
	return dumps(summary)


app.secret_key = '\xafrLJh\xbf\xf8\xdb\x83S\xa3\xa2\xb3\x0b.\xbao2%q4\xf8`\xff'
if __name__ == '__main__':
	app.debug = True
	app.run(threaded=True)
