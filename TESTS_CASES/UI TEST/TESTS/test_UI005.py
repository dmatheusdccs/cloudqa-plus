import pytest
from playwright.sync_api import sync_playwright

# Fixture para iniciar y cerrar el navegador
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Navegador visible
        yield browser
        browser.close()

def test_logout_redirect(browser):
    page = browser.new_page()
    
    # 1. Abrir la página de login
    page.goto("https://www.saucedemo.com/")
    
    # 2. Ingresar credenciales válidas
    page.fill('input[name="user-name"]', "standard_user")
    page.fill('input[name="password"]', "secret_sauce")
    
    # 3. Hacer clic en "Login"
    page.click('input[type="submit"]')
    
    # 4. Abrir el menú lateral
    page.click("#react-burger-menu-btn")
    
    # 5. Hacer clic en "Logout"
    page.click("#logout_sidebar_link")
    
    # 6. Verificar que el usuario es redirigido a la página de login
    try:
        page.wait_for_selector('input[name="user-name"]', timeout=5000)
        print("Logout successful, redirected to login page.")
    except Exception as e:
        page.screenshot(path="logout_error.png")
        raise e
    
    assert page.url == "https://www.saucedemo.com/"
    
    page.close()
