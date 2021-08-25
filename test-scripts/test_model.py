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

    def test_basic_model(self):
        translated_model = run_saxon('basic_model.cellml')

        m = self._p.parseModel(translated_model)

        self._v.validateModel(m)

        self.assertEqual(0, self._v.errorCount())

    def test_van_der_pol_model(self):
        translated_model = run_saxon('van_der_pol_model.cellml')

        m = self._p.parseModel(translated_model)

        self._v.validateModel(m)

        self.assertEqual(0, self._v.errorCount())

    def test_cellml_1_0_model(self):
        translated_model = run_saxon('cellml1.0.xml')

        m = self._p.parseModel(translated_model)

        self._v.validateModel(m)

        self.assertEqual(2, self._v.errorCount())
        self.assertIn('celsius', self._v.error(0).description())
        self.assertEqual('1.3.1.2', self._v.error(1).referenceHeading())

    def test_cellml_1_1_model(self):
        translated_model = run_saxon('cellml1.1.xml')

        m = self._p.parseModel(translated_model)

        self._v.validateModel(m)

        self.assertEqual(2, self._v.errorCount())
        self.assertIn('celsius', self._v.error(0).description())
        self.assertEqual('1.3.1.2', self._v.error(1).referenceHeading())


if __name__ == '__main__':
    unittest.main()
