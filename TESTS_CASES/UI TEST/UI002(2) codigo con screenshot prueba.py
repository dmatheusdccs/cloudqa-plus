import pytest
from playwright.sync_api import sync_playwright

# Fixture para iniciar y cerrar el navegador
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Abrir el navegador en modo visible
        yield browser
        browser.close()

# Prueba de login con contraseña incorrecta
def test_invalid_login(browser):
    # Iniciar una nueva página
    page = browser.new_page()
    
    # 1. Abrir la página de login
    page.goto('https://www.saucedemo.com/')
    
    # 2. Ingresar un nombre de usuario válido
    page.fill('input[name="user-name"]', 'standard_user')
    
    # 3. Ingresar una contraseña incorrecta (ahora con una contraseña aleatoria)
    page.fill('input[name="password"]', 'A3$hhytio')
    
    # 4. Hacer clic en el botón de login
    page.click('input[type="submit"]')

    # Esperar que el mensaje de error aparezca
    try:
        page.wait_for_selector(".error-message-container", timeout=5000)  # Espera hasta que el mensaje de error esté visible
        print("Login failed as expected.")
        
        # Tomar captura de pantalla si el login falla
        page.screenshot(path="login_error.png")
    except Exception as e:
        # Captura la pantalla si algo falla
        page.screenshot(path="login_error.png")
        raise e  # Vuelve a lanzar la excepción para que la prueba falle

    # Verificar que el mensaje de error está presente
    assert "Epic sadface: Username and password do not match any user in this service" in page.inner_text(".error-message-container")
    
    # Cerrar la página después de la prueba
    page.close()
