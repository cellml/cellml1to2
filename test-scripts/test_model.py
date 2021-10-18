import unittest

import libcellml as lc

from subprocess import Popen, PIPE


def run_saxon(model_name):
    with Popen(["saxon", f"-s:test-models/{model_name}", "-xsl:cellml1to2.xsl"], stdout=PIPE) as proc:
        return proc.stdout.read().decode()


class TranslationTestCase(unittest.TestCase):

    def setUp(self):
        self._p = lc.Parser()
        self._v = lc.Validator()

    def _validate_model(self, model_name):
        translated_model = run_saxon(model_name)

        m = self._p.parseModel(translated_model)

        self._v.validateModel(m)

    def test_basic_model(self):
        self._validate_model('basic_model.cellml')

        self.assertEqual(0, self._v.errorCount())

    def test_van_der_pol_model(self):
        self._validate_model('van_der_pol_model.cellml')

        self.assertEqual(0, self._v.errorCount())

    def test_cellml_1_0_model(self):
        self._validate_model('cellml1.0.xml')

        self.assertEqual(2, self._v.errorCount())
        self.assertIn('celsius', self._v.error(0).description())
        self.assertEqual('1.3.1.2', self._v.error(1).referenceHeading())

    def test_cellml_1_1_model(self):
        self._validate_model('cellml1.1.xml')

        self.assertEqual(2, self._v.errorCount())
        self.assertIn('celsius', self._v.error(0).description())
        self.assertEqual('1.3.1.2', self._v.error(1).referenceHeading())


if __name__ == '__main__':
    unittest.main()
