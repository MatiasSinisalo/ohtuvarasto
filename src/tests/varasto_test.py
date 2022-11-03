import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    def test_konstruktori_ei_aseta_negatiivista_tilavuutta(self):
        uusivarasto = Varasto(-1, 0)
        self.assertEqual(uusivarasto.tilavuus, 0)
    
    def test_konstruktori_ei_aseta_negatiivista_saldoa(self):
        uusivarasto = Varasto(0, -1)
        self.assertEqual(uusivarasto.saldo, 0)
    
    def test_negatiivisen_arvon_lisaaminen_ei_muuta_varaston_saldoa(self):
         self.varasto.lisaa_varastoon(-1)
         self.assertEqual(self.varasto.saldo, 0)
    def test_varaston_saldo_ei_ylita_tilavuutta(self):
         self.varasto.lisaa_varastoon(1)
         self.varasto.lisaa_varastoon(5)
         self.varasto.lisaa_varastoon(50)
         self.assertEqual(self.varasto.saldo, 10)
    
    def test_varastosta_ei_voi_ottaa_negatiivista_arvoa(self):
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, 0)
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, 5)
    
    def test_varasto_palauttaa_kaiken_mita_voi_jos_varastosta_otetaan_enemman_kuin_on_saldoa(self):
        self.varasto.lisaa_varastoon(10)
        maara = self.varasto.ota_varastosta(11)
        self.assertEqual(maara, 10)
    
    def test_varaston_saldo_nollaantuu_jos_varastosta_otetaan_enemman_kuin_on_saldoa(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(11)
        self.assertEqual(self.varasto.saldo, 0)
    
    def test_varaston_ToString_palauttaa_oikean_arvon(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(str(self.varasto), "saldo = 10, vielä tilaa 0")
        self.varasto.ota_varastosta(5)
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")



