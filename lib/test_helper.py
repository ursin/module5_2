from unittest import TestCase, main

class Test01Vorname(TestCase):
    def test_01_vorname_existiert(self):
        try: vorname
        except NameError:
            self.fail("Erstelle eine Variable <nachname>")
        self.assertIsNotNone(vorname, msg="Erstelle eine Variable <vorname>")
        
    def test_02_vorname_sollte_ein_string_sein(self):
        self.assertIsInstance(vorname, str, msg="Die Variable <vorname> muss ein String sein")
        
    def test_03_vorname_darf_kein_leerer_string_sein(self):
        self.assertTrue(len(vorname) > 0, msg="Die Variable <vorname> darf kein leerer String sein")
        
class Test02Nachname(TestCase):        
    def test_01_nachname_existiert(self):
        try: nachname
        except NameError:
            self.fail("Erstelle eine Variable <nachname>")
        self.assertIsNotNone(nachname, msg="Die Variable <nachname> darf nicht None sein")
        
    def test_02_nachname_sollte_ein_string_sein(self):
        self.assertIsInstance(nachname, str, msg="Die Variable <nachname> muss ein String sein")
        
    def test_03_nachname_darf_kein_leerer_string_sein(self):
        self.assertTrue(len(nachname) > 0, msg="Die Variable <nachname> darf kein leerer String sein")
        
class Test03Alter(TestCase):        
    def test_01_alter_existiert(self):
        try: alter
        except NameError:
            self.fail("Erstelle eine Variable <alter>")
        self.assertIsNotNone(alter, msg="Die Variable <nachname> darf nicht None sein")
        
    def test_02_alter_sollte_ein_integer_sein(self):
        self.assertIsInstance(alter, int, msg="Die Variable <alter> muss ein Integer sein")
        
    def test_03_alter_sollte_gt_18_lt_100_sein(self):
        self.assertTrue(100 > alter >= 16, msg="Die Variable <alter> muss kleiner als 100 und grösser als 16 sein")
        
class Test04X(TestCase):        
    def test_01_x_existiert(self):
        try: x
        except NameError:
            self.fail("Erstelle eine Variable <x>")
        self.assertIsNotNone(x, msg="Die Variable <x> darf nicht None sein")
        
    def test_02_x_sollte_ein_float_sein(self):
        self.assertIsInstance(x, float, msg="Die Variable <x> muss ein Float sein")
        
        
class Test05Hobbies(TestCase):        
    def test_01_hobbies_existiert(self):
        try: hobbies
        except NameError:
            self.fail("Erstelle eine Variable <hobbies>")
        self.assertIsNotNone(hobbies, msg="Die Variable <hobbies> darf nicht None sein")
        
    def test_02_hobbies_sollte_eine_liste_sein(self):
        self.assertIsInstance(hobbies, list, msg="Die Variable <hobbies> muss eine Liste sein")
        
    def test_03_hobbies_sollte_nicht_leer_sein(self):
        self.assertTrue(len(hobbies) > 0, msg="<hobbies> darf nicht eine leere Liste sein")
        
    def test_04_hobbies_sollte_min_2_hobbies_enthalten(self):
        self.assertTrue(len(hobbies) >= 2, msg=f"<hobbies> sollte mind. 2 hobbies enthalten, hat aber {len(hobbies)}")
        
    def test_05_hobbies_sollten_alle_strings_sein(self):
        for h in hobbies:
            self.assertIsInstance(h, str, msg=f"Ein Hobby muss ein String sein, {h} ist aber ein {type(h)}")
            
class Test05Reisen(TestCase):        
    def test_01_reisen_existiert(self):
        try: reisen
        except NameError:
            self.fail("Erstelle eine Variable <reisen>")
        self.assertIsNotNone(reisen, msg="Die Variable <reisen> darf nicht None sein")
        
    def test_02_reisen_sollte_ein_dict_sein(self):
        self.assertIsInstance(reisen, dict, msg="Die Variable <reisen> muss ein Dictionary sein")
        
    def test_03_reisen_darf_nicht_leer_sein(self):
        self.assertTrue(len(reisen) > 0, msg="<reisen> darf nicht leer sein")
        
    def test_04_reisen_muss_int_als_key_haben(self):
        for k in reisen.keys():
            self.assertIsInstance(k, int, msg=f"Keys in <reisen> müssen Integers sein, {k} ist aber ein {type(k)}")
   
    def test_05_reisen_muss_string_als_value_haben(self):
        for v in reisen.values():
            self.assertIsInstance(v, str, msg=f"Values in <reisen> müssen Strings sein, {v} ist aber ein {type(v)}")
        
main(argv=[''], verbosity=2, exit=False, failfast=True)