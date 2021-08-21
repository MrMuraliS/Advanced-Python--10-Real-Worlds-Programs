import justpy as jp
import definition
import json


class Api:
    """Handles requests at http://127.0.0.1:8000/?q=moon
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('q')

        defined = definition.Definition(word).get()

        response = {
            "word": word,
            "definition": defined
        }

        wp.html = json.dumps(response)
        return wp


jp.Route("/", Api.serve)
jp.justpy()
