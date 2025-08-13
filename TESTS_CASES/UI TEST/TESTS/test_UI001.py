import pytest
from playwright.sync_api import sync_playwright

# Fixture para iniciar y cerrar el navegador
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Abrir el navegador en modo visible
        yield browser
        browser.close()

# Prueba de login válido
def test_valid_login(browser):
    # Iniciar una nueva página
    page = browser.new_page()
    
    # 1. Abrir la página de login
    page.goto('https://www.saucedemo.com/')
    
    # 2. Ingresar un nombre de usuario válido
    page.fill('input[name="user-name"]', 'standard_user')
    
    # 3. Ingresar la contraseña válida
    page.fill('input[name="password"]', 'secret_sauce')
    
    # 4. Hacer clic en el botón de login
    page.click('input[type="submit"]')

    # Esperar hasta que se redirija a la página de inicio (espera la URL)
    try:
        page.wait_for_selector(".shopping_cart_link", timeout=10000)  # Espera que la página de inicio esté visible
        print("Login successful, redirected to homepage.")
    except Exception as e:
        page.screenshot(path="login_error.png")  # Captura la pantalla si algo falla
        raise e  # Vuelve a lanzar la excepción para que la prueba falle

    # Verificar que la URL sea la de la página de inicio después del login
    assert page.url == 'https://www.saucedemo.com/inventory.html'
    
    # Cerrar la página después de la prueba
    page.close()
