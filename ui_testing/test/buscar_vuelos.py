import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class BuscarVuelosTest(unittest.TestCase):

    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/DuvanArlen/PycharmProjects/ui_testing/drivers/chromedriver.exe")
        cls.driver.maximize_window()

    # Este método recibe como parámetro la URL del sitio
    def test_go_url(self, url):
        self.driver.get(url)

    # Este método recibe como parámetro el login y password y hace clic en el botin Sign-In
    def test_login(self, user, password):
        self.driver.find_element_by_name("userName").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("login").click()

    def test_buscar_vuelo(self, origen, destino, clase, aerolinea):
        Select(self.driver.find_element_by_name("fromPort")).select_by_visible_text(origen)
        Select(self.driver.find_element_by_name("toPort")).select_by_visible_text(destino)
        self.driver.find_element_by_xpath("//input[@name='servClass' and @value='" + clase + "']").click()
        Select(self.driver.find_element_by_name("airline")).select_by_visible_text(aerolinea)
        time.sleep(3)
        self.driver.find_element_by_name("findFlights").click()

    def test_seleccionar_vuelo(self):
        self.driver.find_element_by_xpath("//input[@name='outFlight' and @value='Unified Airlines$363$281$11:24']").click()
        self.driver.find_element_by_xpath("//input[@name='inFlight' and @value='Blue Skies Airlines$631$273$14:30']").click()
        time.sleep(3)
        self.driver.find_element_by_name("reserveFlights").click()

    def test_info_personal(self, nombre, apellido, comida):
        self.driver.find_element_by_name("passFirst0").send_keys(nombre)
        self.driver.find_element_by_name("passLast0").send_keys(apellido)
        Select(self.driver.find_element_by_name("pass.0.meal")).select_by_visible_text(comida)

    def test_ingreso_info_pago(self, tc, nro_tc, mes_exp, anno_exp):
        Select(self.driver.find_element_by_name("creditCard")).select_by_visible_text(tc)
        self.driver.find_element_by_name("creditnumber").send_keys(nro_tc)
        Select(self.driver.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text(mes_exp)
        Select(self.driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text(anno_exp)

    def test_ingreso_info_direccion(self, direccion, ciudad):
        self.driver.find_element_by_name("billAddress1").clear()
        self.driver.find_element_by_name("billCity").clear()
        self.driver.find_element_by_name("billAddress1").send_keys(direccion)
        self.driver.find_element_by_name("billCity").send_keys(ciudad)

    def test_ingreso_direccion_entrega(self, direccion, ciudad):
        self.driver.find_element_by_name("delAddress1").clear()
        self.driver.find_element_by_name("delCity").clear()
        self.driver.find_element_by_name("delAddress1").send_keys(direccion)
        self.driver.find_element_by_name("delCity").send_keys(ciudad)

    def test_compra(self):
        self.driver.find_element_by_name("buyFlights").click()
        time.sleep(2)

    # Este método hace clic en el botón SIGN-OFF
    def test_logout(self):
        self.driver.find_element_by_link_text("SIGN-OFF").click()
        time.sleep(2)

    def test_image_select_flight(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_selectflight.gif')]").is_displayed()
        self.assertTrue(image)

    def test_image_book_flight(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_book.gif')]").is_displayed()
        self.assertTrue(image)

    def test_image_flight_confirmation(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_confirmation.gif')]").is_displayed()
        self.assertTrue(image)

    # Este método se ejecuta al final y cierra el navegador
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Prueba completada con éxito")

if __name__ == '__main__':
    unittest.main()