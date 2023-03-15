from django.test import TestCase

import pyconcept
import json

class TestIntegrations(TestCase):
    
    def test_empty_schema(self):
        with self.assertRaises(RuntimeError):
            pyconcept.check_schema('')
        
    def test_check_schema(self):
        schema = self._default_schema()
        self.assertTrue(pyconcept.check_schema(schema) != '')

    def test_parse_expression(self):
        schema = self._default_schema()
        out1 = json.loads(pyconcept.parse_expression(schema, 'X1=X1'))
        self.assertTrue(out1['parseResult'])

        out2 = json.loads(pyconcept.parse_expression(schema, 'X1=X2'))
        self.assertFalse(out2['parseResult'])

    def _default_schema(self):
        return '''{
    "type": "rsform",
    "title": "default",
    "alias": "default",
    "comment": "",
    "items": [
        {
            "entityUID": 1023383816,
            "type": "constituenta",
            "cstType": "basic",
            "alias": "X1",
            "convention": "",
            "term": {
                "raw": "",
                "resolved": "",
                "forms": []
            },
            "definition": {
                "formal": "",
                "text": {
                    "raw": "",
                    "resolved": ""
                }
            }
        },
        {
            "entityUID": 1877659352,
            "type": "constituenta",
            "cstType": "basic",
            "alias": "X2",
            "convention": "",
            "term": {
                "raw": "",
                "resolved": "",
                "forms": []
            },
            "definition": {
                "formal": "",
                "text": {
                    "raw": "",
                    "resolved": ""
                }
            }
        },
        {
            "entityUID": 1115937389,
            "type": "constituenta",
            "cstType": "structure",
            "alias": "S1",
            "convention": "",
            "term": {
                "raw": "",
                "resolved": "",
                "forms": []
            },
            "definition": {
                "formal": "ℬ(X1×X1)",
                "text": {
                    "raw": "",
                    "resolved": ""
                }
            }
        },
        {
            "entityUID": 94433573,
            "type": "constituenta",
            "cstType": "structure",
            "alias": "S2",
            "convention": "",
            "term": {
                "raw": "",
                "resolved": "",
                "forms": []
            },
            "definition": {
                "formal": "ℬ(X1×X2)",
                "text": {
                    "raw": "",
                    "resolved": ""
                }
            }
        }
    ]
}'''
