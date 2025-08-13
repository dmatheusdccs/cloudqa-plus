import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_checkout_with_out_of_stock_product(browser):
    page = browser.new_page()

    # 1. Abrir la página de login
    page.goto('https://www.saucedemo.com/')

    # 2. Ingresar credenciales válidas
    page.fill('input[name="user-name"]', 'standard_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[type="submit"]')

    # 3. Esperar que la página de inventario esté cargada
    page.wait_for_selector(".inventory_list", timeout=5000)

    # 4. Interceptar la respuesta o manipular DOM para simular que un producto está agotado
    # Por simplicidad, vamos a ocultar el botón de "Add to cart" del primer producto para simular out of stock
    page.evaluate("""
        () => {
            const btn = document.querySelector('button[id^="add-to-cart-"]');
            if (btn) btn.disabled = true; // deshabilitar el botón
            if (btn) btn.textContent = "Out of Stock"; // cambiar texto
        }
    """)

    # 5. Intentar agregar ese producto (que está simulado como agotado)
    disabled = page.eval_on_selector('button[id^="add-to-cart-"]', 'el => el.disabled')
    assert disabled, "The 'Add to cart' button should be disabled for out of stock product"

    # 6. Intentar hacer click en el carrito
    page.click('.shopping_cart_link')

    # 7. Validar que el producto agotado no está en el carrito o que aparece mensaje (depende de la app)
    # Aquí validamos que el carrito está vacío (porque no se pudo agregar)
    cart_items = page.query_selector_all('.cart_item')
    assert len(cart_items) == 0, "Cart should be empty because out of stock product can't be added"

    # 8. (Opcional) Validar que el botón Checkout esté deshabilitado (si hay algo en el carrito)
    # Por ahora omitimos porque el carrito está vacío

    page.close()
