import os
import platform
import time
from dotenv import load_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from typing_extensions import Literal


class FormBot(Chrome):
    def __init__(self, FORM_URL: str) -> None:
        chrome_options = Options()
        chrome_options.add_argument("log-level=3")

        if platform.system() == "Darwin":
            driver_location = os.path.join(os.getcwd(), "chromedriver")
            super().__init__(executable_path=driver_location, options=chrome_options)
        else:
            super().__init__(options=chrome_options)

        self.get(FORM_URL)

    def fill_email(self, email: str) -> None:
        self.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input',
        ).send_keys(email)

    def fill_week(self, week: int) -> None:
        num = (week - 1) * 3 + 9
        self.find_element(By.XPATH, f'//*[@id="i{num}"]/div[3]/div').click()

    def fill_name(self, full_name: str) -> None:
        self.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
        ).send_keys(full_name)

    def fill_rut(self, rut: str) -> None:
        self.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input',
        ).send_keys(rut)

    def fill_nrc(self, nrc: str) -> None:
        self.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input',
        ).send_keys(nrc)

    def fill_day(self, day: int) -> None:
        num = (day - 1) * 3 + 73
        self.find_element(By.XPATH, f'//*[@id="i{num}"]/div[3]/div').click()

    def submit(self) -> None:
        self.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
        ).click()


def check_valid_number(field: Literal["semana", "día"], max_num: int) -> None:
    num = 0
    while num not in range(1, max_num + 1):
        try:
            num = int(input(f"Ingresa {field} que quieres llenar (1-{max_num}): "))
        except ValueError:
            print("ERROR: Ingresa un número")
            continue
        if num not in range(1, max_num + 1):
            print(f"ERROR: Ingresa un número entre 1 y {max_num}")
    return num


print("¡Este bot rellenara su asistencia de forma automática!")
print("¡¿Están listos chicos?!\n")

if ".env" not in os.listdir(os.getcwd()):
    print(
        """No hay un archivo .env con tus credenciales.
Crearemos uno para ti, rellena tus datos"""
    )
    time.sleep(2)

    email = input("Email: ")
    full_name = input("Primer nombre y 2 apellidos (utilice MAYÚSCULA): ")
    rut = input("RUT: ")
    nrc = input("NRC (solo números): ")

    with open(".env", "w") as f:
        f.write(f"EMAIL={email}\n")
        f.write(f"FULL_NAME={full_name}\n")
        f.write(f"RUT={rut}\n")
        f.write(f"NRC={nrc}\n")

load_dotenv()

# Credencials
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScaPxGIKPDwFNlVJcKmRRy7JHDUKQExt1fbrsIMvhwxJWt3kA/viewform"
EMAIL = os.environ.get("EMAIL")
FULL_NAME = os.environ.get("FULL_NAME")
RUT = os.environ.get("RUT")
NRC = os.environ.get("NRC")

print(
    f"""Las credenciales de tu ".env" son:
    Email: {EMAIL}
    Nombre: {FULL_NAME}
    RUT: {RUT}
    NRC (sólo números): {NRC}
De haber algún error en ellas, abre el archivo ".env",
corrigelas y vuelve a correr el programa.
"""
)

WEEK = check_valid_number("semana", 16)
DAY = check_valid_number("día", 3)

try:
    bot = FormBot(FORM_URL)
    bot.fill_email(EMAIL)
    bot.fill_week(WEEK)
    bot.fill_name(FULL_NAME)
    bot.fill_rut(RUT)
    bot.fill_nrc(NRC)
    bot.fill_day(DAY)
    bot.submit()
    print("Asitencia marcada con éxito!")

except Exception as e:
    print(e)

finally:
    time.sleep(5)
    bot.close()
