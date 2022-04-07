from django.test import TestCase


from taxi_service.settings import TEMPLATES


class TemplateTest(TestCase):
    def test_templates_dir(self):
        print(TEMPLATES[0]['DIRS'])
        assert TEMPLATES[0]['DIRS'] == ''
