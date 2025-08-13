import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Modo visible
        yield browser
        browser.close()

def test_checkout_mandatory_fields(browser):
    page = browser.new_page()

    # 1. Login con credenciales válidas
    page.goto('https://www.saucedemo.com/')
    page.fill('input[name="user-name"]', 'standard_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[type="submit"]')

    # 2. Agregar un producto al carrito
    page.click('button[name="add-to-cart-sauce-labs-backpack"]')

    # 3. Ir al carrito
    page.click('.shopping_cart_link')

    # 4. Iniciar el checkout
    page.click('button[name="checkout"]')

    # 5. Dejar los campos obligatorios vacíos y continuar
    page.click('input[name="continue"]')

    # 6. Verificar el mensaje de error
    try:
        page.wait_for_selector('.error-message-container', timeout=5000)
        error_text = page.inner_text('.error-message-container')
        print("Error message displayed:", error_text)
        assert "Error: First Name is required" in error_text
    except Exception as e:
        page.screenshot(path="checkout_mandatory_fields_error.png")
        raise e

    page.close()
